from providers.data.users_provider import UsersProvider
import requests
import pytest


def test_http_status_code200(wordpress_api_client):
    r = requests.get('https://techcrunch.com/wp-json/wp/v2')

    assert r.status_code == 200


def test_user_exists(wordpress_api_client):
    user = UsersProvider().wordpress_existing_user()

    api_user = wordpress_api_client.get_user(user['id'])

    assert api_user['id'] == user['id']
    assert api_user['name'] == user['name']


def test_user_non_exists(wordpress_api_client):
    user = UsersProvider.fake_user()
    
    with pytest.raises(requests.exceptions.HTTPError):
        wordpress_api_client.get_user(user['id'])
    
