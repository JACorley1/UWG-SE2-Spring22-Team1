import unittest
from backend.authentication_manager import AuthenticationManager

from backend.server import _RequestHandler
from backend.service_manager import ServiceManager
from backend.sudoku_puzzle import SudokuPuzzle


class TestUpdateSudokuPuzzle(unittest.TestCase):
    """
    Tests for the _generate_sudoku_puzzle method.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_request(self):
        """
        Tests if _RequestHandler correctly updates the sudoku puzzle.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        numbers = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        userdata = request_handler._service_manager.get_data_for_user(username)
        userdata.sudoku_puzzle = SudokuPuzzle()
        response = request_handler._update_sudoku_puzzle(authentication_token, numbers)
        puzzle = userdata.sudoku_puzzle
        
        self.assertEqual(response["success_code"], 0, "Check if success_code is correct")
        self.assertEqual(puzzle.numbers, numbers, "Check if puzzle is correct")

    def test_puzzle_not_in_progress(self):
        """
        Tests if _RequestHandler returns the correct success code when the puzzle is not in progress.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        response = request_handler._update_sudoku_puzzle(authentication_token, [[0] * 9] * 9)

        self.assertEqual(response["success_code"], 61, "Check if success_code is correct")
        self.assertEqual(response["error_message"], "No puzzle in progress", "Check if error_message is correct")

    def test_invalid_number(self):
        """
        Tests if _RequestHandler throws an exception when the number is not an int.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        user_data = request_handler._service_manager.get_data_for_user(username)
        user_data.sudoku_puzzle = SudokuPuzzle()
        response = request_handler._update_sudoku_puzzle(authentication_token, [[-1] * 9] * 9)

        self.assertEqual(response["success_code"], 60, "Check if success_code is correct")
        self.assertEqual(response["error_message"], "Invalid number (0, 0)", "Check if error_message is correct")

    def test_update_locked_number(self):
        """
        Tests if _RequestHandler throws an exception when the number is locked.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        user_data = request_handler._service_manager.get_data_for_user(username)
        user_data.sudoku_puzzle = SudokuPuzzle()
        user_data.sudoku_puzzle.set_number_locked_at(0, 0, True)
        response = request_handler._update_sudoku_puzzle(authentication_token, [[1] * 9] * 9)

        self.assertEqual(response["success_code"], 62, "Check if success_code is correct")
        self.assertEqual(response["error_message"], "Can't change locked number (0, 0)", "Check if error_message is correct")

    def test_invalid_authentication_token(self):
        """
        Tests if _RequestHandler returns the correct success code when the authentication token doesn't exist.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        numbers = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        request_handler._register_user(username, password, email)
        response = request_handler._update_sudoku_puzzle("authentication_token", numbers)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 14, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid authentication token", "Check if error_message is correct")
    
    def test_invalid_authentication_token(self):
        """
        Tests if _RequestHandler returns the correct success code when the authentication token doesn't exist.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        numbers = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        request_handler._register_user(username, password, email)
        response = request_handler._update_sudoku_puzzle("authentication_token", numbers)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 14, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid authentication token", "Check if error_message is correct")
    
    def test_too_many_rows(self):
        """
        Tests if the correct response is sent if there are too many rows.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        response = request_handler._update_sudoku_puzzle(authentication_token, [[]] * 10)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 64, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid puzzle size", "Check if error_message is correct")
        
    def test_too_few_rows(self):
        """
        Tests if the correct response is sent if there are too few rows.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        response = request_handler._update_sudoku_puzzle(authentication_token, [[]])
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 64, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid puzzle size", "Check if error_message is correct")
    
    def test_too_many_columns(self):
        """
        Tests if the correct response is sent if there are too many columns.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        response = request_handler._update_sudoku_puzzle(authentication_token, [[1] * 10] * 9)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 64, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid puzzle size", "Check if error_message is correct")
    
    def test_too_few_columns(self):
        """
        Tests if the correct response is sent if there are too few columns.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        response = request_handler._update_sudoku_puzzle(authentication_token, [[1]] * 9)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 64, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid puzzle size", "Check if error_message is correct")

    def test_token_is_not_string(self):
        """
        Tests if _RequestHandler throws an exception when the authentication token is not a string.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        self.assertRaises(TypeError, request_handler._generate_sudoku_puzzle, 0, [], "Check if exception is raised")

    def test_numbers_is_not_list(self):
        """
        Tests if _RequestHandler throws an exception when the authentication token is not a string.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        self.assertRaises(
            TypeError, 
            request_handler._generate_sudoku_puzzle, 
            "authentication_token", 
            0, 
            "Check if exception is raised"
        )

    def test_user_data_is_missing(self):
        """
        Tests if _RequestHandler returns the correct success code when the user data doesn't exist.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        numbers = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        request_handler._service_manager._user_information.clear()
        response = request_handler._update_sudoku_puzzle(authentication_token, numbers)

        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 14, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid authentication token", "Check if error_message is correct")