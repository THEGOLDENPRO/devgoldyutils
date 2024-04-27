import logging as log
from typing import Literal

from .colours import Colours

__all__ = (
    "LoggerAdapter", 
    "add_custom_handler"
)

class LoggerAdapter(log.LoggerAdapter):
    """Allows you to create and bind secondary logger to a logger."""
    def __init__(self, logger:log.Logger, prefix:str):
        super().__init__(logger, {'prefix': prefix})

    def process(self, msg, kwargs):
        return f"\u001b[92m[{self.extra['prefix']}\u001b[92m]\u001b[0m {msg}", kwargs

def add_custom_handler(logger:log.Logger, level:Literal[50, 40, 30, 20, 10, 0]) -> log.Logger:
    """Method for adding the devgoldyutils custom logger handler to any logger object."""
    stream_handler = log.StreamHandler()
    stream_handler.setLevel(log.DEBUG)
    stream_handler.setFormatter(CustomFormatter())

    logger.propagate = False
    logger.addHandler(stream_handler)

    logger.setLevel(level) # Added in v2.3.11

    return logger

class CustomFormatter(log.Formatter):
    """This is an internal thing but it creates the amazing logging format I use in all my python programs."""
    format_string = "[%(levelname)s]\u001b[0m (%(name)s) - %(message)s"

    FORMATS = {
        log.DEBUG: Colours.PINK_GREY.value + format_string,
        log.INFO: Colours.CLAY.value + format_string,
        log.WARNING: Colours.YELLOW.value + format_string,
        log.ERROR: Colours.RED.value + format_string,
        log.CRITICAL: Colours.BOLD_RED.value + format_string
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = log.Formatter(log_fmt)
        return formatter.format(record)