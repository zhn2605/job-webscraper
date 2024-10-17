import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

def scrape_website(website):
    print("Launching browser...")

    opera_driver_path = r"C:\ProgramData\Microsoft Visual Studio\operadriver_win64"
    opera_exe_path = r"C:\Users\zziha\AppData\Local\Programs\Opera GX\opera.exe"
    
    options = webdriver.ChromeOptions()
    options.binary_location = opera_exe_path
    options.add_experimental_option('w3c', True)
    webdriver_service = Service(opera_driver_path)
    driver = webdriver.Remote(service=(webdrivergit _service), options=options)

    try:
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source
        time.sleep(10)

        return html
    finally:
        driver.quit()


