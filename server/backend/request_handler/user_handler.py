from typing import Any, List, MutableMapping, Optional
from backend.authentication_manager import AuthenticationManager
from backend.service_manager import ServiceManager
from backend.user_data import UserData

def retrieve_data(service_manager: ServiceManager, authentication_manager: AuthenticationManager,
            token: str, fields: List[str]) -> MutableMapping[str, Any]:
    """
    Attempts to retrieve a set of data for a user using their authentication token.

    Precondition:   isinstance(service_manager, ServiceManager) and
                    isinstance(authentication_manager, AuthenticationManager) and
                    token is not None and
                    isinstance(token, str) and
                    fields is not None and
                    isinstance(fields, list)
    Postcondition: None

    Params - token: The specified authentication token.
                fields: The requested data fields
    Return - The response to the client.
    """
    if not isinstance(service_manager, ServiceManager):
        raise TypeError("service_manager must be a ServiceManager")
    if not isinstance(authentication_manager, AuthenticationManager):
        raise TypeError("authentication_manager must be an AuthenticationManager")
    if token is None:
        raise TypeError("token must not be None")
    if not isinstance(token, str):
        raise TypeError("token must be a str")
    if fields is None:
        raise TypeError("fields must not be None")
    if not isinstance(fields, list):
        raise TypeError("fields must be a list of str")
    
    username: str = authentication_manager.get_username_for_token(token)
    if username is None:
        return {
            "success_code": 14,
            "error_message": f"Invalid authentication token"
        }
    
    user_data: Optional[UserData] = service_manager.get_data_for_user(username)
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