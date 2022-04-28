import unittest
from backend.service_manager import ServiceManager
from backend.user_data import UserData
import backend.request_handler.authentication_handler as authentication_handler

class TestConstructor(unittest.TestCase):    
    """
    Tests for the register_user method.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_request(self):
        """
        Checks if the authentication_handler registers a valid user.
        """
        service_manager = ServiceManager()
        username = "username"
        password = "password"
        email = "email@email.com"

        result = authentication_handler.register_user(service_manager, username, password, email)
        user_data: UserData = service_manager._user_information[username]

        self.assertEqual(result["success_code"], 0, "Check if success_code is correct")
        self.assertEqual(user_data.username, username, "Check if the username is correct")
        self.assertEqual(user_data.password, password, "Check if the password is correct")
        self.assertEqual(user_data.email, email, "Check if the email is correct")

    def test_duplicate_username(self):
        """
        Checks if the authentication_handler registers a valid user.
        """
        service_manager = ServiceManager()
        username = "username"
        password = "password"
        email = "email@email.com"

        authentication_handler.register_user(service_manager, username, password, email)
        result = authentication_handler.register_user(service_manager, username, password, email)

        self.assertEqual(result["success_code"], 20, "Check if success_code is correct")
        self.assertEqual(result["error_message"], f"Username ({username}) already exists")

    def test_empty_username(self):
        """
        Checks if the the success code and error message are correct when the username is empty.
        """
        username = ""
        password = "password"
        email = "email@email.com"
        service_manager = ServiceManager()

        authentication_handler.register_user(service_manager, username, password, email)
        result = authentication_handler.register_user(service_manager, username, password, email)

        self.assertEqual(result["success_code"], 21, "Check if success_code is correct")
        self.assertEqual(result["error_message"], f"Username ({username}) is invalid", "Check if error_message is correct")

    def test_none_username(self):
        """
        Checks if the the success code and error message are correct when the username is None.
        """
        username = None
        password = "password"
        email = "email@email.com"
        service_manager = ServiceManager()

        authentication_handler.register_user(service_manager, username, password, email)
        result = authentication_handler.register_user(service_manager, username, password, email)

        self.assertEqual(result["success_code"], 21, "Check if success_code is correct")
        self.assertEqual(result["error_message"], f"Username ({username}) is invalid", "Check if error_message is correct")

    def test_non_str_username(self):
        """
        Checks if the the success code and error message are correct when the username is not a str.
        """
        username = 0
        password = "password"
        email = "email@email.com"
        service_manager = ServiceManager()

        authentication_handler.register_user(service_manager, username, password, email)
        result = authentication_handler.register_user(service_manager, username, password, email)

        self.assertEqual(result["success_code"], 21, "Check if success_code is correct")
        self.assertEqual(result["error_message"], f"Username ({username}) is invalid", "Check if error_message is correct")

    def test_empty_password(self):
        """
        Checks if the the success code and error message are correct when the password is empty.
        """
        username = "username"
        password = ""
        email = "email@email.com"
        service_manager = ServiceManager()

        authentication_handler.register_user(service_manager, username, password, email)
        result = authentication_handler.register_user(service_manager, username, password, email)

        self.assertEqual(result["success_code"], 22, "Check if success_code is correct")
        self.assertEqual(result["error_message"], f"Password is invalid")

    def test_none_password(self):
        """
        Checks if the the success code and error message are correct when the password is None.
        """
        username = "username"
        password = None
        email = "email@email.com"
        service_manager = ServiceManager()

        authentication_handler.register_user(service_manager, username, password, email)
        result = authentication_handler.register_user(service_manager, username, password, email)

        self.assertEqual(result["success_code"], 22, "Check if success_code is correct")
        self.assertEqual(result["error_message"], f"Password is invalid")

    def test_non_str_password(self):
        """
        Checks if the the success code and error message are correct when the password is a non str.
        """
        username = "username"
        password = 0
        email = "email@email.com"
        service_manager = ServiceManager()

        authentication_handler.register_user(service_manager, username, password, email)
        result = authentication_handler.register_user(service_manager, username, password, email)

        self.assertEqual(result["success_code"], 22, "Check if success_code is correct")
        self.assertEqual(result["error_message"], f"Password is invalid")

    def test_empty_email(self):
        """
        Checks if the the success code and error message are correct when the password is empty.
        """
        username = "username"
        password = "password"
        email = ""
        service_manager = ServiceManager()

        authentication_handler.register_user(service_manager, username, password, email)
        result = authentication_handler.register_user(service_manager, username, password, email)

        self.assertEqual(result["success_code"], 23, "Check if success_code is correct")
        self.assertEqual(result["error_message"], f"Email ({email}) is invalid")

    def test_none_email(self):
        """
        Checks if the the success code and error message are correct when the password is None.
        """
        username = "username"
        password = "password"
        email = None
        service_manager = ServiceManager()

        authentication_handler.register_user(service_manager, username, password, email)
        result = authentication_handler.register_user(service_manager, username, password, email)

        self.assertEqual(result["success_code"], 23, "Check if success_code is correct")
        self.assertEqual(result["error_message"], f"Email ({email}) is invalid")

    def test_non_str_email(self):
        """
        Checks if the the success code and error message are correct when the password is a non str.
        """
        username = "username"
        password = "password"
        email = 0
        service_manager = ServiceManager()

        authentication_handler.register_user(service_manager, username, password, email)
        result = authentication_handler.register_user(service_manager, username, password, email)

        self.assertEqual(result["success_code"], 23, "Check if success_code is correct")
        self.assertEqual(result["error_message"], f"Email ({email}) is invalid")

    def test_service_manager_is_none(self):
        """
        Checks if the the success code and error message are correct when the service manager is None.
        """
        username = "username"
        password = "password"
        email = "email@email.com"
        service_manager = None

        self.assertRaises(
            TypeError, 
            authentication_handler.register_user, 
            (service_manager, username, password, email),
            "Check if the function raises a TypeError when the service manager is None"
        )

    def test_service_manager_is_not_a_service_manager(self):
        """
        Checks if the the success code and error message are correct when the service manager is not a service manager.
        """
        username = "username"
        password = "password"
        email = "email@email.com"
        service_manager = 0

        self.assertRaises(
            TypeError,
            authentication_handler.register_user,
            (service_manager, username, password, email),
            "Check if the function raises a TypeError when the service manager is not a service manager"
        )