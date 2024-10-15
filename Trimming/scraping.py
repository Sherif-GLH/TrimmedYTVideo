######### scraping on y2mate website to download videos from youtube ##########
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium_stealth import stealth

## method to close  pop upp ##
def closePopUp(driver):
    try:
        time.sleep(1)
        driver.execute_script("""
            const iframes = document.querySelectorAll('iframe');
            iframes.forEach(iframe => iframe.remove());
        """)
    except Exception as e:
        print(f"error: {e}")

## method for download ##
def downloadVideo(id):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("disable-infobars")
     # Set Chrome options for file download
    prefs = {
        "download.default_directory": 'app/Media/',  # Use the path you defined earlier
    }
    options.add_experimental_option("prefs", prefs)
    chromedriver_path = '/usr/bin/chromedriver'
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service , options=options)
    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="MacIntel",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True)
    ## open webdriver for y2mate ##
    driver.get(url=f'https://www.y2mate.com/youtube/{id}/') 
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script("return document.readyState") == "complete")
    closePopUp(driver=driver)
    ## to get the title of video ##
    title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'.//div[@class="caption text-left"]')))
    get_download_button = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,'.//button[@class="btn btn-success"]')))
    closePopUp(driver=driver)
    ActionChains(driver).move_to_element(get_download_button[1]).click().perform()
    get_second_download_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'.//a[@class="btn btn-success btn-file"]')))
    closePopUp(driver=driver)
    ActionChains(driver).move_to_element(get_second_download_button).click().perform()
    time.sleep(50)
    driver.close()
    return str(title) 

    



