import unittest
import list_average


class TestList(unittest.TestCase):

    def test_list_length(self):
        self.assertEqual(list_average.average([]), "Zero length for the list")
        self.assertEqual(list_average.average([     ]), "Zero length for the list")

    def test_list_type(self):
        self.assertEqual(list_average.average(["a", "b", "c"]), "VError")
        self.assertEqual(list_average.average([" "]), "VError")
    
    def test_list_value(self):
        self.assertEqual(list_average.average([1, 2, 3]), 2)
        self.assertEqual(list_average.average([5, 8]), 6.5)
        self.assertEqual(list_average.average([-1, 0, 4, 1, 0]), .8)
        self.assertEqual(list_average.average([3,3]), 3)
        self.assertEqual(list_average.average([0, 0, 0]), 0)
        self.assertEqual(list_average.average([1.2, .8]), 1)
        self.assertEqual(list_average.average([-3, -2, -1]), -2)





if __name__ == "__main__":
    unittest.main()