import unittest
from backend.authentication_manager import AuthenticationManager

from backend.server import _RequestHandler
from backend.service_manager import ServiceManager
from backend.sudoku_puzzle import SudokuPuzzle


class TestRetrieveData(unittest.TestCase):
    """
    Tests for the _retrieve_data method.

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
        fields = ["username", "email", "coins", "sudoku_puzzle", "habits"]
        puzzle = SudokuPuzzle()

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        userdata = request_handler._service_manager.get_data_for_user(username)
        userdata.sudoku_puzzle = puzzle
        response = request_handler._retrieve_data(authentication_token, fields)
        
        self.assertEqual(response["success_code"], 0, "Check if success_code is correct")
        self.assertEqual(response["username"], username, "Check if username is correct.")
        self.assertEqual(response["email"], email, "Check if email is correct.")
        self.assertEqual(response["coins"], 0, "Check if coins is correct.")
        self.assertEqual(response["sudoku_puzzle"]["numbers"], puzzle.numbers, "Check if sudoku_puzzle numbers is correct.")
        self.assertEqual(response["sudoku_puzzle"]["number_locks"], puzzle.number_locks, "Check if sudoku_puzzle numbers is correct.")
        self.assertEqual(response["habits"], [], "Check if habits is correct.")

    def test_invalid_authentication_token(self):
        """
        Tests if _RequestHandler returns the correct success code when the username doesn't exist.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        fields = ["username", "email", "coins", "sudoku_puzzle", "habits"]

        request_handler._register_user(username, password, email)
        response = request_handler._retrieve_data("authentication_token", fields)
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
        fields = ["username", "email", "coins", "sudoku_puzzle", "habits"]

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        request_handler._service_manager._user_information.clear()
        response = request_handler._retrieve_data(authentication_token, fields)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 14, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid authentication token", "Check if error_message is correct")

    def test_no_fields_requested(self):
        """
        Tests if _RequestHandler returns the correct success code when no fields are requested.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        fields = []

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        response = request_handler._retrieve_data(authentication_token, fields)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 41, "Check if success_code is correct")
        self.assertEqual(error_message, "No fields provided", "Check if error_message is correct")

    def test_unknown_field(self):
        """
        Tests if _RequestHandler returns the correct success code when no fields are requested.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        fields = ["bad_field"]

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        response = request_handler._retrieve_data(authentication_token, fields)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 40, "Check if success_code is correct")
        self.assertEqual(error_message, "Unknown field name (bad_field)", "Check if error_message is correct")
