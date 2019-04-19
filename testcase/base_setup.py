import unittest
from time import sleep

class BaseSetup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass


    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()