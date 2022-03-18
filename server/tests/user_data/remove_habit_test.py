import unittest

from server.user_data import UserData

class TestRemoveHabit(unittest.TestCase):    
    """
    Tests for removing a habit from the user's list of habits.

    @author Team 1
    @version Spring 2022
    """

    def test_remove_habit(self):
        """
        Checks if a habit is removed correctly.
        """
        user_data = UserData("username", "password", "email@email.com")
        habit_name = "Habit"
        habit_freq = 0

        user_data.add_habit(habit_name, habit_freq)

        self.assertTrue(user_data.remove_habit(0), "Check if the return value is correct.")
        self.assertEqual(len(user_data.habits), 0, "Check if the habit was removed from the list.")

    def test_habit_doesnt_exist(self):
        """
        Checks if the return value is correct when habits doens't exist.
        """
        user_data = UserData("username", "password", "email@email.com")

        self.assertFalse(user_data.remove_habit(0), "Check if the return value is correct.")