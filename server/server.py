import json
from typing import Any, MutableMapping
from server.service_manager import ServiceManager
import zmq

class _RequestHandler:
    """
    Handles server requests and returns appropriately formatted responses

    @author Team 1
    @version Spring 2022
    """
    _service_manager: ServiceManager

    def __init__(self, service_manager: ServiceManager):
        """
        Creates a new RequestHandler using the specified ServiceManager.

        Precondition:  service_manager is not None and
                       isinstance(service_manager, ServiceManager)
        Postcondition: RequestHandler has appropriate ServiceManager to server requests

        Params - service_manager: The specified ServiceManager
        """
        if service_manager is None:
            raise Exception("service_manager must not be None")
        if not isinstance(service_manager, ServiceManager):
            raise Exception("service_manager must be an instance of ServiceManager.")

        self._service_manager = service_manager

    def _get_missing_fields(self, request: MutableMapping[str, Any], fields: list[str]) -> list[str]:
        """
        Creates a list of anf missing fields from a request.

        Precondition:  request is not None and
                       isinstance(request, MutableMapping) and
                       field is not None and
                       isinstance(field, list)
        Postcondition: None

        Params - request: The received request from the client.
                 fields: The list of fields that should be present in the request.
        Return - A list containing any missing fields.
        """
        if request is None:
            raise Exception("request must not be None")
        if not isinstance(request, MutableMapping):
            raise Exception("request must be a dictionary with str as keys")
        if fields is None:
            raise Exception("fields must not be None")
        if not isinstance(fields, list):
            raise Exception("fields must be a list of str")
        missing_fields: list[str] = []
        for field in fields:
            if field not in request:
                missing_fields.append(field)
        return missing_fields

    def _register_user(self, username: str, email: str, password: str) -> MutableMapping[str, Any]:
        """
        Attempts to add a new user to the server using the specified username, password, and email.
        Generates and returns a response to be sent back to the client.

        Precondition:  None
        Postcondition: None

        Params - username: The specified username.
                 password: The specified password.
                 email: The specified email address.
        Return - The response to the client.
        """
        success_code: int = self._service_manager.create_user(username, password, email)
        response: MutableMapping[str, Any]
        if success_code == 20:
            response = {
                "successCode": 20,
                "error_message": f"Username ({username}) already exists"
            }
        elif success_code == 21:
            response = {
                "successCode": 21,
                "error_message": f"Username ({username}) is invalid"
            }
        elif success_code == 22:
            response = {
                "successCode": 22,
                "error_message": "Password is invalid"
            }
        elif success_code == 23:
            response = {
                "successCode": 23,
                "error_message": f"Email ({email}) is invalid"
            }
        else:
            response = {
                "successCode": 0
            }
        return response

    def handle_request(self, request: MutableMapping[str, Any]) -> MutableMapping[str, Any]:
        """
        Accepts a request from the client and performs an action depending on the request body.
        Generates and returns a response to the client.

        Precondition:  request is not None and
                       isinstance(request, MutableMapping)
        Postcondition: The action in the request is carried out, if the request if formed properly.

        Params - request: The received request from the client.
        Return - The response to be sent back to the client.
        """
        if request is None:
            raise Exception("request must not be None")
        if not isinstance(request, MutableMapping):
            raise Exception("request must be a dictionary with str as keys")

        response: MutableMapping[str, Any]
        if "request_type" not in request :
            return {
                "successCode": 10,
                "error_message": "Malformed Request, missing Request Type"
            }

        if request["request_type"] == "register_user" :
            missing_fields: list[str] = self._get_missing_fields(request, ["username", "password", "email"])
            if len(missing_fields) > 0:
                response = {
                    "successCode": 12,
                    "error_message": f"Malformed Request, missing Request Fields ({', '.join(missing_fields)})"
                }
            else:
                response = self._register_user(request["username"], request["password"], request["email"])

        else :
            error_message = f"Unsupported Request Type ({request['request_type']})"
            response = {"successCode": 11, "error_message": error_message}
        return response

class Server:
    """
    The server for Habit Mode.
    Maintains and modifies user information.

    @author Team 1
    @version Spring 2022
    """
    def run(self, service_manager: ServiceManager):
        """
        Launches the server with a specified ServiceManager.
        The server will run indefinitely.

        Precondition:  service_manager is not None and
                       isinstance(service_manager, ServiceManager)
        Postcondition: The server becomes active.
        """
        if service_manager is None:
            raise Exception("service_manager must not be None")
        if not isinstance(service_manager, ServiceManager):
            raise Exception("service_manager must be an instance of ServiceManager.")

        request_handler = _RequestHandler(service_manager)
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://0.0.0.0:8000")

        while True:
            #  Wait for next request from client
            print("waiting for message...")
            json_request = socket.recv_string()
            request = json.loads(json_request)
            json_response: str
            print(f"Received request: {request}")
            if request == "exit":
                return
            response = request_handler.handle_request(request)
            json_response = json.dumps(response)

            #  Send reply back to client
            socket.send_string(json_response)
