import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

def scrape_website(website):
    print("Launching browser...")

    chrome_driver_path = "./chromedriver-win64/chromedriver.exe"
    # opera_exe_path = r"C:\Users\zziha\AppData\Local\Programs\Opera GX\opera.exe"
    
    options = webdriver.ChromeOptions()
    # options.binary_location = opera_exe_path
    # options.add_experimental_option('w3c', True)

    # Create driver path
    # webdriver_service = service.Service(opera_driver_path)

    # Init driver using chrome service and options
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source
        time.sleep(10)

        return html
    finally:
        driver.quit()