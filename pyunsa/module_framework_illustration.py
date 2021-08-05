'''
This module only exists to easily illustrate the order of processing for the different functions within 
a module intended to make use of unittest tests.


The expected output of the following ... 

(python-unittest-sandbox) rshea@mayari:~/src/python-unittest-sandbox/pyunsa$ python -m  module_framework_illustration
setUpModule: __main__ set up A

    setUpClass: TestCase1 set up B

        setUp: __main__.TestCase1.test_one set up C

            __main__.TestCase1.test_one running

        tearDown: __main__.TestCase1.test_one tear down C

.        setUp: __main__.TestCase1.test_two set up C

            __main__.TestCase1.test_two running

        tearDown: __main__.TestCase1.test_two tear down C

.    tearDownClass: TestCase1 tear down B

setUpModule: __main__ tear down A


----------------------------------------------------------------------
Ran 2 tests in 0.013s

OK
'''


import unittest

def setUpModule():
    print( "setUpModule: " + __name__ + " set up A")
    print("")

def tearDownModule():
    print( "setUpModule: " + __name__ + " tear down A")
    print("")


class TestCase1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print( "    setUpClass: " + cls.__name__ + " set up B")
        print("")

    @classmethod
    def tearDownClass(cls):
        print( "    tearDownClass: " + cls.__name__ + " tear down B")
        print("")

    def setUp(self):
        print( "        setUp: " + self.id() + " set up C")
        print("")

    def tearDown(self):
        print( "        tearDown: " + self.id() + " tear down C")
        print("")

    def test_one(self):
        print( "            " + self.id() + " running")
        print("")

    def test_two(self):
        print( "            " + self.id() + " running")
        print("")




if __name__ == "__main__":
    unittest.main()
