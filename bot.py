import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("🚀 Starting WhatsApp Bot on GitHub Actions...")

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    print("Opening WhatsApp Web...")
    driver.get("https://web.whatsapp.com")
    
    print("Waiting for login...")
    WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='chat-list']"))
    )
    
    print("✓ Login successful!")
    time.sleep(3)
    
    print("Viewing statuses...")
    items = driver.find_elements(By.XPATH, "//div[@role='button']//span[@dir='auto']")
    print(f"Found {len(items)} items")
    
    viewed = 0
    for item in items[:5]:
        try:
            name = item.text
            if name and name.strip():
                print(f"Viewing: {name}")
                driver.execute_script("arguments[0].scrollIntoView(true);", item)
                time.sleep(0.3)
                parent = item.find_element(By.XPATH, "ancestor::div[@role='button']")
                parent.click()
                time.sleep(1.5)
                
                try:
                    back = driver.find_element(By.XPATH, "//button[@aria-label='Back']")
                    back.click()
                    time.sleep(0.3)
                except:
                    pass
                
                viewed += 1
        except:
            pass
    
    print(f"✓ Viewed {viewed} statuses!")

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()
    print("✓ Bot finished!")
