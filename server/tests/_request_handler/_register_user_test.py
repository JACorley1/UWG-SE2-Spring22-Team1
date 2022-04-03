import unittest
from server.server import _RequestHandler
from server.service_manager import ServiceManager
from server.user_data import UserData

class TestConstructor(unittest.TestCase):    
    """
    Tests for the _register_user method.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_request(self):
        """
        Checks if the RequestHandler registers a valid user.
        """
        username = "username"
        password = "password"
        email = "email@email.com"
        request_handler = _RequestHandler(ServiceManager())
        result = request_handler._register_user(username, password, email)
        user_data: UserData = request_handler._service_manager._user_information[username]

        self.assertEqual(result["successCode"], 0, "Check if success_code is correct")
        self.assertEqual(user_data.get_username(), username, "Check if the username is correct")
        self.assertEqual(user_data.get_password(), password, "Check if the password is correct")
        self.assertEqual(user_data.get_email(), email, "Check if the email is correct")

    def test_duplicate_username(self):
        """
        Checks if the correct success code and error message are returned when using a duplicate username.
        """
        username = "username"
        password = "password"
        email = "email@email.com"
        request_handler = _RequestHandler(ServiceManager())
        request_handler._register_user(username, password, email)
        result = request_handler._register_user(username, password, email)

        self.assertEqual(result["successCode"], 20, "Check if success_code is correct")
        self.assertEqual(result["error_message"], f"Username ({username}) already exists")

    def test_empty_username(self):
        """
        Checks if the the success code and error message are correct when the username is empty.
        """
        username = ""
        password = "password"
        email = "email@email.com"
        request_handler = _RequestHandler(ServiceManager())
        result = request_handler._register_user(username, password, email)

        self.assertEqual(result["successCode"], 21, "Check if success_code is correct")
        self.assertEqual(result["error_message"], f"Username ({username}) is invalid", "Check if error_message is correct")

    def test_none_username(self):
        """
        Checks if the the success code and error message are correct when the username is None.
        """
        username = None
        password = "password"
        email = "email@email.com"
        request_handler = _RequestHandler(ServiceManager())
        result = request_handler._register_user(username, password, email)

        self.assertEqual(result["successCode"], 21, "Check if success_code is correct")
        self.assertEqual(result["error_message"], f"Username ({username}) is invalid", "Check if error_message is correct")

    def test_non_str_username(self):
        """
        Checks if the the success code and error message are correct when the username is not a str.
        """
        username = 0
        password = "password"
        email = "email@email.com"
        request_handler = _RequestHandler(ServiceManager())
        result = request_handler._register_user(username, password, email)

        self.assertEqual(result["successCode"], 21, "Check if success_code is correct")
        self.assertEqual(result["error_message"], f"Username ({username}) is invalid", "Check if error_message is correct")

    def test_empty_password(self):
        """
        Checks if the the success code and error message are correct when the password is empty.
        """
        username = "username"
        password = ""
        email = "email@email.com"
        request_handler = _RequestHandler(ServiceManager())
        result = request_handler._register_user(username, password, email)

        self.assertEqual(result["successCode"], 22, "Check if success_code is correct")
        self.assertEqual(result["error_message"], f"Password is invalid")

    def test_none_password(self):
        """
        Checks if the the success code and error message are correct when the password is None.
        """
        username = "username"
        password = None
        email = "email@email.com"
        request_handler = _RequestHandler(ServiceManager())
        result = request_handler._register_user(username, password, email)

        self.assertEqual(result["successCode"], 22, "Check if success_code is correct")
        self.assertEqual(result["error_message"], f"Password is invalid")

    def test_non_str_password(self):
        """
        Checks if the the success code and error message are correct when the password is a non str.
        """
        username = "username"
        password = 0
        email = "email@email.com"
        request_handler = _RequestHandler(ServiceManager())
        result = request_handler._register_user(username, password, email)

        self.assertEqual(result["successCode"], 22, "Check if success_code is correct")
        self.assertEqual(result["error_message"], f"Password is invalid")

    def test_empty_email(self):
        """
        Checks if the the success code and error message are correct when the password is empty.
        """
        username = "username"
        password = "password"
        email = ""
        request_handler = _RequestHandler(ServiceManager())
        result = request_handler._register_user(username, password, email)

        self.assertEqual(result["successCode"], 23, "Check if success_code is correct")
        self.assertEqual(result["error_message"], f"Email ({email}) is invalid")

    def test_none_email(self):
        """
        Checks if the the success code and error message are correct when the password is None.
        """
        username = "username"
        password = "password"
        email = None
        request_handler = _RequestHandler(ServiceManager())
        result = request_handler._register_user(username, password, email)

        self.assertEqual(result["successCode"], 23, "Check if success_code is correct")
        self.assertEqual(result["error_message"], f"Email ({email}) is invalid")

    def test_non_str_email(self):
        """
        Checks if the the success code and error message are correct when the password is a non str.
        """
        username = "username"
        password = "password"
        email = 0
        request_handler = _RequestHandler(ServiceManager())
        result = request_handler._register_user(username, password, email)

        self.assertEqual(result["successCode"], 23, "Check if success_code is correct")
        self.assertEqual(result["error_message"], f"Email ({email}) is invalid")
