import unittest
from duplicate import duplicate2

class TestDuplicate(unittest.TestCase):
    def test_duplicate2(self):
        # Test case 1: Empty list
        arr = []
        self.assertEqual(duplicate2(arr), [])

        # Test case 2: List with a single element
        arr = [1]
        self.assertEqual(duplicate2(arr), [1, 1])

        # Test case 3: List with multiple elements
        arr = [1, 2, 3]
        self.assertEqual(duplicate2(arr), [1, 1, 2, 2, 3, 3])

        # Test case 4: List with duplicate elements
        arr = [1, 1, 2, 2, 3, 3]
        self.assertEqual(duplicate2(arr), [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3])

if __name__ == '__main__':
    unittest.main()