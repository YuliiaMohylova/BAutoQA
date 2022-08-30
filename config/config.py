import os


class Config:
    wordpress_base_url_api = os.environ.get("WP_BASE_URL_API", 'https://techcrunch.com/wp-json/wp/v2')
    wordpress_login_url_ui = os.environ.get("WP_BASE_URL_UI", 'https://login.wordpress.org/wp-login.php')