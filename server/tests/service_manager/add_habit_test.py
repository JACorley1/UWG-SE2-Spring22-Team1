import unittest
from unittest import result
from server.service_manager import ServiceManager
from server.user_data import UserData

class TestAddHabit(unittest.TestCase):    
    """
    Tests for the add_habit method.

    @author Team 1
    @version Spring 2022
    """
    def test_valid_information(self):
        """
        Checks if a valid habit is added.
        """
        service_manager = ServiceManager()
        username = "username"
        password = "password"
        email = "email@email.com"
        habit_name = "Habit"
        habit_freq = 0

        service_manager.create_user(username, password, email)
        user_data = service_manager.get_data_for_user(username)
        result = service_manager.add_habit(username, habit_name, habit_freq)

        self.assertEqual(result, 0, "Checks if the success code is correct")
        self.assertEqual(len(user_data.habits), 1, "Check if habit was added")
    
    def test_username_not_added(self):
        """
        Checks if the correct success code is returned when the username doesn't exist.
        """
        service_manager = ServiceManager()

        result = service_manager.add_habit("username", "Habit", 0)

        self.assertEqual(result, 14, "Checks if success code is correct")

    def test_invalid_habit_name(self):
        """
        Checks if the correct success code is returned when the username doesn't exist.
        """
        service_manager = ServiceManager()

        service_manager.create_user("username", "password", "email@email.com")
        result = service_manager.add_habit("username", "", 0)

        self.assertEqual(result, 50, "Checks if success code is correct")
    
    def test_invalid_habit_frequency(self):
        """
        Checks if the correct success code is returned when the username doesn't exist.
        """
        service_manager = ServiceManager()

        service_manager.create_user("username", "password", "email@email.com")
        result = service_manager.add_habit("username", "Habit", -1)

        self.assertEqual(result, 51, "Checks if success code is correct")
