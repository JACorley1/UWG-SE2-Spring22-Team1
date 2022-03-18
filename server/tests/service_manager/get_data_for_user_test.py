import unittest
from server.service_manager import ServiceManager
from server.user_data import UserData

class TestGetDataForUser(unittest.TestCase):    
    """
    Tests for the get_data_for_user method.

    @author Team 1
    @version Spring 2022
    """
    def test_valid_username(self):
        """
        Checks if an object is returned when added and retrieved.
        """
        service_manager = ServiceManager()
        username = "username"
        password = "password"
        email = "email@email.com"

        service_manager.create_user(username, password, email)
        result = service_manager.get_data_for_user(username)

        self.assertTrue(isinstance(result, UserData), "Checks if an object was returned")
        self.assertEqual(result.username, username, "Check if the username is correct")
        self.assertEqual(result.password, password, "Check if the password is correct")
        self.assertEqual(result.email, email, "Check if the email is correct")
    
    def test_username_not_added(self):
        """
        Checks if an object is returned when added and retrieved.
        """
        service_manager = ServiceManager()

        result = service_manager.get_data_for_user("username")

        self.assertTrue(result is None, "Checks if None was returned")
    
    
