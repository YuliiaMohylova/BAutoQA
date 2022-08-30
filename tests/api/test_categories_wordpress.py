from providers.data.categories_provider import CategoriesProvider
import requests
import pytest

def test_check_category_can_be_found(wordpress_api_client):
    category = CategoriesProvider.existing_category()
    categories = wordpress_api_client.get_category(category['id'])

    assert categories['count'] >= category['count']


def test_check_category_cannot_be_found(wordpress_api_client):
    category = CategoriesProvider.non_existing_category()
    with pytest.raises(requests.exceptions.HTTPError):
     wordpress_api_client.get_category(category['id'])

    