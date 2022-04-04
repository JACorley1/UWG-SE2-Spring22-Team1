import unittest

from backend.user_data import UserData

class TestContainsHabitId(unittest.TestCase):    
    """
    Tests for the contains_habit_id method.

    @author Team 1
    @version Spring 2022
    """

    def test_habit_exists(self):
        """
        Checks if a habit is retrieved correctly.
        """
        user_data = UserData("username", "password", "email@email.com")
        habit_name = "Habit"
        habit_freq = 0

        user_data.add_habit(habit_name, habit_freq)
        
        self.assertTrue(user_data.contains_habit_id(0), "Check if the habit was found")

    def test_habit_doesnt_exist(self):
        """
        Checks if the return value is correct when habits doesn't exist.
        """
        user_data = UserData("username", "password", "email@email.com")

        self.assertFalse(user_data.contains_habit_id(0), "Check if the habit was not found")