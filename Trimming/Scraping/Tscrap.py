from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium_stealth import stealth
from time import sleep
from .YTscrap import randomName
import shutil , glob , os

def downloadTVideo(link):
    # Ensure you use the absolute path #
    download_directory = os.path.abspath('Media/')  
    print("link",link)
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("disable-infobars")
    # Set Chrome options for file download
    prefs = {
        "download.default_directory": download_directory , # Use the path you defined earlier
        "safebrowsing.enabled": True , # Enable safe browsing for downloads
    }
    options.add_experimental_option("prefs", prefs)
    chromedriver_path = '/usr/bin/chromedriver'
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service , options=options)
    ## stealth for browsing as a human ##
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
    print("text of button",btn.text)
    ActionChains(driver).move_to_element(btn).click().perform()
    sleep(80)
    driver.close()
    ## get random name ##
    name = randomName()
    # Rename the downloaded video #
    original_file = max(glob.glob(f'{download_directory}/*'), key=os.path.getatime)  # Get the latest file
    print("original_file",original_file)
    new_filename = os.path.join(download_directory, f"{name}.mp4")
    print(f"new file name : {new_filename}")
    
    # # Rename the file #
    try:
        shutil.move(original_file, new_filename)
    except Exception as e:
        print(f"Error renaming file: {e}")
    return  name 