from mitmproxy import http
from bs4 import BeautifulSoup
import re

def response(flow: http.HTTPFlow) -> None:
    # 只处理 HTML 类型的响应
    if flow.response and "text/html" in flow.response.headers.get("content-type", ""):
        
        # 目标网站，比如我们要净化 example.com
        if "example.com" in flow.request.pretty_url:
            
            # 解析 HTML 内容
            html = flow.response.get_text()
            soup = BeautifulSoup(html, "html.parser")
            
            # 查找所有的 <script> 标签
            scripts = soup.find_all("script")
            
            for script in scripts:
                if script.string:
                    # 场景 A：根据关键词匹配内嵌脚本内容（比如包含某个广告商的初始化代码）
                    if "bad_ad_function" in script.string or "ad_client_id" in script.string:
                        script.string = "console.log('广告脚本已被安全替换');"
                        #script.decompose() # 从 HTML 中彻底删除该脚本标签
                        
                # 场景 B：根据 src 属性拦截外部引入的广告脚本（顺便一起拦截）
                elif script.get("src"):
                    if "google-analytics.com" in script["src"] or "ad_service.js" in script["src"]:
                        script.decompose()
            
            # 将修改后的 HTML 重新写回响应中
            flow.response.text = str(soup)
