import unittest
from server.server import _RequestHandler
from server.service_manager import ServiceManager

class TestConstructor(unittest.TestCase):    
    """
    Tests for the handle_request method.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_register_user(self):
        """
        Checks if a valid register_user request is handled correctly.
        """
        request_handler = _RequestHandler(ServiceManager())
        request = {
            "request_type": "register_user",
            "username": "username",
            "password": "password",
            "email": "email@email.com"
        }

        result = request_handler.handle_request(request)
        self.assertEqual(result["successCode"], 0, "Check if success_code is correct.")

    def test_missing_request_type(self):
        """
        Checks if a the correct response is created when not providing a request type.
        """
        request_handler = _RequestHandler(ServiceManager())
        request = {
            "username": "username",
            "password": "password",
            "email": "email@email.com"
        }

        result = request_handler.handle_request(request)
        self.assertEqual(result["successCode"], 10, "Check if success_code is correct.")
        self.assertEqual(
            result["error_message"], 
            "Malformed Request, missing Request Type", 
            "Check if error_message is correct."
        )

    def test_none_request(self):
        """
        Checks if an exception is raised when passing None in for the request.
        """
        request_handler = _RequestHandler(ServiceManager())
        request = None

        self.assertRaises(
            Exception, 
            request_handler.handle_request, 
            (request), 
            "Check if an exception is raised when None is passed in"
        )

    def test_non_dict_request(self):
        """
        Checks if an exception is raised when passing None in for the request.
        """
        request_handler = _RequestHandler(ServiceManager())
        request = 0

        self.assertRaises(
            Exception, 
            request_handler.handle_request, 
            (request), 
            "Check if an exception is raised when a non-dict is passed in"
        )

    def test_unknown_request_type(self):
        """
        Checks if a the correct response is created when giving an invalid request type.
        """
        request_handler = _RequestHandler(ServiceManager())
        request = {
            "request_type": "",
            "username": "username",
            "password": "password",
            "email": "email@email.com"
        }

        result = request_handler.handle_request(request)
        self.assertEqual(result["successCode"], 11, "Check if success_code is correct.")
        self.assertEqual(
            result["error_message"], 
            "Unsupported Request Type ()", 
            "Check if error_message is correct."
        )

    def test_missing_request_type(self):
        """
        Checks if a the correct response is created when not providing a request type.
        """
        request_handler = _RequestHandler(ServiceManager())
        request = {
            "username": "username",
            "password": "password",
            "email": "email@email.com"
        }

        result = request_handler.handle_request(request)
        self.assertEqual(result["successCode"], 10, "Check if success_code is correct.")
        self.assertEqual(
            result["error_message"], 
            "Malformed Request, missing Request Type", 
            "Check if error_message is correct."
        )


    def test_missing_fields(self):
        """
        Checks if a the correct response is created when missing fields.
        """
        request_handler = _RequestHandler(ServiceManager())
        request = {
            "request_type": "register_user",
            "username": "username",
            "password": "password",
        }

        result = request_handler.handle_request(request)
        self.assertEqual(result["successCode"], 12, "Check if success_code is correct.")
        self.assertEqual(
            result["error_message"], 
            f"Malformed Request, missing Request Fields (email)", 
            "Check if error_message is correct."
        )
