import unittest
from backend.authentication_manager import AuthenticationManager
from backend.service_manager import ServiceManager
import backend.request_handler.authentication_handler as authentication_handler
import backend.request_handler.habit_handler as habit_handler


class TestAddHabit(unittest.TestCase):
    """
    Tests for the add_habit method.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_request(self):
        """
        Tests if habit_handler correctly adds a new habit.
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
        response = habit_handler.add_habit(service_manager, authentication_manager, authentication_token, habit_name, habit_freq)

        self.assertEqual(response["success_code"], 0, "Check if success_code is correct")

    def test_invalid_authentication_token(self):
        """
        Tests if habit_handler returns the correct success code when the username doesn't exist.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        authentication_handler.register_user(service_manager, username, password, email)
        response = habit_handler.add_habit(service_manager, authentication_manager, "invalid_token", habit_name, habit_freq)
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
        service_manager._user_information.clear()
        response = habit_handler.add_habit(service_manager, authentication_manager, authentication_token, habit_name, habit_freq)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 14, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid authentication token", "Check if error_message is correct")

    def test_invalid_habit_name(self):
        """
        Tests if habit_handler returns the correct success code when the user data doesn't exist.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = ""
        habit_freq = 0

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        response = habit_handler.add_habit(service_manager, authentication_manager, authentication_token, habit_name, habit_freq)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 50, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid habit name ()", "Check if error_message is correct")

    def test_invalid_habit_frequency(self):
        """
        Tests if habit_handler returns the correct success code when the user data doesn't exist.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = -1

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        response = habit_handler.add_habit(service_manager, authentication_manager, authentication_token, habit_name, habit_freq)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 51, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid habit frequency (-1)", "Check if error_message is correct")

    def test_non_str_token(self):
        """
        Test if an exception is thrown when the authentication token is not a str.
        """
        with self.assertRaises(TypeError):
            habit_handler.add_habit(ServiceManager(), AuthenticationManager(), 0, "Habit", 0)

    def test_none_token(self):
        """
        Test if an exception is thrown when the authentication token is None.
        """
        with self.assertRaises(TypeError):
            habit_handler.add_habit(ServiceManager(), AuthenticationManager(), None, "Habit", 0)

    def test_non_str_habit_name(self):
        """
        Test if an exception is thrown when the authentication token is not a str.
        """
        with self.assertRaises(TypeError):
            habit_handler.add_habit(ServiceManager(), AuthenticationManager(), "token", 0, 0)

    def test_none_habit_name(self):
        """
        Test if an exception is thrown when the authentication token is None.
        """
        with self.assertRaises(TypeError):
            habit_handler.add_habit(ServiceManager(), AuthenticationManager(), "token", None, 0)

    def test_non_int_habit_frequency(self):
        """
        Test if an exception is thrown when the authentication token is not a str.
        """
        with self.assertRaises(TypeError):
            habit_handler.add_habit(ServiceManager(), AuthenticationManager(), "token", "Habit", "0")
    
    def test_none_habit_frequency(self):
        """
        Test if an exception is thrown when the authentication token is None.
        """
        with self.assertRaises(TypeError):
            habit_handler.add_habit(ServiceManager(), AuthenticationManager(), "token", "Habit", None)
    
    def test_service_manager_not_service_manager(self):
        """
        Test if an exception is thrown when the service manager is not a ServiceManager.
        """
        with self.assertRaises(TypeError):
            habit_handler.add_habit(0, AuthenticationManager(), "token", "Habit", 0)
    
    def test_none_service_manager(self):
        """
        Test if an exception is thrown when the service manager is None.
        """
        with self.assertRaises(TypeError):
            habit_handler.add_habit(None, AuthenticationManager(), "token", "Habit", 0)

    def test_authentication_manager_not_authentication_manager(self):
        """
        Test if an exception is thrown when the authentication manager is not a AuthenticationManager.
        """
        with self.assertRaises(TypeError):
            habit_handler.add_habit(ServiceManager(), 0, "token", "Habit", 0)
    
    def test_none_authentication_manager(self):
        """
        Test if an exception is thrown when the authentication manager is None.
        """
        with self.assertRaises(TypeError):
            habit_handler.add_habit(ServiceManager(), None, "token", "Habit", 0)
