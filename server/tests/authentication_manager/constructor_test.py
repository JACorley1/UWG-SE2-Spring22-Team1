import unittest
from backend.authentication_manager import AuthenticationManager

class TestConstructor(unittest.TestCase):    
    """
    Tests for the AuthentiactionManager constructor.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_constructor(self):
        """
        Checks if the constructor sets the default values.
        """
        authentication_manager = AuthenticationManager()

        self.assertEqual(
            authentication_manager._tokens_to_usernames,
            {}, 
            "Check if _tokens_to_usernames is correct."
        )
        self.assertEqual(
            authentication_manager._usernames_to_tokens, 
            {}, 
            "Check if _usernames_to_tokens is correct."
        )
