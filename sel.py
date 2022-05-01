import time
from datetime import datetime
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from consts import *

path = Path(__file__).parent
today = datetime.today().strftime('%d-%m-%Y')


class Selenium:
    def __init__(self):
        options = Options()
        # options.add_argument("--headless")  # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox')  # Bypass OS security model
        options.add_argument('--disable-gpu')  # applicable to windows os only
        options.add_argument('start-maximized')  #
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)

    def launch_chrome(self):
        self.driver.get(BASE_URL)
        time.sleep(10)

    def wait(self, wait_time=2):
        self.driver.implicitly_wait(time_to_wait=wait_time)

    def save_screenshot(self):
        original_size = self.driver.get_window_size()
        required_width = self.driver.execute_script('return document.body.parentNode.scrollWidth')
        required_height = self.driver.execute_script('return document.body.parentNode.scrollHeight')
        # driver.save_screenshot(path)  # has scrollbar
        self.driver.set_window_size(required_width, required_height)
        try:
            self.driver.find_element_by_tag_name('body').screenshot(path)  # avoids scrollbar
            self.driver.set_window_size(original_size['width'], original_size['height'])
        except Exception:
            pass
        screenshot = f"ISHUR_{today}.png"
        # self.driver.refresh()
        time.sleep(5)
        self.driver.get_screenshot_as_file(screenshot)
        return screenshot

    def delete_file(self):
        file_name = f"ISHUR_{today}.png"
        for filename in path.iterdir():
            if filename.is_file():
                if filename.name == file_name:
                    filename.unlink()

    def quit(self):
        self.delete_file()
        self.driver.quit()
        time.sleep(10)
