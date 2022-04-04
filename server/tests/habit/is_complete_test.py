import unittest

from server.habit import Habit
from server import datetime_extension

class TestIsComplete(unittest.TestCase):    
    """
    Tests for the is_complete property.

    @author Team 1
    @version Spring 2022
    """

    def test_daily_habit_reset_yesteday(self):
        """
        Checks if a habit whose reset_date is after today will be marked as incomplete.
        """
        name = "Habit"
        frequency = 0
        id = 0
        
        habit = Habit(name, frequency, id)
        habit._reset_date = datetime_extension.yesterday()

        self.assertFalse(habit.is_complete, "Test if a habit that reset yesterday is marked as incomplete")

    def test_daily_habit_resets_tomorrow(self):
        """
        Checks if a habit whose reset_date is before today will be marked as complete.
        """
        name = "Habit"
        frequency = 0
        id = 0
        
        habit = Habit(name, frequency, id)
        habit._reset_date = datetime_extension.tomorrow()

        self.assertTrue(habit.is_complete, "Test if a habit that resets tomorrow is marked as complete")
