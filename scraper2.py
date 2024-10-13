from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from time import sleep
# Chrome options

driver = webdriver.Chrome()

driver.get("https://linkedin.com/login/")

username_field = driver.find_element(By.ID, "username")
username_field.send_keys('sakrmo788@gmail.com')
# Find and fill in the password field
password_field = driver.find_element(By.ID, "password")
password_field.send_keys('Polo_1991')

sign_in_btn = driver.find_element(By.XPATH, "//button[normalize-space(text())='Sign in']")
sign_in_btn.click()
WebDriverWait(driver, 15).until(lambda driver: driver.execute_script("return document.readyState") == "complete")

try:
    verify_button = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, "//button[@class='DRUpX']")))
    ActionChains(driver).move_to_element(verify_button).click().perform()
except:
    print("No 'Verify' button found")

driver.maximize_window()
driver.get("https://www.linkedin.com/job-posting/?trk=nav_spotlight_post_job&")
sleep(2)
job_title = "Backend Developer"
Company = "orientation code"
job_location = "Maadi"
workspace_type = "Hybrid"
job_type = "Volunteer"
description = """ 
this is the description of the job that will be created in the database and will be used to create a new job
this is the description of the job that will be created in the database and will be used to create a new job
this is the description of the job that will be created in the database and will be used to create a new job
this is the description of the job that will be created in the database and will be used to create a new job 
"""
questions = {
    "are you exprienced in back end development ?" : "yes" ,
    "If yes how many years are you experienced in development ?": 3,
    "what is your expected salary?": 10000,
    "have you finised your military service?" :"no" , 
}
tags = ['Python', 'django', 'backend' ]

title = driver.find_element(By.XPATH, '//input[contains(@class, "artdeco-typeahead__input")]')
title.send_keys(Keys.CONTROL + "a")
title.send_keys(Keys.BACKSPACE)
title.send_keys(job_title)
sleep(2)
ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
ActionChains(driver).send_keys(Keys.ENTER).perform()
sleep(5)
btn = driver.find_element(By.XPATH, '//button[contains(@class, "job-posting-wow-1step__cta-btn-secondary")]')
driver.execute_script("arguments[0].click();", btn)
sleep(4)
## End OF THE FIRST PAGE ## 
company_name = driver.find_element(By.XPATH, '//input[contains(@class, "job-posting-shared-company-typeahead__input")]')
ActionChains(driver).move_to_element(company_name).click().perform()
company_name.send_keys(Keys.CONTROL + "a")  
company_name.send_keys(Keys.BACKSPACE)
company_name.send_keys(Company)

workplace = driver.find_element(By.XPATH, '//button[contains(@class, "job-posting-shared-workplace-type-selection__dropdown-trigger")]')
ActionChains(driver).move_to_element(workplace).click().perform()
sleep(1)
menuitems = driver.find_elements(By.XPATH, './/div[@role="menuitem"]')
print(menuitems)
for item in menuitems:
        print(item.text)
        sleep(3)
        if workspace_type in item.text:
            ActionChains(driver).move_to_element(item).click().perform()
            break

if workspace_type == 'Remote':
    location = driver.find_element(By.XPATH, '//input[@placeholder="Country or state"]')
    location.send_keys(Keys.CONTROL + "a")
    location.send_keys(Keys.BACKSPACE)    
    location.send_keys(job_location)
    sleep(2)
    ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
else:
    location = driver.find_element(By.CSS_SELECTOR, '.artdeco-typeahead__input[placeholder=""]')
    location.send_keys(Keys.CONTROL + "a")
    location.send_keys(Keys.BACKSPACE)
    location.send_keys(job_location)
    sleep(2)
    ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()

type = driver.find_element(By.XPATH, '//button[contains(@class, "job-posting-shared-job-type-dropdown__trigger")]')
ActionChains(driver).move_to_element(type).click().perform()

sleep(3)
menuitem = driver.find_elements(By.XPATH, './/div[@role="menuitem"]')
for item in menuitem:
     print(item.text)
     if job_type in item.text:
         ActionChains(driver).move_to_element(item).click().perform()
         break
     
description_input = driver.find_element(By.XPATH, '//div[@class="ql-editor"]')
description_input.clear()
description_input.send_keys(description)

cancel_icons = driver.find_elements(By.XPATH, '//li-icon[@class="artdeco-pill__icon"]')

for icon in cancel_icons:
    ActionChains(driver).move_to_element(icon).click().perform()

for tag in tags:
    input_skill = driver.find_element(By.XPATH,'//input[contains(@class, "job-posting-shared-job-skill-typeahead__ta-trigger")]')
    ActionChains(driver).move_to_element(input_skill).click().perform()
    input_skill.send_keys(tag)
    sleep(2)
    ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()

next_button = driver.find_element(By.XPATH, '//button[span[text()="Next"]]')
driver.execute_script("arguments[0].click();", next_button)
# ActionChains(driver).move_to_element(next_button).click().perform()
WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, './/button[contains(@class, "artdeco-button--tertiary ember-view artdeco-card__dismiss")]')))
close_signs = driver.find_elements(By.XPATH, './/button[contains(@class, "artdeco-button--tertiary ember-view artdeco-card__dismiss")]')

for sign in close_signs:
    ActionChains(driver).move_to_element(sign).click().perform()

for i in range(0, len(questions)):
    new_question = driver.find_element(By.XPATH, "//div[@class='inline']")  
    ActionChains(driver).move_to_element(new_question).click().perform()
input_questions = driver.find_elements(By.XPATH, '//section[contains(@class, "artdeco-card display-flex")]')

for (question, answer), input_question in zip(questions.items(), input_questions):
    sleep(2)
    # input_question = driver.find_element(By.XPATH, '//textarea[contains(@class, "job-posting-shared-custom-question-description__input")]')
    textarea = input_question.find_element(By.XPATH, './/textarea[contains(@class, "job-posting-shared-custom-question-description__input")]')
    textarea.send_keys(question)
    label_question = input_question.find_element(By.XPATH, './/div[contains(@class, "job-posting-shared-custom-question-response-type")]')
    ActionChains(driver).move_to_element(label_question).click().perform()

    if isinstance(answer, str):
        ActionChains(driver).move_to_element(label_question).send_keys("y").perform()
        label_answer = input_question.find_element(By.XPATH, './/div[contains(@class, "job-posting-shared-ideal-answer-custom-question")]')
        ActionChains(driver).move_to_element(label_answer).click().perform()

        if answer == "yes":
            ActionChains(driver).move_to_element(label_answer).send_keys("y").perform()
        elif answer == "no":
            ActionChains(driver).move_to_element(label_answer).send_keys("n").perform() 

    if isinstance(answer, (int, float)):
        ActionChains(driver).move_to_element(label_question).send_keys("n").perform()
        label_answer = input_question.find_element(By.XPATH, './/div[contains(@class, "job-posting-shared-ideal-answer-custom-question")]')
        ActionChains(driver).move_to_element(label_answer).click().perform()
        ActionChains(driver).send_keys(Keys.CONTROL + "a").perform() 
        ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
        ActionChains(driver).send_keys(answer).perform()

    checkbox = input_question.find_element(By.XPATH, './/div[contains(@class, "job-posting-shared-must-have-qualification")]')
    ActionChains(driver).move_to_element(checkbox).click().perform()
continue_button = driver.find_element(By.XPATH, '//button[@data-validate-submit-type="Next"]')
ActionChains(driver).move_to_element(continue_button).click().perform()
sleep(10)
promote_button = driver.find_element(By.XPATH, '//button[contains(@class, "job-posting-footer__secondary-cta")]')

# Perform click action
ActionChains(driver).move_to_element(promote_button).click().perform()
print("last line ")
sleep(1000)