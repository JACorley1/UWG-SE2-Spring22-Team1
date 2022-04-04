import unittest
from backend.authentication_manager import AuthenticationManager
from backend.server import _RequestHandler
from backend.service_manager import ServiceManager

class TestConstructor(unittest.TestCase):    
    """
    Tests for the _get_missing_fields method.

    @author Team 1
    @version Spring 2022
    """

    def test_no_missing_fields(self):
        """
        Checks if the field was detected correctly.
        """
        request_handler = _RequestHandler(ServiceManager())
        request = {"field": 0}
        fields = ["field"]

        result = request_handler._get_missing_fields(request, fields)
        self.assertEqual(len(result), 0, "Check if the returned list is empty.")

    def test_empty_field_list(self):
        """
        Checks if checking for no fields causes issues.
        """
        request_handler = _RequestHandler(ServiceManager())
        request = {"field": 0}
        fields = []

        result = request_handler._get_missing_fields(request, fields)
        self.assertEqual(len(result), 0, "Check if the returned list is empty.")

    def test_one_missing_field(self):
        """
        Checks if the missing field is detected correctly.
        """
        request_handler = _RequestHandler(ServiceManager())
        request = {}
        fields = ["field"]

        result = request_handler._get_missing_fields(request, fields)
        self.assertEqual(len(result), 1, "Check if the returned list is the right size.")
        self.assertTrue("field" in result, "Check if the missing field is in the returned list.")

    def test_many_missing_field(self):
        """
        Checks if the missing fields are detected correctly.
        """
        request_handler = _RequestHandler(ServiceManager())
        request = {}
        fields = ["field1", "field2", "field3"]

        result = request_handler._get_missing_fields(request, fields)
        self.assertEqual(len(result), 3, "Check if the returned list is the right size.")
        self.assertTrue("field1" in result, "Check if the first missing field is in the returned list.")
        self.assertTrue("field2" in result, "Check if the second missing field is in the returned list.")
        self.assertTrue("field3" in result, "Check if the third missing field is in the returned list.")
