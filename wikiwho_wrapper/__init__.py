import pkg_resources
name = "wikiwho_wrapper"
try:
	__version__ = pkg_resources.require(name)[0].version
except:
	__version__ = None


from .api import WikiWhoAPI
from .pickle_api import WikiWhoPickleAPI
from .views import DataView
from .wikiwho import WikiWho
