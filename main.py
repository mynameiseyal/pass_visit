# from email_client import EmailClient
from sel import Selenium
from selenium.webdriver.common.by import By

import os
from pathlib import Path

# parent_username = os.getenv("parent_username")
# parent_password = os.getenv("parent_password")
# email_username = os.getenv("email_username")
# email_password = os.getenv("email_password")
# to_whatsapp_numbers = os.getenv("to_whatsapp_numbers")
# to_email = os.getenv("to_email")

sel = Selenium()
# mail = EmailClient(username=email_username, password=email_password,
#                    recipients=to_email)

if __name__ == '__main__':
    sel.launch_chrome()
    sel.driver.find_element(by=By.XPATH, value="//*[@id='continueSkip']/div[1]/div/a").click()  # Skip account
    sel.driver.implicitly_wait(time_to_wait=3)
    iframe = sel.driver.find_element(by=By.XPATH, value="//*[@id='mCSB_2']")  # locate to inner iframe
    sel.wait()
    iframe = sel.driver.find_element(by=By.XPATH, value="//*[@id='mCSB_2']")  # locate to inner iframe
    sel.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", iframe)  # scroll iframe bottom
    sel.driver.find_element(by=By.XPATH,
                            value="//*[@id='continueSkip']/div[2]/div/div[3]/a").click()  # click continue without account
    sel.driver.implicitly_wait(time_to_wait=15)  # wait for page load. REPLACE
    sel.driver.find_element(by=By.XPATH,
                            value="//span[contains(text(),'לשכת פתח תקוה')]").click()  # select רשות ההגירה
    sel.driver.implicitly_wait(time_to_wait=6)  # wait for page load. REPLACE
    sel.driver.find_element(by=By.XPATH,
                            value="//span[contains(text(),'מוטה גור 4, מגדלי עופר, פתח תקוה')]").click()  # select PT
    sel.driver.implicitly_wait(time_to_wait=4)  # wait for page load. REPLACE
    sel.driver.find_element(by=By.XPATH,
                            value="//div[contains(text(),'בכל פנייה יינתן שירות לפונה/אדם אחד בלבד')]").click()
    sel.driver.implicitly_wait(time_to_wait=4)  # wait for page load. REPLACE
    sel.driver.find_element(by=By.XPATH, value="//input[@id='ID_KEYPAD']").send_keys('060405719')
    sel.driver.find_element(by=By.XPATH, value="//button[contains(text(),'Continue')]").click()
    sel.driver.implicitly_wait(time_to_wait=4)  # wait for page load. REPLACE
    sel.driver.find_element(by=By.XPATH, value="//*[@id='PHONE_KEYPAD']").send_keys('0544931233')
    sel.driver.find_element(by=By.XPATH, value="//button[contains(text(),'Continue')]").click()
    sel.driver.implicitly_wait(time_to_wait=4)  # wait for page load. REPLACE
    sel.driver.find_element(by=By.XPATH, value="//div[contains(text(),'דרכון ביומטרי- ראשון')]").click()
    file = Path(__file__).parent / screenshot
    mail.send_mail_with_file(filename=file)
    sel.quit()
