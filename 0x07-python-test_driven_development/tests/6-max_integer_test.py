#!/usr/bin/python3
"""
test module
"""

import unittest


max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ class test """

    def test_no_input(self):
        """ test no input method """

        self.assertEqual(max_integer(), None)

    def test_int(self):
        """ test integer method """

        with self.assertRaises(TypeError):
            max_integer(14)

    def test_float(self):
        """ test float """

        with self.assertRaises(TypeError):
            max_integer(14.5)

    def test_bool(self):
        """ test bool """

        with self.assertRaises(TypeError):
            max_integer(True)

    def test_str(self):
        """ test string """

        self.assertEqual(max_integer("ahmed"), 'm')

    def test_valid(self):
        """ test valid """

        self.assertEqual(max_integer([1, 2, 3]), 3)
