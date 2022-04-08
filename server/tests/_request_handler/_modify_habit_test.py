

import unittest
from backend.authentication_manager import AuthenticationManager

from backend.server import _RequestHandler
from backend.service_manager import ServiceManager


class TestModifyHabit(unittest.TestCase):
    """
    Tests for the _modify_habit method.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_request(self):
        """
        Tests if _RequestHandler correctly modifies a habit.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0
        new_habit_name = "Habit1"
        new_habit_freq = 1

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        request_handler._add_habit(authentication_token, habit_name, habit_freq)
        response = request_handler._modify_habit(authentication_token, 0, new_habit_name, new_habit_freq)
        habit = request_handler._service_manager._user_information[username].habits[0]

        self.assertEqual(response["success_code"], 0, "Check if success_code is correct")
        self.assertEqual(habit.name, new_habit_name, "Check if habit name was updated")
        self.assertEqual(habit.frequency, new_habit_freq, "Check is habit frequency was updated")

    def test_invalid_authentication_token(self):
        """
        Tests if _RequestHandler returns the correct success code when the username doesn't exist.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        request_handler._register_user(username, password, email)
        response = request_handler._modify_habit("authentication_token", 0, habit_name, habit_freq)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 14, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid authentication token", "Check if error_message is correct")

    def test_user_data_is_missing(self):
        """
        Tests if _RequestHandler returns the correct success code when the user data doesn't exist.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        request_handler._service_manager._user_information.clear()
        response = request_handler._modify_habit(authentication_token, 0, habit_name, habit_freq)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 14, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid authentication token", "Check if error_message is correct")

    def test_invalid_habit_name(self):
        """
        Tests if _RequestHandler returns the correct success code when the user data doesn't exist.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0
        new_habit_name = ""
        new_habit_freq = 1

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        request_handler._add_habit(authentication_token, habit_name, habit_freq)
        response = request_handler._modify_habit(authentication_token, 0, new_habit_name, new_habit_freq)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 50, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid habit name ()", "Check if error_message is correct")

    def test_invalid_habit_frequency(self):
        """
        Tests if _RequestHandler returns the correct success code when the user data doesn't exist.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0
        new_habit_name = "Habit1"
        new_habit_freq = -1

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        request_handler._add_habit(authentication_token, habit_name, habit_freq)
        response = request_handler._modify_habit(authentication_token, 0, new_habit_name, new_habit_freq)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 51, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid habit frequency (-1)", "Check if error_message is correct")

    def test_invalid_habit_id(self):
        """
        Tests if _RequestHandler returns the correct success code when no habit exists with the given id.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0
        new_habit_name = "Habit1"
        new_habit_freq = 0

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        request_handler._add_habit(authentication_token, habit_name, habit_freq)
        response = request_handler._modify_habit(authentication_token, -1, new_habit_name, new_habit_freq)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 52, "Check if success_code is correct")
        self.assertEqual(error_message, "No habit with id (-1)", "Check if error_message is correct")

    def test_non_str_token(self):
        """
        Test if an exception is thrown when the authentication token is not a str.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())

        self.assertRaises(Exception, request_handler._modify_habit, (0, 0, "Habit", 0), "Check if an exception is raised")

    def test_non_str_habit_name(self):
        """
        Test if an exception is thrown when the habit name is not a str.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())

        self.assertRaises(Exception, request_handler._modify_habit, ("token", 0, 0, 0), "Check if an exception is raised")

    def test_non_int_habit_frequency(self):
        """
        Test if an exception is thrown when the habit frequency is not an int.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())

        self.assertRaises(Exception, request_handler._add_habit, ("token", 0, "Habit", "freq"), "Check if an exception is raised")

    def test_non_int_habit_id(self):
        """
        Test if an exception is thrown when the id is not an int.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())

        self.assertRaises(Exception, request_handler._add_habit, ("token", "1", "Habit", 0), "Check if an exception is raised")
