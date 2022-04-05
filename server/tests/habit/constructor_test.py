import unittest

from backend.habit import Habit

class TestConstructor(unittest.TestCase):    
    """
    Tests for the Habit constructor.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_constructor(self):
        """
        Checks if the constructor sets the default values correctly.
        """
        name = "Habit"
        frequency = 0
        id = 0
        
        habit = Habit(name, frequency, id)

        self.assertEqual(habit.name, name, "Check if name is correct")
        self.assertEqual(habit.frequency, frequency, "Check if frequency is correct")
        self.assertEqual(habit.id, id, "Check if id is correct")
        self.assertFalse(habit.is_complete, "Check if the habit isn't complete")

    def test_max_frequency(self):
        """
        Checks if the constructor sets the default values correctly when frequency is max.
        """
        name = "Habit"
        frequency = 2
        id = 0
        
        habit = Habit(name, frequency, id)

        self.assertEqual(habit.name, name, "Check if name is correct")
        self.assertEqual(habit.frequency, frequency, "Check if frequency is correct")
        self.assertEqual(habit.id, id, "Check if id is correct")
        self.assertFalse(habit.is_complete, "Check if the habit isn't complete")

    def test_empty_name(self):
        """
        Checks if an exception is thrown if the name is empty.
        """
        name = ""
        frequency = 0
        id = 0
        
        self.assertRaises(
            Exception,
            Habit,
            (name, frequency, id),
            "Check if an exception is raised when name is empty"
        )

    def test_none_name(self):
        """
        Checks if an exception is thrown if the name is empty.
        """
        name = None
        frequency = 0
        id = 0
        
        self.assertRaises(
            Exception,
            Habit,
            (name, frequency, id),
            "Check if an exception is raised when name is None"
        )

    def test_non_str_name(self):
        """
        Checks if an exception is thrown if the name is empty.
        """
        name = 0
        frequency = 0
        id = 0
        
        self.assertRaises(
            Exception,
            Habit,
            (name, frequency, id),
            "Check if an exception is raised when name is a non-str"
        )

    def test_frequency_too_low(self):
        """
        Checks if an exception is thrown if the frequency is too low.
        """
        name = "Habit"
        frequency = -1
        id = 0
        
        self.assertRaises(
            Exception,
            Habit,
            (name, frequency, id),
            "Check if an exception is raised when frequency is too low"
        )

    def test_frequency_too_high(self):
        """
        Checks if an exception is thrown if the frequency is too high.
        """
        name = "Habit"
        frequency = 3
        id = 0
        
        self.assertRaises(
            Exception,
            Habit,
            (name, frequency, id),
            "Check if an exception is raised when frequency is too high"
        )

    def test_non_int_frequency(self):
        """
        Checks if an exception is thrown if the frequency is a non-int.
        """
        name = "Habit"
        frequency = ""
        id = 0
        
        self.assertRaises(
            Exception,
            Habit,
            (name, frequency, id),
            "Check if an exception is raised when frequency is a non-int"
        )

    def test_none_frequency(self):
        """
        Checks if an exception is thrown if the frequency is None.
        """
        name = "Habit"
        frequency = None
        id = 0
        
        self.assertRaises(
            Exception,
            Habit,
            (name, frequency, id),
            "Check if an exception is raised when frequency is None"
        )

    def test_non_int_id(self):
        """
        Checks if an exception is thrown if the id is a non-int.
        """
        name = "Habit"
        frequency = 0
        id = ""
        
        self.assertRaises(
            Exception,
            Habit,
            (name, frequency, id),
            "Check if an exception is raised when id is a non-int"
        )

    def test_none_id(self):
        """
        Checks if an exception is thrown if the id is None.
        """
        name = "Habit"
        frequency = 0
        id = None
        
        self.assertRaises(
            Exception,
            Habit,
            (name, frequency, id),
            "Check if an exception is raised when id is None"
        )
