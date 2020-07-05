import unittest
import random
from quickSort import *

class QuickSortTests(unittest.Testcase):
    def test_quick_sort(self):
        arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
        arr2 = []
        arr3 = [2]
        arr4 = [0, 1, 2, 3, 4, 5]
        arr5 = random.sample(range(200), 50)

        self.assertEqual(quick_sort(arr1), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(quick_sort(arr2), [])
        self.assertEqual(quick_sort(arr3), [2])
        self.assertEqual(quick_sort(arr4), [0, 1, 2, 3, 4, 5])
        self.assertEqual(quick_sort(arr5), sorted(arr5))

if __name__ == '__main__':
    unittest.main()
