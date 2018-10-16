
from typing import Union

from . import session


class WikiWhoAPI:
    def __init__(self, lng:str="en", domain="api.wikiwho.net", version="v1.0.0-beta", attempts=2):
        """Constructor of the WikiWhoAPI
        
        Args:
            lng (str, optional): the language that needs to be query
            domain (str, optional): the domain that hosts the api
            version (str, optional): the version of the api
            attempts (int, optional): the number of attempts before giving up trying to connect
        """
        self.id = id
        self.base = f"https://{domain}/{lng}/api/{version}"
        self.attempts = 2

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
        params = f'o_rev_id={o_rev_id}&editor={editor}&token_id={token_id}&out={out}&in={_in}'

        # create the query
        if isinstance(article, int):
            url = f"{self.base}/all_content/page_id/{article}/?{params}"
        else:
            url = f"{self.base}/all_content/{article}/?{params}"

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
                response = session.get(url)
                response.raise_for_status()
                return response.json()
            except Exception as exc:
                if attempt == self.attempts:
                    raise exc
                else:
                    print(f"Connection failed (attempt {attempt + 1} of {self.attempts}) ")
