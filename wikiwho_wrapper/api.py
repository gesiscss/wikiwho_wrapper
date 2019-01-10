"""Summary
"""
from typing import Union

import os
import requests
import deprecation

from . import __version__


class WikiWhoAPI:

    """The APIs provide provenance and change information about the tokens a Wikipedia article consists of, for several languages. Apart from the source language edition they draw from, their specifications and usage are identical

    Attributes:
        attempts (int): Number of attempts to be done to the server
        base (url): Base request url
        base_editor (TYPE): Description
        session (TYPE): Description
    """

    def __init__(self,
                 wikiwho_api_username: str=None,
                 wikiwho_api_password: str=None,
                 wikiwho_api_key: str=None,
                 lng: str="en",
                 protocol: str="https",
                 domain: str="api.wikiwho.net",
                 version: str="v1.0.0-beta",
                 attempts: int=2):
        """Constructor of the WikiWhoAPI

        Args:
            wikiwho_api_username (str, optional): WikiWho API username
            wikiwho_api_password (str, optional): WikiWho API password
            wikiwho_api_key (str, optional): WikiWho API key
            lng (str, optional): the language that needs to be query
            protocol (str, optional): the protocol of the url
            domain (str, optional): the domain that hosts the api
            version (str, optional): the version of the api
            attempts (int, optional): the number of attempts before giving up trying to connect
        """

        self.session = requests.Session()
        if wikiwho_api_username and wikiwho_api_password:
            self.session.auth = (wikiwho_api_username, wikiwho_api_password)

        if wikiwho_api_key:
            self.session.params = {}
            self.session.params['api_key'] = WIKIWHO_API_KEY

        self.base = f"{protocol}://{domain}/{lng}/api/{version}"
        self.base_editor = f"{protocol}://{domain}/{lng}/edit_persistence/{version}"
        self.attempts = attempts

    def all_content(self,
                    article: Union[int, str],
                    o_rev_id: bool=True,
                    editor: bool=True,
                    token_id: bool=True,
                    out: bool=True,
                    _in: bool=True):
        """Get all content on an article, i.e. Outputs all tokens that have ever existed 
        in a given article, including their change history for each.

        Args:
            article (Union[int, str]): page id (int) or title (str) of the page.
            o_rev_id (bool, optional): Origin revision ID per token
            editor (bool, optional): Editor ID/Name per token
            token_id (bool, optional): Token ID per token
            out (bool, optional): Outbound revision IDs per token
            _in (bool, optional): Outbound revision IDs per token

        Returns:
            dict: result of the api query as documented in 2 - All content in 
                https://api.wikiwho.net/en/api/v1.0.0-beta/
        """

        # flatten the parameters
        params = f'o_rev_id={o_rev_id}&editor={editor}&token_id={token_id}&out={out}&in={_in}'.lower()

        # create the query
        if isinstance(article, int):
            url = f"{self.base}/all_content/page_id/{article}/?{params}"
        else:
            url = f"{self.base}/all_content/{article}/?{params}"

        # return the dictionary
        return self.request(url)

    def last_rev_content(self,
                         article: Union[int, str],
                         o_rev_id: bool=True,
                         editor: bool=True,
                         token_id: bool=True,
                         out: bool=True,
                         _in: bool=True):
        """Get the content of the most recent (last) revision of the given article, as available on Wikipedia.

        Args:
            article (Union[int, str]): page id (int) or title (str) of the page.
            o_rev_id (bool, optional): Origin revision ID per token
            editor (bool, optional): Editor ID/Name per token
            token_id (bool, optional): Token ID per token
            out (bool, optional): Outbound revision IDs per token
            _in (bool, optional): Outbound revision IDs per token

        Returns:
            dict: result of the api query as documented in 1 - Content per revision for GET /rev_content/{article_title}/ and GET /rev_content/page_id/{page_id}/ in 
                https://api.wikiwho.net/en/api/v1.0.0-beta/
        """

        # flatten the parameters
        params = f'o_rev_id={o_rev_id}&editor={editor}&token_id={token_id}&out={out}&in={_in}'.lower()

        # create the query
        if isinstance(article, int):
            url = f"{self.base}/rev_content/page_id/{article}/?{params}"
        else:
            url = f"{self.base}/rev_content/{article}/?{params}"

        # return the dictionary
        return self.request(url)

    def specific_rev_content_by_rev_id(self,
                                       rev_id: int,
                                       article_title=None,
                                       o_rev_id: bool=True,
                                       editor: bool=True,
                                       token_id: bool=True,
                                       out: bool=True,
                                       _in: bool=True):
        """Get the content of the given revision id.

        Args:
            rev_id (int): Revision ID to get content for.
            article_title (None, optional): the title of the article of the revision
            o_rev_id (bool, optional): Origin revision ID per token
            editor (bool, optional): Editor ID/Name per token
            token_id (bool, optional): Token ID per token
            out (bool, optional): Outbound revision IDs per token
            _in (bool, optional): Outbound revision IDs per token

        Returns:
            dict: result of the api query as documented in 1 - Content per revision  for GET /rev_content/rev_id/{rev_id}/ in 
                https://api.wikiwho.net/en/api/v1.0.0-beta/
        """

        # flatten the parameters
        params = f'o_rev_id={o_rev_id}&editor={editor}&token_id={token_id}&out={out}&in={_in}'.lower()

        if article_title is None:
            url = f"{self.base}/rev_content/rev_id/{rev_id}/?{params}"
        else:
            url = f"{self.base}/rev_content/{article_title}/{rev_id}/?{params}"

        # return the dictionary
        return self.request(url)

    @deprecation.deprecated(deprecated_in="1.4", removed_in="1.6",
                            current_version=__version__,
                            details=("Use the specific_rev_content_by_rev_id function with the article_title parameter instead."))
    def specific_rev_content_by_article_title(self,
                                              article: str,
                                              rev_id: int,
                                              o_rev_id: bool=True,
                                              editor: bool=True,
                                              token_id: bool=True,
                                              out: bool=True,
                                              _in: bool=True):
        """Get the content of the given revision of the given article title.

        Args:
            article (str): Title (str) of the page.
            rev_id (int): Revision ID to get content for.
            o_rev_id (bool, optional): Origin revision ID per token
            editor (bool, optional): Editor ID/Name per token
            token_id (bool, optional): Token ID per token
            out (bool, optional): Outbound revision IDs per token
            _in (bool, optional): Outbound revision IDs per token

        Returns:
            dict: result of the api query as documented in 1 - Content per revision  for GET /rev_content/{article_title}/{rev_id}/ in 
                https://api.wikiwho.net/en/api/v1.0.0-beta/
        """

        # flatten the parameters
        params = f'o_rev_id={o_rev_id}&editor={editor}&token_id={token_id}&out={out}&in={_in}'.lower()

        url = f"{self.base}/rev_content/{article}/{rev_id}/?{params}"

        # return the dictionary
        return self.request(url)

    def range_rev_content_by_article_title(self,
                                           article: str,
                                           start_rev_id: int,
                                           end_rev_id: int,
                                           o_rev_id: bool=True,
                                           editor: bool=True,
                                           token_id: bool=True,
                                           out: bool=True,
                                           _in: bool=True):
        """Get the content of a range of revisions of an article, by given article title, start revison id and end revison id.

        Args:
            article (str): Title (str) of the page.
            start_rev_id (int): Start revision ID
            end_rev_id (int): End revision ID
            o_rev_id (bool, optional): Origin revision ID per token
            editor (bool, optional): Editor ID/Name per token
            token_id (bool, optional): Token ID per token
            out (bool, optional): Outbound revision IDs per token
            _in (bool, optional): Outbound revision IDs per token

        Returns:
            dict: result of the api query as documented in 1 - Content per revision  for GET /rev_content/{article_title}/{start_rev_id}/{end_rev_id}/ in 
                https://api.wikiwho.net/en/api/v1.0.0-beta/
        """

        # flatten the parameters
        params = f'o_rev_id={o_rev_id}&editor={editor}&token_id={token_id}&out={out}&in={_in}'.lower()

        url = f"{self.base}/rev_content/{article}/{start_rev_id}/{end_rev_id}/?{params}"

        # return the dictionary
        return self.request(url)

    def rev_ids_of_article(self,
                           article: Union[int, str],
                           editor: bool=True,
                           timestamp: bool=True):
        """Get revision IDs of an article by given article title or page id.

        Args:
            article (Union[int, str]): page id (int) or title (str) of the page.
            editor (bool, optional): Editor ID/Name per token
            timestamp (bool, optional): timestamp of each revision

        Returns:
            dict: result of the api query as documented in 1 - Content per revision for GET /rev_ids/{article_title}/ and GET /rev_ids/page_id/{page_id}/ in 
                https://api.wikiwho.net/en/api/v1.0.0-beta/
        """

        # flatten the parameters
        params = f'editor={editor}&timestamp={timestamp}'.lower()

        # create the query
        if isinstance(article, int):
            url = f"{self.base}/rev_ids/page_id/{article}/?{params}"
        else:
            url = f"{self.base}/rev_ids/{article}/?{params}"

        # return the dictionary
        return self.request(url)

    @deprecation.deprecated(deprecated_in="1.4", removed_in="1.6",
                            details="Use the edit_persistence function instead.")
    def actions(self,
                page_id: int=None,
                editor_id: int=None,
                start: str=None,
                end: str=None):
        """Get monthly editons for given page id or editor id or both.

        Args:
            page_id (int, optional): page id (int).
            editor_id (int, optional): editor id (int).
            start (str, optional): Origin revision ID per token
            end (str, optional): Editor ID/Name per token

        Returns:
            dict: result of the api query as documented in /editor/{editor_id}/ in 
                https://www.wikiwho.net/en/edit_persistence/v1.0.0-beta/
        """

        # flatten the parameters
        params = ''
        if start and end:
            params = f'start={start}&end={end}'
        elif start:
            params = f'start={start}'
        elif end:
            params = f'end={end}'

        if page_id and editor_id:
            url = f"{self.base_editor}/page/editor/{page_id}/{editor_id}/?{params}"
        elif editor_id:
            url = f"{self.base_editor}/editor/{editor_id}/?{params}"
        elif page_id:
            url = f"{self.base_editor}/page/{page_id}/?{params}"

        # return the dictionary
        return self.request(url)

    @deprecation.deprecated(deprecated_in="1.4", removed_in="1.6",
                            current_version=__version__,
                            details="Use the edit_persistence_as_table function instead.")
    def actions_as_table(self,
                         page_id: int=None,
                         editor_id: int=None,
                         start: str=None,
                         end: str=None):
        """Get monthly editons in tabular format for given page id or editor id or both.

        Args:
            page_id (int, optional): page id (int).
            editor_id (int, optional): editor id (int).
            start (str, optional): Origin revision ID per token
            end (str, optional): Editor ID/Name per token

        Returns:
            dict: result of the api query as documented in /editor/{editor_id}/ in 
                https://www.wikiwho.net/en/edit_persistence/v1.0.0-beta/
        """

        # flatten the parameters
        params = ''
        if start and end:
            params = f'start={start}&end={end}'
        elif start:
            params = f'start={start}'
        elif end:
            params = f'end={end}'

        if page_id and editor_id:
            url = f"{self.base_editor}/as_table/page/editor/{page_id}/{editor_id}/?{params}"
        elif editor_id:
            url = f"{self.base_editor}/as_table/editor/{editor_id}/?{params}"
        elif page_id:
            url = f"{self.base_editor}/as_table/page/{page_id}/?{params}"

        # return the dictionary
        return self.request(url)

    def edit_persistence(self,
                         page_id: int=None,
                         editor_id: int=None,
                         start: str=None,
                         end: str=None):
        """Get monthly editons for given page id or editor id or both.

        Args:
            page_id (int, optional): page id (int).
            editor_id (int, optional): editor id (int).
            start (str, optional): Origin revision ID per token
            end (str, optional): Editor ID/Name per token

        Returns:
            dict: result of the api query as documented in /editor/{editor_id}/ in 
                https://www.wikiwho.net/en/edit_persistence/v1.0.0-beta/
        """

        # flatten the parameters
        params = ''
        if start and end:
            params = f'start={start}&end={end}'
        elif start:
            params = f'start={start}'
        elif end:
            params = f'end={end}'

        if page_id and editor_id:
            url = f"{self.base_editor}/page/editor/{page_id}/{editor_id}/?{params}"
        elif editor_id:
            url = f"{self.base_editor}/editor/{editor_id}/?{params}"
        elif page_id:
            url = f"{self.base_editor}/page/{page_id}/?{params}"

        # return the dictionary
        return self.request(url)

    def edit_persistence_as_table(self,
                                  page_id: int=None,
                                  editor_id: int=None,
                                  start: str=None,
                                  end: str=None):
        """Get monthly editons in tabular format for given page id or editor id or both.

        Args:
            page_id (int, optional): page id (int).
            editor_id (int, optional): editor id (int).
            start (str, optional): Origin revision ID per token
            end (str, optional): Editor ID/Name per token

        Returns:
            dict: result of the api query as documented in /editor/{editor_id}/ in 
                https://www.wikiwho.net/en/edit_persistence/v1.0.0-beta/
        """

        # flatten the parameters
        params = ''
        if start and end:
            params = f'start={start}&end={end}'
        elif start:
            params = f'start={start}'
        elif end:
            params = f'end={end}'

        if page_id and editor_id:
            url = f"{self.base_editor}/as_table/page/editor/{page_id}/{editor_id}/?{params}"
        elif editor_id:
            url = f"{self.base_editor}/as_table/editor/{editor_id}/?{params}"
        elif page_id:
            url = f"{self.base_editor}/as_table/page/{page_id}/?{params}"

        # return the dictionary
        return self.request(url)

    def request(self, url: str, tries=2) -> dict:
        """Do the request

        Args:
            url (str): The request url
            tries (int, optional): the number of attemts to be done in the server

        Returns:
            dict: The results of the request

        Raises:
            exc: If a connection has failed
        """

        for attempt in range(0, self.attempts + 1):
            try:
                response = self.session.get(url)
                response.raise_for_status()
                return response.json()
            except Exception as exc:
                if attempt == self.attempts:
                    raise exc
                else:
                    print(f"Connection failed (attempt {attempt + 1} of {self.attempts}) ")
