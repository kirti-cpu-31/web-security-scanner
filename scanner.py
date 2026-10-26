import requests, sys

HEADERS = {
    "Strict-Transport-Security": "Forces HTTPS",
    "Content-Security-Policy": "Blocks XSS",
    "X-Frame-Options": "Prevents clickjacking",
    "X-Content-Type-Options": "Stops MIME sniffing",
}

def scan(url):
    fake = "https://evil.example"
    r = requests.get(url, timeout=10, headers={"Origin": fake})
    print("Scanning", url)
    for h, why in HEADERS.items():
        print("PASS" if h in r.headers else "FAIL", h, "-", why)
    acao = r.headers.get("Access-Control-Allow-Origin")
    bad = acao in ("*", fake)
    print("FAIL" if bad else "PASS", "CORS:", acao)

scan(sys.argv[1])