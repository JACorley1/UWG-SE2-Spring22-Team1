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
        print(result)
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

    def test_valid_complete_habits(self):
        """
        Checks if a valid complete_habits request is handled correctly.
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
        complete_habit_request = {
            "request_type": "complete_habits",
            "habit_ids": [0],
        }

        request_handler.handle_request(register_request)
        add_habit_request["authentication_token"] = request_handler.handle_request(login_request)["authentication_token"]
        complete_habit_request["authentication_token"] = add_habit_request["authentication_token"]
        request_handler.handle_request(add_habit_request)
        response = request_handler.handle_request(complete_habit_request)

        success_code = response["success_code"]
        already_completed = response["already_completed"]
        habit = request_handler._service_manager._user_information[username].habits[0]

        self.assertEqual(success_code, 0, "Check if success_code is correct.")
        self.assertEqual(already_completed, [], "Check if no habits were already completed")
        self.assertTrue(habit.is_complete)

    def test_valid_generate_sudoku_puzzle(self):
        """
        Checks if a valid generate_sudoku_puzzle request is handled correctly.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"

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
        generate_sudoku_puzzle_request = {
            "request_type": "generate_sudoku_puzzle",
        }

        request_handler.handle_request(register_request)
        generate_sudoku_puzzle_request["authentication_token"] = request_handler.handle_request(login_request)["authentication_token"]
        response = request_handler.handle_request(generate_sudoku_puzzle_request)

        success_code = response["success_code"]
        numbers = response["sudoku_puzzle"]["numbers"]
        number_locks = response["sudoku_puzzle"]["number_locks"]

        self.assertEqual(success_code, 0, "Check if success_code is correct.")
        self.assertEqual(len(numbers), 9, "Check if puzzle is 9 rows long.")
        for row in numbers:
            self.assertEqual(len(row), 9, "Check if puzzle is 9 columns long.")
        self.assertEqual(len(number_locks), 9, "Check if puzzle is 9 rows long.")
        for row in number_locks:
            self.assertEqual(len(row), 9, "Check if puzzle is 9 columns long.")

    def test_valid_update_sudoku_puzzle(self):
        """
        Checks if a valid update_sudoku_puzzle request is handled correctly.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"

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
        generate_sudoku_puzzle_request = {
            "request_type": "generate_sudoku_puzzle",
        }
        update_sudoku_puzzle_request = {
            "request_type": "update_sudoku_puzzle",
        }

        request_handler.handle_request(register_request)
        generate_sudoku_puzzle_request["authentication_token"] = request_handler.handle_request(login_request)["authentication_token"]
        response = request_handler.handle_request(generate_sudoku_puzzle_request)

        numbers = response["sudoku_puzzle"]["numbers"]
        for row, col in [(row, col) for row in range(9) for col in range(9)]:
            if numbers[row][col] == 0:
                numbers[row][col] = 1
                break
        
        update_sudoku_puzzle_request["authentication_token"] = generate_sudoku_puzzle_request["authentication_token"]
        update_sudoku_puzzle_request["numbers"] = numbers

        response = request_handler.handle_request(update_sudoku_puzzle_request)
        success_code = response["success_code"]

        self.assertEqual(success_code, 0, "Check if success_code is correct.")

    def test_valid_buy_hint(self):
        """
        Checks if a valid buy_hint request is handled correctly.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"

        register_request = {
            "request_type": "register_user",
            "username": username,
            "password": password,
            "email": email,
        }
        retrieve_data_request = {
            "request_type": "retrieve_data",
            "fields": ["sudoku_puzzle"]
        }
        login_request = {
            "request_type": "login",
            "username": username,
            "password": password,
        }
        generate_sudoku_puzzle_request = {
            "request_type": "generate_sudoku_puzzle",
        }
        buy_hint_request = {
            "request_type": "buy_hint",
        }

        request_handler.handle_request(register_request)
        generate_sudoku_puzzle_request["authentication_token"] = request_handler.handle_request(login_request)["authentication_token"]
        request_handler._service_manager.get_data_for_user(username).coins = 20
        response = request_handler.handle_request(generate_sudoku_puzzle_request)

        buy_hint_request["authentication_token"] = generate_sudoku_puzzle_request["authentication_token"]
        retrieve_data_request["authentication_token"] = buy_hint_request["authentication_token"]
        response = request_handler.handle_request(buy_hint_request)
        data_response = request_handler.handle_request(retrieve_data_request)

        success_code = response["success_code"]
        number = response["number"]
        row = response["row"]
        col = response["col"]
        numbers = data_response["sudoku_puzzle"]["numbers"]
        number_locks = data_response["sudoku_puzzle"]["number_locks"]

        self.assertEqual(success_code, 0, "Check if success_code is correct.")
        self.assertEqual(number, numbers[row][col], "Check if number is correct.")
        self.assertTrue(number_locks[row][col], "Check if number_lock is correct.")

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

    def test_missing_fields(self):
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

    def test_complete_habits_missing_fields(self):
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
        complete_habits_request = {
            "request_type": "complete_habits",
        }

        request_handler.handle_request(register_request)
        add_habit_request["authentication_token"] = request_handler.handle_request(login_request)["authentication_token"]
        complete_habits_request["authentication_token"] = add_habit_request["authentication_token"]
        request_handler.handle_request(add_habit_request)
        response = request_handler.handle_request(complete_habits_request)

        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 12, "Check if success_code is correct.")
        self.assertEqual(
            error_message, 
            f"Malformed Request, missing Request Fields (habit_ids)", 
            "Check if error_message is correct."
        )

    def test_generate_sudoku_puzzle_missing_fields(self):
        """
        Checks if a the correct response is created when missing fields.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())

        response = request_handler.handle_request({"request_type": "generate_sudoku_puzzle"})
        success_code = response["success_code"]
        error_message = response["error_message"]
        
        self.assertEqual(success_code, 12, "Check if success_code is correct.")
        self.assertEqual(
            error_message, 
            f"Malformed Request, missing Request Fields (authentication_token)", 
            "Check if error_message is correct."
        )

    def test_update_sudoku_puzzle_missing_fields(self):
        """
        Checks if a the correct response is created when missing fields.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())

        response = request_handler.handle_request({"request_type": "update_sudoku_puzzle"})
        success_code = response["success_code"]
        error_message = response["error_message"]
        
        self.assertEqual(success_code, 12, "Check if success_code is correct.")
        self.assertEqual(
            error_message, 
            f"Malformed Request, missing Request Fields (authentication_token, numbers)", 
            "Check if error_message is correct."
        )

    def test_buy_hint_missing_fields(self):
        """
        Checks if a the correct response is created when missing fields.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())

        response = request_handler.handle_request({"request_type": "buy_hint"})
        success_code = response["success_code"]
        error_message = response["error_message"]
        
        self.assertEqual(success_code, 12, "Check if success_code is correct.")
        self.assertEqual(
            error_message, 
            f"Malformed Request, missing Request Fields (authentication_token)", 
            "Check if error_message is correct."
        )