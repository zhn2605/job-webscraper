import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

def scrape_website(website):
    print("Launching browser...")

    chrome_driver_path = "./chromedriver-win64\chromedriver.exe"
    # opera_exe_path = r"C:\Users\zziha\AppData\Local\Programs\Opera GX\opera.exe"
    
    options = webdriver.ChromeOptions()

    # Init driver using chrome service and options
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        # Potential 


        print("Page loaded...")
        html = driver.page_source
        time.sleep(10)


        return html
    finally:
        driver.quit()