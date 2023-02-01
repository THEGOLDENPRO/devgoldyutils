import random
import os, sys

from . import colours

class LegacyConsole(colours.LegacyColours):
    def __init__(self):
        if sys.platform == "win32": os.system("color")

# V1 support. (See 'https://gist.github.com/THEGOLDENPRO/34dccf77a3c0eb2d86bfebe90502e4c4' for more info.)
setattr(sys.modules[__name__], "Console", LegacyConsole)