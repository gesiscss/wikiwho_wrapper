"""Summary
"""
from typing import Union
import numpy as np
import deprecation

from wikiwho import open_pickle

from . import __version__
from .api import WikiWhoAPI


class WikiWhoPickleAPI(WikiWhoAPI):

    """The WikiWho Pickle API can be used to skip the overhead caused by server requests. It
    however required direct access to the pickles.
    """

    def __init__(self,
                 pickle_path: str="pickles",
                 lng: str="en"):
        """Constructor of the WikiWhoAPI

        Args:
            pickle_path (str, optional): Description
            lng (str, optional): the language that needs to be query
        """
        self.pickle_path = pickle_path
        self.lng = lng

        self.current = ''

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
            article (Union[int, str]): filename of the page without extension, usually the 
                page id (int) or title (str) of the page.
            o_rev_id (bool, optional): Origin revision ID per token
            editor (bool, optional): Editor ID/Name per token
            token_id (bool, optional): Token ID per token
            out (bool, optional): Outbound revision IDs per token
            _in (bool, optional): Outbound revision IDs per token

        Returns:
            dict: result of the api query as documented in 2 - All content in
                https://api.wikiwho.net/en/api/v1.0.0-beta/
        """

        if self.current != article:
            self.ww = open_pickle(article, pickle_path=self.pickle_path, lang=self.lng)
            self.current = article

        # flatten the parameters
        params = []
        if o_rev_id:
            params.append('o_rev_id')
        if editor:
            params.append('editor')
        if token_id:
            params.append('token_id')
        if out:
            params.append('out')
        if _in:
            params.append('in')
        params.append(0)

        return self.ww.get_all_content(params)

    def last_rev_content(self,
                         article: Union[int, str],
                         o_rev_id: bool=True,
                         editor: bool=True,
                         token_id: bool=True,
                         out: bool=True,
                         _in: bool=True):
        """Get the content of the most recent (last) revision of the given article, as available on Wikipedia.

        Args:
            article (Union[int, str]): filename of the page without extension, usually the 
                page id (int) or title (str) of the page.
            o_rev_id (bool, optional): Origin revision ID per token
            editor (bool, optional): Editor ID/Name per token
            token_id (bool, optional): Token ID per token
            out (bool, optional): Outbound revision IDs per token
            _in (bool, optional): Outbound revision IDs per token

        Returns:
            dict: result of the api query as documented in 1 - Content per revision for GET /rev_content/{article_title}/ and GET /rev_content/page_id/{page_id}/ in
                https://api.wikiwho.net/en/api/v1.0.0-beta/
        """

        if self.current != article:
            self.ww = open_pickle(article, pickle_path=self.pickle_path, lang=self.lng)
            self.current = article

        # flatten the parameters
        params = []
        if o_rev_id:
            params.append('o_rev_id')
        if editor:
            params.append('editor')
        if token_id:
            params.append('token_id')
        if out:
            params.append('out')
        if _in:
            params.append('in')

        # return the dictionary
        return self.ww.get_revision_content([self.ww.ordered_revisions[-1]], params)

    def specific_rev_content_by_rev_id(self,
                                       rev_id: int,
                                       article: Union[int, str],
                                       o_rev_id: bool=True,
                                       editor: bool=True,
                                       token_id: bool=True,
                                       out: bool=True,
                                       _in: bool=True):
        """Get the content of the given revision id.

        Args:
            rev_id (int): Revision ID to get content for.
            article (Union[int, str]): filename of the page without extension, usually the 
                page id (int) or title (str) of the page.
            o_rev_id (bool, optional): Origin revision ID per token
            editor (bool, optional): Editor ID/Name per token
            token_id (bool, optional): Token ID per token
            out (bool, optional): Outbound revision IDs per token
            _in (bool, optional): Outbound revision IDs per token

        Returns:
            dict: result of the api query as documented in 1 - Content per revision  for GET /rev_content/rev_id/{rev_id}/ in
                https://api.wikiwho.net/en/api/v1.0.0-beta/
        """

        if self.current != article:
            self.ww = open_pickle(
                article, pickle_path=self.pickle_path, lang=self.lng)
            self.current = article

        # flatten the parameters
        params = []
        if o_rev_id:
            params.append('o_rev_id')
        if editor:
            params.append('editor')
        if token_id:
            params.append('token_id')
        if out:
            params.append('out')
        if _in:
            params.append('in')

        # return the dictionary
        return self.ww.get_revision_content([rev_id], params)


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
            article (Union[int, str]): filename of the page without extension, usually the 
                page id (int) or title (str) of the page.
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

        if self.current != article:
            self.ww = open_pickle(article, pickle_path=self.pickle_path, lang=self.lng)
            self.current = article

        # flatten the parameters
        params = []
        if o_rev_id:
            params.append('o_rev_id')
        if editor:
            params.append('editor')
        if token_id:
            params.append('token_id')
        if out:
            params.append('out')
        if _in:
            params.append('in')

        # return the dictionary
        return self.ww.get_revision_content([start_rev_id, end_rev_id], params)

    def rev_ids_of_article(self,
                           article: Union[int, str],
                           editor: bool=True,
                           timestamp: bool=True):
        """Get revision IDs of an article by given article title or page id.

        Args:
            article (Union[int, str]): filename of the page without extension, usually the 
                page id (int) or title (str) of the page.
            editor (bool, optional): Editor ID/Name per token
            timestamp (bool, optional): timestamp of each revision

        Returns:
            dict: result of the api query as documented in 1 - Content per revision for GET /rev_ids/{article_title}/ and GET /rev_ids/page_id/{page_id}/ in
                https://api.wikiwho.net/en/api/v1.0.0-beta/
        """

        if self.current != article:
            self.ww = open_pickle(article, pickle_path=self.pickle_path, lang=self.lng)
            self.current = article

        # flatten the parameters
        params = []
        if editor:
            params.append('editor')
        if timestamp:
            params.append('timestamp')

        # return the dictionary
        return self.ww.get_revision_ids(params)

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
        raise NotImplementedError("edit_persistence cannot be access through the pickle file. You "
                                  "should use the WikiWhoAPI instead.")

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

        raise NotImplementedError("edit_persistence_as_table cannot be access through the pickle file. You "
                                  "should use the WikiWhoAPI instead.")
