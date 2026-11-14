from mitmproxy import http


DOMAIN_SUFFIXES = {
    "example.com",
    "example.org",
    "example.net",
}
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/150.0.0.0 Safari/537.36 Darwin/..."
)


def request(flow: http.HTTPFlow) -> None:
    host = flow.request.host.lower().rstrip(".")
    if any(host == suffix or host.endswith(f".{suffix}") for suffix in DOMAIN_SUFFIXES):
        flow.request.headers["User-Agent"] = USER_AGENT
