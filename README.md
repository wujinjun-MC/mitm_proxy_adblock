# mitm_proxy_adblock
MITMproxy 脚本集合，去广告

## Feature

支持的网站列表:
- xjtlu.edu.cn
    - etd.xjtlu.edu.cn
        - [fuck-ad-xjtlu-etd-paper-cannot-dl.py]()
            - XJTLU Electronic Theses and Dissertations (ETD) system 试卷查阅可下载。
            - 原来的PDF阅读器有下载按钮，或按下CTRL+S即可下载，但是新版无法下载，并且有anticheat脚本内嵌在HTML中，无法按下CTRL+S保存或CTRL+P打印，手动选择打印是显示白屏
            - 内嵌脚本使用 Adblock Adguard Tampermonkey 等工具移除无效，因为浏览器接收到后已经执行，即使使用F12开发人员工具也无法恢复
            - 使用MITMproxy运行此脚本，HTML在到达浏览器之前已经被移除，不会被执行，功能恢复正常
            - 虽然有 [qwqqaq0/XJTLU_Past_Paper_Downloader](https://github.com/qwqqaq0/XJTLU_Past_Paper_Downloader) 这类实现，但是我只想下载一两个试卷，不想要overhead
- cn.bing.com
    - **TODO**
- [templates]
    - [simple-adblock-remove-embed-js.py]()
        - 模板: 去掉包含广告的内嵌脚本。普通广告拦截插件 (Adblock, Adguard等等) 或油猴脚本难以拦截，因为已经在处理前执行了，使用此脚本，即可在响应到达浏览器之前移除这类脚本

## How to use
1. 在 MITMproxy 官网下载并安装
2. 将脚本保存到本地
3. 启动MITMproxy: `mitmproxy --listen-port 8080 -s <path to script>`
4. 设置系统/浏览器代理
    - Windows: Internet选项 - 连接 - 局域网设置，地址http://127.0.0.1 端口8080
    - Linux: 设置环境变量 `export HTTP_PROXY=http://127.0.0.1:7897 HTTPS_PROXY=http://127.0.0.1:7897 http_proxy=http://127.0.0.1:7897 https_proxy=http://127.0.0.1:7897` 然后启动程序
    - 浏览器: 在浏览器设置中找到代理设置
