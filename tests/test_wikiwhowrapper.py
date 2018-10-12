
from pytest import fixture

from wikiwho_wrapper import WikiWhoAPI


@fixture
def all_content_keys():
    # Responsible only for returning the test data
    return [ "message", "success", "page_id", "article_title", "all_tokens", ]

def test_wikiwho_all_content_by_id():
    """Tests an API call to get a all content of a page"""

    api = WikiWhoAPI(6187)
    response = api.all_content()

    assert isinstance(response, dict)
    assert response['page_id'] == 6187, "The ID should be in the response"
    assert set(all_content_keys()).issubset(response.keys()), "All keys should be in the response"


def test_wikiwho_all_content_by_name():
    """Tests an API call to get a all content of a page"""

    api = WikiWhoAPI("Cologne")
    response = api.all_content()

    assert isinstance(response, dict)
    assert response['page_id'] == 6187, "The ID should be in the response"
    assert set(all_content_keys()).issubset(response.keys()), "All keys should be in the response"