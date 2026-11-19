from mitmproxy import http


DOMAIN_SUFFIXES = [
    "sso.xjtlu.edu.cn",
    "uim.xjtlu.edu.cn",
    "timetableplus.xjtlu.edu.cn",
    "peselection.xjtlu.edu.cn",
    "echo.free.beeceptor.com",
    "dnschecker.org",
]
# UA guide: https://github.com/LYJW131/xjtlu-uim-login#%E7%BB%93%E8%AE%BA
USER_AGENT = "TDMBrowser/12172 CFNetwork/3896.100.1.2.1 Darwin/27.0.0"


def request(flow: http.HTTPFlow) -> None:
    host = flow.request.host.lower().rstrip(".")
    if any(host == suffix or host.endswith(f".{suffix}") for suffix in DOMAIN_SUFFIXES):
        flow.request.headers["User-Agent"] = USER_AGENT
        
        flow.request.headers.pop("Sec-Ch-Ua")
        flow.request.headers.pop("Sec-Ch-Ua-Mobile")
        flow.request.headers.pop("Sec-Ch-Ua-Platform")

