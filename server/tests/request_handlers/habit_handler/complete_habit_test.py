import unittest
from backend.authentication_manager import AuthenticationManager
from backend.service_manager import ServiceManager
import backend.request_handler.habit_handler as habit_handler
import backend.request_handler.authentication_handler as authentication_handler

class TestCompleteHabit(unittest.TestCase):
    """
    Tests for the _complete_habit method.

    @author Team 1
    @version Spring 2022
    """

    def test_single_valid_id(self):
        """
        Tests if habit_handler correctly completes a single habit.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        habit_handler.add_habit(service_manager, authentication_manager, authentication_token, habit_name, habit_freq)

        response = habit_handler.complete_habits(service_manager, authentication_manager, authentication_token, [0])
        success_code = response["success_code"]
        already_complete = response["already_completed"]
        coins = response["coins"]

        self.assertEqual(success_code, 0, "Check if success_code is correct")
        self.assertEqual(already_complete, [], "Check if an empty list is created")
        self.assertEqual(coins, 70, "Check if coins is correct")
        self.assertTrue(service_manager._user_information[username].habits[0].is_complete, "Check if habit is completed")
    
    def test_many_valid_ids(self):
        """
        Tests if habit_handler correctly completes multiple habits.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        habit_handler.add_habit(service_manager, authentication_manager, authentication_token, habit_name, habit_freq)
        habit_handler.add_habit(service_manager, authentication_manager, authentication_token, habit_name, habit_freq)
        habit_handler.add_habit(service_manager, authentication_manager, authentication_token, habit_name, habit_freq)

        response = habit_handler.complete_habits(service_manager, authentication_manager, authentication_token, [0, 1, 2])

        self.assertEqual(response["success_code"], 0, "Check if success_code is correct")
        self.assertEqual(response["already_completed"], [], "Check if an empty list is created")
        self.assertEqual(response["coins"], 110, "Check if coins is correct")
        self.assertTrue(
            service_manager._user_information[username].habits[0].is_complete, 
            "Check if the first habit is completed"
        )
        self.assertTrue(
            service_manager._user_information[username].habits[1].is_complete, 
            "Check if the second habit is completed"
        )
        self.assertTrue(
            service_manager._user_information[username].habits[2].is_complete, 
            "Check if the third habit is completed"
        )

    def test_single_valid_id_already_completed(self):
        """
        Tests if habit_handler correctly lists that the habit was already completed.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        habit_handler.add_habit(service_manager, authentication_manager, authentication_token, habit_name, habit_freq)

        habit_handler.complete_habits(service_manager, authentication_manager, authentication_token, [0])
        response = habit_handler.complete_habits(service_manager, authentication_manager, authentication_token, [0])

        self.assertEqual(response["success_code"], 0, "Check if success_code is correct")
        self.assertEqual(response["already_completed"], [0], "Check if an empty list is created")
        self.assertTrue(service_manager._user_information[username].habits[0].is_complete, "Check if habit is completed")

    def test_many_valid_ids_some_completed(self):
        """
        Tests if habit_handler correctly completes many habits and lists any habits that were
        already complete.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        habit_handler.add_habit(service_manager, authentication_manager, authentication_token, habit_name, habit_freq)
        habit_handler.add_habit(service_manager, authentication_manager, authentication_token, habit_name, habit_freq)
        habit_handler.add_habit(service_manager, authentication_manager, authentication_token, habit_name, habit_freq)

        habit_handler.complete_habits(service_manager, authentication_manager, authentication_token, [1, 2])
        response = habit_handler.complete_habits(service_manager, authentication_manager, authentication_token, [0, 1, 2])

        self.assertEqual(response["success_code"], 0, "Check if success_code is correct")
        self.assertEqual(response["already_completed"], [1, 2], "Check if an empty list is created")
        self.assertTrue(
            service_manager._user_information[username].habits[0].is_complete, 
            "Check if the first habit is completed"
        )
        self.assertTrue(
            service_manager._user_information[username].habits[1].is_complete, 
            "Check if the second habit is completed"
        )
        self.assertTrue(
            service_manager._user_information[username].habits[2].is_complete, 
            "Check if the third habit is completed"
        )
    
    def test_habit_doesnt_exist(self):
        """
        Tests if habit_handler correctly returns that the habit doesn't exist.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        habit_handler.add_habit(service_manager, authentication_manager, authentication_token, habit_name, habit_freq)

        response = habit_handler.complete_habits(service_manager, authentication_manager, authentication_token, [1])
        success_code = response["success_code"]
        error_message = response["error_message"]
        
        self.assertEqual(success_code, 52, "Check if success_code is correct")
        self.assertEqual(error_message, "No habit with id (1)", "Check if error_message is correct")

    def test_many_habits_dont_exist(self):
        """
        Tests if habit_handler correctly returns that the habit doesn't exist.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        authentication_handler.register_user(service_manager, username, password, email)
        authentication_token = authentication_handler.login(service_manager, authentication_manager, username, password)["authentication_token"]
        habit_handler.add_habit(service_manager, authentication_manager, authentication_token, habit_name, habit_freq)

        response = habit_handler.complete_habits(service_manager, authentication_manager, authentication_token, [1, 2, 3])
        success_code = response["success_code"]
        error_message = response["error_message"]
        
        self.assertEqual(success_code, 52, "Check if success_code is correct")
        self.assertEqual(error_message, "No habit with id (1, 2, 3)", "Check if error_message is correct")

    def test_invalid_authentication_token(self):
        """
        Tests if habit_handler returns the correct success code when the username doesn't exist.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()
        username = "username"
        password = "password"
        email = "email@email.com"

        authentication_handler.register_user(service_manager, username, password, email)
        response = habit_handler.complete_habits(service_manager, authentication_manager, "invalid_authentication_token", [0])
        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 14, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid authentication token", "Check if error_message is correct")

    def test_user_data_is_missing(self):
        """
        Tests if habit_handler returns the correct success code when the user data doesn't exist.
        """
        service_manager = ServiceManager()
        authentication_manager = AuthenticationManager()

        response = habit_handler.complete_habits(service_manager, authentication_manager, "invalid_authentication_token", [0])

        success_code = response["success_code"]
        error_message = response["error_message"]

        self.assertEqual(success_code, 14, "Check if success_code is correct")
        self.assertEqual(error_message, "Invalid authentication token", "Check if error_message is correct")

    def test_service_manager_is_not_service_manager(self):
        """
        Tests if habit_handler returns the correct success code when the service_manager is not a ServiceManager.
        """
        with self.assertRaises(TypeError):
            habit_handler.complete_habits(1, AuthenticationManager(), "token", [0])
    
    def test_none_service_manager(self):
        """
        Tests if habit_handler returns the correct success code when the service_manager is None.
        """
        with self.assertRaises(TypeError):
            habit_handler.complete_habits(None, AuthenticationManager(), "token", [0])
    
    def test_authentication_manager_is_not_authentication_manager(self):
        """
        Tests if habit_handler returns the correct success code when the authentication_manager is not a AuthenticationManager.
        """
        with self.assertRaises(TypeError):
            habit_handler.complete_habits(ServiceManager(), 1, "token", [0])
    
    def test_none_authentication_manager(self):
        """
        Tests if habit_handler returns the correct success code when the authentication_manager is None.
        """
        with self.assertRaises(TypeError):
            habit_handler.complete_habits(ServiceManager(), None, "token", [0])
    
    def test_token_is_not_string(self):
        """
        Tests if habit_handler returns the correct success code when the token is not a string.
        """
        with self.assertRaises(TypeError):
            habit_handler.complete_habits(ServiceManager(), AuthenticationManager(), 1, [0])
    
    def test_token_is_none(self):
        """
        Tests if habit_handler returns the correct success code when the token is None.
        """
        with self.assertRaises(TypeError):
            habit_handler.complete_habits(ServiceManager(), AuthenticationManager(), None, [0])
    
    def test_habit_ids_is_not_list(self):
        """
        Tests if habit_handler returns the correct success code when the habit_ids is not a list.
        """
        with self.assertRaises(TypeError):
            habit_handler.complete_habits(ServiceManager(), AuthenticationManager(), "token", 1)

    def test_habit_ids_is_none(self):
        """
        Tests if habit_handler returns the correct success code when the habit_ids is None.
        """
        with self.assertRaises(TypeError):
            habit_handler.complete_habits(ServiceManager(), AuthenticationManager(), "token", None)