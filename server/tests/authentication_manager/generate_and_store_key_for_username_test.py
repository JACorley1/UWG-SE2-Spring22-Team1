import unittest
import server.authentication_manager as authentication_manager

class TestGenerateAndStoreKeyForUsername(unittest.TestCase):    
    """
    Tests for the generate_and_store_key_for_username method.

    @author Team 1
    @version Spring 2022
    """
    iteration: int = 0

    def test_username_exists(self):
        """
        Checks if the constructor sets the default values.
        """
        manager = authentication_manager.AuthenticationManager()
        username = "username"

        token = manager.generate_and_store_key_for_username(username)
        
        self.assertEqual(
            token, 
            manager.get_token_for_username(username), 
            "Check if a token was generated"
        )
        self.assertEqual(
            username, 
            manager.get_username_for_token(token), 
            "Check if a token was generated"
        )

    def test_token_generated_twice(self):
        """
        Tests if the authentication token gets regenerated if already generated and stored previously.
        """
        manager = authentication_manager.AuthenticationManager()
        username = "username"
        prev_func = authentication_manager.generate_token

        def temp():
            res = "0" if self.iteration < 2 else "1"
            self.iteration += 1
            return res
        
        authentication_manager.generate_token = temp

        manager.generate_and_store_key_for_username("username1")
        manager.generate_and_store_key_for_username(username)
        
        self.assertEqual(
            "1", 
            manager.get_token_for_username(username), 
            "Check if a token was generated"
        )
        self.assertEqual(
            username, 
            manager.get_username_for_token("1"), 
            "Check if a token was generated"
        )

        self.iteration = 0
        authentication_manager.generate_token = prev_func