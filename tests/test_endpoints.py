import os
import sys
import unittest
from unittest import TestCase

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from country_state_city.endpoints import *
from country_state_city.utils import ensure_trailing_slash as ets

class TestEndpoints(TestCase):

    def test_endpoints(self):

        # Countries
        self.assertEqual(COUNTRIES, 'countries/')
        self.assertEqual(COUNTRIES + 'US', 'countries/US')
        self.assertEqual(COUNTRIES + ets('US'), 'countries/US/')
        self.assertEqual(COUNTRIES + ets('US/'), 'countries/US/')

        # States
        self.assertEqual(STATES, 'states/')
        self.assertEqual(COUNTRIES + ets('US') + STATES, 'countries/US/states/' )
        self.assertEqual(COUNTRIES + ets('US') + STATES + 'TX', 'countries/US/states/TX' )
        self.assertEqual(COUNTRIES + ets('US') + STATES + ets('TX'), 'countries/US/states/TX/' )

        # Cities
        self.assertEqual(CITIES, 'cities/')
        self.assertEqual(COUNTRIES + ets('AU') +  CITIES, 'countries/AU/cities/')
        self.assertEqual(COUNTRIES + ets('US') + STATES + ets('CA') + CITIES, 'countries/US/states/CA/cities/')

if __name__ == '__main__':
    unittest.main()