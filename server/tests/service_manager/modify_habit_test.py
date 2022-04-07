import unittest
from backend.service_manager import ServiceManager
from backend.user_data import UserData

class TestModifyHabit(unittest.TestCase):    
    """
    Tests for the modify_habit method.

    @author Team 1
    @version Spring 2022
    """
    def test_modify_existing_habit(self):
        """
        Checks if a valid habit is removed.
        """
        service_manager = ServiceManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0
        new_habit_name = "Habit1"
        new_habit_freq = 1

        service_manager.create_user(username, password, email)
        user_data = service_manager.get_data_for_user(username)
        service_manager.add_habit(username, habit_name, habit_freq)
        result = service_manager.modify_habit(username, 0, new_habit_name, new_habit_freq)
        habit = user_data.habits[0]

        self.assertEqual(result, 0, "Checks if the success code is correct")
        self.assertEqual(habit.name, new_habit_name, "Check if habit's name was updated")
        self.assertEqual(habit.frequency, new_habit_freq, "Check if habit's frequency was updated")
    
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
        new_habit_name = "Habit1"
        new_habit_freq = 1

        service_manager.create_user(username, password, email)
        service_manager.add_habit(username, habit_name, habit_freq)
        result = service_manager.modify_habit("user", 0, new_habit_name, new_habit_freq)

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
        new_habit_name = "Habit1"
        new_habit_freq = 1

        service_manager.create_user(username, password, email)
        service_manager.add_habit(username, habit_name, habit_freq)
        result = service_manager.modify_habit(username, -1, new_habit_name, new_habit_freq)

        self.assertEqual(result, 52, "Checks if success code is correct")

    def test_invalid_name(self):
        """
        Checks if the correct success code is returned.
        """
        service_manager = ServiceManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0
        new_habit_name = ""
        new_habit_freq = 1

        service_manager.create_user(username, password, email)
        service_manager.add_habit(username, habit_name, habit_freq)
        result = service_manager.modify_habit(username, -1, new_habit_name, new_habit_freq)

        self.assertEqual(result, 50, "Checks if success code is correct")

    def test_invalid_frequency(self):
        """
        Checks if the correct success code is returned.
        """
        service_manager = ServiceManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0
        new_habit_name = "Habit1"
        new_habit_freq = -1

        service_manager.create_user(username, password, email)
        service_manager.add_habit(username, habit_name, habit_freq)
        result = service_manager.modify_habit(username, -1, new_habit_name, new_habit_freq)

        self.assertEqual(result, 51, "Checks if success code is correct")
