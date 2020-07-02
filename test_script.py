import unittest
import script
import os

class Testscript(unittest.TestCase):

    def setUp(self):
        with open(os.path.join(script.path, "test_file.txt"), "w") as target:
            pass
        