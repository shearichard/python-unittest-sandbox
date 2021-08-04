#from unittest import TestCase
import unittest

def setUpModule():
    print( "setUpModule: " + __name__ + " set up")
    print("")

def tearDownModule():
    print( "setUpModule: " + __name__ + " tear down")
    print("")


class TestCase1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print( "    setUpClass: " + cls.__name__ + " set up")
        print("")

    @classmethod
    def tearDownClass(cls):
        print( "    tearDownClass: " + cls.__name__ + " tear down")
        print("")

    def setUp(self):
        print( "        setUp: " + self.id() + " set up")
        print("")

    def tearDown(self):
        print( "        tearDown: " + self.id() + " tear down")
        print("")

    def test_one(self):
        print( "            " + self.id() + " running")
        print("")

    def test_two(self):
        print( "            " + self.id() + " running")
        print("")

if __name__ == "__main__":
    unittest.main()
