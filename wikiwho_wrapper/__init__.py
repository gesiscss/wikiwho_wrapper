import os
import requests

WIKIWHO_API_KEY = os.environ.get('WIKIWHO_API_KEY', None)

class APIKeyMissingError(Exception):
    pass

# if WIKIWHO_API_KEY is None:
#     raise APIKeyMissingError(
#         "All methods require an API key."
#     )

session = requests.Session()
#session.params = {}
#session.params['api_key'] = WIKIWHO_API_KEY


from .api import WikiWhoAPI