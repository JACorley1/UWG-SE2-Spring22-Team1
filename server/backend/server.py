import json
from typing import Any, List, MutableMapping, Optional, Tuple
from backend.user_data import UserData
from backend.authentication_manager import AuthenticationManager
from backend.service_manager import ServiceManager
from backend.sudoku_puzzle import SudokuPuzzle, PUZZLE_SIZE, HINT_COST
import backend.sudoku_generator
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

    def _register_user(self, username: str, password: str, email: str) -> MutableMapping[str, Any]:
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
                "success_code": 20,
                "error_message": f"Username ({username}) already exists"
            }
        elif success_code == 21:
            response = {
                "success_code": 21,
                "error_message": f"Username ({username}) is invalid"
            }
        elif success_code == 22:
            response = {
                "success_code": 22,
                "error_message": "Password is invalid"
            }
        elif success_code == 23:
            response = {
                "success_code": 23,
                "error_message": f"Email ({email}) is invalid"
            }
        else:
            response = {
                "success_code": 0
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

    def _retrieve_data(self, token: str, fields: List[str]) -> MutableMapping[str, Any]:
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
        
        user_data: Optional[UserData] = self._service_manager.get_data_for_user(username)
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
                if user_data.sudoku_puzzle is None:
                    message["sudoku_puzzle"] = None
                else:
                    message["sudoku_puzzle"] = {
                        "numbers": user_data.sudoku_puzzle.numbers,
                        "number_locks": user_data.sudoku_puzzle.number_locks,
                    }
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

    def _complete_habits(self, token: str, habit_ids: List[int]) -> MutableMapping[str, Any]:
        """
        Marks a habit as completed.

        Precondition:  isinstance(token, str) and
                       isinstance(habit_id, list)
        Postcondition: None

        Params - token: The specified authentication token.
                 habit_ids: The ids of the habit to mark as completed.
        Return - The response to the client.
        """
        if not isinstance(token, str):
            raise Exception("token must be a str")
        if not isinstance(habit_ids, list):
            raise Exception("habit_ids must be a list")
        
        username: str = self._authentication_manager.get_username_for_token(token)
        if username is None:
            return {
                "success_code": 14,
                "error_message": f"Invalid authentication token"
            }

        user_data: Any = self._service_manager.get_data_for_user(username)

        unknown_habits: List[str] = list(
            map(str, filter(lambda habit_id: habit_id not in user_data.habits, habit_ids))
        )
        if len(unknown_habits) > 0:
            return {
                "success_code": 52,
                "error_message": f"No habit with id ({', '.join(unknown_habits)})"
            }

        incomplete_habits: List[int] = list(
            filter(lambda habit_id: habit_id in user_data.get_incomplete_habit_ids(), habit_ids)
        )
        already_completed_habits: List[int] = list(
            filter(lambda habit_id: not habit_id in incomplete_habits, habit_ids)
        )

        for habit_id in incomplete_habits:
            self._service_manager.complete_habit(username, habit_id)

        return {
            "success_code": 0,
            "already_completed": already_completed_habits,
            "coins": user_data.coins
        }

    def _generate_sudoku_puzzle(self, token: str) -> MutableMapping[str, Any]:
        """
        Generates a sudoku puzzle.

        Precondition:  isinstance(token, str)
        Postcondition: None

        Params - token: The specified authentication token.
        Return - The response to the client.
        """
        if not isinstance(token, str):
            raise TypeError("token must be a str")
        
        username: str = self._authentication_manager.get_username_for_token(token)
        if username is None:
            return {
                "success_code": 14,
                "error_message": f"Invalid authentication token"
            }

        user_data: Optional[UserData] = self._service_manager.get_data_for_user(username)

        if user_data is None:
            return {
                "success_code": 14,
                "error_message": f"Invalid authentication token"
            }

        sudoku_puzzle: SudokuPuzzle = backend.sudoku_generator.generate_sudoku_puzzle()
        user_data.sudoku_puzzle = sudoku_puzzle

        return {
            "success_code": 0,
            "sudoku_puzzle": {
                "numbers": user_data.sudoku_puzzle.numbers,
                "number_locks": user_data.sudoku_puzzle.number_locks,
            }
        }

    def _update_sudoku_puzzle(self, token: str, numbers: List[List[int]]):
        """
        Updates the sudoku puzzle.

        Precondition:  isinstance(token, str) and
                       isinstance(numbers, list)
        Postcondition: None

        Params - token: The specified authentication token.
                 numbers: The numbers to update the puzzle with.
        Return - The response to the client.
        """
        if not isinstance(token, str):
            raise Exception("token must be a str")
        if not isinstance(numbers, list):
            raise Exception("numbers must be a list")
        
        username: str = self._authentication_manager.get_username_for_token(token)
        if username is None:
            return {
                "success_code": 14,
                "error_message": "Invalid authentication token"
            }

        if len(numbers) != PUZZLE_SIZE:
            return {
                "success_code": 64,
                "error_message": "Invalid puzzle size"
            }
        for num_row in numbers:
            if len(num_row) != PUZZLE_SIZE:
                return {
                    "success_code": 64,
                    "error_message": "Invalid puzzle size"
                }

        user_data: Optional[UserData] = self._service_manager.get_data_for_user(username)

        if user_data is None:
            return {
                "success_code": 14,
                "error_message": "Invalid authentication token"
            }

        if user_data.sudoku_puzzle is None:
            return {
                "success_code": 61,
                "error_message": "No puzzle in progress"
            }

        puzzle: SudokuPuzzle = user_data.sudoku_puzzle

        coords = [(row, col) for row in range(PUZZLE_SIZE) for col in range(PUZZLE_SIZE)]

        for row, col in coords:
            cur_number = numbers[row][col]
            cur_colution = puzzle.solution[row][col]
            if cur_number not in range(PUZZLE_SIZE + 1):
                return {
                    "success_code": 60,
                    "error_message": f"Invalid number ({row}, {col})"
                }
            if puzzle.is_number_locked_at(row, col) and cur_number != cur_colution:
                    return {
                        "success_code": 62,
                        "error_message": f"Can't change locked number ({row}, {col})"
                    }
        
        for row, col in coords:
            puzzle.set_number_at(row, col, numbers[row][col])
        
        return {
            "success_code": 0,
        }

    def _buy_hint(self, token: str) -> MutableMapping[str, Any]:
        """
        Buys a hint.

        Precondition:  isinstance(token, str)
        Postcondition: None

        Params - token: The specified authentication token.
        Return - The response to the client.
        """
        if not isinstance(token, str):
            raise Exception("token must be a str")
        
        username: str = self._authentication_manager.get_username_for_token(token)
        if username is None:
            return {
                "success_code": 14,
                "error_message": f"Invalid authentication token"
            }

        user_data: Optional[UserData] = self._service_manager.get_data_for_user(username)

        if user_data is None:
            return {
                "success_code": 14,
                "error_message": f"Invalid authentication token"
            }

        if user_data.coins < HINT_COST:
            return {
                "success_code": 70,
                "error_message": f"Not enough coins (have {user_data.coins}, need {HINT_COST})"
            }

        sudoku_puzzle: Optional[SudokuPuzzle] = user_data.sudoku_puzzle

        if sudoku_puzzle is None:
            return {
                "success_code": 61,
                "error_message": f"No puzzle in progress"
            }
        
        hint_coords: Optional[Tuple[int, int]] = sudoku_puzzle.unlock_random_hint()
        if hint_coords is None:
            return {
                "success_code": 63,
                "error_message": "No valid cells for hint"
            }
        row: int = hint_coords[0]
        col: int = hint_coords[1]

        user_data.coins -= HINT_COST
        return {
            "success_code": 0,
            "number": sudoku_puzzle.get_number_at(row, col),
            "row": row,
            "col": col,
            "coins": user_data.coins,
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

        elif request["request_type"] == "complete_habits":
            missing_fields = self._get_missing_fields(request, ["authentication_token", "habit_ids"])
            if len(missing_fields) > 0:
                response = {
                    "success_code": 12,
                    "error_message": f"Malformed Request, missing Request Fields ({', '.join(missing_fields)})"
                }
            else:
                response = self._complete_habits(request["authentication_token"], request["habit_ids"])

        elif request["request_type"] == "generate_sudoku_puzzle":
            missing_fields = self._get_missing_fields(request, ["authentication_token"])
            if len(missing_fields) > 0:
                response = {
                    "success_code": 12,
                    "error_message": f"Malformed Request, missing Request Fields ({', '.join(missing_fields)})"
                }
            else:
                response = self._generate_sudoku_puzzle(request["authentication_token"])

        elif request["request_type"] == "update_sudoku_puzzle":
            missing_fields = self._get_missing_fields(request, ["authentication_token", "numbers"])
            if len(missing_fields) > 0:
                response = {
                    "success_code": 12,
                    "error_message": f"Malformed Request, missing Request Fields ({', '.join(missing_fields)})"
                }
            else:
                response = self._update_sudoku_puzzle(request["authentication_token"], request["numbers"])
        
        elif request["request_type"] == "buy_hint":
            missing_fields = self._get_missing_fields(request, ["authentication_token"])
            if len(missing_fields) > 0:
                response = {
                    "success_code": 12,
                    "error_message": f"Malformed Request, missing Request Fields ({', '.join(missing_fields)})"
                }
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
