import unittest
from server.user_data import UserData

class TestIncrementHabitId(unittest.TestCase):    
    """
    Tests for the increment_habit_id method.

    @author Team 1
    @version Spring 2022
    """

    def test_incremenet_once(self):
        """
        Checks if the constructor sets the default values correctly.
        """
        user_data = UserData("username", "password", "email@email.com")
        user_data.increment_habit_id()

        self.assertEqual(user_data.next_habit_id, 1, "Check if next_habit_id was incremented correctly")

    def test_incremenet_many_times(self):
        """
        Checks if the constructor sets the default values correctly.
        """
        user_data = UserData("username", "password", "email@email.com")
        user_data.increment_habit_id()
        user_data.increment_habit_id()
        user_data.increment_habit_id()
        user_data.increment_habit_id()
        user_data.increment_habit_id()

        self.assertEqual(user_data.next_habit_id, 5, "Check if next_habit_id was incremented correctly")
