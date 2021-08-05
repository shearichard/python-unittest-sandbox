import unittest

from name_formatter import formatted_name

def setUpModule():
    print( "setUpModule: " + __name__ + " set up")
    print("")

def tearDownModule():
    print( "setUpModule: " + __name__ + " tear down")
    print("")


class TestCase_NameFormatting(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''
        Executed once when class is instantiated

        cls.__name__ makes the name of the class available
        '''
        pass

    @classmethod
    def tearDownClass(cls):
        '''
        Executed once when class is finished with 

        cls.__name__ makes the name of the class available
        '''
        pass

    def setUp(self):
        '''
        self.id() 
        '''
        pass

    def tearDown(self):
        '''
        self.id() 
        '''
        pass

    def test_name_formatting_bad_args(self):
        with self.assertRaises(TypeError):
            formatted_name()

        with self.assertRaises(TypeError):
            formatted_name(None,None,None)

        with self.assertRaises(TypeError):
            formatted_name("",None,None)

        with self.assertRaises(TypeError):
            formatted_name("","",None)


    def test_name_formatting_args_1(self):
        self.assertNotEqual(formatted_name("John", "Watson"),"Xohn Watson")

    def test_name_formatting_args_2(self):
        self.assertEqual(formatted_name("John", "Watson", "Hamish"),"John Hamish Watson")


if __name__ == "__main__":
    unittest.main()
