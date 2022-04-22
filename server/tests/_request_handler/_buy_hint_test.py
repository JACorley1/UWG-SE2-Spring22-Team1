import unittest
from urllib import response

from numpy import number
from backend.authentication_manager import AuthenticationManager

from backend.server import _RequestHandler
from backend.service_manager import ServiceManager
from backend.sudoku_puzzle import SudokuPuzzle


class TestBuyHint(unittest.TestCase):
    """
    Tests for the _generate_sudoku_puzzle method.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_request(self):
        """
        Tests if _RequestHandler correctly gets a hint for the current puzzle.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        puzzle = SudokuPuzzle()
        puzzle._solution = [[1] * 9] * 9

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        userdata = request_handler._service_manager.get_data_for_user(username)
        userdata.coins = 100
        userdata.sudoku_puzzle = puzzle
        response = request_handler._buy_hint(authentication_token)
        
        success_code = response["success_code"]
        number = response["number"]
        row = response["row"]
        col = response["col"]
        coins = response["coins"]

        self.assertEqual(success_code, 0, "Check if success_code is correct")
        self.assertEqual(number, 1, "Check if number is correct")
        self.assertEqual(coins, 80, "Check if coins is correct")
        self.assertTrue(puzzle.is_number_locked_at(row, col), "Check if number is locked")
        self.assertEqual(puzzle.get_number_at(row, col), number, "Check if number is correct")
        self.assertEqual(number, puzzle.get_solution_at(row, col), "Check if number is correct")

    def test_not_enough_coins(self):
        """
        Tests if _RequestHandler returns the correct success code when the user doesn't have enough coins.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        puzzle = SudokuPuzzle()

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        userdata = request_handler._service_manager.get_data_for_user(username)
        userdata.sudoku_puzzle = puzzle
        response = request_handler._buy_hint(authentication_token)
        
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 70, "Check if success_code is correct")
        self.assertEqual(error_message, "Not enough coins (have 0, need 20)", "Check if error_message is correct")

    def test_no_puzzle_in_progress(self):
        """
        Tests if _RequestHandler returns the correct success code when the user data doesn't exist.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        userdata = request_handler._service_manager.get_data_for_user(username)
        userdata.coins = 100
        response = request_handler._buy_hint(authentication_token)
        
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 61, "Check if success_code is correct")
        self.assertEqual(error_message, "No puzzle in progress", "Check if error_message is correct")

    def test_all_cells_are_locked(self):
        """
        Tests if _RequestHandler returns the correct success code when all cells are locked.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        puzzle = SudokuPuzzle()
        puzzle._number_locks = [[True] * 9] * 9

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        userdata = request_handler._service_manager.get_data_for_user(username)
        userdata.coins = 100
        userdata.sudoku_puzzle = puzzle
        response = request_handler._buy_hint(authentication_token)
        
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 63, "Check if success_code is correct")
        self.assertEqual(error_message, "No valid cells for hint", "Check if error_message is correct")

    def test_invalid_authentication_token(self):
        """
        Tests if _RequestHandler returns the correct success code when the authentication token doesn't exist.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"

        request_handler._register_user(username, password, email)
        response = request_handler._buy_hint("authentication_token")
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 14, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid authentication token", "Check if error_message is correct")

    def test_token_is_not_string(self):
        """
        Tests if _RequestHandler throws an exception when the authentication token is not a string.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        self.assertRaises(TypeError, request_handler._buy_hint, 0, "Check if exception is raised")

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
        response = request_handler._buy_hint(authentication_token)

        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 14, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid authentication token", "Check if error_message is correct")