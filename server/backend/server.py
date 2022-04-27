import json
from typing import Any, List, MutableMapping, Tuple
from backend.authentication_manager import AuthenticationManager
from backend.service_manager import ServiceManager
import backend.request_handler.authentication_handler as authentication_handler
import backend.request_handler.habit_handler as habit_handler
import backend.request_handler.user_handler as user_handler
import backend.request_handler.sudoku_handler as sudoku_handler
import zmq

class _RequestHandler:
    """
    Handles server requests and returns appropriately formatted responses

    @author Team 1
    @version Spring 2022
    """
    _service_manager: ServiceManager
    _authentication_manager: AuthenticationManager

    def __init__(self, service_manager: ServiceManager, authentication_manager: AuthenticationManager):
        """
        Creates a new RequestHandler using the specified ServiceManager.

        Precondition:  service_manager is not None and
                       isinstance(service_manager, ServiceManager)
        Postcondition: RequestHandler has appropriate ServiceManager to server requests

        Params - service_manager: The specified ServiceManager
                 authentication_manager: The specified AuthenticationManager
        """
        if service_manager is None:
            raise Exception("service_manager must not be None")
        if not isinstance(service_manager, ServiceManager):
            raise Exception("service_manager must be an instance of ServiceManager.")
        if authentication_manager is None:
            raise Exception("authentication_manager must not be None")
        if not isinstance(authentication_manager, AuthenticationManager):
            raise Exception("authentication_manager must be an instance of AuthenticationManager.")

        self._service_manager = service_manager
        self._authentication_manager = authentication_manager

    def _get_missing_fields(self, request: MutableMapping[str, Any], fields: List[str]) -> List[str]:
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
        missing_fields: List[str] = []
        for field in fields:
            if field not in request:
                missing_fields.append(field)
        return missing_fields

    def _create_missing_field_response(self, missing_fields: List[str]):
        return {
            "success_code": 12,
            "error_message": f"Malformed Request, missing Request Fields ({', '.join(missing_fields)})"
        }

    def _register_user(self, username: str, password: str, email: str) -> MutableMapping[str, Any]:
        return authentication_handler.register_user(
            self._service_manager, 
            username, 
            password, 
            email
        )
        
    def _login(self, username: str, password: str) -> MutableMapping[str, Any]:
        return authentication_handler.login(
            self._service_manager, 
            self._authentication_manager, 
            username, 
            password
        )

    def _retrieve_data(self, token: str, fields: List[str]) -> MutableMapping[str, Any]:
        return user_handler.retrieve_data(
            self._service_manager,
            self._authentication_manager,
            token,
            fields
        )

    def _add_habit(self, token: str, habit_name: str, habit_frequency: int) -> MutableMapping[str, Any]:
        return habit_handler.add_habit(
            self._service_manager, 
            self._authentication_manager, 
            token, 
            habit_name, 
            habit_frequency
        )

    def _remove_habit(self, token: str, habit_id: int) -> MutableMapping[str, Any]:
        return habit_handler.remove_habit(
            self._service_manager, 
            self._authentication_manager, 
            token, 
            habit_id
        )
    
    def _modify_habit(self, token: str, habit_id: int, habit_name: str, habit_frequency: int) -> MutableMapping[str, Any]:
        return habit_handler.modify_habit(
            self._service_manager, 
            self._authentication_manager, 
            token, 
            habit_id, 
            habit_name, 
            habit_frequency
        )

    def _complete_habits(self, token: str, habit_ids: List[int]) -> MutableMapping[str, Any]:
        return habit_handler.complete_habits(
            self._service_manager, 
            self._authentication_manager, 
            token, 
            habit_ids
        )

    def _generate_sudoku_puzzle(self, token: str) -> MutableMapping[str, Any]:
        return sudoku_handler.generate_sudoku_puzzle(
            self._service_manager, 
            self._authentication_manager, 
            token
        )

    def _update_sudoku_puzzle(self, token: str, numbers: List[List[int]]):
        return sudoku_handler.update_sudoku_puzzle(
            self._service_manager, 
            self._authentication_manager, 
            token, 
            numbers
        )

    def _buy_hint(self, token: str) -> MutableMapping[str, Any]:
        return sudoku_handler.buy_hint(
            self._service_manager, 
            self._authentication_manager, 
            token
        )

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
                "success_code": 10,
                "error_message": "Malformed Request, missing Request Type"
            }

        missing_fields: List[str]

        if request["request_type"] == "register_user" :
            missing_fields = self._get_missing_fields(request, ["username", "password", "email"])
            if len(missing_fields) > 0:
                response = {
                    "success_code": 12,
                    "error_message": f"Malformed Request, missing Request Fields ({', '.join(missing_fields)})"
                }
            else:
                response = authentication_handler.register_user(
                    self._service_manager, request["username"], 
                    request["password"], request["email"]
                )

        elif request["request_type"] == "login":
            missing_fields = self._get_missing_fields(request, ["username", "password"])
            if len(missing_fields) > 0:
                response = self._create_missing_field_response(missing_fields)
            else:
                response = self._login(request["username"], request["password"])

        elif request["request_type"] == "retrieve_data":
            missing_fields = self._get_missing_fields(request, ["authentication_token", "fields"])
            if len(missing_fields) > 0:
                response = self._create_missing_field_response(missing_fields)
            else:
                response = self._retrieve_data(request["authentication_token"], request["fields"])

        elif request["request_type"] == "add_habit":
            missing_fields = self._get_missing_fields(request, ["authentication_token", "habit_name", "habit_frequency"])
            if len(missing_fields) > 0:
                response = self._create_missing_field_response(missing_fields)
            else:
                response = self._add_habit(request["authentication_token"], request["habit_name"], request["habit_frequency"])

        elif request["request_type"] == "remove_habit":
            missing_fields = self._get_missing_fields(request, ["authentication_token", "habit_id"])
            if len(missing_fields) > 0:
                response = self._create_missing_field_response(missing_fields)
            else:
                response = self._remove_habit(request["authentication_token"], request["habit_id"])

        elif request["request_type"] == "modify_habit":
            missing_fields = self._get_missing_fields(request, ["authentication_token", "habit_id", "habit_name", "habit_frequency"])
            if len(missing_fields) > 0:
                response = self._create_missing_field_response(missing_fields)
            else:
                response = self._modify_habit(request["authentication_token"], request["habit_id"], request["habit_name"], request["habit_frequency"])

        elif request["request_type"] == "complete_habits":
            missing_fields = self._get_missing_fields(request, ["authentication_token", "habit_ids"])
            if len(missing_fields) > 0:
                response = self._create_missing_field_response(missing_fields)
            else:
                response = self._complete_habits(request["authentication_token"], request["habit_ids"])

        elif request["request_type"] == "generate_sudoku_puzzle":
            missing_fields = self._get_missing_fields(request, ["authentication_token"])
            if len(missing_fields) > 0:
                response = self._create_missing_field_response(missing_fields)
            else:
                response = self._generate_sudoku_puzzle(request["authentication_token"])

        elif request["request_type"] == "update_sudoku_puzzle":
            missing_fields = self._get_missing_fields(request, ["authentication_token", "numbers"])
            if len(missing_fields) > 0:
                response = self._create_missing_field_response(missing_fields)
            else:
                response = self._update_sudoku_puzzle(request["authentication_token"], request["numbers"])
        
        elif request["request_type"] == "buy_hint":
            missing_fields = self._get_missing_fields(request, ["authentication_token"])
            if len(missing_fields) > 0:
                response = self._create_missing_field_response(missing_fields)
            else:
                response = self._buy_hint(request["authentication_token"])

        else :
            error_message = f"Unsupported Request Type ({request['request_type']})"
            response = {"success_code": 11, "error_message": error_message}
        return response

class Server:
    """
    The server for Habit Mode.
    Maintains and modifies user information.

    @author Team 1
    @version Spring 2022
    """
    def run(self, socket_info: Tuple[str, int], service_manager: ServiceManager, 
            authentication_manager: AuthenticationManager, context: zmq.Context = zmq.Context()) -> None:
        """
        Launches the server with a specified ServiceManager.
        The server will run indefinitely.

        Precondition:  isinstance(socket_info, tuple) and
                       len(socket_info) == 2 and
                       isinstance(socket_info[0], str) and
                       isinstance(socket_info[1], int) and
                       isinstance(service_manager, ServiceManager) and
                       isinstance(authentication_manager, AuthenticationManager) and
                       isinstance(context, zmq.Context)
        Postcondition: The server becomes active.

        Params:
            socket_info - A tuple of the form (str, int) containing the hostname and port number
                            of the server.
            service_manager - The ServiceManager to use for the server.
            authentication_manager - The AuthenticationManager to use for the server.
            context - The context to use for the server.
        """
        if not isinstance(socket_info, tuple):
            raise Exception("socket_info must be a tuple")
        if len(socket_info) != 2:
            raise Exception("socket_info must be a tuple of length 2")
        if not isinstance(socket_info[0], str):
            raise Exception("socket_info[0] must be a string")
        if not isinstance(socket_info[1], int):
            raise Exception("socket_info[1] must be an integer")
        if not isinstance(service_manager, ServiceManager):
            raise Exception("service_manager must be an instance of ServiceManager.")
        if not isinstance(authentication_manager, AuthenticationManager):
            raise Exception("authentication_manager must be an instance of AuthenticationManager.")
        if not isinstance(context, zmq.Context):
            raise Exception("context must be an instance of zmq.Context.")

        request_handler = _RequestHandler(service_manager, authentication_manager)
        socket = context.socket(zmq.REP)
        socket.bind(f"tcp://{socket_info[0]}:{socket_info[1]}")

        while True:
            #  Wait for next request from client
            print("waiting for message...")
            json_request = socket.recv_string()
            request = json.loads(json_request)
            json_response: str
            print(f"Received request: {request}")
            if request == "exit":
                print("Server closing...")
                socket.close()
                return
            try:
                response = request_handler.handle_request(request)
            except:
                print(f"{'-' * 15}\nException was thrown. Please check the request.\n{'-' * 15}")
                print(request)
                response = {
                    "success_code": 15,
                    "error_message": "Unknown error (Exception thrown)"
                }
            json_response = json.dumps(response)

            #  Send reply back to client
            socket.send_string(json_response)
