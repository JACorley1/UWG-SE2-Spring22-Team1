import unittest

from server.user_data import UserData

class TestAddHabit(unittest.TestCase):    
    """
    Tests for adding a habit to the user's list of habits.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_habit(self):
        """
        Checks if a single habit is added correctly.
        """
        user_data = UserData("username", "password", "email@email.com")
        habit_name = "Habit"
        habit_freq = 0

        user_data.add_habit(habit_name, habit_freq)
        habit = user_data.habits[0]

        self.assertEqual(len(user_data.habits), 1, "Check if habits is the right length.")
        self.assertEqual(habit.name, habit_name, "Check if habit.name is correct.")
        self.assertEqual(habit.frequency, habit_freq, "Check if habit.frequency is correct.")
        self.assertEqual(habit.id, 0, "Check if habit.id is correct.")

    def test_many_valid_habits(self):
        """
        Checks if many habits are added correctly.
        """
        user_data = UserData("username", "password", "email@email.com")
        habit_name1 = "Habit1"
        habit_name2 = "Habit2"
        habit_freq1 = 0
        habit_freq2 = 1

        user_data.add_habit(habit_name1, habit_freq1)
        user_data.add_habit(habit_name2, habit_freq2)
        habit1 = user_data.habits[0]
        habit2 = user_data.habits[1]

        self.assertEqual(len(user_data.habits), 2, "Check if habits is the right length.")
        self.assertEqual(habit1.name, habit_name1, "Check if habit.name is correct.")
        self.assertEqual(habit1.frequency, habit_freq1, "Check if habit.frequency is correct.")
        self.assertEqual(habit1.id, 0, "Check if habit.id is correct.")
        self.assertEqual(habit2.name, habit_name2, "Check if habit.name is correct.")
        self.assertEqual(habit2.frequency, habit_freq2, "Check if habit.frequency is correct.")
        self.assertEqual(habit2.id, 1, "Check if habit.id is correct.")