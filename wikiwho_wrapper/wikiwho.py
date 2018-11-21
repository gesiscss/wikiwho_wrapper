"""Summary
"""
from .api import WikiWhoAPI
from .views import DataView


class WikiWho:

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
        """Constructor of the WikiWho

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

        self.api = WikiWhoAPI(wikiwho_api_username,
                              wikiwho_api_password,
                              wikiwho_api_key,
                              lng,
                              protocol,
                              domain,
                              version,
                              attempts)

        self.dv = DataView(self.api)
