import random
from typing import List, Optional, Tuple

PUZZLE_SIZE: int = 9
SQUARE_SIZE: int = 3
HINT_COST: int = 20

class SudokuPuzzle:
    _numbers: List[List[int]]
    _solution: List[List[int]]
    _number_locks: List[List[bool]]

    """
    Stores the numbers, default solution, and states of the numbers in the puzzle.

    @author Team 1
    @version Spring 2022
    """
    def __init__(self):
        """
        Creates a new, blank SudokuPuzzle.

        Precondition:  None
        Postcondition: self.numbers is a 2d list of 0s and
                       self.default_solution is a 2d list of 0s
        """
        self._numbers = [[0 for _ in range(PUZZLE_SIZE)] for _ in range(PUZZLE_SIZE)]
        self._solution = [[0 for _ in range(PUZZLE_SIZE)] for _ in range(PUZZLE_SIZE)]
        self._number_locks = [[False for _ in range(PUZZLE_SIZE)] for _ in range(PUZZLE_SIZE)]
  
    def is_complete(self):
        """
        Returns whether the puzzle is complete.

        Precondition:  None
        Postcondition: None

        Returns: Whether the puzzle is complete.
        """
        valid_values = set(range(1, PUZZLE_SIZE + 1))
        for coord in [(row, col) for row in range(PUZZLE_SIZE) for col in range(PUZZLE_SIZE)]:
            num = self._numbers[coord[0]][coord[1]]
            if num not in valid_values or not self.is_number_valid_at(coord[0], coord[1], num):
                return False
        return True

    def is_number_valid_at(self, row: int, col: int, number: int) -> bool:
        """
        Returns whether the number is valid at the specified row and column.

        Precondition:  isinstance(row, int) and
                       isinstance(col, int) and
                       isinstance(number, int) and
                       0 <= row < _PUZZLE_SIZE and
                       0 <= col < _PUZZLE_SIZE and
                       0 <= number <= _PUZZLE_SIZE
        Postcondition: None
        """
        _check_valid_position(row, col)
        _check_valid_number(number)

        if self._column_contains_number(row, col, number):
            return False
        if self._row_contains_number(row, col, number):
            return False
        if self._square_contains_number(row, col, number):
            return False
        return True

    def unlock_random_hint(self) -> Optional[Tuple[int, int]]:
        """
        Randomly selects a cell that isn't locked, replaces the number with the solution, and
        locks the cell.

        Precondition:  None
        Postcondition: A cell is locked and the number is replaced with the solution.

        Params: None
        Return: A tuple containing the row and column of the cell that was filled if a hint was 
                given, otherwise None.
        """
        coords: List[Tuple[int, int]] = [(row, col) for row in range(PUZZLE_SIZE) for col in range(PUZZLE_SIZE)]
        unlocked_cells: List[Tuple[int, int]] = list(filter(lambda coord: not self._number_locks[coord[0]][coord[1]], coords))

        if not unlocked_cells:
            return None
        
        hint_cell = random.choice(unlocked_cells)
        self._numbers[hint_cell[0]][hint_cell[1]] = self._solution[hint_cell[0]][hint_cell[1]]
        self._number_locks[hint_cell[0]][hint_cell[1]] = True
        return hint_cell

    def _column_contains_number(self, row: int, col: int, number: int) -> bool:
        """
        Returns whether the specified column contains the specified number. Ignores the number
        at the specified row.

        Precondition:  isinstance(row, int) and
                       isinstance(col, int) and
                       isinstance(number, int) and
                       0 <= row < _PUZZLE_SIZE and
                       0 <= col < _PUZZLE_SIZE and
                       0 <= number <= _PUZZLE_SIZE
        Postcondition: None

        Params:
            row - The row to check.
            col - The column to check.
            number - The number to check.
        Returns: Whether the specified column contains the specified number.
        """
        _check_valid_position(row, col)
        _check_valid_number(number)

        for cur_row in range(PUZZLE_SIZE):
            if row != cur_row and self._numbers[cur_row][col] == number:
                return True
        
        return False

    def _row_contains_number(self, row: int, col: int, number: int) -> bool:
        """
        Returns whether the specified row contains the specified number. Ignores the number
        at the specified column.

        Precondition:  isinstance(row, int) and
                       isinstance(col, int) and
                       isinstance(number, int) and
                       0 <= row < _PUZZLE_SIZE and
                       0 <= col < _PUZZLE_SIZE and
                       0 <= number <= _PUZZLE_SIZE
        Postcondition: None

        Params:
            row - The row to check.
            col - The column to check.
            number - The number to check.
        Returns: Whether the specified row contains the specified number.
        """
        _check_valid_position(row, col)
        _check_valid_number(number)

        for cur_col in range(PUZZLE_SIZE):
            if col != cur_col and self._numbers[row][cur_col] == number:
                return True
        
        return False

    def _square_contains_number(self, row: int, col: int, number: int) -> bool:
        """
        Returns whether the specified square contains the specified number. Ignores the number
        at the specified row and column.

        Precondition:  isinstance(row, int) and
                       isinstance(col, int) and
                       isinstance(number, int) and
                       0 <= row < _PUZZLE_SIZE and
                       0 <= col < _PUZZLE_SIZE and
                       0 <= number <= _PUZZLE_SIZE
        Postcondition: None

        Params:
            row - The row to check.
            col - The column to check.
            number - The number to check.
        Returns: Whether the specified square contains the specified number.
        """
        _check_valid_position(row, col)
        _check_valid_number(number)

        row_start = row - row % SQUARE_SIZE
        row_end = row_start + SQUARE_SIZE
        col_start = col - col % SQUARE_SIZE
        col_end = col_start + SQUARE_SIZE

        for coords in [(row, col) for row in range(row_start, row_end) for col in range(col_start, col_end)]:
            if coords != (row, col) and self._numbers[coords[0]][coords[1]] == number:
                return True
        
        return False

    def is_solution_valid(self):
        """
        Returns whether the puzzle's solution is valid.

        Precondition:  None
        Postcondition: None

        Returns: Whether the puzzle's solution is valid.
        """
        valid_values = set(range(1, PUZZLE_SIZE + 1))
        for coord in [(row, col) for row in range(PUZZLE_SIZE) for col in range(PUZZLE_SIZE)]:
            num = self._solution[coord[0]][coord[1]]
            if num not in valid_values or not self.is_solution_valid_at(coord[0], coord[1], num):
                return False
        return True

    def is_solution_valid_at(self, row: int, col: int, number: int) -> bool:
        """
        Returns whether the solution is valid at the specified row and column.

        Precondition:  isinstance(row, int) and
                       isinstance(col, int) and
                       isinstance(number, int) and
                       0 <= row < _PUZZLE_SIZE and
                       0 <= col < _PUZZLE_SIZE and
                       0 <= number <= _PUZZLE_SIZE
        Postcondition: None
        """
        _check_valid_position(row, col)
        _check_valid_number(number)

        if self._solution_column_contains_number(row, col, number):
            return False
        if self._solution_row_contains_number(row, col, number):
            return False
        if self._solution_square_contains_number(row, col, number):
            return False
        return True

    def _solution_column_contains_number(self, row: int, col: int, number: int) -> bool:
        """
        Returns whether the specified column contains the specified number. Ignores the number
        at the specified row.

        Precondition:  isinstance(row, int) and
                       isinstance(col, int) and
                       isinstance(number, int) and
                       0 <= row < _PUZZLE_SIZE and
                       0 <= col < _PUZZLE_SIZE and
                       0 <= number <= _PUZZLE_SIZE
        Postcondition: None

        Params:
            row - The row to check.
            col - The column to check.
            number - The number to check.
        Returns: Whether the specified column contains the specified number.
        """
        _check_valid_position(row, col)
        _check_valid_number(number)

        for cur_row in range(PUZZLE_SIZE):
            if row != cur_row and self._solution[cur_row][col] == number:
                return True
        
        return False

    def _solution_row_contains_number(self, row: int, col: int, number: int) -> bool:
        """
        Returns whether the specified row contains the specified number. Ignores the number
        at the specified column.

        Precondition:  isinstance(row, int) and
                       isinstance(col, int) and
                       isinstance(number, int) and
                       0 <= row < _PUZZLE_SIZE and
                       0 <= col < _PUZZLE_SIZE and
                       0 <= number <= _PUZZLE_SIZE
        Postcondition: None

        Params:
            row - The row to check.
            col - The column to check.
            number - The number to check.
        Returns: Whether the specified row contains the specified number.
        """
        _check_valid_position(row, col)
        _check_valid_number(number)

        for cur_col in range(PUZZLE_SIZE):
            if col != cur_col and self._solution[row][cur_col] == number:
                return True
        
        return False

    def _solution_square_contains_number(self, row: int, col: int, number: int) -> bool:
        """
        Returns whether the specified square contains the specified number. Ignores the number
        at the specified row and column.

        Precondition:  isinstance(row, int) and
                       isinstance(col, int) and
                       isinstance(number, int) and
                       0 <= row < _PUZZLE_SIZE and
                       0 <= col < _PUZZLE_SIZE and
                       0 <= number <= _PUZZLE_SIZE
        Postcondition: None

        Params:
            row - The row to check.
            col - The column to check.
            number - The number to check.
        Returns: Whether the specified square contains the specified number.
        """
        _check_valid_position(row, col)
        _check_valid_number(number)

        row_start = row - row % SQUARE_SIZE
        row_end = row_start + SQUARE_SIZE
        col_start = col - col % SQUARE_SIZE
        col_end = col_start + SQUARE_SIZE

        for coords in [(row, col) for row in range(row_start, row_end) for col in range(col_start, col_end)]:
            if coords != (row, col) and self._solution[coords[0]][coords[1]] == number:
                return True
        
        return False

    @property
    def numbers(self) -> List[List[int]]:
        """
        Returns the puzzle's numbers.

        Precondition:  None
        Postcondition: None

        Returns: The puzzle's numbers.
        """
        return self._numbers

    def get_number_at(self, row: int, col: int) -> int:
        """
        Returns the number at the specified row and column.

        Precondition:  isinstance(row, int) and
                       isinstance(col, int) and
                       0 <= row < _PUZZLE_SIZE and
                       0 <= col < _PUZZLE_SIZE
        Postcondition: None

        Params:
            row - The row of the number to get.
            col - The column of the number to get.
        Returns: The number at the specified row and column.
        """
        _check_valid_position(row, col)
        
        return self._numbers[row][col]
    
    def set_number_at(self, row: int, col: int, number: int) -> None:
        """
        Sets the number at the specified row and column.

        Precondition:  isinstance(row, int) and
                       isinstance(col, int) and
                       isinstance(number, int) and
                       0 <= row < _PUZZLE_SIZE and
                       0 <= col < _PUZZLE_SIZE and
                       0 <= number <= _PUZZLE_SIZE
        Postcondition: self.get_number_at(row, col) == number

        Params:
            row - The row of the number to set.
            col - The column of the number to set.
            number - The number to set.
        Returns: None
        """
        _check_valid_position(row, col)
        _check_valid_number(number)
        
        self._numbers[row][col] = number

    @property
    def solution(self) -> List[List[int]]:
        """
        Returns the puzzle's default solution.

        Precondition:  None
        Postcondition: None

        Returns: The puzzle's default solution.
        """
        return self._solution

    def get_solution_at(self, row: int, col: int) -> int:
        """
        Returns the default solution at the specified row and column.

        Precondition:  isinstance(row, int) and
                       isinstance(col, int) and
                       0 <= row < _PUZZLE_SIZE and
                       0 <= col < _PUZZLE_SIZE
        Postcondition: None

        Params:
            row - The row of the default solution to get.
            col - The column of the default solution to get.
        Returns: The default solution at the specified row and column.
        """
        _check_valid_position(row, col)
        
        return self._solution[row][col]

    def set_solution_at(self, row: int, col: int, number: int) -> None:
        """
        Sets the default solution at the specified row and column.

        Precondition:  isinstance(row, int) and
                       isinstance(col, int) and
                       isinstance(number, int) and
                       0 <= row < _PUZZLE_SIZE and
                       0 <= col < _PUZZLE_SIZE and
                       0 <= number <= _PUZZLE_SIZE
        Postcondition: self.get_default_solution_at(row, col) == number

        Params:
            row - The row of the default solution to set.
            col - The column of the default solution to set.
            number - The default solution to set.
        Returns: None
        """
        _check_valid_position(row, col)
        _check_valid_number(number)
        
        self._solution[row][col] = number

    @property
    def number_locks(self) -> List[List[bool]]:
        """
        Returns the puzzle's number locks.

        Precondition:  None
        Postcondition: None

        Returns: The puzzle's number locks.
        """
        return self._number_locks

    def is_number_locked_at(self, row: int, col: int) -> bool:
        """
        Returns whether the number at the specified row and column is locked.

        Precondition:  isinstance(row, int) and
                       isinstance(col, int) and
                       0 <= row < _PUZZLE_SIZE and
                       0 <= col < _PUZZLE_SIZE
        Postcondition: None

        Params:
            row - The row of the number to check.
            col - The column of the number to check.
        Returns: Whether the number at the specified row and column is locked.
        """
        _check_valid_position(row, col)
        
        return self._number_locks[row][col]

    def set_number_locked_at(self, row: int, col: int, locked: bool) -> None:
        """
        Sets whether the number at the specified row and column is locked.

        Precondition:  isinstance(row, int) and
                       isinstance(col, int) and
                       isinstance(locked, bool) and
                       0 <= row < _PUZZLE_SIZE and
                       0 <= col < _PUZZLE_SIZE
        Postcondition: self.is_number_locked_at(row, col) == locked

        Params:
            row - The row of the number to set.
            col - The column of the number to set.
            locked - Whether the number is locked.
        Returns: None
        """
        _check_valid_position(row, col)
        if not isinstance(locked, bool):
            raise TypeError("locked must be a boolean")

        self._number_locks[row][col] = locked

def _check_valid_position(row: int, col: int) -> None:
    """
    Returns whether the specified position is valid.

    Precondition:  isinstance(row, int) and
                   isinstance(col, int) and
                   0 <= row < _PUZZLE_SIZE and
                   0 <= col < _PUZZLE_SIZE
    Postcondition: None
    """
    if not isinstance(row, int):
        raise TypeError("row must be an int")
    if not isinstance(col, int):
        raise TypeError("col must be an int")
    if row < 0 or row >= PUZZLE_SIZE:
        raise IndexError("row must be between 0 and " + str(PUZZLE_SIZE - 1))
    if col < 0 or col >= PUZZLE_SIZE:
        raise IndexError("col must be between 0 and " + str(PUZZLE_SIZE - 1))

def _check_valid_number(number: int) -> None:
    """
    Returns whether the specified number is valid.

    Precondition:  isinstance(number, int) and
                   0 <= number <= _PUZZLE_SIZE
    Postcondition: None
    """
    if not isinstance(number, int):
        raise TypeError("number must be an int")
    if number < 0 or number > PUZZLE_SIZE:
        raise Exception("number must be between 0 and " + str(PUZZLE_SIZE))