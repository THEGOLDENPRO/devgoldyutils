from importlib.util import find_spec

from .console import Console

from .colours import Colours
from .dict_classes import DictDataclass, DictClass
from .errors import DevGoldyUtilsError
from .logging import add_custom_handler, LoggerAdapter
from .file_configs import JSONConfig
from .strings import *
from .debugging import debug

from . import better_get

# For those Americans. Imagine not using English UK.
Colors = Colours

# Optional utils from other libraries.
# -------------------------------------
# Install devgoldyutils with 'pprint' optional dependency to get this like so --> pip install devgoldyutils[pprint]
if find_spec("prettyprinter") is not None:
    from prettyprinter import cpprint as pprint, install_extras
    install_extras(include=["dataclasses"])