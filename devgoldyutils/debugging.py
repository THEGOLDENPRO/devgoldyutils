"""
Utils I use for quick debugging. Nothing special.
"""

from .colours import Colours

__all__ = (
    "debug", 
)

def debug(obj: object) -> None:
    """Print debug an object."""
    print(
        Colours.CLAY.apply(">"), obj, type(obj)
    )