import unittest

from backend.user_data import UserData

class TestRemoveHabit(unittest.TestCase):    
    """
    Tests for getting a habit from the user's list of habits.

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
        habit = user_data.get_habit(0)

        self.assertEqual(habit.name, habit_name, "Check if the habit has the right name")
        self.assertEqual(habit.frequency, habit_freq, "Check if the habit has the right frequency")

    def test_habit_doesnt_exist(self):
        """
        Checks if the return value is correct when habits doens't exist.
        """
        user_data = UserData("username", "password", "email@email.com")

        self.assertTrue(user_data.get_habit(0) is None, "Check if the return value is correct.")