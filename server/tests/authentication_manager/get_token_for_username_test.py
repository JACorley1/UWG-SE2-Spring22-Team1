import unittest
from backend.authentication_manager import AuthenticationManager

class TestGetTOkenForUsername(unittest.TestCase):    
    """
    Tests for the get_token_for_username method.

    @author Team 1
    @version Spring 2022
    """

    def test_generate_and_store_token(self):
        """
        Checks if the constructor sets the default values.
        """
        authentication_manager = AuthenticationManager()
        username = "username"

        token = authentication_manager.generate_and_store_key_for_username(username)
        
        self.assertEqual(
            token, 
            authentication_manager.get_token_for_username(username), 
            "Check if a token was generated"
        )

    def test_token_not_exists(self):
        """
        Checks if the constructor sets the default values.
        """
        authentication_manager = AuthenticationManager()
        
        self.assertTrue(
            authentication_manager.get_token_for_username("username") is None, 
            "Check if None is returned when no token exists"
        )