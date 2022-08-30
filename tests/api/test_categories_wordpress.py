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

    #assert r.status_code == 404
    #assert categories['count'] == category['count']
  

# def test_check_categories_exist(wordpress_api_client):
#     category = CategoriesProvider.existing_category()
#     categories = wordpress_api_client.get_category([])

#     assert categories['count'] >= category['count']


# def test_check_total_count_eq_to_items_length_for_exsiting_category(wordpress_api_client):
#     category = CategoriesProvider.existing_category()
#     categories = wordpress_api_client.get_category(category['id'])

#     assert len(categories['items']) >= category['items_count']
  