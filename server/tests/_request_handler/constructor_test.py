import unittest
from backend.authentication_manager import AuthenticationManager
from backend.server import _RequestHandler
from backend.service_manager import ServiceManager

class TestConstructor(unittest.TestCase):    
    """
    Tests for the _RequestHandler constructor.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_constructor(self):
        """
        Checks if the constructor sets the default values.
        """
        service_manager = ServiceManager()
        request_handler = _RequestHandler(service_manager)

        self.assertEqual(request_handler._service_manager, service_manager, "Check if the service manager is correct.")

    def test_none_service_manager(self):
        """
        Check if an exception is raised if service_manager is None.
        """

        self.assertRaises(Exception, _RequestHandler, (None), "Check if an exception is raised.")

    def test_service_manager_incorrect_type(self):
        
        """
        Check if an exception is raised if service_manager is not a ServiceManager.
        """
        self.assertRaises(Exception, _RequestHandler, (0), "Check if an exception is raised.")
