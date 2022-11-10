import selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

EMAIL = "@yandex.ru"
PASSWORD = "pass"
RESUME = ["https://",
          "https://"]

        
def login(email, password):
        
    driver.get("https://rostov.hh.ru/account/login?backurl=%2F&hhtmFrom=main")
    
    actions.move_to_element(driver.find_element(By.XPATH, '//div[@class="account-login-actions"]/button[@class="bloko-link bloko-link_pseudo"]')).click()
    actions.perform()

    time.sleep(1)

    driver.find_element(By.XPATH, '//fieldset[@class="bloko-input-text-wrapper"]/input[@class="bloko-input-text"]')\
          .send_keys(email)

    driver.find_element(By.XPATH, '//fieldset[@class="bloko-input-text-wrapper bloko-input-text-wrapper_icon-right"]/input[@aria-label="Введите пароль"]')\
          .send_keys(password)

    time.sleep(1)

    actions.move_to_element(driver.find_element(By.XPATH, '//div[@class="account-login-actions"]/button[@class="bloko-button bloko-button_kind-primary"]'))\
           .click()
    actions.perform()
    time.sleep(5)


def click_update(html):

    driver.get(html)
    time.sleep(3)
    
    try:
        actions.move_to_element(driver.find_elements(By.XPATH, '//button[@class="bloko-button bloko-button_kind-primary bloko-button_stretched"]')[2]).click()
        actions.perform()
    except Exception as ex:
        print(ex)
    

while True:

    service = Service(executable_path=ChromeDriverManager().install())
        
    driver = webdriver.Chrome(service=service)
    actions = ActionChains(driver)
        
    login(EMAIL,PASSWORD)
    for resume in RESUME:
        click_update(resume)  

    driver.quit()
    
    for i in range(24):
        print(f"{240 - i * 10} minutes left")
        time.sleep(600)
    
