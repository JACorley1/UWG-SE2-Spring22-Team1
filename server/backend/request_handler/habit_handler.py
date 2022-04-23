from typing import Any, List, MutableMapping
from backend.authentication_manager import AuthenticationManager
from backend.service_manager import ServiceManager

def add_habit(service_manager: ServiceManager, authentication_manager: AuthenticationManager, 
            token: str, habit_name: str, habit_frequency: int) -> MutableMapping[str, Any]:
    """
    Attempts to add a new habit to a user's list of habits.

    Precondition: isinstance(service_manager, ServiceManager) and
                  isinstance(authentication_manager, AuthenticationManager) and
                  isinstance(token, str) and
                  isinstance(habit_name, str) and
                  isinstance(habit_frequency, int) 
    Postcondition: None

    Params - token: The specified authentication token.
                habit_name: The name of the new habit.
                habit_frequency: How frequently the habit needs to be completed.
    Return - The response to the client.
    """
    if not isinstance(service_manager, ServiceManager):
        raise Exception("service_manager must be a ServiceManager")
    if not isinstance(authentication_manager, AuthenticationManager):
        raise Exception("authentication_manager must be an AuthenticationManager")
    if not isinstance(token, str):
        raise Exception("token must be a str")
    if not isinstance(habit_name, str):
        raise Exception("habit_name must be a str")
    if not isinstance(habit_frequency, int):
        raise Exception("habit_frequency must be an int")
    
    username: str = authentication_manager.get_username_for_token(token)
    if username is None:
        return {
            "success_code": 14,
            "error_message": f"Invalid authentication token"
        }

    success_code = service_manager.add_habit(username, habit_name, habit_frequency)
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

def remove_habit(service_manager: ServiceManager, authentication_manager: AuthenticationManager,
            token: str, habit_id: int) -> MutableMapping[str, Any]:
    """
    Removes a habit with the specified ID from a user's habit list.

    Precondition: isinstance(service_manager, ServiceManager) and
                  isinstance(authentication_manager, AuthenticationManager) and
                  isinstance(token, str) and
                  isinstance(habit_id, int)
    Postcondition: The specified doesn't have a habit with the matching id.

    Params - token: The user's authentication token.
                habit_id: The ID for the habit to remove.
    Return - The response to the client.
    """
    if not isinstance(service_manager, ServiceManager):
        raise Exception("service_manager must be a ServiceManager")
    if not isinstance(authentication_manager, AuthenticationManager):
        raise Exception("authentication_manager must be an AuthenticationManager")
    if not isinstance(token, str):
        raise Exception("token must be a str")
    if not isinstance(habit_id, int):
        raise Exception("habit_id must be an int")
    
    username: str = authentication_manager.get_username_for_token(token)
    if username is None:
        return {
            "success_code": 14,
            "error_message": f"Invalid authentication token"
        }

    success_code = service_manager.remove_habit(username, habit_id)
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

def modify_habit(service_manager: ServiceManager, authentication_manager: AuthenticationManager,
            token: str, habit_id: int, habit_name: str, habit_frequency: int) -> MutableMapping[str, Any]:
    """
    Modifies an existing habit's name and frequency.

    Precondition: isinstance(service_manager, ServiceManager) and
                  isinstance(authentication_manager, AuthenticationManager) and
                  isinstance(token, str) and
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
    if not isinstance(service_manager, ServiceManager):
        raise Exception("service_manager must be a ServiceManager")
    if not isinstance(authentication_manager, AuthenticationManager):
        raise Exception("authentication_manager must be an AuthenticationManager")
    if not isinstance(token, str):
        raise Exception("token must be a str")
    if not isinstance(habit_id, int):
        raise Exception("habit_id must be an int")
    if not isinstance(habit_name, str):
        raise Exception("habit_name must be a str")
    if not isinstance(habit_frequency, int):
        raise Exception("habit_frequency must be an int")
    
    username: str = authentication_manager.get_username_for_token(token)
    if username is None:
        return {
            "success_code": 14,
            "error_message": f"Invalid authentication token"
        }

    success_code = service_manager.modify_habit(username, habit_id, habit_name, habit_frequency)
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

def complete_habits(service_manager: ServiceManager, authentication_manager: AuthenticationManager,
            token: str, habit_ids: List[int]) -> MutableMapping[str, Any]:
    """
    Marks a habit as completed.

    Precondition: isinstance(service_manager, ServiceManager) and
                  isinstance(authentication_manager, AuthenticationManager) and
                  isinstance(token, str) and
                  isinstance(habit_id, list)
    Postcondition: None

    Params - token: The specified authentication token.
                habit_ids: The ids of the habit to mark as completed.
    Return - The response to the client.
    """
    if not isinstance(service_manager, ServiceManager):
        raise Exception("service_manager must be a ServiceManager")
    if not isinstance(authentication_manager, AuthenticationManager):
        raise Exception("authentication_manager must be an AuthenticationManager")        
    if not isinstance(token, str):
        raise Exception("token must be a str")
    if not isinstance(habit_ids, list):
        raise Exception("habit_ids must be a list")
    
    username: str = authentication_manager.get_username_for_token(token)
    if username is None:
        return {
            "success_code": 14,
            "error_message": f"Invalid authentication token"
        }

    user_data: Any = service_manager.get_data_for_user(username)

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
        service_manager.complete_habit(username, habit_id)

    return {
        "success_code": 0,
        "already_completed": already_completed_habits,
        "coins": user_data.coins
    }
