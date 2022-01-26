from django.test import TestCase

from calc import add, subtract


class CalcTests(TestCase):

    def test_add_num(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """Test that two numbers are subtracted and returned"""
        self.assertEqual(subtract(10, 2), 8)
