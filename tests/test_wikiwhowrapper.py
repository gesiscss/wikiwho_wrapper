
from pytest import fixture

from wikiwho_wrapper import WikiWhoAPI

@fixture
def all_content_keys():
    # Responsible only for returning the test data
    return ['id', 'origin_country', 'poster_path', 'name',
              'overview', 'popularity', 'backdrop_path',
              'first_air_date', 'vote_count', 'vote_average']

def test_wikiwho_all_content():
    """Tests an API call to get a TV show's info"""

    api = WikiWhoAPI(6187)
    response = api.all_content()

    assert isinstance(response, dict)
    assert response['page_id'] == 6187, "The ID should be in the response"
    assert set(all_content_keys()).issubset(response.keys()), "All keys should be in the response"