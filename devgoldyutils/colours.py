from enum import Enum
import sys, os

if sys.platform == "win32":
    os.system("color")

class Colours(Enum):
    """Enum class containing codes for most console colours. (Added in v2.0)"""
    GREEN = "\u001b[32m"
    BLUE = "\u001b[36m"
    CLAY = "\u001b[38;5;51m"
    PURPLE = "\u001b[38;5;200m"
    RED = "\u001b[31m"
    BOLD_RED = "\u001b[31;1m"
    PINK_GREY = "\u001b[38;5;139m"
    GREY = "\u001b[1;37;30m"
    YELLOW = "\u001b[33;20m"
    ORANGE = "\u001b[38;5;214m"
    WHITE = "\u001b[1;37;40m"

    RESET = "\u001b[0m"
    RESET_COLOUR = "\u001b[0m"

    def __init__(self, colour_value:str):
        ...

    # NEW in v2.3.5! Check out here for info: https://gist.github.com/THEGOLDENPRO/317a1238c581557712d234ff10e41a61
    # -----------------------------------------------------------------------------------------------------------------
    def __str__(self):
        return str(self.value)
    
    def __add__(self, other):
        return self.value + str(other)
    
    def __radd__(self, other):
        return str(other) + self.value
    # -----------------------------------------------------------------------------------------------------------------

    def apply_to_string(self, string:str) -> str:
        """Returns that string but with this colour applied to it."""
        return self.value + string + self.RESET_COLOUR.value
    
    def apply(self, string:str) -> str:
        """Returns that string but with this colour applied to it."""
        return self.apply_to_string(string)