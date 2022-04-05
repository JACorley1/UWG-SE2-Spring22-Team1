import unittest
from urllib import response
from backend.authentication_manager import AuthenticationManager

from backend.server import _RequestHandler
from backend.service_manager import ServiceManager

class TestCompleteHabit(unittest.TestCase):
    """
    Tests for the _complete_habit method.

    @author Team 1
    @version Spring 2022
    """

    def test_single_valid_id(self):
        """
        Tests if _RequestHandler correctly completes a single habit.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        request_handler._add_habit(authentication_token, habit_name, habit_freq)

        response = request_handler._complete_habits(authentication_token, [0])
        success_code = response["success_code"]
        already_complete = response["already_completed"]
        coins = response["coins"]

        self.assertEqual(success_code, 0, "Check if success_code is correct")
        self.assertEqual(already_complete, [], "Check if an empty list is created")
        self.assertEqual(coins, 70, "Check if coins is correct")
        self.assertTrue(request_handler._service_manager._user_information[username].habits[0].is_complete, "Check if habit is completed")
    
    def test_many_valid_ids(self):
        """
        Tests if _RequestHandler correctly completes multiple habits.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        request_handler._add_habit(authentication_token, habit_name, habit_freq)
        request_handler._add_habit(authentication_token, habit_name, habit_freq)
        request_handler._add_habit(authentication_token, habit_name, habit_freq)

        response = request_handler._complete_habits(authentication_token, [0, 1, 2])

        self.assertEqual(response["success_code"], 0, "Check if success_code is correct")
        self.assertEqual(response["already_completed"], [], "Check if an empty list is created")
        self.assertEqual(response["coins"], 110, "Check if coins is correct")
        self.assertTrue(
            request_handler._service_manager._user_information[username].habits[0].is_complete, 
            "Check if the first habit is completed"
        )
        self.assertTrue(
            request_handler._service_manager._user_information[username].habits[1].is_complete, 
            "Check if the second habit is completed"
        )
        self.assertTrue(
            request_handler._service_manager._user_information[username].habits[2].is_complete, 
            "Check if the third habit is completed"
        )

    def test_single_valid_id_already_completed(self):
        """
        Tests if _RequestHandler correctly lists that the habit was already completed.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        request_handler._add_habit(authentication_token, habit_name, habit_freq)

        request_handler._complete_habits(authentication_token, [0])
        response = request_handler._complete_habits(authentication_token, [0])

        self.assertEqual(response["success_code"], 0, "Check if success_code is correct")
        self.assertEqual(response["already_completed"], [0], "Check if an empty list is created")
        self.assertTrue(request_handler._service_manager._user_information[username].habits[0].is_complete, "Check if habit is completed")

    def test_many_valid_ids_some_completed(self):
        """
        Tests if _RequestHandler correctly completes many habits and lists any habits that were
        already complete.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        request_handler._add_habit(authentication_token, habit_name, habit_freq)
        request_handler._add_habit(authentication_token, habit_name, habit_freq)
        request_handler._add_habit(authentication_token, habit_name, habit_freq)

        request_handler._complete_habits(authentication_token, [1, 2])
        response = request_handler._complete_habits(authentication_token, [0, 1, 2])

        self.assertEqual(response["success_code"], 0, "Check if success_code is correct")
        self.assertEqual(response["already_completed"], [1, 2], "Check if an empty list is created")
        self.assertTrue(
            request_handler._service_manager._user_information[username].habits[0].is_complete, 
            "Check if the first habit is completed"
        )
        self.assertTrue(
            request_handler._service_manager._user_information[username].habits[1].is_complete, 
            "Check if the second habit is completed"
        )
        self.assertTrue(
            request_handler._service_manager._user_information[username].habits[2].is_complete, 
            "Check if the third habit is completed"
        )
    
    def test_habit_doesnt_exist(self):
        """
        Tests if _RequestHandler correctly returns that the habit doesn't exist.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        request_handler._add_habit(authentication_token, habit_name, habit_freq)

        response = request_handler._complete_habits(authentication_token, [1])
        success_code = response["success_code"]
        error_message = response["error_message"]
        
        self.assertEqual(success_code, 52, "Check if success_code is correct")
        self.assertEqual(error_message, "No habit with id (1)", "Check if error_message is correct")

    def test_many_habits_dont_exist(self):
        """
        Tests if _RequestHandler correctly returns that the habit doesn't exist.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        request_handler._register_user(username, password, email)
        authentication_token = request_handler._login(username, password)["authentication_token"]
        request_handler._add_habit(authentication_token, habit_name, habit_freq)

        response = request_handler._complete_habits(authentication_token, [1, 2, 3])
        success_code = response["success_code"]
        error_message = response["error_message"]
        
        self.assertEqual(success_code, 52, "Check if success_code is correct")
        self.assertEqual(error_message, "No habit with id (1, 2, 3)", "Check if error_message is correct")

    def test_invalid_authentication_token(self):
        """
        Tests if _RequestHandler returns the correct success code when the username doesn't exist.
        """
        request_handler = _RequestHandler(ServiceManager(), AuthenticationManager())
        username = "username"
        password = "password"
        email = "email@email.com"

        request_handler._register_user(username, password, email)
        response = request_handler._complete_habits("authentication_token", [0])
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

        response = request_handler._complete_habits("authentication_token", [0])

        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 14, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid authentication token", "Check if error_message is correct")
