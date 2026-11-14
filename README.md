# 🛡️ mitm_proxy_adblock

> **MITMproxy 拦截脚本集合** - 专为广告过滤器无法拦截的内嵌广告/烦人脚本设计

[![License](https://img.shields.io/badge/License-Under%20Consideration-yellow.svg)](#)
[![Last Updated](https://img.shields.io/badge/last%20updated-2026-brightgreen.svg)](https://github.com/wujinjun-MC/mitm_proxy_adblock)

## 📖 简介
本仓库提供用于配合 **MITMproxy** 运行的 Python 脚本。

**核心用途**：拦截和移除已注入到客户端浏览器但无法通过常规插件（如 Adblock, Tampermonkey）清除的内嵌恶意脚本（广告、扰人弹窗、白屏逻辑等）；在数据包层面优化使用体验；小工具

## ✨ 特性与支持场景

支持的网站列表:
- xjtlu.edu.cn
    - etd.xjtlu.edu.cn
        - [fuck-ad-xjtlu-etd-paper-cannot-dl.py](https://github.com/wujinjun-MC/mitm_proxy_adblock/raw/refs/heads/main/scripts/by-site/xjtlu.edu.cn/etd.xjtlu.edu.cn/fuck-ad-xjtlu-etd-paper-cannot-dl.py)
            - [View code](https://github.com/wujinjun-MC/mitm_proxy_adblock/blob/main/scripts/by-site/xjtlu.edu.cn/etd.xjtlu.edu.cn/fuck-ad-xjtlu-etd-paper-cannot-dl.py)
            - XJTLU Electronic Theses and Dissertations (ETD) system 试卷查阅可下载。
            - **💡 为什么需要此脚本？**
                - **原生失效**：新版 PDF 阅读器无下载按钮，且无法通过 CTRL+S 保存。浏览器已加载 HTML 并执行内嵌脚本，F12 无法阻止。
                    - 原来的PDF阅读器有下载按钮，或按下CTRL+S即可下载，但是新版无法下载，并且有anticheat脚本内嵌在HTML中，无法按下CTRL+S保存或CTRL+P打印，手动选择打印显示白屏
                    - 内嵌脚本使用 Adblock/Adguard/Tampermonkey 等工具移除无效，因为浏览器接收到后已经执行，即使使用F12开发人员工具也无法恢复
                - **MITMproxy 优势**：在请求到达浏览器前拦截并移除恶意 JS，无需浏览器插件
                    - 使用MITMproxy运行此脚本，HTML内嵌的两个censorship在到达浏览器之前已经被移除，不会被执行，功能恢复正常
                - **轻量级**：相比其他下载器（如 `qwqqaq0/XJTLU_Past_Paper_Downloader`），本脚本仅针对单个需求优化。
                    - 虽然有 [qwqqaq0/XJTLU_Past_Paper_Downloader](https://github.com/qwqqaq0/XJTLU_Past_Paper_Downloader) 这类实现，但是我只想下载一两个试卷，不想要overhead
            - Disclaimer:
                - This tool is for reference and learning purposes only. 文档内有明文水印 (可以通过Acrobat之类工具删掉) 和隐水印 (每次打开时得到的PDF文件的校验和不同)，如果你违反规定分发版权内容，你会被盯上。
                - Also see [this](https://github.com/kevinlasnh/xjtlu-final-paper-pdf-downloader#%EF%B8%8F-%E9%87%8D%E8%A6%81%E6%B3%95%E5%BE%8B%E5%A3%B0%E6%98%8E%E4%B8%8E%E4%BD%BF%E7%94%A8%E6%9D%A1%E6%AC%BE).
            - Alternative:
                - [Adguard 规则 (HTML filtering rules)](https://github.com/wujinjun-MC/adguard-rules/raw/refs/heads/main/adblock-generic.txt)
            - Base:
                - simple-adblock-remove-embed-js.py
    - uim.xjtlu.edu.cn
        - [xjtlu-uim-rs-break.py](https://github.com/wujinjun-MC/mitm_proxy_adblock/raw/refs/heads/main/scripts/by-site/xjtlu.edu.cn/uim.xjtlu.edu.cn/xjtlu-uim-rs-break.py)
            - [View code](https://github.com/wujinjun-MC/mitm_proxy_adblock/blob/main/scripts/by-site/xjtlu.edu.cn/uim.xjtlu.edu.cn/xjtlu-uim-rs-break.py)
            - 我不要闭源WAF代码运行! 我不是机器人!
            - Tags: [XJTLU] [UIM] [TimeTablePlus] [PESelection] [WAF] [rs] [Ruishu] [Bot] [Devtools] [debugger]
            - **💡 为什么需要此脚本？**
                - **省流**：跳过后请求不再包含长串参数，不再自动生成长串Cookie，减少上行流量消耗 (避免被识别为PCDN封宽带)
                    - 已存在的随机Cookie垃圾不会自动清除，请手动清除
                - **MITMproxy 优势**：在请求到达端点前拦截并奇异化UA，无需浏览器插件
                - **轻量级**：相比融合实现（如 `LYJW131/xjtlu-uim-login`），本脚本仅针对单个需求优化。
                    - 我不需要自动化，只想要日常放心使用
            - Disclaimer:
                - *from LYJW131/xjtlu-uim-login*
                    > 本项目仅用于个人账号~~自动化~~，请遵守学校规定。
            - Base:
                - simple-ua-replace.py
    - sso.xjtlu.edu.cn
        - [xjtlu-uim-rs-break.py](https://github.com/wujinjun-MC/mitm_proxy_adblock/raw/refs/heads/main/scripts/by-site/xjtlu.edu.cn/sso.xjtlu.edu.cn/xjtlu-uim-rs-break.py)
            - [View code](https://github.com/wujinjun-MC/mitm_proxy_adblock/blob/main/scripts/by-site/xjtlu.edu.cn/sso.xjtlu.edu.cn/xjtlu-uim-rs-break.py)
    - timetableplus.xjtlu.edu.cn
        - [xjtlu-uim-rs-break.py](https://github.com/wujinjun-MC/mitm_proxy_adblock/raw/refs/heads/main/scripts/by-site/xjtlu.edu.cn/timetableplus.xjtlu.edu.cn/xjtlu-uim-rs-break.py)
            - [View code](https://github.com/wujinjun-MC/mitm_proxy_adblock/blob/main/scripts/by-site/xjtlu.edu.cn/timetableplus.xjtlu.edu.cn/xjtlu-uim-rs-break.py)
    - peselection.xjtlu.edu.cn
        - [xjtlu-uim-rs-break.py](https://github.com/wujinjun-MC/mitm_proxy_adblock/raw/refs/heads/main/scripts/by-site/xjtlu.edu.cn/peselection.xjtlu.edu.cn/xjtlu-uim-rs-break.py)
            - [View code](https://github.com/wujinjun-MC/mitm_proxy_adblock/blob/main/scripts/by-site/xjtlu.edu.cn/peselection.xjtlu.edu.cn/xjtlu-uim-rs-break.py)
- cn.bing.com
    - **TODO**
- [templates]
    - [simple-adblock-remove-embed-js.py](https://github.com/wujinjun-MC/mitm_proxy_adblock/raw/refs/heads/main/scripts/templates/simple-adblock-remove-embed-js.py)
        - [View code](https://github.com/wujinjun-MC/mitm_proxy_adblock/blob/main/scripts/templates/simple-adblock-remove-embed-js.py)
        - 模板: 去掉包含广告的内嵌脚本。普通广告拦截插件 (Adblock, Adguard等等) 或油猴脚本难以拦截，因为已经在处理前执行了，使用此脚本，即可在响应到达浏览器之前移除这类脚本
        - Used in:
            - fuck-ad-xjtlu-etd-paper-cannot-dl.py
    - [simple-image-save.py](https://github.com/wujinjun-MC/mitm_proxy_adblock/raw/refs/heads/main/scripts/templates/simple-image-save.py)
        - [View code](https://github.com/wujinjun-MC/mitm_proxy_adblock/blob/main/scripts/templates/simple-image-save.py)
        - 模板: 保存所有图片: 对目标域名后缀，文件后缀/MIME类型/URL路径匹配时
        - Used in:
            - TODO
    - [simple-ua-replace.py](https://github.com/wujinjun-MC/mitm_proxy_adblock/raw/refs/heads/main/scripts/templates/simple-ua-replace.py)
        - [View code](https://github.com/wujinjun-MC/mitm_proxy_adblock/blob/main/scripts/templates/simple-ua-replace.py)
        - 模板: 匹配域名后缀，更改请求User Agent
        - Used in:
            - xjtlu-uim-rs-break.py

## 🚀 如何开始 (How to Use)
### 前置准备
1.  [下载 MITMproxy](https://mitmproxy.org/) 并安装（支持 Linux/macOS/Windows）。
2.  获取本仓库中的脚本。

### 1. 启动 MITMproxy
根据您的需求配置监听端口（示例使用 `8080`）：
```bash
mitmproxy --listen-port 8080 -s <path_to_script> -s <path_to_another_script>
```
Socks5: 添加 `--mode socks5`

### 2. 配置代理
确保 **服务器监听端口** 与 **系统代理端口** 一致（示例统一使用 8080，若使用 1080/7890/7897/... 请修改命令中的端口号）。

| 操作系统 | 配置方法 |
| :--- | :--- |
| **Windows** | 控制面板 → Internet 选项 → 连接 → 局域网(LAN)设置 → 局域网设置 → 打勾 "为 LAN 设置代理服务器 ..." → 地址填入 `http://127.0.0.1`，端口填入 `8080` |
| **Linux** | 设置环境变量：`export HTTP_PROXY=http://127.0.0.1:8080 HTTPS_PROXY=http://127.0.0.1:8080 http_proxy=http://127.0.0.1:8080 https_proxy=http://127.0.0.1:8080` 并运行程序 |
| **浏览器** | 参考各浏览器设置方法，在代理中填入 `http://127.0.0.1:8080` |

## License
> **Under Consideration**

本仓库在正式添加许可证前，处于`All Rights Reserved`状态，默认禁止修改、分发或用于商业用途，仅允许个人学习和研究 fork。

## 免责声明

1. 使用风险： 用户明确知晓并同意，使用本软件的风险由用户自行承担。本软件按“现状”和“可用”状态提供，不提供任何形式的明示或暗示担保（包括但不限于适销性、特定目的的适用性、不侵权等担保）。
2. 数据损失： 在任何情况下，因使用或不能使用本软件所导致的任何直接、间接、偶然、特殊或连带的损失（包括但不限于利润损失、商业中断、数据丢失等），本软件及开发者不承担任何赔偿责任。
3. 第三方服务： 本软件可能包含指向第三方网站或服务的链接。对于第三方提供的服务或内容，本软件不承担任何审查、保证或赔偿责任。
4. 不可抗力： 因黑客攻击、电脑病毒侵入、政府管制、电信部门技术调整等不可抗力导致的服务中断或数据丢失，本软件不承担任何法律责任。
5. 使用环境限制: 本软件的设计和运行机制是基于客户端代理拦截。因此，其作用域仅限于您的本地设备和您传输的网络数据流，无法对服务器的内部系统、数据库或后台逻辑进行直接修改或管理。
6. 

## Credits
- XJTLU UIM "User Agent trick": https://github.com/LYJW131/xjtlu-uim-login#%E5%8F%91%E7%8E%B0%E6%8C%89-ua-%E5%88%86%E6%B5%81%E4%B8%8D%E6%98%AF%E7%BA%AF%E7%AE%97-vm

## 推荐使用

**✅ XJTLU自动登录系列**:
1. [西浦自动登录](https://greasyfork.org/zh-CN/scripts/484105/): 自动登录LearningMall Core、UIM、sso、mail、eBridge、IDP
    - Fork: [西浦自动登录-fork-wujinjun](https://openuserjs.org/scripts/wujinjun/%E8%A5%BF%E6%B5%A6%E8%87%AA%E5%8A%A8%E7%99%BB%E5%BD%95-fork-wujinjun): 支持更多登录 (例如 netauth) ，活跃更新，轻松配置
2. [XJTLU box 自动登录](https://openuserjs.org/scripts/wujinjun/XJTLU_box_%E8%87%AA%E5%8A%A8%E7%99%BB%E5%BD%95): 自动登录box，并自动勾选 `7天内保持登录`
3. [XJTLU UIM 自动登录 (请求用户名+密码+OTP)](https://openuserjs.org/scripts/wujinjun/XJTLU_UIM_%E8%87%AA%E5%8A%A8%E7%99%BB%E5%BD%95_(%E8%AF%B7%E6%B1%82%E7%94%A8%E6%88%B7%E5%90%8D%2B%E5%AF%86%E7%A0%81%2BOTP)): UIM自动登录(自动完成二次验证)
4. [XJTLU xpcyjgy 自动登录](https://openuserjs.org/scripts/wujinjun/XJTLU_xpcyjgy_%E8%87%AA%E5%8A%A8%E7%99%BB%E5%BD%95): XJTLU(TC)线上自助服务自动登录

**😊 XJTLU体验提升 (QoL)**:
1. [XJTLU AMS Sign-in Code 优化](https://openuserjs.org/scripts/wujinjun/XJTLU_AMS_Sign-in_Code_%E4%BC%98%E5%8C%96)
2. [XJTLU utalk 不要欢迎视频](https://openuserjs.org/scripts/wujinjun/XJTLU_utalk_%E4%B8%8D%E8%A6%81%E6%AC%A2%E8%BF%8E%E8%A7%86%E9%A2%91)
3. [XJTLU utalk 调整 (专为低性能设备优化)](https://openuserjs.org/scripts/wujinjun/XJTLU_utalk_tweaks_(Low-End_Device_Optimizer))
4. [XJTLU eBridge 登录过期自动重新登录](https://openuserjs.org/scripts/wujinjun/XJTLU_eBridge_%E7%99%BB%E5%BD%95%E8%BF%87%E6%9C%9F%E8%87%AA%E5%8A%A8%E9%87%8D%E6%96%B0%E7%99%BB%E5%BD%95)
5. [XJTLU eBridge 考试信息提示弹窗拦截](https://openuserjs.org/scripts/wujinjun/XJTLU_eBridge_%E8%80%83%E8%AF%95%E4%BF%A1%E6%81%AF%E6%8F%90%E7%A4%BA%E5%BC%B9%E7%AA%97%E6%8B%A6%E6%88%AA)

**其他自动登录系列**:
1. [UnoAnalyzer 优诺 自动登录](https://openuserjs.org/scripts/wujinjun/UnoAnalyzer_%E4%BC%98%E8%AF%BA_%E8%87%AA%E5%8A%A8%E7%99%BB%E5%BD%95): 如题

**其他体验提升**:
1. [UnoAnalyzer 优诺 登录状态保存](https://openuserjs.org/scripts/wujinjun/UnoAnalyzer_%E4%BC%98%E8%AF%BA_%E7%99%BB%E5%BD%95%E7%8A%B6%E6%80%81%E4%BF%9D%E5%AD%98): 持久化优诺登录状态，新窗口打开优诺无需重复登录，关闭浏览器不再丢失登录状态
