import os


class Config:
    base_url_api = os.environ.get("BASE_URL_API")
    base_url_ui = os.environ.get("BASE_URL_UI", 'https://github.com')
    wordpress_base_url_api = os.environ.get("WP_BASE_URL_API")
    wordpress_login_url_ui = os.environ.get("BASE_URL_UI", 'https://login.wordpress.org/wp-login.php')