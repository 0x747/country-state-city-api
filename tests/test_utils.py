import os
import sys
import unittest
from unittest import TestCase

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from country_state_city.utils import ensure_trailing_slash as ets

class TestUtils(TestCase):

    def test_ensure_trailing_slash(self):
        slash_added = ets("test")
        no_change = ets("test2/")
        long_url = ets("api.test.com/v1/test")
        concatenated = ets("api.test.com/" + "v1/" + "test")
        empty = ets('')

        self.assertEqual(slash_added, "test/")
        self.assertEqual(no_change, "test2/")
        self.assertEqual(long_url, "api.test.com/v1/test/")
        self.assertEqual(concatenated, "api.test.com/v1/test/")
        self.assertEqual(empty, '/')

        # Test exceptions
        self.assertRaises(TypeError, ets) # Called with no argumnets
        self.assertRaises(AttributeError, ets, None)

if __name__ == '__main__':
    unittest.main()