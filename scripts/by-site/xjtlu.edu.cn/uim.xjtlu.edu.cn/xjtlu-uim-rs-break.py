from mitmproxy import http


DOMAIN_SUFFIXES = {
    "sso.xjtlu.edu.cn",
    "uim.xjtlu.edu.cn",
    "timetableplus.xjtlu.edu.cn",
    "peselection.xjtlu.edu.cn",
}
# UA guide: https://github.com/LYJW131/xjtlu-uim-login#%E7%BB%93%E8%AE%BA
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/150.0.0.0 Safari/537.36 Darwin/..."
)


def request(flow: http.HTTPFlow) -> None:
    host = flow.request.host.lower().rstrip(".")
    if any(host == suffix or host.endswith(f".{suffix}") for suffix in DOMAIN_SUFFIXES):
        flow.request.headers["User-Agent"] = USER_AGENT
