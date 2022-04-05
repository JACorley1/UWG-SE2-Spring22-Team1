import unittest

from backend.habit import Habit

class TestCreateJsonDict(unittest.TestCase):    
    """
    Tests for the create_json_dict property.

    @author Team 1
    @version Spring 2022
    """

    def test_create_dictionary(self):
        """
        Checks if dictionary's values are correct.
        """
        name = "Habit"
        frequency = 0
        id = 0
        habit = Habit(name, frequency, id)

        json_dict = habit.create_json_dict()

        self.assertEqual(json_dict["name"], name, "Check if the dictionary's name value is correct.")
        self.assertEqual(json_dict["frequency"], frequency, "Check if the dictionary's frequency value is correct.")
        self.assertEqual(json_dict["id"], id, "Check if the dictionary's id value is correct.")
        self.assertFalse(json_dict["is_complete"], "Check if the dictionary's is_complete value is correct.")