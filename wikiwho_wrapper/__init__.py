import os
import requests

WIKIWHO_API_USERNAME = os.environ.get('WIKIWHO_API_USERNAME', None)
WIKIWHO_API_PASSWORD = os.environ.get('WIKIWHO_API_PASSWORD', None)
# WIKIWHO_API_KEY = os.environ.get('WIKIWHO_API_KEY', None)


# class APIKeyMissingError(Exception):
#     pass

# if WIKIWHO_API_KEY is None:
#     raise APIKeyMissingError(
#         "All methods require an API key."
#     )

session = requests.Session()
if WIKIWHO_API_USERNAME and WIKIWHO_API_PASSWORD:
    session.auth = (WIKIWHO_API_USERNAME, WIKIWHO_API_PASSWORD)
#session.params = {}
#session.params['api_key'] = WIKIWHO_API_KEY


from .api import WikiWhoAPI
from .queries import APIQuerier