import unittest
from backend.authentication_manager import AuthenticationManager

from backend.server import _RequestHandler
from backend.service_manager import ServiceManager
from backend.sudoku_puzzle import SudokuPuzzle


class TestGenerateSudokuPuzzle(unittest.TestCase):
    """
    Tests for the _generate_sudoku_puzzle method.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_request(self):
        """
        Tests if _RequestHandler correctly generates a new sudoku puzzle.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        response = request_handler._generate_sudoku_puzzle(authentication_token)
        userdata = request_handler._service_manager.get_data_for_user(username)
        puzzle = userdata.sudoku_puzzle
        
        self.assertEqual(response["success_code"], 0, "Check if success_code is correct")
        self.assertEqual(response["sudoku_puzzle"]["numbers"], puzzle.numbers, "Check if sudoku_puzzle numbers is correct.")
        self.assertEqual(response["sudoku_puzzle"]["number_locks"], puzzle.number_locks, "Check if sudoku_puzzle numbers is correct.")

    def test_invalid_authentication_token(self):
        """
        Tests if _RequestHandler returns the correct success code when the authentication token doesn't exist.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"

        request_handler._register_user(username, password, email)
        response = request_handler._generate_sudoku_puzzle("authentication_token")
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 14, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid authentication token", "Check if error_message is correct")

    def test_token_is_not_string(self):
        """
        Tests if _RequestHandler throws an exception when the authentication token is not a string.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        self.assertRaises(TypeError, request_handler._generate_sudoku_puzzle, 0, "Check if exception is raised")

    def test_user_data_is_missing(self):
        """
        Tests if _RequestHandler returns the correct success code when the user data doesn't exist.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        request_handler._service_manager._user_information.clear()
        response = request_handler._generate_sudoku_puzzle(authentication_token)

        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 14, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid authentication token", "Check if error_message is correct")