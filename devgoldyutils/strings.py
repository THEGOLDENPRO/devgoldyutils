"""
文字列に使用するユーティリティ。(wait whaaaaa)
"""

def short_str(string: str, length: int = 30) -> str:
    """Function that shortens strings and adds ellipsis (...) to the end. You get it! Makes then shorter, sometimes as short as you."""

    if len(string) > length:
        return string[:length - 2] + "..."

    return string