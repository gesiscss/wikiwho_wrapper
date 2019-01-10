
from pytest import fixture

from wikiwho_wrapper import WikiWhoAPI


@fixture
def all_content_keys():
    # Responsible only for returning the test data
    return ["message", "success", "page_id", "article_title", "all_tokens"]


@fixture
def rev_content_keys():
    # Responsible only for returning the test data
    return ["message", "success", "page_id", "article_title", "revisions"]


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


def test_wikiwho_last_rev_content_by_id(rev_content_keys):
    """Tests an API call to get the most recent (last) revision of the given article by id"""

    api = WikiWhoAPI()
    response = api.last_rev_content(6187)

    assert isinstance(response, dict)
    assert response['page_id'] == 6187, "The ID should be in the response"
    assert set(rev_content_keys).issubset(
        response.keys()), "All keys should be in the response"


def test_wikiwho_last_rev_content_by_title(rev_content_keys):
    """Tests an API call to get the most recent (last) revision of the given article by title"""

    api = WikiWhoAPI()
    response = api.last_rev_content("Cologne")

    assert isinstance(response, dict)
    assert response['page_id'] == 6187, "The ID should be in the response"
    assert set(rev_content_keys).issubset(
        response.keys()), "All keys should be in the response"


def test_wikiwho_specific_rev_content_by_id(rev_content_keys):
    """Tests an API call to get the content of the given revision of the given article by id"""

    api = WikiWhoAPI()
    response = api.specific_rev_content_by_rev_id(503680497)

    assert isinstance(response, dict)
    assert '503680497' in response['revisions'][
        0], "The ID should be in the response"
    # assert response['success'] == True, "success should be true in the response"
    assert set(rev_content_keys).issubset(
        response.keys()), "All keys should be in the response"


# def test_wikiwho_specific_rev_content_by_title(rev_content_keys):
#     """Tests an API call to get the content of the given revision of the given article by title"""

#     api = WikiWhoAPI()
#     response = api.specific_rev_content_by_article_title("Cologne", 503680497)

#     assert isinstance(response, dict)
#     assert response['page_id'] == 6187, "The ID should be in the response"
#     assert '503680497' in response['revisions'][
#         0], "The ID should be in the response"
#     assert set(rev_content_keys).issubset(
#         response.keys()), "All keys should be in the response"


def test_wikiwho_range_rev_content_by_article_title(rev_content_keys):
    """Tests an API call to get the content of revisions from start revision to end revision ordered by timestamp of the given article by title"""

    api = WikiWhoAPI()
    response = api.range_rev_content_by_article_title(
        "bioglass", 18064039, 79583319)

    assert isinstance(response, dict)
    assert response['page_id'] == 2161298, "The ID should be in the response"
    assert '18064039' in response['revisions'][
        0], "The ID should be in the response"
    assert len(response['revisions']) == 10
    assert set(rev_content_keys).issubset(
        response.keys()), "All keys should be in the response"


def test_wikiwho_article_rev_id_by_page_id(rev_content_keys):
    """Tests an API call to get revision IDs of the given article as processed by WikiWho of the given article by id"""

    api = WikiWhoAPI()
    response = api.rev_ids_of_article(2161298)

    assert isinstance(response, dict)
    assert response['page_id'] == 2161298, "The ID should be in the response"
    assert len(response['revisions']) >= 176
    assert set(rev_content_keys).issubset(
        response.keys()), "All keys should be in the response"


def test_wikiwho_article_rev_id_by_article_title(rev_content_keys):
    """Tests an API call to get revision IDs of the given article as processed by WikiWho of the given article by title"""

    api = WikiWhoAPI()
    response = api.rev_ids_of_article("bioglass")

    assert isinstance(response, dict)
    assert response['page_id'] == 2161298, "The ID should be in the response"
    assert set(rev_content_keys).issubset(
        response.keys()), "All keys should be in the response"
