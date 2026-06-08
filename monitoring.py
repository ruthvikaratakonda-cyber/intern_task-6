from prometheus_client import Counter

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP Requests"
)

def track_request():
    REQUEST_COUNT.inc()