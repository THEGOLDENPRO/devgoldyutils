from __future__ import annotations
from typing import Any, Dict

import logging as log
from dataclasses import dataclass, field

from . import errors

@dataclass
class DictDataclass:
    """
    A base dataclass for handling dict filled dataclasses. I really don't know what to call it but I inherit from this to obtain special methods.
    
    ⚠ KEY ERRORS will be ignored if you do not specify a logger.
    """
    logger:log.Logger|None = field(init=False, repr=False, default=None)
    """A logger for us to use to send warnings about key errors."""

    def __post_init__(self):
        super().__post_init__(self)

    def get(self, *keys, data = None, default_value = None) -> Any|Dict:
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

        ``default_value``
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
                    f"Looks like the dataclass '{self.__class__.__name__}' doesn't countian a data dict field. Please add one or use the data parameter in self.get() instead. \nError --> {e}"
                )

        try:
            for key in keys:
                data = data[key]
            
            return data
        except (KeyError, TypeError) as e:

            if self.logger is not None:
                self.logger.warning(f"Could not find key {e} in dict so I'm returning default value '{default_value}'... Keys: {keys}")

            return default_value