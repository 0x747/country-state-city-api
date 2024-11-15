"""
The MIT License (MIT)

Copyright 2024-present 0x747

Permission is hereby granted, free of charge, to any person obtaining a 
copy of this software and associated documentation files (the “Software”), 
to deal in the Software without restriction, including without limitation 
the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in 
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR 
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR 
OTHER DEALINGS IN THE SOFTWARE.

"""
from .endpoints import *
from json import JSONDecodeError
from .models import *
from typing import List, Optional
import requests.packages
from .utils import ensure_trailing_slash as ets
from urllib.parse import urljoin

class Client:
    """
    API client to make requests and process responses into from the Country State City API. 
    """
    _ERROR_MESSAGE_KEY = "error"
    _API_KEY_HEADER_NAME = "X-CSCAPI-KEY"

    def __init__(self, api_key: str, version: Optional[str] = 'v1', ssl_verify: Optional[bool] = True):
        """
        Arguments
        ---------
        api_key : str
            The API key for Country State City API.
        version : str, default 'v1' 
            The API version.
        ssl_verify : bool, default True
            Sets SSL verification warning.
        """
        self._api_key = api_key
        self._ssl_verify = ssl_verify
        self._HOSTNAME = urljoin(ROOT, ets(version)) 

        if not ssl_verify:
            requests.packages.urllib3.disable_warnings()

    def _get(self, endpoint: str):
        """
        Sends a GET requests to the API ``endpoint``.

        Arguments
        ---------
        endpoint : str
            The endpoint of the API you want to hit
        
        Returns
        -------
        A JSON object represented by a Python ``dict``
        """

        headers = {self._API_KEY_HEADER_NAME: self._api_key}
        url = urljoin(self._HOSTNAME, endpoint)

        try:
            response = requests.get(url=url, verify=self._ssl_verify, headers=headers)
        except Exception as e:
            raise Exception(response_body[self._ERROR_MESSAGE_KEY])
        
        try:
            response_body = response.json()
    
            if response.status_code >= 200 and response.status_code <= 299:
                return response_body
        except JSONDecodeError as e:
            raise

    def get_countries(self, country_iso2_codes: Optional[List[str]] = None) -> List[Country]:
        """
        Gets all countries.

        If  ``iso2_codes``  list is provided, only the given countries will be fetched.

        Arguments
        ---------
        iso2_codes : List[str], default [] 
            List of iso2 country codes. 

        Returns
        -------
        List[Country]
            A list of ``Country`` objects.
        """

        path = COUNTRIES
        countries = []

        if country_iso2_codes:
            for code in country_iso2_codes:
                countries.append(self.get_country(code))
            
            return countries
        
        json = self._get(path)
        for entry in  json:
            countries.append(Country(**entry))
        
        return countries

    def get_country(self, country_iso2: str) -> Country:
        """
        Gets the country based on the ``iso2`` country code.

        Arguments
        ---------
        iso2 : str
            The ISO2 code for the country.
        
        Returns
        -------
        A ``Country`` object.
        """

        path = COUNTRIES + country_iso2
        json = self._get(path)

        return Country(**json)
    
    def get_states(self, country_iso2: Optional[str] = None) -> List[State]:
        """
        Gets all states for all countries 
        OR
        states from a specified country.

        Arguments
        ---------
        country_iso2 : str, default ''
            The ISO2 code for the country.
        
        Returns
        -------
        A list of ``State`` objects.
        """

        states = []

        if country_iso2:
            path = COUNTRIES + ets(country_iso2) + STATES
            json = self._get(path)

            for entry in json:
                states.append(State(**entry))

            return states
        
        path = STATES
        json = self._get(path)

        for entry in json:
            states.append(State(**entry))
        
        return states

    def get_state(self, country_iso2: str, state_iso2: str) -> State:
        """
        Gets a state from the given country.

        Arguments
        ---------
        country_iso2 : str
            The ISO2 code for the country.
        state_iso2 : str
            The ISO2 code for the state.
        
        Returns
        -------
        A `State` object.
        """

        path = COUNTRIES + ets(country_iso2) + STATES + state_iso2
        json = self._get(path)
       
        return State(**json)
    
    def get_cities(self, country_iso2: str, state_iso2: Optional[str] = None) -> List[City]:
        """
        Gets all cities from a country
        OR 
        all cities from a state is specified

        Arguments
        ---------
        country_iso2 : str
            The ISO2 code for the country.
        
        state_iso2 : str, default ''
            The ISO2 code for the state
        
        Returns
        -------
        A list of `City` objects.
        """

        country_cities = COUNTRIES + ets(country_iso2) + CITIES
        state_cities = ''

        if state_iso2:
            state_cities = COUNTRIES + ets(country_iso2) + STATES + ets(state_iso2) + CITIES

        path = state_cities if state_iso2 else country_cities
    
        json = self._get(path)
        cities = []

        for entry in json:
            cities.append(City(**entry))
        
        return cities