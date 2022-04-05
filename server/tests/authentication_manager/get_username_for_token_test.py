import unittest
from backend.authentication_manager import AuthenticationManager

class TestGetUsernameForToken(unittest.TestCase):    
    """
    Tests for the get_username_for_token method.

    @author Team 1
    @version Spring 2022
    """

    def test_token_exists(self):
        """
        Checks if the constructor sets the default values.
        """
        authentication_manager = AuthenticationManager()
        username = "username"

        token = authentication_manager.generate_and_store_key_for_username(username)
        
        self.assertEqual(
            username, 
            authentication_manager.get_username_for_token(token), 
            "Check if a token was generated"
        )

    def test_token_not_exists(self):
        """
        Checks if the constructor sets the default values.
        """
        authentication_manager = AuthenticationManager()
        
        self.assertTrue(
            authentication_manager.get_username_for_token("username") is None, 
            "Check if None is returned when no token exists"
        )