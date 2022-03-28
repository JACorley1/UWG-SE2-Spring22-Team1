

import unittest
from backend.authentication_manager import AuthenticationManager

from backend.server import _RequestHandler
from backend.service_manager import ServiceManager


class TestLogin(unittest.TestCase):
    """
    Tests for the _login method.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_request(self):
        """
        Tests if _RequestHandler logs a user in correctly.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"

        request_handler._register_user(username, password, email)
        response = request_handler._login(username, password)
        success_code = response["success_code"]
        authentication_token = response["authentication_token"]

        self.assertEqual(success_code, 0, "Check if success_code is correct")
        self.assertEqual(
            authentication_token, 
            request_handler._authentication_manager.get_token_for_username(username), 
            "Check if authentication_token is correct"
        )

    def test_username_doesnt_exist(self):
        """
        Tests if _RequestHandler returns the correct success code when the username doesn't exist.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"

        response = request_handler._login(username, "password")
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 30, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid username or password", "Check if error_message is correct")

    def test_wrong_password(self):
        """
        Tests if _RequestHandler returns the correct success code when the password is wrong.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"

        request_handler._register_user(username, password, email)
        response = request_handler._login(username, "")
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 30, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid username or password", "Check if error_message is correct")

    def test_none_username(self):
        """
        Tests if _RequestHandler throws an exception when username is None.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = None
        password = "password"

        self.assertRaises(
            Exception,
            request_handler._login,
            (username, password),
            "Check if an exception is thrown when username is None"
        )

    def test_non_str_username(self):
        """
        Tests if _RequestHandler throws an exception when username is a non-str.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = 0
        password = "password"

        self.assertRaises(
            Exception,
            request_handler._login,
            (username, password),
            "Check if an exception is thrown when username is a non-str"
        )

    def test_none_password(self):
        """
        Tests if _RequestHandler throws an exception when password is None.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = None

        self.assertRaises(
            Exception,
            request_handler._login,
            (username, password),
            "Check if an exception is thrown when password is None"
        )

    def test_non_str_password(self):
        """
        Tests if _RequestHandler throws an exception when password is a non-str.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = 0

        self.assertRaises(
            Exception,
            request_handler._login,
            (username, password),
            "Check if an exception is thrown when password is a non-str"
        )
