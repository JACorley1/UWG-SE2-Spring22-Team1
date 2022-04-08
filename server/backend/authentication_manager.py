from typing import Any, MutableMapping
import string
import random

_TOKEN_LENGTH = 20

class AuthenticationManager:
    """
    Keeps track of which usernames are associated with which authentication tokens.
    
    @author Team 1
    @version Spring 2022
    """
    _tokens_to_usernames: MutableMapping
    _usernames_to_tokens: MutableMapping

    def __init__(self):
        self._tokens_to_usernames = {}
        self._usernames_to_tokens = {}
    
    def get_username_for_token(self, token: str) -> Any:
        """
        Gets the username associated with a token. If the token is invalid, or if no
        username is associated with the token, None will be returned.

        Precondition:  None
        Postcondition: None

        Params - token: The specified token.
        Return - The username associated with the token if one exists, otherwise None.
        """
        if token in self._tokens_to_usernames:
            return self._tokens_to_usernames[token]
        return None

    def get_token_for_username(self, username: str) -> Any:
        """
        Gets the token associated with a username. If the username is invalid, or if no
        token is associated with the username, None will be returned.

        Precondition:  None
        Postcondition: None

        Params - username: The specified username.
        Return - The token associated with the username if one exists, otherwise None.
        """
        if username in self._usernames_to_tokens:
            return self._usernames_to_tokens[username]
        return None
    
    def generate_and_store_key_for_username(self, username) -> str:
        """
        Generates a new token for a username, stores the association internally,
        and returns the new token.

        Precondition:  username is not None and
                       isinstance(username, str)
        Postcondition: self.get_token_for_username(username) == <return> and
                       self.get_username_for_token(<return>) == username

        Params - username: The specified username.
        Return - A newly gerneated token associated with the username.
        """
        if username is None:
            raise Exception("username must not be None")
        if not isinstance(username, str):
            raise Exception("username must not be a str")

        token = generate_token()

        while token in self._tokens_to_usernames:
            token = generate_token()

        self._usernames_to_tokens[username] = token
        self._tokens_to_usernames[token] = username

        return token

def generate_token():
    """
    Generates a random string of characters containing uppercase letters, lowercase
    letters, and numbers.

    Precondition:  None
    Postcondition: None

    Params - None
    Return - A random string of uppercase letters, lowercase letters, and numbers.
    """
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(_TOKEN_LENGTH))