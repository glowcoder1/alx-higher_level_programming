#!/usr/bin/python3

import unittest

"""
Unit test for max_integer
"""
    

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test cases for max_integer
    """

    def test_max_empty(self):
        """
        Tests when list is empty
        """
        
        result = max_integer([])
        self.assertIsNone(result)

    def test_max_ordered_list(self):
        """
        Tests max when list is ordered
        """
        
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_max_str(self):
        """
        Tests max for str list
        """
        
        result = max_integer(["str", "post"])
        self.assertRaises(TypeError, result)

    def test_unordered_list(self):
        result = max_integer([2,3,4,1])
        self.assertEqual(result, 4)

        
if __name__ == '__main__':
    unittest.main()
