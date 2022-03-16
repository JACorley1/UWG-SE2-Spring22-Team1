
from datetime import datetime, timedelta
from enum import Enum
from typing import MutableMapping

class Habit:
    """
    Stores information about a habit, including the name, how frequently it needs
    to be completed, whether it has been completed or not, and its unique id.

    @author Team 1
    @version Spring 2022
    """
    _name: str
    _id: int
    _reset_date: int
    _frequency: int

    def __init__(self, name: str, frequency: int, id: int):
        """
        Creates a new Habit object with a specified name, frequency, and id.

        Precondition:  isinstance(name, str) and
                       not str.isspace(name) and
                       isinstance(frequency, int) and
                       frequency >= 0 and
                       frequency <= 2 and
                       isinstance(id, int)
        Postcondition: self.name == name and
                       self.frequency == frequency and
                       self.id == id
        
        Params - name: The name of the Habit.
                 frequency: How frequently the habit should be completed.
                 id: The habit's unique identifier.
        Return - None
        """
        EPOCH_TIME = 30256871

        self.name = name
        self.frequency = frequency
        self._id = id
        self._reset_time = datetime.fromtimestamp(EPOCH_TIME)

    def complete(self) -> bool:
        """
        Completes the habit, returning whether the habit was already complete.

        Precondition:  None
        Postcondition: self.is_complete

        Params - None
        Return - [True] iff the habit was not already complete, otherwise [False]
        """
        if self.frequency == CompletionFrequency.DAILY.value:
            self._reset_date = datetime.today() + timedelta(days=1)
        elif self.frequency == CompletionFrequency.WEEKLY.value:
            today = datetime.today()
            self._reset_date = today + timedelta(days=7 - today.isoweekday())
        else:
            today = datetime.today()
            self._reset_date = (today.replace(day=1) + timedelta(days=32)).replace(day=1)

    def create_json_dict(self) -> MutableMapping:
        return {
            "name": self._name,
            "id": self._id,
            "frequency": self._frequency,
            "is_complete": self.is_complete
        }

    @property
    def is_complete(self) -> bool:
        """
        Gets whether the habit is complete or not.

        Precondition:  None
        Postcondition: None

        Params - None
        Return - [True] if the Habit is complete, otherwise [False].
        """
        return datetime.now() < self._reset_time

    @property
    def name(self) -> str:
        """
        Gets the name of the habit.

        Precondition:  None
        Postcondition: None

        Params - None
        Return - The name of the habit.
        """
        return self._name
    
    @property
    def id(self) -> int:
        """
        Gets the id of the habit.

        Precondition:  None
        Postcondition: None

        Params - None
        Return - The id of the habit.
        """
        return self._id

    @property
    def frequency(self) -> int:
        """
        Gets the frequency of the habit.

        Precondition:  None
        Postcondition: None

        Params - None
        Return - The frequency of the habit.
        """
        return self._frequency
    
    @name.setter
    def name(self, name: str):
        """
        Sets the name of the habit.

        Precondition:  isinstance(name, str) and
                       not str.isspace(name)
        Postcondition: self.name == name

        Params - name: The new name.
        Return - None
        """
        if not isinstance(name, str):
            raise Exception("name must be a str")
        if str.isspace(name):
            raise Exception("name must not be blank")

        self._name = name

    @frequency.setter
    def frequency(self, frequency: int):
        """
        Sets the name of the habit.

        Precondition:  isinstance(name, int) and
                       frequency >= 0 and
                       frequency <= 2
        Postcondition: self.name == name

        Params - name: The new name.
        Return - None
        """
        if not isinstance(frequency, int):
            raise Exception("frequency must be an int")
        if frequency < CompletionFrequency.DAILY.value or frequency > CompletionFrequency.MONTHLY.value:
            raise Exception("frequency must be betwwn 0 and 2, inclusive")

        self._frequency = frequency

class CompletionFrequency(Enum):
    DAILY: int = 0
    WEEKLY: int = 1
    MONTHLY: int = 2
