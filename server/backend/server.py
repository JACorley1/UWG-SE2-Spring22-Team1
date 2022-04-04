import json
from typing import Any, MutableMapping
from backend.user_data import UserData
from backend.authentication_manager import AuthenticationManager
from backend.service_manager import ServiceManager
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
                 authentication_manager: The specified AuthenticationManager
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

    def _login(self, username: str, password: str) -> MutableMapping[str, Any]:
        """
        Validates a specified username-password combination and sends an authentication token
        back to the client if successful.

        Precondition:  username is not None and
                       isinstance(username, str) and
                       password is not None and
                       isinstance(password, str)
        Postcondition: None

        Params - username: The specified username.
                 password: The specified password.
        Return - The response to the client.
        """
        if username is None:
            raise Exception("username must not be None")
        if not isinstance(username, str):
            raise Exception("username must be a str")
        if password is None:
            raise Exception("password must not be None")
        if not isinstance(password, str):
            raise Exception("password must be a str")
        
        user_data = self._service_manager.get_data_for_user(username)
        if user_data is None or user_data.password != password:
            return {
                "success_code": 30,
                "error_message": "Invalid username or password"
            }

        token = self._authentication_manager.get_token_for_username(username)
        if token is None:
            token = self._authentication_manager.generate_and_store_key_for_username(username)
        
        return {
            "success_code": 0,
            "authentication_token": token,
        }

    def _retrieve_data(self, token: str, fields: list[str]) -> MutableMapping[str, Any]:
        """
        Attempts to retrieve a set of data for a user using their authentication token.

        Precondition:  token is not None and
                       isinstance(token, str) and
                       fields is not None and
                       isinstance(fields, list)
        Postcondition: None

        Params - token: The specified authentication token.
                 fields: The requested data fields
        Return - The response to the client.
        """
        if token is None:
            raise Exception("token must not be None")
        if not isinstance(token, str):
            raise Exception("token must be a str")
        if fields is None:
            raise Exception("fields must not be None")
        if not isinstance(fields, list):
            raise Exception("fields must be a list of str")
        
        username: str = self._authentication_manager.get_username_for_token(token)
        if username is None:
            return {
                "success_code": 14,
                "error_message": f"Invalid authentication token"
            }
        
        user_data: UserData = self._service_manager.get_data_for_user(username)
        if user_data is None:
            return {
                "success_code": 14,
                "error_message": f"Invalid authentication token"
            }
        

        if len(fields) == 0:
            return {
                "success_code": 41,
                "error_message": f"No fields provided"
            }

        message: MutableMapping[str, Any] = {
            "success_code": 0
        }
        
        for field in fields:
            if field == "username":
                message["username"] = user_data.username
            elif field == "email":
                message["email"] = user_data.email
            elif field == "coins":
                message["coins"] = user_data.coins
            elif field == "sudoku_puzzle":
                message["sudoku_puzzle"] = user_data.sudoku_puzzle
            elif field == "habits":
                message["habits"] = list(map(lambda habit: habit.create_json_dict(), user_data.habits.values()))
            else:
                return {
                    "success_code": 40,
                    "error_message": f"Unknown field name ({field})"
                }

        return message

    def _add_habit(self, token: str, habit_name: str, habit_frequency: int) -> MutableMapping[str, Any]:
        """
        Attempts to add a new habit to a user's list of habits.

        Precondition:  isinstance(token, str) and
                       isinstance(habit_name, str) and
                       isinstance(habit_frequency, int) 
        Postcondition: None

        Params - token: The specified authentication token.
                 habit_name: The name of the new habit.
                 habit_frequency: How frequently the habit needs to be completed.
        Return - The response to the client.
        """
        if not isinstance(token, str):
            raise Exception("token must be a str")
        if not isinstance(habit_name, str):
            raise Exception("habit_name must be a str")
        if not isinstance(habit_frequency, int):
            raise Exception("habit_frequency must be an int")
        
        username: str = self._authentication_manager.get_username_for_token(token)
        if username is None:
            return {
                "success_code": 14,
                "error_message": f"Invalid authentication token"
            }

        success_code = self._service_manager.add_habit(username, habit_name, habit_frequency)
        if success_code == 14:
            return {
                "success_code": 14,
                "error_message": f"Invalid authentication token"
            }
        elif success_code == 50:
            return {
                "success_code": 50,
                "error_message": f"Invalid habit name ({habit_name})"
            }
        elif success_code == 51:
            return {
                "success_code": 51,
                "error_message": f"Invalid habit frequency ({habit_frequency})"
            }
        return {
            "success_code": 0
        }

    def _remove_habit(self, token: str, habit_id: int) -> MutableMapping[str, Any]:
        """
        Removes a habit with the specified ID from a user's habit list.

        Precondition:  isinstance(token, str) and
                       isinstance(habit_id, int)
        Postcondition: The specified doesn't have a habit with the matching id.

        Params - token: The user's authentication token.
                 habit_id: The ID for the habit to remove.
        Return - The response to the client.
        """
        if not isinstance(token, str):
            raise Exception("token must be a str")
        if not isinstance(habit_id, int):
            raise Exception("habit_id must be an int")
        
        username: str = self._authentication_manager.get_username_for_token(token)
        if username is None:
            return {
                "success_code": 14,
                "error_message": f"Invalid authentication token"
            }

        success_code = self._service_manager.remove_habit(username, habit_id)
        if success_code == 14:
            return {
                "success_code": 14,
                "error_message": f"Invalid authentication token"
            }
        elif success_code == 52:
            return {
                "success_code": 52,
                "error_message": f"No habit with id ({habit_id}))"
            }
        return {
            "success_code": 0
        }
    
    def _modify_habit(self, token: str, habit_id: int, habit_name: str, habit_frequency: int) -> MutableMapping[str, Any]:
        """
        Modifies an existing habit's name and frequency.

        Precondition:  isinstance(token, str) and
                       isinstance(habit_id, int) and
                       isinstance(habit_name, str) and
                       isinstance(habit_frequency, int)
        Postcondition: None

        Params - token: The specified authentication token.
                 habit_id: The id of the habit to modify.
                 habit_name: The name of the new habit.
                 habit_frequency: How frequently the habit needs to be completed.
        Return - The response to the client.
        """
        if not isinstance(token, str):
            raise Exception("token must be a str")
        if not isinstance(habit_id, int):
            raise Exception("habit_id must be an int")
        if not isinstance(habit_name, str):
            raise Exception("habit_name must be a str")
        if not isinstance(habit_frequency, int):
            raise Exception("habit_frequency must be an int")
        
        username: str = self._authentication_manager.get_username_for_token(token)
        if username is None:
            return {
                "success_code": 14,
                "error_message": f"Invalid authentication token"
            }

        success_code = self._service_manager.modify_habit(username, habit_id, habit_name, habit_frequency)
        if success_code == 14:
            return {
                "success_code": 14,
                "error_message": f"Invalid authentication token"
            }
        elif success_code == 50:
            return {
                "success_code": 50,
                "error_message": f"Invalid habit name ({habit_name})"
            }
        elif success_code == 51:
            return {
                "success_code": 51,
                "error_message": f"Invalid habit frequency ({habit_frequency})"
            }
        elif success_code == 52:
            return {
                "success_code": 52,
                "error_message": f"No habit with id ({habit_id})"
            }
        return {
            "success_code": 0
        }
        
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

        missing_fields: list[str]
        if request["request_type"] == "register_user" :
            missing_fields = self._get_missing_fields(request, ["username", "password", "email"])
            if len(missing_fields) > 0:
                response = {
                    "successCode": 12,
                    "error_message": f"Malformed Request, missing Request Fields ({', '.join(missing_fields)})"
                }
            else:
                response = self._register_user(request["username"], request["password"], request["email"])

        elif request["request_type"] == "login":
            missing_fields = self._get_missing_fields(request, ["username", "password"])
            if len(missing_fields) > 0:
                response = {
                    "success_code": 12,
                    "error_message": f"Malformed Request, missing Request Fields ({', '.join(missing_fields)})"
                }
            else:
                response = self._login(request["username"], request["password"])

        elif request["request_type"] == "retrieve_data":
            missing_fields = self._get_missing_fields(request, ["authentication_token", "fields"])
            if len(missing_fields) > 0:
                response = {
                    "success_code": 12,
                    "error_message": f"Malformed Request, missing Request Fields ({', '.join(missing_fields)})"
                }
            else:
                response = self._retrieve_data(request["authentication_token"], request["fields"])

        elif request["request_type"] == "add_habit":
            missing_fields = self._get_missing_fields(request, ["authentication_token", "habit_name", "habit_frequency"])
            if len(missing_fields) > 0:
                response = {
                    "success_code": 12,
                    "error_message": f"Malformed Request, missing Request Fields ({', '.join(missing_fields)})"
                }
            else:
                response = self._add_habit(request["authentication_token"], request["habit_name"], request["habit_frequency"])

        elif request["request_type"] == "remove_habit":
            missing_fields = self._get_missing_fields(request, ["authentication_token", "habit_id"])
            if len(missing_fields) > 0:
                response = {
                    "success_code": 12,
                    "error_message": f"Malformed Request, missing Request Fields ({', '.join(missing_fields)})"
                }
            else:
                response = self._remove_habit(request["authentication_token"], request["habit_id"])

        elif request["request_type"] == "modify_habit":
            missing_fields = self._get_missing_fields(request, ["authentication_token", "habit_id", "habit_name", "habit_frequency"])
            if len(missing_fields) > 0:
                response = {
                    "success_code": 12,
                    "error_message": f"Malformed Request, missing Request Fields ({', '.join(missing_fields)})"
                }
            else:
                response = self._modify_habit(request["authentication_token"], request["habit_id"], request["habit_name"], request["habit_frequency"])

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
            try:
                response = request_handler.handle_request(request)
            except:
                print("-" * 15)
                print("Exception was thrown. Please check the request.")
                print(request)
                print("-" * 15)
                response = {
                    "success_code": 15,
                    "error_message": "Unknown error (Exception thrown)"
                }
            json_response = json.dumps(response)

            #  Send reply back to client
            socket.send_string(json_response)
