from typing import Callable, MutableMapping, Optional
from datetime import datetime
from backend.habit import Habit, CompletionFrequency
from backend.sudoku_puzzle import SudokuPuzzle
import backend.datetime_extension

_BONUS_RESET_FUNCTIONS: MutableMapping[int, Callable] = {
    CompletionFrequency.DAILY.value: backend.datetime_extension.tomorrow,
    CompletionFrequency.WEEKLY.value: backend.datetime_extension.next_sunday,
    CompletionFrequency.MONTHLY.value: backend.datetime_extension.first_of_next_month,
}

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
    _sudoku_puzzle: Optional[SudokuPuzzle]
    _next_habit_id: int
    _habits: MutableMapping[int, Habit]
    _bonus_reset_dates: MutableMapping[int, datetime]

    def __init__(self, username: str, password: str, email: str):
        """
        Creates a new user with the specified username, password, and email.

        Precondition:  isinstance(username, str) and
                       isinstance(password, str) and
                       isinstance(email, str)
        Postcondition:
        """
        EPOCH_TIME = 30256871

        self.username = username
        self.password = password
        self.email = email
        self.coins = 0
        self.sudoku_puzzle = None
        self._next_habit_id = 0
        self._habits = {}
        self._bonus_reset_dates = {
            CompletionFrequency.DAILY.value: datetime.fromtimestamp(EPOCH_TIME),
            CompletionFrequency.WEEKLY.value: datetime.fromtimestamp(EPOCH_TIME),
            CompletionFrequency.MONTHLY.value: datetime.fromtimestamp(EPOCH_TIME),
        }

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

        self._habits[new_habit.id] = new_habit

    def remove_habit(self, habit_id: int) -> bool:
        """
        Attempts to remove a habit with the specified id and will return whether or not the
        operation was successful.

        Precondition:  None
        Postcondition: habit with id == habit_id not in self.habits

        Params - habit_id: The id for the habit.
        Return - Whether the habit was removed.
        """
        if habit_id in self._habits:
            self._habits.pop(habit_id)
            return True
        return False

    def complete_habit(self, habit_id: int) -> bool:
        """
        Attempts to complete a habit with the specified id and will return whether or not the
        operation was successful. If the habit is complete, coins will be awarded based on whether
        all habits for the habit's frequency are complete.

        Precondition:  None
        Postcondition: self.get_habit[habit_id].is_complete and
                       self.coins == self.coins@prev + 70 if bonus is earned else
                       self.coins == self.coins@prev + 20 if no bonus is earned else
                       self.coins == self.coins@prev if habit was already complete

        Params - habit_id: The id for the habit.
        Return - Whether the habit was completed.
        """
        if habit_id not in self._habits or self._habits[habit_id].is_complete:
            return False
        
        habit: Habit = self._habits[habit_id]
        habit.complete()
        self.coins += 20

        incomplete_habits: list[Habit] = list(
            filter(
                lambda item: not item.is_complete and item.frequency == habit.frequency, 
                self._habits.values()
            )
        )

        if len(incomplete_habits) == 0 and datetime.now() > self._bonus_reset_dates[habit.frequency]:
            self._bonus_reset_dates[habit.frequency] = _BONUS_RESET_FUNCTIONS[habit.frequency]()
            self.coins += 50

        return True

    def contains_habit_id(self, habit_id: int) -> bool:
        """
        Determines whether the user contains a habit with the specified id.

        Precondition:  None
        Postcondition: None

        Params - habit_id: The id for the habit.
        Return - [True] iff the user contains a habit with the specified id, otherwise [False].
        """
        return habit_id in self._habits

    def get_habit(self, habit_id: int) -> Optional[Habit]:
        """
        Gets the first instance of a habit from the habit list with the specified id.

        Precondition:  None
        Postcondition: None

        Params - habit_id: The id for the habit.
        Return - The first habit with the specified id if it exists, otherwise None.
        """
        if habit_id in self._habits:
            return self._habits[habit_id]
        return None

    def get_incomplete_habit_ids(self):
        """
        Gets a list of all incomplete habit ids.

        Precondition:  None
        Postcondition: None

        Params - None
        Return - A list of all incomplete habit ids.
        """
        incomplete_habits = filter(lambda habit: not habit.is_complete, self._habits.values())
        habit_ids = list(map(lambda habit: habit.id, incomplete_habits))
        return habit_ids

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
    def sudoku_puzzle(self) ->  Optional[SudokuPuzzle]:
        """
        Gets the user's current sudoku puzzle.

        Precondition:  None
        Postcondition: None

        Return - The user's current sudoku puzzle.
        """
        return self._sudoku_puzzle

    @sudoku_puzzle.setter
    def sudoku_puzzle(self, sudoku_puzzle:  Optional[SudokuPuzzle]):
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
    def habits(self) -> MutableMapping[int, Habit]:
        """
        Gets the user's list of habits.

        Precondition:  None
        Postcondition: None

        Params - None
        Return - A list of the user's habits.
        """
        return self._habits
