from __future__ import annotations

import logging as log

from typing import Any, Dict

def get(*keys, data: dict, optional: bool = False, default = None, logger: log.Logger = None) -> Any | Dict:
    """
    A small function used to grab data from the ``data`` dictionary with an advantage of handling KeyError respectfully. 
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

    ``logger``
        The logger for us to use to send warnings about key errors.

    Returns
    -------
    ``Any`` | ``Dict``
        Can return anything from the dictionary.
    """

    if logger is None:
        logger = log.getLogger()

    try:
        for key in keys:
            data = data[key]
        
        return data
    except (KeyError, TypeError) as e:
        if optional == False:
            logger.warning(f"Could not find key {e} in dict so I'm returning default value '{default}'... Keys: {keys}")

        return default