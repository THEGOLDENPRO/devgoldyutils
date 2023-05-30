from .console import Console

from .colours import Colours
from .dict_classes import DictDataclass, DictClass
from .errors import DevGoldyUtilsError
from .logging import add_custom_handler, LoggerAdapter
from .file_configs import JSONConfig
from .strings import short_str

from . import better_get

# For those Americans. Imagine not using English UK.
Colors = Colours

# Utils from other libraries
from prettyprinter import cpprint as pprint, install_extras
install_extras(include=["dataclasses"])