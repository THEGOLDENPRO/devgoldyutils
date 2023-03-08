import logging as log

from .colours import Colours

class DevGoldyUtilsError(Exception):
    """Raises whenever there's a known error in devgoldyutils."""
    def __init__(self, message:str, logger:log.Logger = None):
        message = Colours.RED.apply_to_string(message)

        if logger is not None:
            logger.error(message)
        
        super().__init__(message)