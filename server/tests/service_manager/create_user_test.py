import unittest
from server.service_manager import ServiceManager

class TestConstructor(unittest.TestCase):    
    """
    Tests for the create_user function.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_user(self):
        """
        Checks if a user is created when given valid credentials.
        """
        service_manager = ServiceManager()
        result = service_manager.create_user("username", "password", "email@email.com")

        self.assertEqual(result, 0, "Check if success code is correct")
        self.assertTrue(len(service_manager._user_information.items()) == 1, "Check if _user_information contains the user")

    def test_many_valid_user(self):
        """
        Checks if many users are created when given valid credentials.
        """
        service_manager = ServiceManager()
        result1 = service_manager.create_user("username", "password", "email@email.com")
        result2 = service_manager.create_user("username2", "password", "email@email.com")

        self.assertEqual(result1, 0, "Check if first success code is correct")
        self.assertEqual(result2, 0, "Check if second success code is correct")
        self.assertTrue(len(service_manager._user_information.items()) == 2, "Check if _user_information contains both users")

    def test_duplicate_username(self):
        """
        Checks if the correct success code is returned when adding a duplicate username.
        """
        service_manager = ServiceManager()
        service_manager.create_user("username", "password", "email@email.com")
        result = service_manager.create_user("username", "password", "email@email.com")

        self.assertEqual(result, 20, "Check if success code is correct")
        self.assertTrue(len(service_manager._user_information.items()) == 1, "Check if _user_information only contains the first user")
    
    def test_blank_username(self):
        """
        Checks if the correct success code is returned when adding a blank username.
        """
        service_manager = ServiceManager()
        result = service_manager.create_user("", "password", "email@email.com")

        self.assertEqual(result, 21, "Check if success code is correct")
        self.assertTrue(len(service_manager._user_information.items()) == 0, "Check if user wasn't added")

    def test_none_username(self):
        """
        Checks if the correct success code is returned when adding a None username.
        """
        service_manager = ServiceManager()
        result = service_manager.create_user(None, "password", "email@email.com")

        self.assertEqual(result, 21, "Check if success code is correct")
        self.assertTrue(len(service_manager._user_information.items()) == 0, "Check if user wasn't added")

    def test_non_str_username(self):
        """
        Checks if the correct success code is returned when adding a non-str username.
        """
        service_manager = ServiceManager()
        result = service_manager.create_user(0, "password", "email@email.com")

        self.assertEqual(result, 21, "Check if success code is correct")
        self.assertTrue(len(service_manager._user_information.items()) == 0, "Check if user wasn't added")
    
    def test_blank_password(self):
        """
        Checks if the correct success code is returned when adding a blank password.
        """
        service_manager = ServiceManager()
        result = service_manager.create_user("username", "", "email@email.com")

        self.assertEqual(result, 22, "Check if success code is correct")
        self.assertTrue(len(service_manager._user_information.items()) == 0, "Check if user wasn't added")

    def test_none_password(self):
        """
        Checks if the correct success code is returned when adding a None password.
        """
        service_manager = ServiceManager()
        result = service_manager.create_user("username", None, "email@email.com")

        self.assertEqual(result, 22, "Check if success code is correct")
        self.assertTrue(len(service_manager._user_information.items()) == 0, "Check if user wasn't added")

    def test_non_str_password(self):
        """
        Checks if the correct success code is returned when adding a non-str password.
        """
        service_manager = ServiceManager()
        result = service_manager.create_user("username", 0, "email@email.com")

        self.assertEqual(result, 22, "Check if success code is correct")
        self.assertTrue(len(service_manager._user_information.items()) == 0, "Check if user wasn't added")

    def test_blank_email(self):
        """
        Checks if the correct success code is returned when adding a blank email.
        """
        service_manager = ServiceManager()
        result = service_manager.create_user("username", "password", "")

        self.assertEqual(result, 23, "Check if success code is correct")
        self.assertTrue(len(service_manager._user_information.items()) == 0, "Check if user wasn't added")

    def test_none_password(self):
        """
        Checks if the correct success code is returned when adding a None email.
        """
        service_manager = ServiceManager()
        result = service_manager.create_user("username", "password", None)

        self.assertEqual(result, 23, "Check if success code is correct")
        self.assertTrue(len(service_manager._user_information.items()) == 0, "Check if user wasn't added")

    def test_non_str_password(self):
        """
        Checks if the correct success code is returned when adding a non-str email.
        """
        service_manager = ServiceManager()
        result = service_manager.create_user("username", "password", 0)

        self.assertEqual(result, 23, "Check if success code is correct")
        self.assertTrue(len(service_manager._user_information.items()) == 0, "Check if user wasn't added")
