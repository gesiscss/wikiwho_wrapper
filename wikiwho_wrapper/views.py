"""Summary
"""
import pandas as pd
import itertools
from typing import Union

import deprecation

from .api import WikiWhoAPI
from . import __version__


class DataView:

    """Qurey methods for correspondence of the WikiWhoAPI methods

    Attributes:
        api (TYPE): Description
    """

    def __init__(self, api):
        """Constructor of the DataView

        Args:
            api (TYPE): the WikiWhoAPI
        """
        self.api = api

    def __get_iterator(self, token_dict, _in, out):
        if _in and out:
            return enumerate(zip(
                itertools.chain((-1,), token_dict["in"]) if _in else (None,),
                itertools.chain(token_dict["out"], (-1,)) if out else (None,)
            ))
        elif _in:
            return enumerate(itertools.zip_longest(
                itertools.chain((-1,), token_dict["in"]) if _in else (None,),
                itertools.chain(token_dict["out"], (-1,)) if out else (None,)
            ))
        elif out:
            return enumerate(itertools.zip_longest(
                itertools.chain((-1,), token_dict["in"]) if _in else (None,),
                itertools.chain(token_dict["out"]) if out else (None,)
            ))
        else:
            return enumerate(itertools.zip_longest(
                itertools.chain((-1,), token_dict["in"]) if _in else (None,),
                itertools.chain(token_dict["out"], (-1,)) if out else (None,)
            ))

    def all_content(self,
                    article: Union[int, str],
                    o_rev_id: bool=True,
                    editor: bool=True,
                    token_id: bool=True,
                    out: bool=True,
                    _in: bool=True) -> pd.DataFrame:
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
            pd.DataFrame: Return a Pandas DataFrame of the api query as documented in 2 - All content in
                https://api.wikiwho.net/en/api/v1.0.0-beta/
        """
        response = self.api.all_content(
            article, o_rev_id, editor, token_id, out, _in)

        rows = ((response["article_title"],
                 response["page_id"],
                 token_dict["o_rev_id"] if o_rev_id else None,
                 token_dict["editor"] if editor else None,
                 token_dict["str"],
                 token_dict["token_id"] if token_id else None,
                 _i,
                 _o)

                for token_dict in response["all_tokens"]
                for i, (_i, _o) in self.__get_iterator(token_dict, _in, out)
                )

        df = pd.DataFrame(data=rows, columns=[
            'article_title', 'page_id', 'o_rev_id', 'o_editor', 'token', 'token_id', 'in', 'out'
        ])

        return df.drop(columns=[name for name, include in zip(
            ['o_rev_id', 'o_editor', 'token_id', 'in', 'out'],
            [o_rev_id, editor, token_id, _in, out]) if not include
        ])

    def last_rev_content(self,
                         article: Union[int, str],
                         o_rev_id: bool=True,
                         editor: bool=True,
                         token_id: bool=True,
                         out: bool=False,
                         _in: bool=False) -> pd.DataFrame:
        """Get the content of the most recent (last) revision of the given article, as available on Wikipedia.

        Args:
            article (Union[int, str]): page id (int) or title (str) of the page.
            o_rev_id (bool, optional): Origin revision ID per token
            editor (bool, optional): Editor ID/Name per token
            token_id (bool, optional): Token ID per token
            out (bool, optional): Outbound revision IDs per token
            _in (bool, optional): Outbound revision IDs per token

        Returns:
            pd.DataFrame: Return a Pandas DataFrame of the api query as documented in 1 - Content per revision for GET /rev_content/{article_title}/ and GET /rev_content/page_id/{page_id}/ in
                https://api.wikiwho.net/en/api/v1.0.0-beta/
        """

        response = self.api.last_rev_content(
            article, o_rev_id, editor, token_id, out, _in)

        rows = ((response["article_title"],
                 response["page_id"],
                 token_dict["o_rev_id"] if o_rev_id else None,
                 token_dict["editor"] if editor else None,
                 rev_id,
                 rev_dict['editor'] if editor else None,
                 rev_dict['time'],
                 token_dict["str"],
                 token_dict["token_id"] if token_id else None,
                 _i,
                 _o)

                for dummy_rev in response["revisions"]
                for rev_id, rev_dict in dummy_rev.items()
                for token_dict in rev_dict['tokens']
                for i, (_i, _o) in self.__get_iterator(token_dict, _in, out)
                )

        df = pd.DataFrame(data=rows, columns=[
            'article_title', 'page_id', 'o_rev_id', 'o_editor', 'rev_id', 
            'rev_editor', 'rev_time', 'token', 'token_id', 'in', 'out'
        ])

        return df.drop(columns=[name for name, include in zip(
            ['o_rev_id', 'o_editor', 'rev_editor', 'token_id', 'in', 'out'],
            [o_rev_id, editor, editor, token_id, _in, out]) if not include
        ])

    def specific_rev_content_by_rev_id(self,
                                       rev_id: int,
                                       article_title=None,
                                       o_rev_id: bool=True,
                                       editor: bool=True,
                                       token_id: bool=True,
                                       out: bool=False,
                                       _in: bool=False) -> pd.DataFrame:
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
            pd.DataFrame: Return a Pandas DataFrame of the api query as documented in 1 - Content per revision  for GET /rev_content/rev_id/{rev_id}/ in
                https://api.wikiwho.net/en/api/v1.0.0-beta/
        """
        response = self.api.specific_rev_content_by_rev_id(
            rev_id, article_title, o_rev_id, editor, token_id, out, _in)

        rows = ((response["article_title"],
                 response["page_id"],
                 token_dict["o_rev_id"] if o_rev_id else None,
                 token_dict["editor"] if editor else None,
                 rev_id,
                 rev_dict['editor'] if editor else None,
                 rev_dict['time'],
                 token_dict["str"],
                 token_dict["token_id"] if token_id else None,
                 _i,
                 _o
                 )

                for dummy_rev in response["revisions"]
                for rev_id, rev_dict in dummy_rev.items()
                for token_dict in rev_dict['tokens']
                for i, (_i, _o) in self.__get_iterator(token_dict, _in, out)
                )

        df = pd.DataFrame(data=rows, columns=[
            'article_title', 'page_id', 'o_rev_id', 'o_editor', 'rev_id', 
            'rev_editor', 'rev_time', 'token', 'token_id', 'in', 'out'
        ])

        return df.drop(columns=[name for name, include in zip(
            ['o_rev_id', 'o_editor', 'rev_editor', 'token_id', 'in', 'out'],
            [o_rev_id, editor, editor, token_id, _in, out]) if not include
        ])

    @deprecation.deprecated(deprecated_in="1.4", removed_in="1.6",
                            current_version=__version__,
                            details=("Use the specific_rev_content_by_rev_id function with the article_title parameter instead."))
    def specific_rev_content_by_article_title(self,
                                              article: str,
                                              rev_id: int,
                                              o_rev_id: bool=True,
                                              editor: bool=True,
                                              token_id: bool=True,
                                              out: bool=False,
                                              _in: bool=False) -> pd.DataFrame:
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
            pd.DataFrame: Return a Pandas DataFrame of the api query as documented in 1 - Content per revision  for GET /rev_content/{article_title}/{rev_id}/ in
                https://api.wikiwho.net/en/api/v1.0.0-beta/
        """

        response = self.api.specific_rev_content_by_article_title(
            article, rev_id, o_rev_id, editor, token_id, out, _in)

        rows = ((response["article_title"],
                 response["page_id"],
                 token_dict["o_rev_id"] if o_rev_id else None,
                 token_dict["editor"] if editor else None,
                 rev_id,
                 rev_dict['editor'] if editor else None,
                 rev_dict['time'],
                 token_dict["str"],
                 token_dict["token_id"] if token_id else None,
                 _i,
                 _o
                 )

                for dummy_rev in response["revisions"]
                for _, rev_dict in dummy_rev.items()
                for token_dict in rev_dict['tokens']
                for i, (_i, _o) in self.__get_iterator(token_dict, _in, out)
                )

        df = pd.DataFrame(data=rows, columns=[
            'article_title', 'page_id', 'o_rev_id', 'o_editor', 'rev_id', 
            'rev_editor', 'rev_time', 'token', 'token_id', 'in', 'out'
        ])

        return df.drop(columns=[name for name, include in zip(
            ['o_rev_id', 'o_editor', 'rev_editor', 'token_id', 'in', 'out'],
            [o_rev_id, editor, editor, token_id, _in, out]) if not include
        ])

    def range_rev_content_by_article_title(self,
                                           article: str,
                                           start_rev_id: int,
                                           end_rev_id: int,
                                           o_rev_id: bool=True,
                                           editor: bool=True,
                                           token_id: bool=True,
                                           out: bool=False,
                                           _in: bool=False) -> pd.DataFrame:
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
            pd.DataFrame: Return a Pandas DataFrame of the api query as documented in 1 - Content per revision  for GET /rev_content/{article_title}/{start_rev_id}/{end_rev_id}/ in
                https://api.wikiwho.net/en/api/v1.0.0-beta/
        """

        response = self.api.range_rev_content_by_article_title(
            article, start_rev_id, end_rev_id, o_rev_id, editor, token_id, out, _in)

        rows = ((response["article_title"],
                 response["page_id"],
                 token_dict["o_rev_id"] if o_rev_id else None,
                 token_dict["editor"] if editor else None,
                 rev_id,
                 rev_dict['editor'] if editor else None,
                 rev_dict['time'],
                 token_dict["str"],
                 token_dict["token_id"] if token_id else None,
                 _i,
                 _o
                 )

                for dummy_rev in response["revisions"]
                for rev_id, rev_dict in dummy_rev.items()
                for token_dict in rev_dict['tokens']
                for i, (_i, _o) in self.__get_iterator(token_dict, _in, out)
                )

        df = pd.DataFrame(data=rows, columns=[
            'article_title', 'page_id', 'o_rev_id', 'o_editor', 'rev_id', 
            'rev_editor', 'rev_time', 'token', 'token_id', 'in', 'out'
        ])

        return df.drop(columns=[name for name, include in zip(
            ['o_rev_id', 'o_editor', 'rev_editor', 'token_id', 'in', 'out'],
            [o_rev_id, editor, editor, token_id, _in, out]) if not include
        ])

    def rev_ids_of_article(self,
                           article: Union[int, str],
                           editor: bool=True,
                           timestamp: bool=True) -> pd.DataFrame:
        """Get revision IDs of an article by given article title or page id.

        Args:
            article (Union[int, str]): page id (int) or title (str) of the page.
            editor (bool, optional): Editor ID/Name per token
            timestamp (bool, optional): timestamp of each revision

        Returns:
            pd.DataFrame: Return a Pandas DataFrame of the api query as documented in 1 - Content per revision for GET /rev_ids/{article_title}/ and GET /rev_ids/page_id/{page_id}/ in
                https://api.wikiwho.net/en/api/v1.0.0-beta/
        """
        response = self.api.rev_ids_of_article(article, editor, timestamp)

        rows = ((response["article_title"],
                 response["page_id"],
                 rev['timestamp'] if timestamp else None,
                 rev['id'],
                 rev['editor'] if editor else None
                 )

                for rev in response["revisions"]
                )

        df = pd.DataFrame(data=rows, columns=[
            'article_title', 'page_id', 'rev_time', 'rev_id', 'o_editor'
        ])

        return df.drop(columns=[name for name, include in zip(
            ['rev_time', 'o_editor'],
            [timestamp, editor]) if not include
        ])

    @deprecation.deprecated(deprecated_in="1.5", removed_in="1.6",
                            current_version=__version__,
                            details="Use the edit_persistence function instead.")
    def actions(self,
                page_id: int=None,
                editor_id: int=None,
                start: str=None,
                end: str=None) -> pd.DataFrame:
        """Get monthly editons for given editor id.

        Args:
            page_id (int, optional): page id (int).   
            editor_id (int, optional): editor id (int).
            start (str, optional): Origin revision ID per token
            end (str, optional): Editor ID/Name per token

        Returns:
            pd.DataFrame: Return a Pandas DataFrame of the api query as documented in /editor/{editor_id}/ in
                https://www.wikiwho.net/en/edit_persistence/v1.0.0-beta/
        """
        response = self.api.edit_persistence(page_id, editor_id, start, end)

        rows = ((element['year_month'],
                 element["page_id"],
                 element["editor_id"],
                 element["adds"],
                 element["adds_surv_48h"],
                 element["adds_persistent"],
                 element["adds_stopword_count"],
                 element["dels"],
                 element["dels_surv_48h"],
                 element["dels_persistent"],
                 element["dels_stopword_count"],
                 element["reins"],
                 element["reins_surv_48h"],
                 element["reins_persistent"],
                 element["reins_stopword_count"],
                 )

                for element in response["editions"]
                )

        df = pd.DataFrame(data=rows, columns=[
            'year_month', 'page_id', 'editor_id',
            'adds', 'adds_surv_48h', 'adds_persistent', 'adds_stopword_count',
            'dels', 'dels_surv_48h', 'dels_persistent', 'dels_stopword_count',
            'reins', 'reins_surv_48h', 'reins_persistent', 'reins_stopword_count'
        ])

        return df

    @deprecation.deprecated(deprecated_in="1.5", removed_in="1.6",
                            current_version=__version__,
                            details="Use the edit_persistence function instead.")
    def actions_as_table(self,
                         page_id: int=None,
                         editor_id: int=None,
                         start: str=None,
                         end: str=None) -> pd.DataFrame:
        """Get monthly editons in tabular format for given page id or editor id or both.

        Args:
            page_id (int, optional): page id (int).   
            editor_id (int, optional): editor id (int).
            start (str, optional): Origin revision ID per token
            end (str, optional): Editor ID/Name per token

        Returns:
            pd.DataFrame: Return a Pandas DataFrame of the api query as documented in /editor/{editor_id}/ in
                https://www.wikiwho.net/en/edit_persistence/v1.0.0-beta/
        """
        response = self.api.edit_persistence_as_table(
            page_id, editor_id, start, end)

        df = pd.DataFrame(data=response['editions_data'], columns=response[
                          'editions_columns'])

        return df

    def edit_persistence(self,
                                  page_id: int=None,
                                  editor_id: int=None,
                                  start: str=None,
                                  end: str=None) -> pd.DataFrame:
        """Get monthly editons for given editor id.

        Args:
            page_id (int, optional): page id (int).   
            editor_id (int, optional): editor id (int).
            start (str, optional): Origin revision ID per token
            end (str, optional): Editor ID/Name per token

        Returns:
            pd.DataFrame: Return a Pandas DataFrame of the api query as documented in /editor/{editor_id}/ in
                https://www.wikiwho.net/en/edit_persistence/v1.0.0-beta/
        """
        response = self.api.edit_persistence_as_table(
            page_id, editor_id, start, end)

        df = pd.DataFrame(data=response['editions_data'], columns=response[
                          'editions_columns'])

        return df
