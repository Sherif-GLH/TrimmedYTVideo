######### scraping on y2mate website to download videos from youtube ##########
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium_stealth import stealth
import time, os, glob, random, shutil, string, requests, re

### method to generate random string 10 charachters ###
def randomName():
    all_charachters = list(string.ascii_letters)
    random_chars = random.sample(all_charachters, 10)
    name = ''.join(random_chars)
    return name

## method to remove any special charachters from string ##
def remove_special_characters(input_string):
    # Use regular expression to remove any character that is not a letter or number
    clean_string = re.sub(r'[^A-Za-z0-9 ]+', '', input_string)
    return clean_string

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
    # Ensure you use the absolute path #
    download_directory = os.path.abspath('Media/') 
    ## options and services of chrome driver ## 
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("disable-infobars")
    # Set Chrome options for file download
    prefs = {
        "download.default_directory": download_directory ,  # Use the path you defined earlier
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
    ## open webdriver for y2mate ##
    driver.get(url=f'https://www.y2mate.com/youtube/{id}/') 
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script("return document.readyState") == "complete")
    closePopUp(driver=driver)
    ## to get the title of video ##
    title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'.//div[@class="caption text-left"]'))).text
    ## get the quality text ##
    quality = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME,'td')))[3].text.split(" ")
    get_download_button = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,'.//button[@class="btn btn-success"]')))
    closePopUp(driver=driver)
    ActionChains(driver).move_to_element(get_download_button[1]).click().perform()
    get_second_download_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'.//a[@class="btn btn-success btn-file"]')))
    print("text: ",get_second_download_button.text)
    closePopUp(driver=driver)
    # ActionChains(driver).move_to_element(get_second_download_button).click().perform()
    link_of_download = get_second_download_button.get_attribute('href')
    print("link:" , link_of_download)
    requests.get(url=link_of_download)
    # get_second_download_button.click()
    ## remove special charachters from title ##
    # new_title = remove_special_characters(input_string=title)
    ## request on download link ##
    print("Starting download...")
    time.sleep(80)
    # response = requests.get(url=link_of_download, stream=True)
    # if response.status_code == 200:
    #     file_path = os.path.join(download_directory, f"{new_title}.mp4")
    #     print(new_title)
    #     print(file_path)
    #     with open(file_path, 'wb') as f:
    #         for chunk in response.iter_content(chunk_size=8192):
    #             f.write(chunk)
    #     print(f"Downloaded video saved as {file_path}")
    driver.close()
    ## get random name ##
    name = randomName()
    # Rename the downloaded video #
    original_file = max(glob.glob(f'{download_directory}/*'), key=os.path.getatime)  # Get the latest file
    new_filename = os.path.join(download_directory, f"{name}_{quality[0]}.mp4")
    
    # Rename the file
    try:
        shutil.move(original_file, new_filename)
    except Exception as e:
        print(f"Error renaming file: {e}")
    return str(title) , f'{str(name)}_{quality[0]}'

    



