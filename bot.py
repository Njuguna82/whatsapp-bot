import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print("🚀 Starting WhatsApp Bot...")

try:
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--start-maximized')
    
    # Use system Chrome instead of webdriver-manager
    driver = webdriver.Chrome(options=options)
    
    print("Opening WhatsApp Web...")
    driver.get("https://web.whatsapp.com")
    
    print("Waiting for QR scan (60 seconds)...")
    time.sleep(60)
    
    print("✓ Bot ran successfully!")

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

finally:
    try:
        driver.quit()
    except:
        pass
