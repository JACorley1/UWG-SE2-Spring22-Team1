import unittest
from backend.authentication_manager import AuthenticationManager
from backend.service_manager import ServiceManager
from backend.sudoku_puzzle import SudokuPuzzle
import backend.request_handler.sudoku_handler as sudoku_handler
import backend.request_handler.authentication_handler as authentication_handler

class TestBuyHint(unittest.TestCase):
    """
    Tests for the _generate_sudoku_puzzle method.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_request(self):
        """
        Tests if sudoku_handler correctly gets a hint for the current puzzle.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        puzzle = SudokuPuzzle()
        puzzle._solution = [[1] * 9] * 9

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        userdata = service_manager.get_data_for_user(username)
        userdata.coins = 100
        userdata.sudoku_puzzle = puzzle
        response = sudoku_handler.buy_hint(service_manager, authentication_manager, authentication_token)
        
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
        Tests if sudoku_handler returns the correct success code when the user doesn't have enough coins.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        puzzle = SudokuPuzzle()

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        userdata = service_manager.get_data_for_user(username)
        userdata.sudoku_puzzle = puzzle
        response = sudoku_handler.buy_hint(service_manager, authentication_manager, authentication_token)
        
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 70, "Check if success_code is correct")
        self.assertEqual(error_message, "Not enough coins (have 0, need 20)", "Check if error_message is correct")

    def test_no_puzzle_in_progress(self):
        """
        Tests if sudoku_handler returns the correct success code when the user data doesn't exist.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        userdata = service_manager.get_data_for_user(username)
        userdata.coins = 100
        response = sudoku_handler.buy_hint(service_manager, authentication_manager, authentication_token)
        
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 61, "Check if success_code is correct")
        self.assertEqual(error_message, "No puzzle in progress", "Check if error_message is correct")

    def test_all_cells_are_locked(self):
        """
        Tests if sudoku_handler returns the correct success code when all cells are locked.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        puzzle = SudokuPuzzle()
        puzzle._number_locks = [[True] * 9] * 9

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        userdata = service_manager.get_data_for_user(username)
        userdata.coins = 100
        userdata.sudoku_puzzle = puzzle
        response = sudoku_handler.buy_hint(service_manager, authentication_manager, authentication_token)
        
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 63, "Check if success_code is correct")
        self.assertEqual(error_message, "No valid cells for hint", "Check if error_message is correct")

    def test_invalid_authentication_token(self):
        """
        Tests if sudoku_handler returns the correct success code when the authentication token doesn't exist.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"

        authentication_handler.register_user(service_manager, username, password, email)
        response = sudoku_handler.buy_hint(service_manager, authentication_manager, "invalid_authentication_token")
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 14, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid authentication token", "Check if error_message is correct")

    def test_token_is_not_string(self):
        """
        Tests if sudoku_handler throws an exception when the authentication token is not a string.
        """
        self.assertRaises(TypeError, sudoku_handler.buy_hint, (ServiceManager(), AuthenticationManager(), 0), "Check if exception is raised")

    def test_user_data_is_missing(self):
        """
        Tests if sudoku_handler returns the correct success code when the user data doesn't exist.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        service_manager._user_information.clear()
        response = sudoku_handler.buy_hint(service_manager, authentication_manager, authentication_token)

        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 14, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid authentication token", "Check if error_message is correct")

    def test_none_service_manager(self):
        """
        Tests if sudoku_handler throws an exception when the service manager is None.
        """
        self.assertRaises(TypeError, sudoku_handler.buy_hint, None, "Check if exception is raised")

    def test_service_manager_not_service_manager(self):
        """
        Tests if sudoku_handler throws an exception when the service manager is not a service manager.
        """
        self.assertRaises(TypeError, sudoku_handler.buy_hint, "service_manager", AuthenticationManager(), "authentication_token")
    
    def test_authentication_manager_is_none(self):
        """
        Tests if sudoku_handler throws an exception when the authentication manager is None.
        """
        self.assertRaises(TypeError, sudoku_handler.buy_hint, ServiceManager(), None, "authentication_token")

    def test_authentication_manager_not_authentication_manager(self):
        """
        Tests if sudoku_handler throws an exception when the authentication manager is not an authentication manager.
        """
        self.assertRaises(TypeError, sudoku_handler.buy_hint, ServiceManager(), "authentication_manager", "authentication_token")