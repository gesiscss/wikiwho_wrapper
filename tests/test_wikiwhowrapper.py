
from pytest import fixture

from wikiwho_wrapper import WikiWhoAPI


@fixture
def all_content_keys():
    # Responsible only for returning the test data
    return ["message", "success", "page_id", "article_title", "all_tokens"]


def test_wikiwho_all_content_by_id(all_content_keys):
    """Tests an API call to get a all content of a page by id"""

    api = WikiWhoAPI()
    response = api.all_content(6187)

    assert isinstance(response, dict)
    assert response['page_id'] == 6187, "The ID should be in the response"
    assert set(all_content_keys).issubset(
        response.keys()), "All keys should be in the response"


def test_wikiwho_all_content_by_title(all_content_keys):
    """Tests an API call to get a all content of a page by title"""

    api = WikiWhoAPI()
    response = api.all_content("Cologne")

    assert isinstance(response, dict)
    assert response['page_id'] == 6187, "The ID should be in the response"
    assert set(all_content_keys).issubset(
        response.keys()), "All keys should be in the response"
