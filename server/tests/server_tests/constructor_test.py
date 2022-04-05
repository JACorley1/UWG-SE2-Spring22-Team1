import unittest
from backend.server import Server

class TestConstructor(unittest.TestCase):    
    """
    Tests for the Server constructor.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_constructor(self):
        """
        Checks if the constructor doesn't break.
        """
        Server()
