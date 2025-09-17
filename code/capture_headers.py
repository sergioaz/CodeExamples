import asyncio
from playwright.async_api import async_playwright

async def capture_headers():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        # Capture all requests and their headers
        requests_data = []
        
        async def handle_request(request):
            headers = await request.headers_array()
            requests_data.append({
                'url': request.url,
                'method': request.method,
                'headers': headers
            })
            print(f"\n{'='*60}")
            print(f"REQUEST: {request.method} {request.url}")
            print(f"{'='*60}")
            for header in headers:
                print(f"{header['name']}: {header['value']}")
        
        # Listen to all requests
        page.on('request', handle_request)
        
        # Navigate to the Upwork login page
        print("Navigating to Upwork login page...")
        await page.goto('https://www.upwork.com/ab/account-security/login')
        
        # Wait for page to fully load
        await page.wait_for_load_state('networkidle')
        
        # Keep browser open for a moment to capture any additional requests
        await page.wait_for_timeout(3000)
        
        print(f"\n\nCaptured {len(requests_data)} requests")
        
        # Find the main HTML page request
        main_request = None
        for req in requests_data:
            if req['url'] == 'https://www.upwork.com/ab/account-security/login' and req['method'] == 'GET':
                main_request = req
                break
        
        if main_request:
            print(f"\n{'='*80}")
            print("MAIN PAGE REQUEST HEADERS:")
            print(f"{'='*80}")
            for header in main_request['headers']:
                print(f"{header['name']}: {header['value']}")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_headers())
