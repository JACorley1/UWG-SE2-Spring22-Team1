import unittest
from backend.authentication_manager import AuthenticationManager
from backend.server import _RequestHandler
from backend.service_manager import ServiceManager
import backend.request_handler.sudoku_handler as sudoku_handler
import backend.request_handler.authentication_handler as authentication_handler

class TestGenerateSudokuPuzzle(unittest.TestCase):
    """
    Tests for the generate_sudoku_puzzle method.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_request(self):
        """
        Tests if sudoku_handler correctly generates a new sudoku puzzle.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        response = sudoku_handler.generate_sudoku_puzzle(service_manager, authentication_manager, authentication_token)
        userdata = service_manager.get_data_for_user(username)
        puzzle = userdata.sudoku_puzzle
        
        self.assertEqual(response["success_code"], 0, "Check if success_code is correct")
        self.assertEqual(response["sudoku_puzzle"]["numbers"], puzzle.numbers, "Check if sudoku_puzzle numbers is correct.")
        self.assertEqual(response["sudoku_puzzle"]["number_locks"], puzzle.number_locks, "Check if sudoku_puzzle numbers is correct.")

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
        response = sudoku_handler.generate_sudoku_puzzle(service_manager, authentication_manager, "invalid_token")
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 14, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid authentication token", "Check if error_message is correct")

    def test_token_is_not_string(self):
        """
        Tests if sudoku_handler throws an exception when the authentication token is not a string.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        self.assertRaises(TypeError, sudoku_handler.generate_sudoku_puzzle, (service_manager, authentication_manager, 0), "Check if exception is raised")

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
        response = sudoku_handler.generate_sudoku_puzzle(service_manager, authentication_manager, authentication_token)

        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 14, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid authentication token", "Check if error_message is correct")

    def test_service_manager_is_none(self):
        """
        Tests if sudoku_handler throws an exception when the service manager is None.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]

        with self.assertRaises(TypeError):
            sudoku_handler.generate_sudoku_puzzle(None, authentication_manager, authentication_token)

    def test_service_manager_is_not_service_manager(self):
        """
        Tests if sudoku_handler throws an exception when the service manager is not a service manager.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]

        with self.assertRaises(TypeError):
            sudoku_handler.generate_sudoku_puzzle(0, authentication_manager, authentication_token)

    def test_authentication_manager_is_none(self):
        """
        Tests if sudoku_handler throws an exception when the authentication manager is None.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]

        with self.assertRaises(TypeError):
            sudoku_handler.generate_sudoku_puzzle(service_manager, None, authentication_token)

    def test_service_manager_is_not_service_manager(self):
        """
        Tests if sudoku_handler throws an exception when the service manager is not a service manager.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]

        with self.assertRaises(TypeError):
            sudoku_handler.generate_sudoku_puzzle(0, authentication_manager, authentication_token)