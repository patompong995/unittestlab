import unittest
from assignment.testinglab.listutil import count_unique


class TestBuitins(unittest.TestCase):
    """Test some python built-in methods"""
    def test_borderline_cases(self):
        self.assertEqual(0,count_unique([]))
    def test_typical_cases(self):
        self.assertEqual(1,count_unique(['a','a','a','a']))
    def test_impossible_cases(self):
        self.assertEqual(6,count_unique([1,2,3,4,5,6,5,5,5]))
    def test_extreme_cases(self):
        self.assertEqual(9,count_unique([1,1,1,1,2,2,2,3,4,5,5,5,5,6,7,8,8,8,8,9,9,9]))


if __name__ == "__main__":
    unittest.main()