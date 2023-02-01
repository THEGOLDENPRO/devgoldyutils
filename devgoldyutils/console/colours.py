# V1 support. (See 'https://gist.github.com/THEGOLDENPRO/34dccf77a3c0eb2d86bfebe90502e4c4' for more info.)
# -----------------------------------------------------------------------------------------------------------
import sys
from .legacy_colours import LegacyColours
setattr(sys.modules[__name__], "Colours", LegacyColours)