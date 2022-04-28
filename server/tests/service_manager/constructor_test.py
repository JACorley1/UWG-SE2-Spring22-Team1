import unittest
from backend.service_manager import ServiceManager

class TestConstructor(unittest.TestCase):    
    """
    Tests for the ServiceManager constructor.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_constructor(self):
        """
        Checks if the constructor sets the default values correctly.
        """
        service_manager = ServiceManager()
        self.assertEqual(service_manager._user_information, {})
