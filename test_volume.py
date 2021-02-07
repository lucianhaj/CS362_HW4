import unittest
import Volume


class TestVolume(unittest.TestCase):

    def test_volume_values(self):
        self.assertEqual(Volume.volume(1, 1, 1 ), 1)
        self.assertEqual(Volume.volume(3432, 43254, 2), 296895456)
        self.assertEqual(Volume.volume(2.5, 2.5, 2.5), 15.625)


    def test_volume_edge_cases(self):
        self.assertEqual(Volume.volume(-1, 1, 0), "Error: negative value")
        self.assertEqual(Volume.volume(1, 0, 1), "No volume")
        self.assertEqual(Volume.volume(-2, 1, 1), "Error: negative value")
        self.assertEqual(Volume.volume(-1, 1, 0), "Error: negative value")
        self.assertEqual(Volume.volume(-1, 1, 1.2), "Error: negative value")


    def test_volume_input(self):
        self.assertEqual(Volume.volume("g", 3, 3), "One of inputs was not a float")
        self.assertEqual(Volume.volume(1, "ab", 3), "One of inputs was not a float")
        self.assertEqual(Volume.volume(-1, "ab", 3), "One of inputs was not a float")
        self.assertEqual(Volume.volume(1, "ab", 0), "One of inputs was not a float")








if __name__ == "__main__":
    unittest.main()







