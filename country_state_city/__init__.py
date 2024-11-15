"""
Country State City API Wrapper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A simple Python API wrapper for the Country State City API.

Country State City API docs: https://countrystatecity.in/
Country State City API source: https://github.com/dr5hn/countries-states-cities-database

Basic Usage:

    >>> import country_state_city as csc
    >>> client = csc.Client(api_key='your-csc-api-key')
    >>> client.get_countries() # Returns a list of all countries 
    >>> client.get_countries(['US', 'GB', 'DE', 'AU']) # Returns specified countries

:copyright: (c) 2024-present 0x747.
:license: MIT, see LICENSE for more details.

"""

__title__ = 'country_state_city'
__author__ = '0x747'
__copyright__ = 'Copyright 2024-present 0x747'
__version__ = '0.1.0'

from .client import Client
from .models import Country, State, City

__all__ = ["Client", Country, State, City]
