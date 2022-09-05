from applications.ui.github_ui import GitHubUI
from config.config import Config
from applications.api.github_api import GitHubAPI
from applications.api.wordpress_api import WordPressAPI
from applications.ui.wordpress_ui import WordPressUI
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session")
def github_api_client():
    github_api_client = GitHubAPI(Config.base_url_api, "v1")

    yield github_api_client

    print("END-UP TEST")


@pytest.fixture()
def github_ui_client():
    driver = webdriver.Chrome(
        service=Service(r"C:\Users\ulga9\Documents\GL\BAQArepo\Homework\become-qa-auto-jul\chromedriver")
    )

    driver.implicitly_wait(15)

    github_ui_client = GitHubUI(Config.base_url_ui, driver)

    yield github_ui_client

    github_ui_client.close_browser()
    
@pytest.fixture()
def wordpress_api_client():
    wordpress_api_client = WordPressAPI(Config.wordpress_base_url_api)

    yield wordpress_api_client

    print("END-UP TEST")

   

@pytest.fixture()
def wordpress_ui_client():
    driver = webdriver.Chrome(
        service=Service(r"C:\Users\ulga9\Documents\GL\BAQArepo\Homework\become-qa-auto-jul\chromedriver")
    )

    driver.implicitly_wait(15)

    wordpress_ui_client = WordPressUI(Config.wordpress_login_url_ui, driver)

    yield wordpress_ui_client

    wordpress_ui_client.close_browser()

    