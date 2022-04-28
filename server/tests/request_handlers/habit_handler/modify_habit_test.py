import unittest
from backend.authentication_manager import AuthenticationManager
from backend.server import habit_handler
from backend.service_manager import ServiceManager
import backend.request_handler.habit_handler as habit_handler
import backend.request_handler.authentication_handler as authentication_handler


class TestModifyHabit(unittest.TestCase):
    """
    Tests for the modify_habit method.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_request(self):
        """
        Tests if habit_handler correctly modifies a habit.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0
        new_habit_name = "Habit1"
        new_habit_freq = 1

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        habit_handler.add_habit(service_manager, authentication_manager, authentication_token, habit_name, habit_freq)
        response = habit_handler.modify_habit(service_manager, authentication_manager, authentication_token, 0, new_habit_name, new_habit_freq)

        habit = service_manager._user_information[username].habits[0]

        self.assertEqual(response["success_code"], 0, "Check if success_code is correct")
        self.assertEqual(habit.name, new_habit_name, "Check if habit name was updated")
        self.assertEqual(habit.frequency, new_habit_freq, "Check is habit frequency was updated")

    def test_invalid_authentication_token(self):
        """
        Tests if habit_handler returns the correct success code when the username doesn't exist.
        """
        service_manger = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        authentication_handler.register_user(service_manger, username, password, email)
        response = habit_handler.modify_habit(service_manger, authentication_manager, "invalid_token", 0, habit_name, habit_freq)
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
        response = habit_handler.modify_habit(service_manager, authentication_manager, authentication_token, 0, habit_name, habit_freq)
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
        habit_name = "Habit"
        habit_freq = 0
        new_habit_name = ""
        new_habit_freq = 1

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        habit_handler.add_habit(service_manager, authentication_manager, authentication_token, habit_name, habit_freq)
        response = habit_handler.modify_habit(service_manager, authentication_manager, authentication_token, 0, new_habit_name, new_habit_freq)
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
        habit_freq = 0
        new_habit_name = "Habit1"
        new_habit_freq = -1

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        habit_handler.add_habit(service_manager, authentication_manager, authentication_token, habit_name, habit_freq)
        response = habit_handler.modify_habit(service_manager, authentication_manager, authentication_token, 0, new_habit_name, new_habit_freq)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 51, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid habit frequency (-1)", "Check if error_message is correct")

    def test_invalid_habit_id(self):
        """
        Tests if habit_handler returns the correct success code when no habit exists with the given id.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0
        new_habit_name = "Habit1"
        new_habit_freq = 0

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        habit_handler.add_habit(service_manager, authentication_manager, authentication_token, habit_name, habit_freq)
        response = habit_handler.modify_habit(service_manager, authentication_manager, authentication_token, 1, new_habit_name, new_habit_freq)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 52, "Check if success_code is correct")
        self.assertEqual(error_message, "No habit with id (1)", "Check if error_message is correct")

    def test_non_str_token(self):
        """
        Test if an exception is thrown when the authentication token is not a str.
        """
        with self.assertRaises(TypeError):
            habit_handler.modify_habit(ServiceManager(), AuthenticationManager(), 1, 0, "Habit", 0)

    def test_non_str_habit_name(self):
        """
        Test if an exception is thrown when the habit name is not a str.
        """
        with self.assertRaises(TypeError):
            habit_handler.modify_habit(ServiceManager(), AuthenticationManager(), "token", 0, 1, 0)

    def test_non_int_habit_frequency(self):
        """
        Test if an exception is thrown when the habit frequency is not an int.
        """
        with self.assertRaises(TypeError):
            habit_handler.modify_habit(ServiceManager(), AuthenticationManager(), "token", 0, "Habit", "0")

    def test_non_int_habit_id(self):
        """
        Test if an exception is thrown when the id is not an int.
        """
        with self.assertRaises(TypeError):
            habit_handler.modify_habit(ServiceManager(), AuthenticationManager(), "token", "0", "Habit", 0)

    def test_service_manager_not_service_manager(self):
        """
        Test if an exception is thrown when the service manager is not a service manager.
        """
        with self.assertRaises(TypeError):
            habit_handler.modify_habit(1, AuthenticationManager(), "token", 0, "Habit", 0)
    
    def test_none_service_manager(self):
        """
        Test if an exception is thrown when the service manager is None.
        """
        with self.assertRaises(TypeError):
            habit_handler.modify_habit(None, AuthenticationManager(), "token", 0, "Habit", 0)

    def test_authentication_manager_not_authentication_manager(self):
        """
        Test if an exception is thrown when the authentication manager is not an authentication manager.
        """
        with self.assertRaises(TypeError):
            habit_handler.modify_habit(ServiceManager(), 1, "token", 0, "Habit", 0)

    def test_none_authentication_manager(self):
        """
        Test if an exception is thrown when the authentication manager is None.
        """
        with self.assertRaises(TypeError):
            habit_handler.modify_habit(ServiceManager(), None, "token", 0, "Habit", 0)
