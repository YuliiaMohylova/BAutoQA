from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class WordPressUI:

    def __init__(self, base_url, driver) -> None:
        self.base_url = base_url
        self.driver = driver

    def login(self, username, userpassword):
        self.driver.get(f"{self.base_url}")

        elem = self.driver.find_element(By.ID, "user_login")
        elem.send_keys(username)

        elem = self.driver.find_element(By.ID, "user_pass")
        elem.send_keys(userpassword)

        elem.send_keys(Keys.RETURN)

        return True

    def close_browser(self):
        self.driver.close()

    def get_title(self):
        return self.driver.title

    def get_error_message(self):
        return self.driver.find_element(By.ID, "login_error")    


    def get_user_profile_link(self):
        return self.driver.find_element(By.CLASS_NAME, "wrapper")

