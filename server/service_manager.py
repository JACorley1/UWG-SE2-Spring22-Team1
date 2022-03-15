from typing import MutableMapping
from user_data import UserData

class ServiceManager:
    """
    Manages information for all users in a system.

    @author Team 1
    @version Spring 2022
    """
    _user_information: MutableMapping[str, UserData]

    def __init__(self):
        """
        Creates an instance of Service Manager.

        Precondition:  None
        Postcondition: None
        """
        self._user_information = {}

    def create_user(self, username: str, password: str, email: str) -> int:
        """
        Attempts to create a new user with the specified credentials. Returns the success
        code to be sent to the client.

        Precondition:  None
        Postcondition: A new user with the specified username is created if all credentials are
                       valid and the username is not is use, otherwise none.

        Params - username: The specified username.
                 password: The specified password.
                 email: The specified email address.
        Return - The success code to be sent back to the user.
        """
        if username in self._user_information:
            return 20
        if not _validate_username(username):
            return 21
        if not _validate_password(password):
            return 22
        if not _validate_email(email):
            return 23

        new_user: UserData = UserData(username, password, email)
        self._user_information[username] = new_user
        return 0

    def get_data_for_user(self, username: str) -> UserData:
        """
        Gets the user information for a specified username, if it has been registered.

        Precondition:  None
        Postcondition: None

        Params - username: The specified username.
        Return - The UserData associated with the name if it has been registered, otherwise None.
        """
        return self._user_information[username] if username in self._user_information else None

def _validate_username(username: str) -> bool:
    """
    Determines whether a username is valid or not.

    Precondition:  None
    Postcondition: None

    Params - username: The specified username.
    Return - [True] iff the username is valid, otherwise [False].
    """
    return isinstance(username, str) and len(username) > 0

def _validate_password(password: str) -> bool:
    """
    Determines whether a password is valid or not.

    Precondition:  None
    Postcondition: None

    Params - password: The specified password.
    Return - [True] iff the username is valid, otherwise [False].
    """
    return isinstance(password, str) and len(password) > 0

def _validate_email(email: str) -> bool:
    """
    Determines whether an email is valid or not.

    Precondition:  None
    Postcondition: None

    Params - username: The specified email.
    Return - [True] iff the email is valid, otherwise [False].
    """
    return isinstance(email, str) and len(email) > 0
