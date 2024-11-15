from json import JSONDecodeError
import os
import sys
import requests
import unittest
from unittest import TestCase
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import country_state_city as csc
from country_state_city.models import *
from country_state_city.endpoints import *

class TestClient(TestCase):

    def setUp(self):
        self.api_key = "mock_test_csc_api_key"
        self.client = csc.Client(api_key=self.api_key)
        self.response = requests.Response()
    
    def set_sample_response(self, status_code: int, file_name: str):
        """
        Sets the status code and responde body for a sample response

        Arguments
        ---------
        status_code : int
            The status code of the response.
        file_name : str
            The file that contains the response content.

        """
        self.response.status_code = status_code
        
        with open('./sample_responses/' + file_name, 'r') as f:
            self.response._content = f.read().encode()
    
    def test__get_empty_json(self):
        self.set_sample_response(200, 'empty.json')

        with patch("country_state_city.client.requests.get") as mock_get:
            mock_get.return_value = self.response
            response = self.client._get('some-empty-endpoint')
            
            self.assertEqual(response, {})
            mock_get.assert_called_with(url=self.client._HOSTNAME + "some-empty-endpoint",
                                        headers={self.client._API_KEY_HEADER_NAME: self.api_key},
                                        verify=self.client._ssl_verify)
            
    # /v1/not-found        
    def test__get_not_found(self):
        self.set_sample_response(404, 'not_found.json')
        
        with patch("country_state_city.client.requests.get") as mock_get:
            mock_get.return_value = self.response
            response = self.client._get('')

            self.assertEqual(response, None)
            mock_get.assert_called_with(url=self.client._HOSTNAME,
                                        headers={self.client._API_KEY_HEADER_NAME: self.api_key},
                                        verify=self.client._ssl_verify)
    
    def test__get_malformed_bad_value(self):
        self.set_sample_response(200, 'malformed.json')

        with patch("country_state_city.client.requests.get") as mock_get:
            mock_get.return_value = self.response
           
            with self.assertRaises(JSONDecodeError):
                self.client._get('malformed-endpoint')

    # /countries
    def test_get_countries_normal(self):
        self.set_sample_response(200, 'all_countries.json')
        
        with patch("country_state_city.client.requests.get") as mock_get:
            mock_get.return_value = self.response
            response = self.client.get_countries()

            self.assertEqual(len(response), 250)
            self.assertIsInstance(response, list)
            self.assertIsInstance(response[0], Country)
            self.assertIsInstance(response[-1], Country)

            mock_get.assert_called_with(url=self.client._HOSTNAME + COUNTRIES,
                                        headers={self.client._API_KEY_HEADER_NAME: self.api_key},
                                        verify=self.client._ssl_verify)
    # /countries/US
    def test_get_countries_list_single(self):
        self.set_sample_response(200, 'us.json')

        with patch("country_state_city.client.requests.get") as mock_get:
            mock_get.return_value = self.response
            response = self.client.get_countries(['US'])

            self.assertEqual(len(response), 1)
            self.assertIsInstance(response, list)
            self.assertEqual(response[0].name, "United States")
            self.assertIsInstance(response[0].phonecode, str)
            self.assertIsInstance(response[0], Country)
            self.assertIsInstance(response[-1], Country)
            self.assertIsInstance(response[0].latitude, str)
        
            mock_get.assert_called_with(url=self.client._HOSTNAME + COUNTRIES + 'US',
                                        headers={self.client._API_KEY_HEADER_NAME: self.api_key},
                                        verify=self.client._ssl_verify)
    # /countries/US
    def test_get_country(self):
        self.set_sample_response(200, 'us.json')

        with patch("country_state_city.client.requests.get") as mock_get:
            mock_get.return_value = self.response
            response = self.client.get_country('US')

            self.assertIsInstance(response, Country)
            self.assertEqual(response.name, "United States")
            self.assertIsInstance(response.phonecode, str)

            mock_get.assert_called_with(url=self.client._HOSTNAME + COUNTRIES + 'US',
                                        headers={self.client._API_KEY_HEADER_NAME: self.api_key},
                                        verify=self.client._ssl_verify)
    
    # /countries/US
    def test_get_country_short(self):
        self.set_sample_response(200, 'us_short.json')

        with patch("country_state_city.client.requests.get") as mock_get:
            mock_get.return_value = self.response
            response = self.client.get_country('US')

            self.assertIsInstance(response, Country)
            self.assertEqual(response.name, "United States")
            self.assertIsInstance(response.phonecode, str)

            mock_get.assert_called_with(url=self.client._HOSTNAME + COUNTRIES + 'US',
                                        headers={self.client._API_KEY_HEADER_NAME: self.api_key},
                                        verify=self.client._ssl_verify)
    
    # /states
    def test_get_states(self):
        self.set_sample_response(200, 'all_states.json')

        with patch("country_state_city.client.requests.get") as mock_get:
            mock_get.return_value = self.response
            response = self.client.get_states()

            self.assertIsInstance(response, list)
            self.assertEqual(len(response), 5081)
            self.assertIsInstance(response[0], State)
            self.assertIsInstance(response[-1], State)

            mock_get.assert_called_with(url=self.client._HOSTNAME + STATES,
                                        headers={self.client._API_KEY_HEADER_NAME: self.api_key},
                                        verify=self.client._ssl_verify)
    # /counties/US/states
    def test_get_states_from_country(self):
        self.set_sample_response(200, 'us_states.json')

        with patch("country_state_city.client.requests.get") as mock_get:
            mock_get.return_value = self.response
            response = self.client.get_states('US')

            self.assertEqual(len(response), 66)
            self.assertIsInstance(response, list)
            self.assertIsInstance(response[0], State)
            self.assertIsInstance(response[-1], State)
            self.assertIsInstance(response[0].id, int)

            mock_get.assert_called_with(url=self.client._HOSTNAME + COUNTRIES + 'US/' + STATES,
                                        headers={self.client._API_KEY_HEADER_NAME: self.api_key},
                                        verify=self.client._ssl_verify)
    # /countries/US/states/CA
    def test_get_state(self):
        self.set_sample_response(200, 'california.json')

        with patch("country_state_city.client.requests.get") as mock_get:
            mock_get.return_value = self.response
            response = self.client.get_state('US', 'CA')

            self.assertIsInstance(response, State)
            self.assertEqual(response.name, 'California')
        
            mock_get.assert_called_with(url=self.client._HOSTNAME + COUNTRIES + 'US/' + STATES + 'CA',
                                        headers={self.client._API_KEY_HEADER_NAME: self.api_key},
                                        verify=self.client._ssl_verify)
    
    # /countries/US/states/CA
    def test_get_state_short(self):
        self.set_sample_response(200, 'california_short.json')

        with patch("country_state_city.client.requests.get") as mock_get:
            mock_get.return_value = self.response
            response = self.client.get_state('US', 'CA')

            self.assertIsInstance(response, State)
            self.assertEqual(response.name, 'California')
            self.assertEqual(response.latitude, None)
        
            mock_get.assert_called_with(url=self.client._HOSTNAME + COUNTRIES + 'US/' + STATES + 'CA',
                                        headers={self.client._API_KEY_HEADER_NAME: self.api_key},
                                        verify=self.client._ssl_verify)

    # /countries/US/cities
    def test_get_cities_from_country(self):
        self.set_sample_response(200, 'us_cities.json')

        with patch("country_state_city.client.requests.get") as mock_get:
            mock_get.return_value = self.response
            response = self.client.get_cities('US')

            self.assertEqual(len(response), 19820)
            self.assertIsInstance(response, list)
            self.assertIsInstance(response[0], City)
            self.assertIsInstance(response[-1], City)

            mock_get.assert_called_with(url=self.client._HOSTNAME + COUNTRIES + 'US/' + CITIES,
                                        headers={self.client._API_KEY_HEADER_NAME: self.api_key},
                                        verify=self.client._ssl_verify)

    # /countries/US/states/TX/cities
    def test_get_cities_from_state(self):
        self.set_sample_response(200, 'texas_cities.json')

        with patch("country_state_city.client.requests.get") as mock_get:
            mock_get.return_value = self.response
            response = self.client.get_cities('US', 'TX')

            self.assertEqual(len(response), 1277)
            self.assertIsInstance(response, list)
            self.assertIsInstance(response[0], City)
            self.assertIsInstance(response[-1], City)

            mock_get.assert_called_with(url=self.client._HOSTNAME + COUNTRIES + 'US/' + STATES + 'TX/' + CITIES,
                                        headers={self.client._API_KEY_HEADER_NAME: self.api_key},
                                        verify=self.client._ssl_verify)
            


if __name__ == '__main__':
    unittest.main()


    