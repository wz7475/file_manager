import unittest
import script
import os
import shutil
import json

class Testscript(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        path = os.path.join(script.path, "test_folder")
        with open("ext.json") as f:
            data = f.read()
        extentions = json.loads(data)
        os.mkdir(path)
        os.chdir(path)
        for i in extentions:
            name = "file" + i
            with open(name, "w") as target:
                pass

    @classmethod
    def tearDownClass(cls):
        os.chdir(script.path)
        shutil.rmtree("test_folder")

    def test_for_test(self):
        self.assertEqual(False, os.path.exists(
            os.path.join(script.path, "test_file.txt")))


if __name__ == "__main__":
    unittest.main()
