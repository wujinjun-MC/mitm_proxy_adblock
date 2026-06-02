# 🛡️ mitm_proxy_adblock

> **MITMproxy 拦截脚本集合** - 专为广告过滤器无法拦截的内嵌广告/烦人脚本设计

[![License](https://img.shields.io/badge/License-Under%20Consideration-yellow.svg)](#)
[![Last Updated](https://img.shields.io/badge/last%20updated-2026-brightgreen.svg)](https://github.com/wujinjun-MC/mitm_proxy_adblock)

## 📖 简介
本仓库提供用于配合 **MITMproxy** 运行的 Python 拦截脚本。

**核心用途**：拦截和移除已注入到客户端浏览器但无法通过常规插件（如 Adblock, Tampermonkey）清除的内嵌恶意脚本（广告、扰人弹窗、白屏逻辑等）。

## ✨ 特性与支持场景

支持的网站列表:
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
        - Base:
            - simple-adblock-remove-embed-js.py
- cn.bing.com
    - **TODO**
- [templates]
    - [simple-adblock-remove-embed-js.py](https://github.com/wujinjun-MC/mitm_proxy_adblock/raw/refs/heads/main/scripts/templates/simple-adblock-remove-embed-js.py)
        - [View code](https://github.com/wujinjun-MC/mitm_proxy_adblock/blob/main/scripts/templates/simple-adblock-remove-embed-js.py)
        - 模板: 去掉包含广告的内嵌脚本。普通广告拦截插件 (Adblock, Adguard等等) 或油猴脚本难以拦截，因为已经在处理前执行了，使用此脚本，即可在响应到达浏览器之前移除这类脚本
        - Used in:
            - fuck-ad-xjtlu-etd-paper-cannot-dl.py

## 🚀 如何开始 (How to Use)
### 前置准备
1.  [下载 MITMproxy](https://mitmproxy.org/) 并安装（支持 Linux/macOS/Windows）。
2.  获取本仓库中的脚本。

### 1. 启动 MITMproxy
根据您的需求配置监听端口（示例使用 `8080`）：
```bash
mitmproxy --listen-port 8080 -s <path_to_script>
```

### 2. 配置代理
确保 **服务器监听端口** 与 **系统代理端口** 一致（示例统一使用 8080，若使用 1080/7890/7897/... 请修改命令中的端口号）。

| 操作系统 | 配置方法 |
| :--- | :--- |
| **Windows** | 控制面板 → Internet 选项 → 连接 → 局域网(LAN)设置 → 局域网设置 → 打勾 "为 LAN 设置代理服务器 ..." → 地址填入 `http://127.0.0.1`，端口填入 `8080` |
| **Linux** | 设置环境变量：`export HTTP_PROXY=http://127.0.0.1:7897 HTTPS_PROXY=http://127.0.0.1:7897 http_proxy=http://127.0.0.1:7897 https_proxy=http://127.0.0.1:7897` 并运行程序 |
| **浏览器** | 参考各浏览器设置方法，在代理中填入 `http://127.0.0.1:8080` |

## License
> **Under Consideration**

本仓库在正式添加许可证前，处于`All Rights Reserved`状态，默认禁止修改、分发或用于商业用途，仅允许个人学习和研究 fork。

## 免责声明

1. 使用风险： 用户明确知晓并同意，使用本软件的风险由用户自行承担。本软件按“现状”和“可用”状态提供，不提供任何形式的明示或暗示担保（包括但不限于适销性、特定目的的适用性、不侵权等担保）。
2. 数据损失： 在任何情况下，因使用或不能使用本软件所导致的任何直接、间接、偶然、特殊或连带的损失（包括但不限于利润损失、商业中断、数据丢失等），本软件及开发者不承担任何赔偿责任。
3. 第三方服务： 本软件可能包含指向第三方网站或服务的链接。对于第三方提供的服务或内容，本软件不承担任何审查、保证或赔偿责任。
4. 不可抗力： 因黑客攻击、电脑病毒侵入、政府管制、电信部门技术调整等不可抗力导致的服务中断或数据丢失，本软件不承担任何法律责任。
5. ...

## Credits
\-

## 推荐使用
1. [西浦自动登录](https://greasyfork.org/zh-CN/scripts/484105/): 自动登录LearningMall Core、UIM、sso、mail、eBridge、IDP
2. [XJTLU box 自动登录](https://greasyfork.org/zh-CN/scripts/550860): 自动登录box
3. [XJTLU xpcyjgy 自动登录](https://greasyfork.org/zh-CN/scripts/551035): XJTLU(TC)线上自助服务自动登录
4. [XJTLU UIM 自动登录 (请求用户名+密码+OTP)](https://greasyfork.org/zh-CN/scripts/550518): XJTLU UIM 自动登录增强版，自动完成辅助验证，无需手动输入验证码/OTP
