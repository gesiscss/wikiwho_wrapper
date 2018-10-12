
from wikiwho_wrapper import WikiWhoAPI

def test_wikiwho_all_content():
    """Tests an API call to get a TV show's info"""

    api = WikiWhoAPI(6187)
    response = api.all_content()

    assert isinstance(response, dict)
    assert response['page_id'] == 6187, "The ID should be in the response"