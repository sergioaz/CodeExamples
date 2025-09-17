import asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

async def auto_login():
    async with async_playwright() as p:
        # Launch with more realistic browser settings
        browser = await p.chromium.launch(
            headless=False,
            args=[
                '--disable-blink-features=AutomationControlled',
                '--disable-features=VizDisplayCompositor',
                '--disable-web-security',
                '--disable-dev-shm-usage',
                '--no-sandbox'
            ]
        )
        
        # Use a Windows Chrome User-Agent that matches your OS
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        page = await browser.new_page(
            user_agent=user_agent,
            extra_http_headers={
              'Host': "www.upwork.com",
              'Connection': 'keep - alive',
              'Cache-Control': 'max-age=0',
              'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
              'sec-ch-ua-full-version': "138.0.7204.101",
              'sec-ch-ua-arch': "x86",
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
              'Accept-Encoding': 'gzip, deflate, br, zstd',
              'Accept-Language': 'en-US,en;q=0.9,uk;q=0.8,ru;q=0.7',
              'sec-ch-ua-platform-version': "19.0.0",
              'sec-ch-ua-bitness': "64",
              'Sec-Ch-Ua-Mobile': '?0',
              'Sec-Ch-Ua-Platform': "Windows",
              'Sec-Fetch-Dest': 'document',
              'Sec-Fetch-Mode': 'navigate',
              'Sec-Fetch-Site': 'same-origin',
              'Sec-Fetch-User': '?1',
              'Upgrade-Insecure-Requests': '1'
          }
          )
        
        # Add stealth scripts to hide automation
        await page.add_init_script("""
            // Remove webdriver property
            Object.defineProperty(navigator, 'webdriver', {
                get: () => false,
            });
            
            // Mock chrome object
            window.chrome = {
                runtime: {},
                loadTimes: function() {},
                csi: function() {},
            };
            
            // Mock plugins
            Object.defineProperty(navigator, 'plugins', {
                get: () => [1, 2, 3, 4, 5],
            });
            
            // Mock languages
            Object.defineProperty(navigator, 'languages', {
                get: () => ['en-US', 'en'],
            });
        """)
        
        try:
            await page.goto('https://www.upwork.com/account-security/login')
                        
            # Wait for the page to load and find the username field
            # Upwork uses different selectors, let's try multiple approaches
            username_selectors = [
                'input[name="username"]',
                'input[id="login_username"]', 
                'input[data-qa="login_username"]',
                '#login_username',
                'input[type="email"]'
            ]
            
            username_field = None
            for selector in username_selectors:
                try:
                    await page.wait_for_selector(selector, timeout=5000)
                    username_field = selector
                    print(f"Found username field with selector: {selector}")
                    break
                except PlaywrightTimeoutError:
                    continue
            
            if username_field:
                await page.fill(username_field, 'srmitin@yahoo.com')
                print("Successfully filled username field")
                
                # Now find and click the Continue button
                continue_selectors = [
                    'button:has-text("Continue")',
                    'input[type="submit"][value="Continue"]',
                    'button[data-qa="btn-continue"]',
                    'button[id*="continue"]',
                    'button[class*="continue"]',
                    'input[type="submit"]',
                    'button[type="submit"]'
                ]
                
                continue_button = None
                for selector in continue_selectors:
                    try:
                        await page.wait_for_selector(selector, timeout=5000)
                        continue_button = selector
                        print(f"Found Continue button with selector: {selector}")
                        break
                    except PlaywrightTimeoutError:
                        continue
                
                if continue_button:
                    await page.click(continue_button)
                    print("Successfully clicked Continue button")
                    
                    # Wait a moment for the page to process
                    #await page.wait_for_timeout(2000)
                    #print("Waiting for next page to load...")
                else:
                    print("Could not find Continue button")
            else:
                print("Could not find username field")
                
        except Exception as e:
            print(f"Error during login process: {e}")
            
        # Optional: Keep browser open to see the result
        await page.wait_for_timeout(50000)
        #await browser.close()

asyncio.run(auto_login())