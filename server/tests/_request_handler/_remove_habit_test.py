

import unittest
from backend.authentication_manager import AuthenticationManager

from backend.server import _RequestHandler
from backend.service_manager import ServiceManager


class TestRemoveData(unittest.TestCase):
    """
    Tests for the _remove_habit method.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_request(self):
        """
        Tests if _RequestHandler correctly returns all of a new user's data.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        request_handler._add_habit(authentication_token, habit_name, habit_freq)
        response = request_handler._remove_habit(authentication_token, 0)

        self.assertEqual(response["success_code"], 0, "Check if success_code is correct")

    def test_invalid_authentication_token(self):
        """
        Tests if _RequestHandler returns the correct success code when the authentication token is invalid.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        request_handler._add_habit(authentication_token, habit_name, habit_freq)
        response = request_handler._remove_habit("authentication_token", 0)
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
        request_handler._add_habit(authentication_token, habit_name, habit_freq)
        request_handler._service_manager._user_information.clear()
        response = request_handler._remove_habit(authentication_token, 0)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 14, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid authentication token", "Check if error_message is correct")

    def test_no_habit_with_id(self):
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        request_handler._add_habit(authentication_token, habit_name, habit_freq)
        response = request_handler._remove_habit(authentication_token, -1)

        self.assertEqual(response["success_code"], 52, "Check if success_code is correct")
        self.assertEqual(response["error_message"], "No habit with id (-1))", "Check if arror_message is correct")

    def test_non_str_token(self):
        """
        Test if an exception is thrown when the authentication token is not a str.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())

        self.assertRaises(Exception, request_handler._remove_habit, (0, 0), "Check if an exception is raised")

    def test_non_int_id(self):
        """
        Test if an exception is thrown when the authentication token is not a str.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())

        self.assertRaises(Exception, request_handler._remove_habit, (0, "0"), "Check if an exception is raised")
