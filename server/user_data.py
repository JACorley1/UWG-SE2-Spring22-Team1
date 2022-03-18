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

    def add_habit(self, habit_name: str, habit_frequency: int):
        """
        Adds a habit with a specified name and frequency to the user's list of habits.

        Precondition:  isinstance(habit_name, str) and
                       not str.isspace(habit_name) and
                       isinstance(habit_frequency, int) and
                       habit_frequency >= 0 and
                       habit_frequency <= 2
        Postcondition: len(self.habits) == len(self.habits) + 1
        """
        new_habit = Habit(habit_name, habit_frequency, self.next_habit_id)
        self.increment_habit_id()

        self._habits.append(new_habit)

    def remove_habit(self, habit_id: int) -> bool:
        """
        Attempts to remove a habit with the specified id and will return whether or not the
        operation was successful.

        Precondition:  None
        Postcondition: habit with id == habit_id not in self.habits

        Params - habit_id: The id for the habit.
        Return - Whether the habit was removed.
        """
        for habit in self._habits:
            if habit.id == habit_id:
                self._habits.remove(habit)
                return True
        return False

    def get_habit(self, habit_id: int) -> Habit:
        """
        Gets the first instance of a habit from the habit list with the specified id.

        Precondition:  None
        Postcondition: None

        Params - habit_id: The id for the habit.
        Return - The first habit with the specified id if exists, otherwise None.
        """
        for habit in self._habits:
            if habit.id == habit_id:
                return habit
        return False

    @property
    def username(self) -> str:
        """
        Gets the user's username.

        Precondition:  None
        Postcondition: None

        Return - The user's username.
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """
        Sets the user's username.

        Precondition:  isinstance(username, str)
        Postcondition: self.username == username
        """
        if not isinstance(username, str):
            raise Exception("username must be a string")
        self._username = username

    @property
    def password(self) -> str:
        """
        Gets the user's password.

        Precondition:  None
        Postcondition: None

        Return - The user's password.
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """
        Sets the user's password.

        Precondition:  isinstance(password, str)
        Postcondition: self.password == password
        """
        if not isinstance(password, str):
            raise Exception("password must be a string")
        self._password = password

    @property
    def email(self) -> str:
        """
        Gets the user's email address.

        Precondition:  None
        Postcondition: None

        Return - The user's email address.
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """
        Sets the user's email address.

        Precondition:  isinstance(email, str)
        Postcondition: self.email == email
        """
        if not isinstance(email, str):
            raise Exception("email must be a string")
        self._email = email

    @property
    def coins(self) -> int:
        """
        Gets the user's coin count.

        Precondition:  None
        Postcondition: None

        Return - The user's coin count.
        """
        return self._coins

    @coins.setter
    def coins(self, coins: int):
        """
        Sets the user's coins.

        Precondition:  isinstance(coins, int)
        Postcondition: self.coins == coins
        """
        if not isinstance(coins, int):
            raise Exception("coins must be an int")
        self._coins = coins

    @property
    def sudoku_puzzle(self) -> SudokuPuzzle:
        """
        Gets the user's current sudoku puzzle.

        Precondition:  None
        Postcondition: None

        Return - The user's current sudoku puzzle.
        """
        return self._sudoku_puzzle

    @sudoku_puzzle.setter
    def sudoku_puzzle(self, sudoku_puzzle: SudokuPuzzle):
        """
        Sets the user's current sudoku puzzle.

        Precondition:  sudoku_puzzle is None or
                       isinstance(sudoku_puzzle, SudokuPuzzle)
        Postcondition: self.sudoku_puzzle == sudoku_puzzle
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
