
from providers.data.users_provider import UsersProvider


def test_check_login_failed_empty_password(wordpress_ui_client):
    user = UsersProvider.fake_user()

    wordpress_ui_client.login(user['login'], [''])

    assert wordpress_ui_client.get_error_message().text == "Error: The password field is empty."
    assert wordpress_ui_client.get_title() == "WordPress.org Login | WordPress.org English"

def test_check_login_failed_empty_login(wordpress_ui_client):
    user = UsersProvider.fake_user()

    wordpress_ui_client.login([''], user['password'])

    assert wordpress_ui_client.get_error_message().text == "Error: The username field is empty."
    assert wordpress_ui_client.get_title() == "WordPress.org Login | WordPress.org English"

def test_check_login_failed_not_registered_user(wordpress_ui_client):
    user = UsersProvider.fake_user()

    wordpress_ui_client.login(user['login'], user['password'])

    assert wordpress_ui_client.get_error_message().text == "Error: The username kashekfjhkajsdhfkjhsdaf is not registered on WordPress.org. If you're unsure of your username, you can attempt to log in using your email address instead."
    assert wordpress_ui_client.get_title() == "WordPress.org Login | WordPress.org English"


def test_check_login_passed(wordpress_ui_client):
    user = UsersProvider.wordpress_my_user_from_env()

    wordpress_ui_client.login(user['login'], user['password'])

    #assert wordpress_ui_client.get_error_message().text.contains "Error"
    assert wordpress_ui_client.get_title() == "yuliia999 (@yuliia999) – WordPress user profile | WordPress.org"


