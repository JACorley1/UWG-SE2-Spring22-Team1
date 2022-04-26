import unittest
from backend.authentication_manager import AuthenticationManager
from backend.service_manager import ServiceManager
import backend.request_handler.habit_handler as habit_handler
import backend.request_handler.authentication_handler as authentication_handler

class TestRemoveData(unittest.TestCase):
    """
    Tests for the _remove_habit method.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_request(self):
        """
        Tests if habit_handler correctly returns all of a new user's data.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        habit_handler.add_habit(service_manager, authentication_manager, authentication_token, habit_name, habit_freq)
        response = habit_handler.remove_habit(service_manager, authentication_manager, authentication_token, 0)

        self.assertEqual(response["success_code"], 0, "Check if success_code is correct")

    def test_invalid_authentication_token(self):
        """
        Tests if habit_handler returns the correct success code when the authentication token is invalid.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        habit_handler.add_habit(service_manager, authentication_manager, authentication_token, habit_name, habit_freq)
        response = habit_handler.remove_habit(service_manager, authentication_manager, "invalid_token", 0)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 14, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid authentication token", "Check if error_message is correct")

    def test_user_data_is_missing(self):
        """
        Tests if habit_handler returns the correct success code when the user data doesn't exist.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        habit_handler.add_habit(service_manager, authentication_manager, authentication_token, habit_name, habit_freq)
        service_manager._user_information.clear()
        response = habit_handler.remove_habit(service_manager, authentication_manager, authentication_token, 0)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 14, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid authentication token", "Check if error_message is correct")

    def test_no_habit_with_id(self):
        """
        Tests if habit_handler returns the correct success code when the user data doesn't exist.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        habit_handler.add_habit(service_manager, authentication_manager, authentication_token, habit_name, habit_freq)
        response = habit_handler.remove_habit(service_manager, authentication_manager, authentication_token, 1)

        self.assertEqual(response["success_code"], 52, "Check if success_code is correct")
        self.assertEqual(response["error_message"], "No habit with id (1))", "Check if arror_message is correct")

    def test_non_str_token(self):
        """
        Test if an exception is thrown when the authentication token is not a str.
        """
        with self.assertRaises(TypeError):
            habit_handler.remove_habit(ServiceManager(), AuthenticationManager(), 0, 0)

    def test_none_token(self):
        """
        Test if an exception is thrown when the authentication token is None.
        """
        with self.assertRaises(TypeError):
            habit_handler.remove_habit(ServiceManager(), AuthenticationManager(), None, 0)

    def test_non_int_id(self):
        """
        Test if an exception is thrown when the authentication token is not a str.
        """
        with self.assertRaises(TypeError):
            habit_handler.remove_habit(ServiceManager(), AuthenticationManager(), 0, "0")

    def test_none_id(self):
        """
        Test if an exception is thrown when the authentication token is None.
        """
        with self.assertRaises(TypeError):
            habit_handler.remove_habit(ServiceManager(), AuthenticationManager(), 0, None)

    def test_service_manager_is_not_service_manager(self):
        """
        Test if an exception is thrown when the service_manager is not a ServiceManager.
        """
        with self.assertRaises(TypeError):
            habit_handler.remove_habit(0, AuthenticationManager(), 0, 0)
    
    def test_none_service_manager(self):
        """
        Test if an exception is thrown when the service_manager is None.
        """
        with self.assertRaises(TypeError):
            habit_handler.remove_habit(None, AuthenticationManager(), 0, 0)

    def test_authentication_manager_is_not_authentication_manager(self):
        """
        Test if an exception is thrown when the authentication_manager is not a AuthenticationManager.
        """
        with self.assertRaises(TypeError):
            habit_handler.remove_habit(ServiceManager(), 0, 0, 0)

    def test_none_authentication_manager(self):
        """
        Test if an exception is thrown when the authentication_manager is None.
        """
        with self.assertRaises(TypeError):
            habit_handler.remove_habit(ServiceManager(), None, 0, 0)