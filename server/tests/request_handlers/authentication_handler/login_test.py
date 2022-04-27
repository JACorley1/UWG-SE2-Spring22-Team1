import unittest
from backend.authentication_manager import AuthenticationManager
from backend.server import _RequestHandler
from backend.service_manager import ServiceManager
import backend.request_handler.authentication_handler as authentication_handler

class TestLogin(unittest.TestCase):
    """
    Tests for the login method.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_request(self):
        """
        Tests if authentication_handler logs a user in correctly.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"

        authentication_handler.register_user(service_manager, username, password, email)
        response = authentication_handler.login(service_manager, authentication_manager, username, password)
        success_code = response["success_code"]
        authentication_token = response["authentication_token"]

        self.assertEqual(success_code, 0, "Check if success_code is correct")
        self.assertEqual(
            authentication_token, 
            authentication_manager.get_token_for_username(username), 
            "Check if authentication_token is correct"
        )

    def test_username_doesnt_exist(self):
        """
        Tests if authentication_handler returns the correct success code when the username doesn't exist.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"

        response = authentication_handler.login(service_manager, authentication_manager, username, "password")
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 30, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid username or password", "Check if error_message is correct")

    def test_wrong_password(self):
        """
        Tests if authentication_handler returns the correct success code when the password is wrong.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"

        authentication_handler.register_user(service_manager, username, password, email)
        response = authentication_handler.login(service_manager, authentication_manager, username, "")
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 30, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid username or password", "Check if error_message is correct")

    def test_none_username(self):
        """
        Tests if authentication_handler throws an exception when username is None.
        """
        username = None
        password = "password"

        self.assertRaises(
            TypeError,
            authentication_handler.login,
            (username, password),
            "Check if an exception is thrown when username is None"
        )

    def test_non_str_username(self):
        """
        Tests if authentication_handler throws an exception when username is a non-str.
        """
        username = 0
        password = "password"

        self.assertRaises(
            TypeError,
            authentication_handler.login,
            (username, password),
            "Check if an exception is thrown when username is a non-str"
        )

    def test_none_password(self):
        """
        Tests if authentication_handler throws an exception when password is None.
        """
        username = "username"
        password = None

        self.assertRaises(
            TypeError,
            authentication_handler.login,
            (username, password),
            "Check if an exception is thrown when password is None"
        )

    def test_non_str_password(self):
        """
        Tests if authentication_handler throws an exception when password is a non-str.
        """
        username = "username"
        password = 0

        self.assertRaises(
            TypeError,
            authentication_handler.login,
            (username, password),
            "Check if an exception is thrown when password is a non-str"
        )

    def test_none_service_manager(self):
        """
        Tests if authentication_handler throws an exception when service_manager is None.
        """
        username = "username"
        password = "password"
        service_manager = None

        self.assertRaises(
            TypeError,
            authentication_handler.login,
            (username, password, service_manager),
            "Check if an exception is thrown when service_manager is None"
        )
    
    def test_non_service_manager(self):
        """
        Tests if authentication_handler throws an exception when service_manager is a non-ServiceManager.
        """
        username = "username"
        password = "password"
        service_manager = 0

        self.assertRaises(
            TypeError,
            authentication_handler.login,
            (username, password, service_manager),
            "Check if an exception is thrown when service_manager is a non-ServiceManager"
        )
    
    def test_none_authentication_manager(self):
        """
        Tests if authentication_handler throws an exception when authentication_manager is None.
        """
        username = "username"
        password = "password"
        service_manager = ServiceManager()
        authentication_manager = None

        self.assertRaises(
            TypeError,
            authentication_handler.login,
            (username, password, service_manager, authentication_manager),
            "Check if an exception is thrown when authentication_manager is None"
        )
    
    def test_non_authentication_manager(self):
        """
        Tests if authentication_handler throws an exception when authentication_manager is a non-AuthenticationManager.
        """
        username = "username"
        password = "password"
        service_manager = ServiceManager()
        authentication_manager = 0

        self.assertRaises(
            TypeError,
            authentication_handler.login,
            (username, password, service_manager, authentication_manager),
            "Check if an exception is thrown when authentication_manager is a non-AuthenticationManager"
        )