import unittest

from server.habit import Habit

class TestComplete(unittest.TestCase):    
    """
    Tests for the complete method.

    @author Team 1
    @version Spring 2022
    """

    def test_complete_daily_habit(self):
        """
        Checks if complete correctly completes a daily habit.
        """
        name = "Habit"
        frequency = 0
        id = 0
        
        habit = Habit(name, frequency, id)
        habit.complete()
        self.assertTrue(habit.is_complete, "Check if a daily habit is correctly completed")

    def test_complete_weekly_habit(self):
        """
        Checks if complete correctly completes a weekly habit.
        """
        name = "Habit"
        frequency = 1
        id = 0
        
        habit = Habit(name, frequency, id)
        habit.complete()
        self.assertTrue(habit.is_complete, "Check if a daily habit is correctly completed")

    def test_complete_monthly_habit(self):
        """
        Checks if complete correctly completes a monthly habit.
        """
        name = "Habit"
        frequency = 2
        id = 0
        
        habit = Habit(name, frequency, id)
        habit.complete()
        self.assertTrue(habit.is_complete, "Check if a daily habit is correctly completed")
