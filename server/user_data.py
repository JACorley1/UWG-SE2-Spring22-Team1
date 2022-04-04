from server.habit import Habit
from server.sudoku_puzzle import SudokuPuzzle

class UserData:
    """
    Stores information about a user.

    @author Team 1
    @version Spring 2022
    """
    _username: str
    _password: str
    _email: str
    _coins: int
    _sudoku_puzzle: SudokuPuzzle
    _next_habit_id: int
    _habits: list[Habit]

    def __init__(self, username: str, password: str, email: str):
        """
        Creates a new user with the specified username, password, and email.

        Precondition:  isinstance(username, str) and
                       isinstance(password, str) and
                       isinstance(email, str)
        Postcondition:
        """
        self.username = username
        self.password = password
        self.email = email
        self.coins = 0
        self.sudoku_puzzle = None
        self._next_habit_id = 0
        self._habits = []

    def increment_habit_id(self):
        """
        Increments the next valid habit id by one.

        Precondition:  None
        Postcondition: self.next_habit_id == self.next_habit_id@prev

        Params - None
        Return - None
        """
        self._next_habit_id += 1


    def get_username(self) -> str:
        """
        Gets the user's username.

        Precondition:  None
        Postcondition: None

        Return - The user's username.
        """
        return self._username

    def set_username(self, username: str):
        """
        Sets the user's username.

        Precondition:  isinstance(username, str)
        Postcondition: self.get_username() == username
        """
        if not isinstance(username, str):
            raise Exception("username must be a string")
        self._username = username

    def get_password(self) -> str:
        """
        Gets the user's password.

        Precondition:  None
        Postcondition: None

        Return - The user's password.
        """
        return self._password

    def set_password(self, password: str):
        """
        Sets the user's password.

        Precondition:  isinstance(password, str)
        Postcondition: self.get_password() == password
        """
        if not isinstance(password, str):
            raise Exception("password must be a string")
        self._password = password

    def get_email(self) -> str:
        """
        Gets the user's email address.

        Precondition:  None
        Postcondition: None

        Return - The user's email address.
        """
        return self._email

    def set_email(self, email: str):
        """
        Sets the user's email address.

        Precondition:  isinstance(email, str)
        Postcondition: self.get_email() == email
        """
        if not isinstance(email, str):
            raise Exception("email must be a string")
        self._email = email

    def get_coins(self) -> int:
        """
        Gets the user's coin count.

        Precondition:  None
        Postcondition: None

        Return - The user's coin count.
        """
        return self._coins

    def set_coins(self, coins: int):
        """
        Sets the user's coins.

        Precondition:  isinstance(coins, int)
        Postcondition: self.get_coins() == coins
        """
        if not isinstance(coins, int):
            raise Exception("coins must be an int")
        self._coins = coins

    def get_sudoku_puzzle(self) -> SudokuPuzzle:
        """
        Gets the user's current sudoku puzzle.

        Precondition:  None
        Postcondition: None

        Return - The user's current sudoku puzzle.
        """
        return self._sudoku_puzzle

    def set_sudoku_puzzle(self, sudoku_puzzle: SudokuPuzzle):
        """
        Sets the user's current sudoku puzzle.

        Precondition:  sudoku_puzzle is None or
                       isinstance(sudoku_puzzle, SudokuPuzzle)
        Postcondition: self.get_sudoku_puzzle() == sudoku_puzzle
        """
        if sudoku_puzzle is not None and not isinstance(sudoku_puzzle, str):
            raise Exception("sudoku_puzzle must be a SudokuPuzzle")
        self._sudoku_puzzle = sudoku_puzzle

    @property
    def next_habit_id(self) -> int:
        """
        Gets the next valid id for habits for this user.

        Precondition:  None
        Postcondition: None

        Params - None
        Return - The next valid habit id.
        """
        return self._next_habit_id

    @property
    def habits(self) -> list[Habit]:
        """
        Gets the user's list of habits.

        Precondition:  None
        Postcondition: None

        Params - None
        Return - A list of the user's habits.
        """
        return self._habits
