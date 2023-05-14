import json

from .colours import Colours
from .logging import LoggerAdapter, log
from . import better_get

class JSONConfig():
    """
    A base class that can be used to wrap a configuration class around a json file. (Added in v2.3)
    """
    def __init__(self, json_path:str, logger:log.Logger = None):
        self.json_path = json_path

        if logger is None:
            logger = log.getLogger()

        self.logger = LoggerAdapter(logger, prefix="JSONConfig")

        self.logger.debug(f"Opening config file at '{self.json_path}'...")

        self.file = open(
            self.json_path, 
            "r+", 
            encoding='utf-8'
        )

        self.logger.debug("Phrasing json in config to dict...")
        self.json_data: dict = json.loads(self.file.read())
        self.file.close()
        self.logger.debug(Colours.GREEN.apply_to_string("Done!"))

    def get(self, *keys, json_data = None, optional: bool = False, default = None, **_):
        """
        A small method used to grab data from the json dictionary with an advantage of handling KeyError respectfully. 
        Use this method please instead of just directly accessing the dict via self.
        """
        if json_data is None:
            json_data = self.json_data

        data = json_data

        # In version 2.4 and 2.5 we renamed the argument 'default_value' to default so to maintain backwards compatibility we still have to grab the other one.
        if default is None:
            default = _.get("default_value")

        return better_get.get(*keys, data=data, optional=optional, default=default, logger=self.logger)