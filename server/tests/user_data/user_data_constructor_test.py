import unittest
from server.user_data import UserData

class TestConstructor(unittest.TestCase):    
    """
    Tests for the UserData constructor.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_constructor(self):
        """
        Checks if the constructor sets the default values correctly.
        """
        user_data = UserData("username", "password", "email@email.com")
        self.assertEqual(user_data.get_username(), "username", "Check if username is set correctly.")
        self.assertEqual(user_data.get_password(), "password", "Check if password is set correctly.")
        self.assertEqual(user_data.get_email(), "email@email.com", "Check if email is set correctly.")
        self.assertEqual(user_data.get_coins(), 0, "Check if coins are set correctly.")
        self.assertEqual(user_data.get_sudoku_puzzle(), None, "Check if sudoku_puzzle is set correctly.")
    
    def test_empty_username(self):
        """
        Checks if the an exception is raised when using an empty username.
        """
        self.assertRaises(Exception, UserData, ("", "password", "email@email.com"))

    def test_empty_password(self):
        """
        Checks if the an exception is raised when using an empty password.
        """
        self.assertRaises(Exception, UserData, ("username", "", "email@email.com"))

    def test_empty_email(self):
        """
        Checks if the an exception is raised when using an empty username.
        """
        self.assertRaises(Exception, UserData, ("username", "password", ""))

    def test_none_username(self):
        """
        Checks if the an exception is raised when passing None as the username.
        """
        self.assertRaises(Exception, UserData, (None, "password", "email@email.com"))

    def test_none_password(self):
        """
        Checks if the an exception is raised when passing None as the password.
        """
        self.assertRaises(Exception, UserData, ("username", None, "email@email.com"))

    def test_none_email(self):
        """
        Checks if the an exception is raised when passing None as the email.
        """
        self.assertRaises(Exception, UserData, ("username", "password", None))

    def test_non_str_username(self):
        """
        Checks if the an exception is raised when passing a non-str username.
        """
        self.assertRaises(Exception, UserData, (0, "password", "email@email.com"))

    def test_non_str_password(self):
        """
        Checks if the an exception is raised when passing a non-str password.
        """
        self.assertRaises(Exception, UserData, ("username", 0, "email@email.com"))

    def test_non_str_email(self):
        """
        Checks if the an exception is raised when passing a non-str email.
        """
        self.assertRaises(Exception, UserData, ("username", "password", 0))
