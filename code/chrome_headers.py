#!/usr/bin/env python3

# Typical headers that Chrome sends when visiting https://www.upwork.com/ab/account-security/login

chrome_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'www.upwork.com',
    'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

print("=== TYPICAL CHROME HEADERS FOR UPWORK LOGIN ===\n")
for header, value in chrome_headers.items():
    print(f"{header}: {value}")

print("\n=== INSTRUCTIONS TO GET REAL HEADERS ===")
print("""
To see the actual headers Chrome sends:

1. Open Chrome and press F12 (Developer Tools)
2. Go to the Network tab
3. Visit: https://www.upwork.com/ab/account-security/login
4. Find the first request (usually the HTML document)
5. Click on it and look at the Request Headers section

Or use this curl command to see what headers are expected:
curl -I -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" https://www.upwork.com/ab/account-security/login
""")
