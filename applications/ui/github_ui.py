from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class GitHubUI:

    def __init__(self, base_url, driver) -> None:
        self.base_url = base_url
        self.driver = driver

    def login(self, username, userpassword):
        self.driver.get(f"{self.base_url}/login")

        elem = self.driver.find_element(By.ID, "login_field")
        elem.send_keys(username)

        elem = self.driver.find_element(By.ID, "password")
        elem.send_keys(userpassword)

        elem.send_keys(Keys.RETURN)

        return True

    def close_browser(self):
        self.driver.close()

    def get_title(self):
        return self.driver.title

    def get_error_banner(self):
        return self.driver.find_element(By.CLASS_NAME, "flash-error")

    def get_user_avatar(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[aria-label='View profile and more'] .dropdown-caret")

    def get_user_profile_link(self):
        return self.driver.find_element(By.CLASS_NAME, "user-profile-link")

