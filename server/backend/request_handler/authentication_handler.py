from typing import Any, MutableMapping
from backend.service_manager import ServiceManager
from backend.authentication_manager import AuthenticationManager

def register_user(service_manager: ServiceManager, username: str, password: str, 
            email: str) -> MutableMapping[str, Any]:
    """
    Attempts to add a new user to the server using the specified username, password, and email.
    Generates and returns a response to be sent back to the client.

    Precondition:  isinstance(service_manager, ServiceManager)
    Postcondition: None

    Params - username: The specified username.
                password: The specified password.
                email: The specified email address.
    Return - The response to the client.
    """
    if not isinstance(service_manager, ServiceManager):
        raise Exception("service_manager must be an instance of ServiceManager")

    success_code: int = service_manager.create_user(username, password, email)
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

def login(service_manager: ServiceManager, authentication_manager: AuthenticationManager, 
            username: str, password: str) -> MutableMapping[str, Any]:
    """
    Validates a specified username-password combination and sends an authentication token
    back to the client if successful.

    Precondition: isinstance(service_manager, ServiceManager) and
                  isinstance(authentication_manager, AuthenticationManager) and
                  isinstance(username, str) and
                  isinstance(password, str)
    Postcondition: None

    Params - username: The specified username.
                password: The specified password.
    Return - The response to the client.
    """
    if not isinstance(service_manager, ServiceManager):
        raise Exception("service_manager must be an instance of ServiceManager")
    if not isinstance(authentication_manager, AuthenticationManager):
        raise Exception("authentication_manager must be an instance of AuthenticationManager")
    if not isinstance(username, str):
        raise Exception("username must be a str")
    if not isinstance(password, str):
        raise Exception("password must be a str")
    
    user_data = service_manager.get_data_for_user(username)
    if user_data is None or user_data.password != password:
        return {
            "success_code": 30,
            "error_message": "Invalid username or password"
        }

    token = authentication_manager.get_token_for_username(username)
    if token is None:
        token = authentication_manager.generate_and_store_key_for_username(username)
    
    return {
        "success_code": 0,
        "authentication_token": token,
    }
