from wikiwho_wrapper import WikiWhoAPI, WikiWhoPickleAPI, WikiWho


# def test_wikiwhopickle_all_content_by_id():
#     """Tests an API call to get a all content of a page by id"""

#     api = WikiWhoAPI()
#     df = api.all_content(2161298)

#     ww_pickle_api = WikiWhoPickleAPI(pickle_path='pickles', lng='en')
#     df_pickle = ww_pickle_api.all_content(2161298)

#     assert df == df_pickle


# def test_wikiwhopickle_last_rev_content_by_id():
#     """Tests an API call to get the most recent (last) revision of the given article by id"""

#     ww = WikiWho()
#     df = ww.dv.last_rev_content(2161298)

#     ww_pickle = WikiWho(pickle_path='pickles', lng='en')
#     df_pickle = ww_pickle.dv.last_rev_content(2161298)

#     df_pickle['rev_id'] = df_pickle['rev_id'].astype(str)

#     assert df.equals(df_pickle)


def test_wikiwhopickle_specific_rev_content_by_id():
    """Tests an API call to get the content of the given revision of the given article by id"""

    ww = WikiWho()
    df = ww.dv.specific_rev_content_by_rev_id(363901244)

    ww_pickle = WikiWho(pickle_path='pickles', lng='en')
    df_pickle = ww_pickle.dv.specific_rev_content_by_rev_id(363901244, 2161298)

    df_pickle['rev_id'] = df_pickle['rev_id'].astype(str)

    assert df.equals(df_pickle)


def test_wikiwho_range_rev_content_by_article_title():
    """Tests an API call to get the content of revisions from start revision to end revision ordered by timestamp of the given article by title"""

    ww = WikiWho()
    df = ww.dv.range_rev_content_by_article_title(
        "bioglass", 18064039, 79583319)

    ww_pickle = WikiWho(pickle_path='pickles', lng='en')
    df_pickle = ww_pickle.dv.range_rev_content_by_article_title(
        2161298, 18064039, 79583319)

    df_pickle['rev_id'] = df_pickle['rev_id'].astype(str)

    assert df.equals(df_pickle)


# def test_wikiwho_article_rev_id_by_page_id():
#     """Tests an API call to get revision IDs of the given article as processed by WikiWho of the given article by id"""

#     api = WikiWhoAPI()
#     df = api.rev_ids_of_article(2161298)

#     ww_pickle_api = WikiWhoPickleAPI(pickle_path='pickles', lng='en')
#     df_pickle = ww_pickle_api.rev_ids_of_article(2161298)

#     assert df == df_pickle
