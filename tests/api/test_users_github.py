from providers.data.users_provider import UsersProvider
import requests
import pytest


def test_http_status_code200(github_api_client):
    r = requests.get('https://api.github.com/zen')

    assert r.status_code == 200


def test_user_exists(github_api_client):
    user = UsersProvider().existing_user()

    api_user = github_api_client.get_user(user['login'])

    assert api_user['login'] == user['login']
    assert api_user['id'] == user['id']


def test_user_non_exists(github_api_client):
    user = UsersProvider.fake_user()

    with pytest.raises(requests.exceptions.HTTPError):
        github_api_client.get_user(user['login'])
