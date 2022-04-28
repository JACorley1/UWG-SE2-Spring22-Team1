import unittest
from backend.service_manager import ServiceManager
from backend.user_data import UserData

class TestRemoveHabit(unittest.TestCase):    
    """
    Tests for the remove_habit method.

    @author Team 1
    @version Spring 2022
    """
    def test_remove_single_habit(self):
        """
        Checks if a valid habit is removed.
        """
        service_manager = ServiceManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        service_manager.create_user(username, password, email)
        user_data = service_manager.get_data_for_user(username)
        service_manager.add_habit(username, habit_name, habit_freq)
        result = service_manager.remove_habit(username, 0)

        self.assertEqual(result, 0, "Checks if the success code is correct")
        self.assertEqual(len(user_data.habits), 0, "Check if habit was added")
    
    def test_remove_many_habits(self):
        """
        Checks if a valid habit is removed.
        """
        service_manager = ServiceManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        service_manager.create_user(username, password, email)
        user_data = service_manager.get_data_for_user(username)
        service_manager.add_habit(username, habit_name, habit_freq)
        service_manager.add_habit(username, habit_name, habit_freq)
        result1 = service_manager.remove_habit(username, 0)
        result2 = service_manager.remove_habit(username, 1)

        self.assertEqual(result1, 0, "Checks if the success code is correct")
        self.assertEqual(result2, 0, "Checks if the success code is correct")
        self.assertEqual(len(user_data.habits), 0, "Check if habit was added")
    
    def test_username_not_added(self):
        """
        Checks if the correct success code is returned.
        """
        service_manager = ServiceManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        service_manager.create_user(username, password, email)
        service_manager.add_habit(username, habit_name, habit_freq)
        result = service_manager.remove_habit("user", 0)

        self.assertEqual(result, 14, "Checks if success code is correct")

    def test_invalid_id(self):
        """
        Checks if the correct success code is returned.
        """
        service_manager = ServiceManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        service_manager.create_user(username, password, email)
        service_manager.add_habit(username, habit_name, habit_freq)
        result = service_manager.remove_habit(username, -1)

        self.assertEqual(result, 52, "Checks if success code is correct")

