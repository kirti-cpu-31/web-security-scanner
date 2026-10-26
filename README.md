# Automated Web Scanner

A simple Python script that checks a website for missing security headers and CORS misconfiguration.

## What it checks
- **Strict-Transport-Security:** forces HTTPS
- **Content-Security-Policy:** helps block XSS
- **X-Frame-Options:** prevents clickjacking
- **X-Content-Type-Options:** stops MIME sniffing
- **CORS:** flags the site if it allows any origin (`*`) or echoes back a fake origin

## Requirements
- Python 3
- requests library: `pip install requests`

## How to run
```
python scanner.py https://example.com
```

## Sample output
```
Scanning https://example.com
FAIL Strict-Transport-Security - Forces HTTPS
FAIL Content-Security-Policy - Blocks XSS
FAIL X-Frame-Options - Prevents clickjacking
FAIL X-Content-Type-Options - Stops MIME sniffing
PASS CORS: None
```

## Results 
1.python Kirti_AutomatedWebScanner.py https://github.com
Scanning https://github.com
PASS Strict-Transport-Security - Forces HTTPS
PASS Content-Security-Policy - Blocks XSS
PASS X-Frame-Options - Prevents clickjacking
PASS X-Content-Type-Options - Stops MIME sniffing
PASS CORS: None
2.python Kirti_AutomatedWebScanner.py https://example.com
Scanning https://example.com
FAIL Strict-Transport-Security - Forces HTTPS
FAIL Content-Security-Policy - Blocks XSS
FAIL X-Frame-Options - Prevents clickjacking
FAIL X-Content-Type-Options - Stops MIME sniffing
PASS CORS: None

## What I learned
- How security headers protect users
- What CORS is and why `*` can be risky
- How to send HTTP requests in Python

  No dataset used

## Disclaimer
Only scan websites you own or have permission to test.
