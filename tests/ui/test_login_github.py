
from providers.data.users_provider import UsersProvider


def test_check_login_failed(github_ui_client):
    user = UsersProvider.fake_user()

    github_ui_client.login(user['login'], user['password'])

    assert github_ui_client.get_error_banner().text == "Incorrect username or password."
    assert github_ui_client.get_title() == "Sign in to GitHub · GitHub"


def test_check_login_passed(github_ui_client):
    user = UsersProvider.existing_user_from_env()

    github_ui_client.login(user['login'], user['password'])
    # assert github_ui_client.get_title() == "GitHub"

    github_ui_client.get_user_avatar().click()
    assert github_ui_client.get_user_profile_link().text == "Signed in as YuliiaMohylova"

