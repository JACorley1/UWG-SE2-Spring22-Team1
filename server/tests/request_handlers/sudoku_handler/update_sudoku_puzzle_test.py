import unittest
from backend.authentication_manager import AuthenticationManager
from backend.server import _RequestHandler
from backend.service_manager import ServiceManager
from backend.sudoku_puzzle import SudokuPuzzle
import backend.request_handler.sudoku_handler as sudoku_handler
import backend.request_handler.authentication_handler as authentication_handler

class TestUpdateSudokuPuzzle(unittest.TestCase):
    """
    Tests for the update_sudoku_puzzle method.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_request(self):
        """
        Tests if update_sudoku_puzzle correctly updates the sudoku puzzle.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
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

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        userdata = service_manager.get_data_for_user(username)
        userdata.sudoku_puzzle = SudokuPuzzle()
        response = sudoku_handler.update_sudoku_puzzle(service_manager, authentication_manager, authentication_token, numbers)
        puzzle = userdata.sudoku_puzzle
        
        self.assertEqual(response["success_code"], 0, "Check if success_code is correct")
        self.assertEqual(puzzle.numbers, numbers, "Check if puzzle is correct")

    def test_puzzle_not_in_progress(self):
        """
        Tests if update_sudoku_puzzle returns the correct success code when the puzzle is not in progress.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        response = sudoku_handler.update_sudoku_puzzle(service_manager, authentication_manager, authentication_token, [[1] * 9] * 9)

        self.assertEqual(response["success_code"], 61, "Check if success_code is correct")
        self.assertEqual(response["error_message"], "No puzzle in progress", "Check if error_message is correct")

    def test_invalid_number(self):
        """
        Tests if update_sudoku_puzzle throws an exception when the number is not an int.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        user_data = service_manager.get_data_for_user(username)
        user_data.sudoku_puzzle = SudokuPuzzle()
        response = sudoku_handler.update_sudoku_puzzle(service_manager, authentication_manager, authentication_token, [[-1] * 9] * 9)

        self.assertEqual(response["success_code"], 60, "Check if success_code is correct")
        self.assertEqual(response["error_message"], "Invalid number (0, 0)", "Check if error_message is correct")

    def test_update_locked_number(self):
        """
        Tests if update_sudoku_puzzle throws an exception when the number is locked.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        user_data = service_manager.get_data_for_user(username)
        user_data.sudoku_puzzle = SudokuPuzzle()
        user_data.sudoku_puzzle.set_number_locked_at(0, 0, True)
        response = sudoku_handler.update_sudoku_puzzle(service_manager, authentication_manager, authentication_token, [[1] * 9] * 9)

        self.assertEqual(response["success_code"], 62, "Check if success_code is correct")
        self.assertEqual(response["error_message"], "Can't change locked number (0, 0)", "Check if error_message is correct")

    def test_invalid_authentication_token(self):
        """
        Tests if update_sudoku_puzzle returns the correct success code when the authentication token doesn't exist.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
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

        authentication_handler.register_user(service_manager, username, password, email)
        response = sudoku_handler.update_sudoku_puzzle(service_manager, authentication_manager, "authentication_token", numbers)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 14, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid authentication token", "Check if error_message is correct")
    
    def test_too_many_rows(self):
        """
        Tests if the correct response is sent if there are too many rows.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        response = sudoku_handler.update_sudoku_puzzle(service_manager, authentication_manager, authentication_token, [[1] * 9] * 10)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 64, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid puzzle size", "Check if error_message is correct")
        
    def test_too_few_rows(self):
        """
        Tests if the correct response is sent if there are too many rows.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        response = sudoku_handler.update_sudoku_puzzle(service_manager, authentication_manager, authentication_token, [[1] * 9] * 8)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 64, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid puzzle size", "Check if error_message is correct")
    
    def test_too_many_columns(self):
        """
        Tests if the correct response is sent if there are too many columns.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        response = sudoku_handler.update_sudoku_puzzle(service_manager, authentication_manager, authentication_token, [[1] * 8] * 9)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 64, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid puzzle size", "Check if error_message is correct")
    
    def test_too_few_columns(self):
        """
        Tests if the correct response is sent if there are too few columns.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        response = sudoku_handler.update_sudoku_puzzle(service_manager, authentication_manager, authentication_token, [[1] * 8] * 9)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 64, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid puzzle size", "Check if error_message is correct")

    def test_token_is_not_string(self):
        """
        Tests if update_sudoku_puzzle throws an exception when the authentication token is not a string.
        """
        self.assertRaises(
            TypeError, 
            sudoku_handler.generate_sudoku_puzzle, 
            (ServiceManager(), AuthenticationManager(), 0, [[0] * 9] * 9), 
            "Check if exception is raised"
        )

    def test_numbers_is_not_list(self):
        """
        Tests if update_sudoku_puzzle throws an exception when the authentication token is not a string.
        """
        self.assertRaises(
            TypeError, 
            sudoku_handler.generate_sudoku_puzzle, 
            (ServiceManager(), AuthenticationManager(), "token", 0), 
            "Check if exception is raised"
        )

    def test_user_data_is_missing(self):
        """
        Tests if update_sudoku_puzzle returns the correct success code when the user data doesn't exist.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
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

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        service_manager._user_information.clear()
        response = sudoku_handler.update_sudoku_puzzle(service_manager, authentication_manager, authentication_token, numbers)

        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 14, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid authentication token", "Check if error_message is correct")

    def test_service_manager_is_not_service_manager(self):
        """
        Tests if update_sudoku_puzzle returns the correct success code when the service manager is None.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        numbers = [[0] * 9] * 9

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]

        with self.assertRaises(TypeError):
            sudoku_handler.update_sudoku_puzzle(0, authentication_manager, authentication_token, numbers)
    
    def test_service_manager_is_none(self):
        """
        Tests if update_sudoku_puzzle returns the correct success code when the service manager is None.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        numbers = [[0] * 9] * 9

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]

        with self.assertRaises(TypeError):
            sudoku_handler.update_sudoku_puzzle(None, authentication_manager, authentication_token, numbers)
    
    def test_authentication_manager_is_not_authentication_manager(self):
        """
        Tests if update_sudoku_puzzle returns the correct success code when the authentication manager is not an instance
        of AuthenticationManager.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        numbers = [[0] * 9] * 9

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]

        with self.assertRaises(TypeError):
            sudoku_handler.update_sudoku_puzzle(service_manager, 0, authentication_token, numbers)
    
    def test_authentication_manager_is_none(self):
        """
        Tests if update_sudoku_puzzle returns the correct success code when the authentication manager is None.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        numbers = [[0] * 9] * 9

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]

        with self.assertRaises(TypeError):
            sudoku_handler.update_sudoku_puzzle(service_manager, None, authentication_token, numbers)
