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
        """Test for unordered list """
        
        result = max_integer([2,3,4,1])
        self.assertEqual(result, 4)

    def test_max_at_start(self):
        """Test for max at start of list"""
        
        result = max_integer([5, 3, 2, 1])
        self.assertEqual(result, 5)

    def test_one_elem(self):
        """ Test for only one elem"""
        
        result = max_integer([3])
        self.assertEqual(result, 3)

    def test_negative(self):
        """ Test for negative and positive elem"""
        
        result = max_integer([0, -5, 1])
        self.assertEqual(result, 1)

        
if __name__ == '__main__':
    unittest.main()
