import unittest
from urllib import response
from backend.authentication_manager import AuthenticationManager
from backend.server import _RequestHandler
from backend.service_manager import ServiceManager
from backend.sudoku_puzzle import SudokuPuzzle
import backend.request_handler.authentication_handler as authentication_handler
import backend.request_handler.user_handler as user_handler


class TestRetrieveData(unittest.TestCase):
    """
    Tests for the retrieve_data method.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_request(self):
        """
        Tests if user_handler correctly returns all of a new user's data.
        """
        username = "username"
        password = "password"
        email = "email@email.com"
        fields = ["username", "email", "coins", "sudoku_puzzle", "habits"]
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        puzzle = SudokuPuzzle()

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        userdata = service_manager.get_data_for_user(username)
        userdata.sudoku_puzzle = puzzle
        response = user_handler.retrieve_data(service_manager, authentication_manager, authentication_token, fields)
        
        self.assertEqual(response["success_code"], 0, "Check if success_code is correct")
        self.assertEqual(response["username"], username, "Check if username is correct.")
        self.assertEqual(response["email"], email, "Check if email is correct.")
        self.assertEqual(response["coins"], 0, "Check if coins is correct.")
        self.assertEqual(response["sudoku_puzzle"]["numbers"], puzzle.numbers, "Check if sudoku_puzzle numbers is correct.")
        self.assertEqual(response["sudoku_puzzle"]["number_locks"], puzzle.number_locks, "Check if sudoku_puzzle numbers is correct.")
        self.assertEqual(response["habits"], [], "Check if habits is correct.")

    def test_invalid_authentication_token(self):
        """
        Tests if user_handler returns the correct success code when the username doesn't exist.
        """
        username = "username"
        password = "password"
        email = "email@email.com"
        fields = ["username", "email", "coins", "sudoku_puzzle", "habits"]
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()

        authentication_handler.register_user(service_manager, username, password, email)
        response = user_handler.retrieve_data(service_manager, authentication_manager, "authentication_token", fields)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 14, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid authentication token", "Check if error_message is correct")

    def test_user_data_is_missing(self):
        """
        Tests if user_handler returns the correct success code when the user data doesn't exist.
        """
        username = "username"
        password = "password"
        email = "email@email.com"
        fields = ["username", "email", "coins", "sudoku_puzzle", "habits"]
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        service_manager._user_information.clear()
        response = user_handler.retrieve_data(service_manager, authentication_manager, authentication_token, fields)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 14, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid authentication token", "Check if error_message is correct")

    def test_no_fields_requested(self):
        """
        Tests if user_handler returns the correct success code when no fields are requested.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        fields = []

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        response = user_handler.retrieve_data(service_manager, authentication_manager, authentication_token, fields)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 41, "Check if success_code is correct")
        self.assertEqual(error_message, "No fields provided", "Check if error_message is correct")

    def test_unknown_field(self):
        """
        Tests if _RequestHandler returns the correct success code when no fields are requested.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        fields = ["bad_field"]

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        response = user_handler.retrieve_data(service_manager, authentication_manager, authentication_token, fields)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 40, "Check if success_code is correct")
        self.assertEqual(error_message, "Unknown field name (bad_field)", "Check if error_message is correct")

    def test_fields_not_list(self):
        """
        Tests if a TypeError is raised when fields is not a list
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        fields = "bad_field"

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        with self.assertRaises(TypeError):
            user_handler.retrieve_data(service_manager, authentication_manager, authentication_token, fields)

    def test_none_fields(self):
        """
        Tests if a TypeError is raised when fields is None
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        fields = None

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        with self.assertRaises(TypeError):
            user_handler.retrieve_data(service_manager, authentication_manager, authentication_token, fields)

    def test_authentication_token_not_string(self):
        """
        Tests if a TypeError is raised when authentication_token is not a string
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        fields = ["username", "email", "coins", "sudoku_puzzle", "habits"]
        authentication_token = 1

        authentication_handler.register_user(service_manager, username, password, email)
        with self.assertRaises(TypeError):
            user_handler.retrieve_data(service_manager, authentication_manager, authentication_token, fields)

    def test_none_authentication_token(self):
        """
        Tests if a TypeError is raised when authentication_token is None
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        fields = ["username", "email", "coins", "sudoku_puzzle", "habits"]
        authentication_token = None

        authentication_handler.register_user(service_manager, username, password, email)
        with self.assertRaises(TypeError):
            user_handler.retrieve_data(service_manager, authentication_manager, authentication_token, fields)

    def test_service_manager_not_service_manager(self):
        """
        Tests if a TypeError is raised when service_manager is not a ServiceManager
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        fields = ["username", "email", "coins", "sudoku_puzzle", "habits"]

        authentication_handler.register_user(service_manager, username, password, email)
        with self.assertRaises(TypeError):
            user_handler.retrieve_data(1, authentication_manager, username, fields)
    
    def test_none_service_manager(self):
        """
        Tests if a TypeError is raised when service_manager is None
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        fields = ["username", "email", "coins", "sudoku_puzzle", "habits"]

        authentication_handler.register_user(service_manager, username, password, email)
        with self.assertRaises(TypeError):
            user_handler.retrieve_data(None, authentication_manager, username, fields)
    
    def test_authentication_manager_not_authentication_manager(self):
        """
        Tests if a TypeError is raised when authentication_manager is not an AuthenticationManager
        """
        service_manager = ServiceManager()
        authentication_manager = 1
        username = "username"
        password = "password"
        email = "email@email.com"
        fields = ["username", "email", "coins", "sudoku_puzzle", "habits"]

        authentication_handler.register_user(service_manager, username, password, email)
        with self.assertRaises(TypeError):
            user_handler.retrieve_data(service_manager, authentication_manager, username, fields)
