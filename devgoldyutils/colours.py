from enum import Enum
import sys, os

class Colours(Enum):
    """Enum class containing codes for most console colours. (Added in v2.0)"""
    GREEN = "\u001b[32m"
    BLUE = "\u001b[36m"
    CLAY = "\u001b[38;5;51m"
    PURPLE = "\u001b[38;5;200m"
    RED = "\u001b[31m"
    BOLD_RED = "\u001b[31;1m"
    PINK_GREY = "\u001b[38;5;139m"
    GREY = "\u001b[38;20m"
    YELLOW = "\u001b[33;20m"
    ORANGE = "\u001b[38;5;214m"

    RESET_COLOUR = "\u001b[0m"

    def __init__(self, colour_value:str):
        if sys.platform == "win32": os.system("color")

    def apply_to_string(self, string:str) -> str:
        """Returns that string but with this colour applied to it."""
        return self.value + string + self.RESET_COLOUR.value