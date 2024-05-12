from importlib.util import find_spec

from .colours import *
from .logging import *
from .strings import *

from .debugging import debug

__all__ = (
    "debug", 
    "pprint"
)

Colors = Colours # For those Americans. Imagine not using English UK.

# Optional utils from other libraries.
# -------------------------------------
# Install devgoldyutils with 'pprint' optional dependency to get this like so --> pip install devgoldyutils[pprint]
if find_spec("prettyprinter") is not None:
    from prettyprinter import cpprint as pprint, install_extras
    install_extras(include=["dataclasses"])

__version__ = "3.0.0"