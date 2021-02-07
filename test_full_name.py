import unittest
import full_name
import random


class TestFullName(unittest.TestCase):
    middle_names = ("Hoven", "Everett", "Avery", "Evan", "River", "Devin", "Gavin", "Vardhan")
    
    def test_name_first_and_last(self):
        self.assertEqual(full_name.full_name("", "Scott"), "One or more name(s) not provided")
        self.assertEqual(full_name.full_name("Henry", ""), "One or more name(s) not provided")
        self.assertEqual(full_name.full_name("Ch", ""), "One or more name(s) not provided")
        self.assertEqual(full_name.full_name("Sir", ""), "One or more name(s) not provided")
        self.assertEqual(full_name.full_name("abc", ""), "One or more name(s) not provided")
        self.assertEqual(full_name.full_name("", "Lincoln"), "One or more name(s) not provided")



    def test_name_valid_names(self):
        self.assertEqual(full_name.full_name("123", "Scott"), "One or more name(s) are not numbers")
        self.assertEqual(full_name.full_name("Henry", "123"), "One or more name(s) are not numbers")
        self.assertEqual(full_name.full_name("Chi", "32"), "One or more name(s) are not numbers")
        self.assertEqual(full_name.full_name("O", "23"), "One or more name(s) are not numbers")
        self.assertEqual(full_name.full_name("123", "23"), "One or more name(s) are not numbers")


    def test_name_non_strings(self):
        self.assertEqual(full_name.full_name(132, "123"), "InvalidType")
        self.assertEqual(full_name.full_name(324, 1), "InvalidType")
        self.assertEqual(full_name.full_name("John", 43), "InvalidType")
        self.assertEqual(full_name.full_name(321, "123"), "InvalidType")







if __name__ == "__main__":
    unittest.main()