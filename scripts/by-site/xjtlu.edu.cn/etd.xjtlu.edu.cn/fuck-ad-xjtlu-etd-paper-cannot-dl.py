from mitmproxy import http
from bs4 import BeautifulSoup
import re

def response(flow: http.HTTPFlow) -> None:
    # 只处理 HTML 类型的响应
    if flow.response and "text/html" in flow.response.headers.get("content-type", ""):
        
        # 目标网站
        if "etd.xjtlu.edu.cn" in flow.request.pretty_url:

            # 解析 HTML 内容
            html = flow.response.get_text()
            soup = BeautifulSoup(html, "html.parser")

            # 查找所有的 <script> 标签
            scripts = soup.find_all("script")

            for script in scripts:
                if script.string:
                    # 场景 A：根据关键词匹配内嵌脚本内容（比如包含某个广告商的初始化代码）
                    if "此文档禁止打印" in script.string or "下载已被禁用" in script.string:
                        script.string = "console.log('PDF阅读器限制已被解除，按下CTRL+S直接保存');"
                        #script.decompose() # 从 HTML 中彻底删除该脚本标签

            # 将修改后的 HTML 重新写回响应中
            flow.response.text = str(soup)
