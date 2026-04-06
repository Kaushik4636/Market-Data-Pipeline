import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new") # Using the newer headless engine
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--remote-debugging-port=9222") # Prevents certain hang-ups
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)

def scrape_trending_tickers(retries=3):
    for i in range(retries):
        driver = get_driver()
        try:
            print(f"🔗 Attempt {i+1}: Connecting to Yahoo Finance...")
            driver.get("https://finance.yahoo.com/trending-tickers")
            
            # Shorter wait but more specific
            wait = WebDriverWait(driver, 20)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tbody tr")))
            
            rows = driver.find_elements(By.CSS_SELECTOR, "tbody tr")
            tickers = []
            for row in rows[:10]:
                cols = row.find_elements(By.TAG_NAME, "td")
                if len(cols) >= 5:
                    tickers.append({
                        "Symbol": cols[0].text,
                        "Name": cols[1].text,
                        "Price": cols[2].text,
                        "Change": cols[3].text,
                        "Percent_Change": cols[4].text
                    })
            
            if tickers:
                print("✅ Data successfully extracted.")
                return tickers
                
        except Exception as e:
            print(f"⚠️ Attempt {i+1} failed: {e}")
            time.sleep(2) # Wait before retrying
        finally:
            driver.quit()
    
    return []

if __name__ == "__main__":
    data = scrape_trending_tickers()
    if data:
        print(pd.DataFrame(data))
    else:
        print("❌ All attempts failed. Check your internet or if Yahoo is blocking you.")