import pkg_resources
name = "wikiwho_wrapper"
__version__ = pkg_resources.require(name)[0].version


from .api import WikiWhoAPI
from .views import DataView
from .wikiwho import WikiWho
