from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium_stealth import stealth
from time import sleep

def downloadTVideo(link):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("disable-infobars")
     # Set Chrome options for file download
    prefs = {
        "download.default_directory": 'Media/',  # Use the path you defined earlier
    }
    options.add_experimental_option("prefs", prefs)
    chromedriver_path = '/usr/bin/chromedriver'
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service , options=options)
    # driver = webdriver.Chrome()
    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="MacIntel",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True)
    driver.get(url='https://ssstwitter.com/en')
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script("return document.readyState") == "complete")
    search_bar = driver.find_element(By.XPATH, "//input[@placeholder='Insert link']")
    search_bar.send_keys(link)
    search_bar.submit()
    sleep(5)
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script("return document.readyState") == "complete")
    btn = driver.find_element(By.XPATH, '//a[contains(@class, "quality-best")]')
    ActionChains(driver).move_to_element(btn).click().perform()
    sleep(30)
    driver.close()
    return 