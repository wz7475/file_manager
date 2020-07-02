import unittest
import script
import os
import shutil

class Testscript(unittest.TestCase):

    """ def setUp(self):
        with open(os.path.join(script.path, "test_file.txt"), "w") as target:
            pass
        
    def tearDown(self):
        os.remove(os.path.join(script.path, "test_file.txt")) """

    @classmethod
    def setUpClass(cls):
        with open(os.path.join(script.path, "test_file.txt"), "w") as target:
            pass

    @classmethod
    def tearDownClass(cls):
        os.remove(os.path.join(script.path, "test_file.txt"))

    def test_for_test(self):
        self.assertEqual(True, os.path.exists(os.path.join(script.path, "test_file.txt")))

if __name__ == "__main__":
    unittest.main()