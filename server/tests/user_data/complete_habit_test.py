import unittest

from backend.user_data import UserData

class TestCompleteHabit(unittest.TestCase):    
    """
    Tests for the complete_habit method.

    @author Team 1
    @version Spring 2022
    """

    def test_incomplete_habit_exists(self):
        """
        Checks if a habit is correctly completed.
        """
        user_data = UserData("username", "password", "email@email.com")
        habit_name = "Habit"
        habit_freq = 0

        user_data.add_habit(habit_name, habit_freq)
        
        self.assertTrue(user_data.complete_habit(0), "Check if the return value is correct.")
        self.assertTrue(user_data.get_habit(0).is_complete, "Check if the habit was completed")
        self.assertEqual(user_data.coins, 70, "Check if the coins were added correctly")

    def test_habit_doesnt_exist(self):
        """
        Checks if the return value is correct when the habit doesn't exist.
        """
        user_data = UserData("username", "password", "email@email.com")

        self.assertFalse(user_data.complete_habit(0), "Check if the return value is correct.")
        self.assertEqual(user_data.coins, 0, "Check if no coins were added")
        
    def test_habit_already_completed(self):
        """
        Checks if a habit is retrieved correctly.
        """
        user_data = UserData("username", "password", "email@email.com")
        habit_name = "Habit"
        habit_freq = 0

        user_data.add_habit(habit_name, habit_freq)
        user_data.complete_habit(0)
        
        self.assertFalse(user_data.complete_habit(0), "Check if the return value is correct.")
        self.assertTrue(user_data.get_habit(0).is_complete, "Check if the habit was completed")
        self.assertEqual(user_data.coins, 70, "Check if the coins were added correctly")

    def test_weekly_bonus_earned(self):
        """
        Checks if the weekly bonus is correctly earned.
        """
        user_data = UserData("username", "password", "email@email.com")
        habit_name = "Habit"
        habit_freq = 1

        user_data.add_habit(habit_name, habit_freq)
        user_data.complete_habit(0)

        self.assertEqual(user_data.coins, 70, "Check if the coins were added correctly")

    def test_monthly_bonus_earned(self):
        """
        Checks if the monthly bonus is correctly earned.
        """
        user_data = UserData("username", "password", "email@email.com")
        habit_name = "Habit"
        habit_freq = 2

        user_data.add_habit(habit_name, habit_freq)
        user_data.complete_habit(0)

        self.assertEqual(user_data.coins, 70, "Check if the coins were added correctly")