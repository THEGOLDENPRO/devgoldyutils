from __future__ import annotations
from typing import Any, Dict

import logging as log
from dataclasses import dataclass, field

from . import errors, better_get

@dataclass
class DictDataclass:
    """
    A base dataclass for handling dict filled dataclasses. I really don't know what to call it but I inherit from this to obtain special methods.
    
    ⚠ KEY ERRORS may be ignored if you silence the global logger.
    """
    logger: log.Logger|None = field(init=False, repr=False, default=None)
    """A logger for us to use to send warnings about key errors."""

    def __post_init__(self, logger=None):
        if logger is not None: self.logger = logger

        if self.logger is None:
            self.logger = log.getLogger()

    def get(self, *keys, data:dict = None, optional:bool = False, default = None, **_) -> Any | Dict:
        """
        A small method used to grab data from the ``data`` dictionary with an advantage of handling KeyError respectfully. 
        It's better to use this method instead of just directly accessing the dictionary.
        ------------------

        Parameters
        ----------
        ``*keys``
            The keys to get to the dictionary object. E.g ``self.data['cities']['london']['population']`` would be written like --> ``self.get('cities', 'london', 'population')``.

        ``data``
            The dictionary containing the data, if left none we'll use ``self.data``.

        ``optional``
            If this is true, no warning will be given if this key is missing.

        ``default``
            The default value to return if the object is not found in the dictionary.

        Returns
        -------
        ``Any`` | ``Dict``
            Can return anything from the dictionary.
        """
        if data is None:
            try:
                data = self.data
            except AttributeError as e:
                raise errors.DevGoldyUtilsError(
                    f"Looks like the dataclass '{self.__class__.__name__}' doesn't countian a data dict field. " \
                    "Please add one or use the data parameter in self.get() instead. \nError --> {e}"
                )
            
        # In v2.4 we renamed the argument 'default_value' to default so to maintain backwards compatibility we still have to grab it.
        if default is None:
            default = _.get("default_value")

        return better_get.get(*keys, data=data, optional=optional, default=default, logger=self.logger)


class DictClass():
    """
    A copy of DictDataclass but for normal classes.
    
    ⚠ KEY ERRORS may be ignored if you silence the global logger.
    """
    def __init__(self, logger: log.Logger = None) -> None:
        self.logger = log.getLogger() if logger is None else logger
        """A logger for us to use to send warnings about key errors."""

    def get(self, *keys, data:dict = None, optional:bool = False, default = None) -> Any | Dict:
        """
        A small method used to grab data from the ``data`` dictionary with an advantage of handling KeyError respectfully. 
        It's better to use this method instead of just directly accessing the dictionary.
        ------------------

        Parameters
        ----------
        ``*keys``
            The keys to get to the dictionary object. E.g ``self.data['cities']['london']['population']`` would be written like --> ``self.get('cities', 'london', 'population')``.

        ``data``
            The dictionary containing the data, if left none we'll use ``self.data``.

        ``optional``
            If this is true, no warning will be given if this key is missing.

        ``default``
            The default value to return if the object is not found in the dictionary.

        Returns
        -------
        ``Any`` | ``Dict``
            Can return anything from the dictionary.
        """
        if data is None:
            try:
                data = self.data
            except AttributeError as e:
                raise errors.DevGoldyUtilsError(
                    f"Looks like the class '{self.__class__.__name__}' doesn't countian a data variable." \
                    "Please add one or use the data parameter in self.get() instead. \nError --> {e}"
                )

        return better_get.get(*keys, data=data, optional=optional, default=default, logger=self.logger)