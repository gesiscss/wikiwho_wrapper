import pandas as pd
import itertools
from typing import Union


from .api import WikiWhoAPI


class APIQuerier:

    def __init__(self, api):
        self.api = api

    def all_content(self,
                    article: Union[int, str],
                    o_rev_id: bool=True,
                    editor: bool=True,
                    token_id: bool=True,
                    out: bool=True,
                    _in: bool=True) -> pd.DataFrame:

        response = self.api.all_content(article)

        # rows = []

        # for myVal in response["all_tokens"]:

        #     if not (len(myVal["out"]) == len(myVal["in"]) or
        #             len(myVal["out"]) == len(myVal["in"]) + 1):
        #         raise Exception("Difference lists length!")

        #     for i, (_in, _out) in enumerate(zip(itertools.chain((-1,), myVal["in"]),
        #                                         itertools.chain(myVal["out"], (-1,)))):
        #         each_row = (
        #             response["article_title"],
        #             response["page_id"],
        #             myVal["o_rev_id"],
        #             myVal["editor"],
        #             myVal["str"],
        #             myVal["token_id"],
        #             _in,
        #             _out)

        #         rows.append(each_row)

        rows = ((response["article_title"],
                 response["page_id"],
                 myVal["o_rev_id"],
                 myVal["editor"],
                 myVal["str"],
                 myVal["token_id"],
                 _in,
                 _out)

                for myVal in response["all_tokens"]
                for i, (_in, _out) in enumerate(zip(itertools.chain((-1,), myVal["in"]),
                                                    itertools.chain(myVal["out"], (-1,)))))

        df = pd.DataFrame(data=rows, columns=[
            'article_title', 'page_id', 'o_rev_id', 'o_editor', 'token', 'token_id', 'in', 'out'])

        return df

    def last_rev_content(self,
                         article: Union[int, str],
                         o_rev_id: bool=True,
                         editor: bool=True,
                         token_id: bool=True,
                         out: bool=True,
                         _in: bool=True) -> pd.DataFrame:

        response = self.api.last_rev_content(article)

        rows = ((response["article_title"],
                 response["page_id"],
                 token_dict["o_rev_id"],
                 token_dict["editor"],
                 rev_id,
                 rev_dict['editor'],
                 rev_dict['time'],
                 token_dict["str"],
                 token_dict["token_id"],
                 #_in,
                 #_out
                 )

                for dummy_rev in response["revisions"]
                for rev_id, rev_dict in dummy_rev.items()
                for token_dict in rev_dict['tokens']
                # for i, (_in, _out) in enumerate(zip(itertools.chain((-1,), token_dict["in"]),
                # itertools.chain(token_dict["out"], (-1,))))
                )

        df = pd.DataFrame(data=rows, columns=[
            'article_title', 'page_id', 'o_rev_id', 'o_editor', 'rev_id', 'rev_editor', 'rev_time', 'token', 'token_id',  # 'in', 'out'
        ])

        return df

    def specific_rev_content_by_rev_id(self,
                                       rev_id: int,
                                       o_rev_id: bool=True,
                                       editor: bool=True,
                                       token_id: bool=True,
                                       out: bool=True,
                                       _in: bool=True) -> pd.DataFrame:

        # use the wrapper to query the api
        response = self.api.specific_rev_content_by_rev_id(rev_id)

        rows = ((response["article_title"],
                 response["page_id"],
                 token_dict["o_rev_id"],
                 token_dict["editor"],
                 rev_id,
                 rev_dict['editor'],
                 rev_dict['time'],
                 token_dict["str"],
                 token_dict["token_id"],
                 #_in,
                 #_out
                 )

                for dummy_rev in response["revisions"]
                for rev_id, rev_dict in dummy_rev.items()
                for token_dict in rev_dict['tokens']
                # for i, (_in, _out) in enumerate(zip(itertools.chain((-1,), token_dict["in"]),
                # itertools.chain(token_dict["out"], (-1,))))
                )

        df = pd.DataFrame(data=rows, columns=[
            'article_title', 'page_id', 'o_rev_id', 'o_editor', 'rev_id', 'rev_editor', 'rev_time', 'token', 'token_id',  # 'in', 'out'
        ])

        return df

    def specific_rev_content_by_article_title(self,
                                              article: str,
                                              rev_id: int,
                                              o_rev_id: bool=True,
                                              editor: bool=True,
                                              token_id: bool=True,
                                              out: bool=True,
                                              _in: bool=True) -> pd.DataFrame:

        # use the wrapper to query the api
        response = self.api.specific_rev_content_by_article_title(
            article, rev_id)

        rows = ((response["article_title"],
                 response["page_id"],
                 token_dict["o_rev_id"],
                 token_dict["editor"],
                 rev_id,
                 rev_dict['editor'],
                 rev_dict['time'],
                 token_dict["str"],
                 token_dict["token_id"],
                 #_in,
                 #_out
                 )

                for dummy_rev in response["revisions"]
                for rev_id, rev_dict in dummy_rev.items()
                for token_dict in rev_dict['tokens']
                # for i, (_in, _out) in enumerate(zip(itertools.chain((-1,), token_dict["in"]),
                # itertools.chain(token_dict["out"], (-1,))))
                )

        df = pd.DataFrame(data=rows, columns=[
            'article_title', 'page_id', 'o_rev_id', 'o_editor', 'rev_id', 'rev_editor', 'rev_time', 'token', 'token_id',  # 'in', 'out'
        ])

        return df

    def range_rev_content_by_article_title(self,
                                           article: str,
                                           start_rev_id: int,
                                           end_rev_id: int,
                                           o_rev_id: bool=True,
                                           editor: bool=True,
                                           token_id: bool=True,
                                           out: bool=True,
                                           _in: bool=True) -> pd.DataFrame:

        # use the wrapper to query the api
        response = self.api.range_rev_content_by_article_title(
            article_title, start_rev_id, end_rev_id)

        rows = ((response["article_title"],
                 response["page_id"],
                 token_dict["o_rev_id"],
                 token_dict["editor"],
                 rev_id,
                 rev_dict['editor'],
                 rev_dict['time'],
                 token_dict["str"],
                 token_dict["token_id"],
                 #_in,
                 #_out
                 )

                for dummy_rev in response["revisions"]
                for rev_id, rev_dict in dummy_rev.items()
                for token_dict in rev_dict['tokens']
                # for i, (_in, _out) in enumerate(zip(itertools.chain((-1,), token_dict["in"]),
                # itertools.chain(token_dict["out"], (-1,))))
                )

        df = pd.DataFrame(data=rows, columns=[
            'article_title', 'page_id', 'o_rev_id', 'o_editor', 'rev_id', 'rev_editor', 'rev_time', 'token', 'token_id',  # 'in', 'out'
        ])

        return df

    def rev_ids_of_article(self,
                           article: Union[int, str],
                           editor: bool=True,
                           timestamp: bool=True) -> pd.DataFrame:

        response = self.api.rev_ids_of_article(article)

        rows = ((response["article_title"],
                 response["page_id"],
                 rev['timestamp'],
                 rev['id'],
                 rev['editor']
                 )

                for rev in response["revisions"]
                )

        df = pd.DataFrame(data=rows, columns=[
            'article_title', 'page_id', 'rev_time', 'rev_id', 'o_editor'
        ])

        return df
