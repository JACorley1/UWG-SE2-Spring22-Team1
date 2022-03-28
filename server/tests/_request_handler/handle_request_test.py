import unittest
from backend.authentication_manager import AuthenticationManager
from backend.server import _RequestHandler
from backend.service_manager import ServiceManager

class TestHandleRequest(unittest.TestCase):    
    """
    Tests for the handle_request method.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_register_user(self):
        """
        Checks if a valid register_user request is handled correctly.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        request = {
            "request_type": "register_user",
            "username": "username",
            "password": "password",
            "email": "email@email.com"
        }

        result = request_handler.handle_request(request)
        self.assertEqual(result["success_code"], 0, "Check if success_code is correct.")

    def test_valid_login(self):
        """
        Checks if a valid login request is handled correctly.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"

        register_request = {
            "request_type": "register_user",
            "username": username,
            "password": password,
            "email": "email@email.com"
        }
        login_request = {
            "request_type": "login",
            "username": username,
            "password": password
        }

        request_handler.handle_request(register_request)
        response = request_handler.handle_request(login_request)
        success_code = response["success_code"]
        authentication_token = response["authentication_token"]

        self.assertEqual(success_code, 0, "Check if success_code is correct.")
        self.assertEqual(
            authentication_token,
            request_handler._authentication_manager.get_token_for_username(username),
            "Check if the token is correct"
        )

    def test_valid_retrieve_data(self):
        """
        Checks if a valid login request is handled correctly.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"

        register_request = {
            "request_type": "register_user",
            "username": username,
            "password": password,
            "email": email
        }
        login_request = {
            "request_type": "login",
            "username": username,
            "password": password
        }
        data_request = {
            "request_type": "retrieve_data",
            "fields": ["username", "email", "coins", "sudoku_puzzle", "habits"]
        }

        request_handler.handle_request(register_request)
        data_request["authentication_token"] = request_handler.handle_request(login_request)["authentication_token"]
        response = request_handler.handle_request(data_request)

        success_code = response["success_code"]
        coins = response["coins"]
        sudoku_puzzle = response["sudoku_puzzle"]
        habits = response["habits"]

        self.assertEqual(success_code, 0, "Check if success_code is correct.")
        self.assertEqual(response["username"], username, "Check if the username is correct")
        self.assertEqual(response["email"], email, "Check if the email is correct")
        self.assertEqual(coins, 0, "Check if the coins are correct")
        self.assertEqual(sudoku_puzzle, None, "Check if the sudoku_puzzle is correct")
        self.assertEqual(habits, [], "Check if the habits are correct")

    def test_valid_add_habit(self):
        """
        Checks if a valid add_habit request is handled correctly.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        register_request = {
            "request_type": "register_user",
            "username": username,
            "password": password,
            "email": email,
        }
        login_request = {
            "request_type": "login",
            "username": username,
            "password": password,
        }
        add_habit_request = {
            "request_type": "add_habit",
            "habit_name": habit_name,
            "habit_frequency": habit_freq,
        }

        request_handler.handle_request(register_request)
        add_habit_request["authentication_token"] = request_handler.handle_request(login_request)["authentication_token"]
        response = request_handler.handle_request(add_habit_request)

        success_code = response["success_code"]
        habit = request_handler._service_manager._user_information[username].habits[0]

        self.assertEqual(success_code, 0, "Check if success_code is correct.")
        self.assertEqual(habit.name, habit_name, "Check if the habit name is correct")
        self.assertEqual(habit.frequency, habit_freq, "Check if the habit frequency is correct")

    def test_valid_remove_habit(self):
        """
        Checks if a valid remove_habit request is handled correctly.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        register_request = {
            "request_type": "register_user",
            "username": username,
            "password": password,
            "email": email,
        }
        login_request = {
            "request_type": "login",
            "username": username,
            "password": password,
        }
        add_habit_request = {
            "request_type": "add_habit",
            "habit_name": habit_name,
            "habit_frequency": habit_freq,
        }
        remove_habit_request = {
            "request_type": "remove_habit",
            "habit_id": 0,
        }

        request_handler.handle_request(register_request)
        add_habit_request["authentication_token"] = request_handler.handle_request(login_request)["authentication_token"]
        remove_habit_request["authentication_token"] = add_habit_request["authentication_token"]
        request_handler.handle_request(add_habit_request)
        response = request_handler.handle_request(remove_habit_request)

        success_code = response["success_code"]

        self.assertEqual(success_code, 0, "Check if success_code is correct.")
        self.assertEqual(
            len(request_handler._service_manager._user_information[username].habits), 
            0, 
            "Check if no habits exist"
        )

    def test_valid_modify_habit(self):
        """
        Checks if a valid modify_habit request is handled correctly.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0
        new_habit_name = "Habit"
        new_habit_freq = 0

        register_request = {
            "request_type": "register_user",
            "username": username,
            "password": password,
            "email": email,
        }
        login_request = {
            "request_type": "login",
            "username": username,
            "password": password,
        }
        add_habit_request = {
            "request_type": "add_habit",
            "habit_name": habit_name,
            "habit_frequency": habit_freq,
        }
        modify_habit_request = {
            "request_type": "modify_habit",
            "habit_id": 0,
            "habit_name": new_habit_name,
            "habit_frequency": new_habit_freq,
        }

        request_handler.handle_request(register_request)
        add_habit_request["authentication_token"] = request_handler.handle_request(login_request)["authentication_token"]
        modify_habit_request["authentication_token"] = add_habit_request["authentication_token"]
        request_handler.handle_request(add_habit_request)
        response = request_handler.handle_request(modify_habit_request)

        success_code = response["success_code"]
        habit = request_handler._service_manager._user_information[username].habits[0]

        self.assertEqual(success_code, 0, "Check if success_code is correct.")
        self.assertEqual(habit.name, new_habit_name, "Check if the habit name is correct")
        self.assertEqual(habit.frequency, new_habit_freq, "Check if the habit frequency is correct")

    def test_missing_request_type(self):
        """
        Checks if a the correct response is created when not providing a request type.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        request = {
            "username": "username",
            "password": "password",
            "email": "email@email.com"
        }

        result = request_handler.handle_request(request)
        self.assertEqual(result["success_code"], 10, "Check if success_code is correct.")
        self.assertEqual(
            result["error_message"], 
            "Malformed Request, missing Request Type", 
            "Check if error_message is correct."
        )

    def test_none_request(self):
        """
        Checks if an exception is raised when passing None in for the request.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        request = None

        self.assertRaises(
            Exception, 
            request_handler.handle_request, 
            (request), 
            "Check if an exception is raised when None is passed in"
        )

    def test_non_dict_request(self):
        """
        Checks if an exception is raised when passing None in for the request.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        request = 0

        self.assertRaises(
            Exception, 
            request_handler.handle_request, 
            (request), 
            "Check if an exception is raised when a non-dict is passed in"
        )

    def test_unknown_request_type(self):
        """
        Checks if a the correct response is created when giving an invalid request type.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        request = {
            "request_type": "",
            "username": "username",
            "password": "password",
            "email": "email@email.com"
        }

        result = request_handler.handle_request(request)
        self.assertEqual(result["success_code"], 11, "Check if success_code is correct.")
        self.assertEqual(
            result["error_message"], 
            "Unsupported Request Type ()", 
            "Check if error_message is correct."
        )

    def test_missing_request_type(self):
        """
        Checks if a the correct response is created when not providing a request type.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        request = {
            "username": "username",
            "password": "password",
            "email": "email@email.com"
        }

        result = request_handler.handle_request(request)
        self.assertEqual(result["success_code"], 10, "Check if success_code is correct.")
        self.assertEqual(
            result["error_message"], 
            "Malformed Request, missing Request Type", 
            "Check if error_message is correct."
        )

    def test_register_user_missing_fields(self):
        """
        Checks if a the correct response is created when missing fields.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        request = {
            "request_type": "register_user",
            "username": "username",
            "password": "password",
        }

        result = request_handler.handle_request(request)
        self.assertEqual(result["success_code"], 12, "Check if success_code is correct.")
        self.assertEqual(
            result["error_message"], 
            f"Malformed Request, missing Request Fields (email)", 
            "Check if error_message is correct."
        )

    def test_login_missing_fields(self):
        """
        Checks if a the correct response is created when missing fields.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"

        register_request = {
            "request_type": "register_user",
            "username": username,
            "password": password,
            "email": "email@email.com"
        }
        login_request = {
            "request_type": "login",
            "password": password
        }

        request_handler.handle_request(register_request)
        response = request_handler.handle_request(login_request)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 12, "Check if success_code is correct.")
        self.assertEqual(
            error_message, 
            f"Malformed Request, missing Request Fields (username)", 
            "Check if error_message is correct."
        )

    def test_retrieve_data_missing_fields(self):
        """
        Checks if a the correct response is created when missing fields.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"

        register_request = {
            "request_type": "retrieve_data",
            "username": username,
            "password": password,
            "email": "email@email.com"
        }
        login_request = {
            "request_type": "login",
            "password": password
        }

        request_handler.handle_request(register_request)
        response = request_handler.handle_request(login_request)
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 12, "Check if success_code is correct.")
        self.assertEqual(
            error_message, 
            f"Malformed Request, missing Request Fields (username)", 
            "Check if error_message is correct."
        )

    def test_add_habit_missing_fields(self):
        """
        Checks if a the correct response is created when missing fields.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_freq = 0

        register_request = {
            "request_type": "register_user",
            "username": username,
            "password": password,
            "email": email,
        }
        login_request = {
            "request_type": "login",
            "username": username,
            "password": password,
        }
        add_habit_request = {
            "request_type": "add_habit",
            "habit_frequency": habit_freq,
        }

        request_handler.handle_request(register_request)
        add_habit_request["authentication_token"] = request_handler.handle_request(login_request)["authentication_token"]
        response = request_handler.handle_request(add_habit_request)

        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 12, "Check if success_code is correct.")
        self.assertEqual(
            error_message, 
            f"Malformed Request, missing Request Fields (habit_name)", 
            "Check if error_message is correct."
        )

    def test_remove_habit_missing_fields(self):
        """
        Checks if a the correct response is created when missing fields.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        register_request = {
            "request_type": "register_user",
            "username": username,
            "password": password,
            "email": email,
        }
        login_request = {
            "request_type": "login",
            "username": username,
            "password": password,
        }
        add_habit_request = {
            "request_type": "add_habit",
            "habit_name": habit_name,
            "habit_frequency": habit_freq,
        }
        remove_habit_request = {
            "request_type": "remove_habit",
        }

        request_handler.handle_request(register_request)
        add_habit_request["authentication_token"] = request_handler.handle_request(login_request)["authentication_token"]
        remove_habit_request["authentication_token"] = add_habit_request["authentication_token"]
        request_handler.handle_request(add_habit_request)
        response = request_handler.handle_request(remove_habit_request)

        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 12, "Check if success_code is correct.")
        self.assertEqual(
            error_message, 
            f"Malformed Request, missing Request Fields (habit_id)", 
            "Check if error_message is correct."
        )

    def test_modify_habit_missing_fields(self):
        """
        Checks if a the correct response is created when missing fields.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0
        new_habit_name = "Habit"
        new_habit_freq = 0

        register_request = {
            "request_type": "register_user",
            "username": username,
            "password": password,
            "email": email,
        }
        login_request = {
            "request_type": "login",
            "username": username,
            "password": password,
        }
        add_habit_request = {
            "request_type": "add_habit",
            "habit_name": habit_name,
            "habit_frequency": habit_freq,
        }
        modify_habit_request = {
            "request_type": "modify_habit",
            "habit_name": new_habit_name,
            "habit_frequency": new_habit_freq,
        }

        request_handler.handle_request(register_request)
        add_habit_request["authentication_token"] = request_handler.handle_request(login_request)["authentication_token"]
        modify_habit_request["authentication_token"] = add_habit_request["authentication_token"]
        request_handler.handle_request(add_habit_request)
        response = request_handler.handle_request(modify_habit_request)

        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 12, "Check if success_code is correct.")
        self.assertEqual(
            error_message, 
            f"Malformed Request, missing Request Fields (habit_id)", 
            "Check if error_message is correct."
        )
