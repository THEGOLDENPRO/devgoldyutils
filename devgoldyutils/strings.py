"""
文字列に使用するユーティリティ。(wait whaaaaa)
"""
from pathlib import Path

__all__ = (
    "short_str",
    "shorter_path",
)

def short_str(string: str, length: int = 30) -> str:
    """Function that shortens strings and adds ellipsis (...) to the end. You get it! Makes then shorter, sometimes as short as you."""

    if len(string) > length:
        return string[:length - 2] + "..."

    return string

def shorter_path(path: Path, length: int = 2) -> str: # Stolen from https://stackoverflow.com/a/49758154
    """Splits this path into shorter sections for representation purposes."""
    return str(Path(*Path(path).parts[-length:]))