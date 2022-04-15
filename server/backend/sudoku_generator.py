from random import shuffle
from typing import Any, List
from backend.sudoku_puzzle import SudokuPuzzle, PUZZLE_SIZE, SQUARE_SIZE

def _generate_diagonal(puzzle: SudokuPuzzle) -> None:
    for offset in range(0, 9, 3):
        num_order: List[int] = list(range(1, PUZZLE_SIZE + 1))
        shuffle(num_order)
        index: int = 0
        for coord in [(row + offset, col + offset) for row in range(3) for col in range(3)]:
            puzzle.set_solution_at(coord[0], coord[1], num_order[index])
            index += 1

def _generate_cells(puzzle: SudokuPuzzle) -> bool:
    number_order = list(range(1, PUZZLE_SIZE + 1))
    shuffle(number_order)

    row: Any = None
    col: Any = None

    for coords in [(row, col) for row in range(PUZZLE_SIZE) for col in range(PUZZLE_SIZE)]:
        if puzzle.get_solution_at(coords[0], coords[1]) == 0:
            row, col = coords
            break

    if row is None:
        return True
    
    for num in number_order:
        if puzzle.is_solution_valid_at(row, col, num):
            puzzle.set_solution_at(row, col, num)
            if _generate_cells(puzzle):
                return True
            puzzle.set_solution_at(row, col, 0)
    
    return False

def _set_default_cells(puzzle: SudokuPuzzle) -> None:
    """
    Randomly selects cells to be shown at the start of the puzzle.

    Precondition: isinstance(puzzle, SudokuPuzzle)
    Postcondition: None

    Return - None
    """

    squares = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1)]
    for square in squares:
        cell_count = 4 if square != (1, 1) else 2
        start_row = square[0] * SQUARE_SIZE
        end_row = start_row + SQUARE_SIZE
        start_col = square[1] * SQUARE_SIZE
        end_col = start_col + SQUARE_SIZE
        coords = [(row, col) for row in range(start_row, end_row) for col in range(start_col, end_col)]
        shuffle(coords)

        for coord in coords[:cell_count]:
            inverse_coord = (PUZZLE_SIZE - coord[0] - 1, PUZZLE_SIZE - coord[1] - 1)
            solution = puzzle.get_solution_at(coord[0], coord[1])
            inverse_solution = puzzle.get_solution_at(inverse_coord[0], inverse_coord[1])

            puzzle.set_number_at(coord[0], coord[1], solution)
            puzzle.set_number_at(inverse_coord[0], inverse_coord[1], inverse_solution)
            puzzle.set_number_locked_at(coord[0], coord[1], True)
            puzzle.set_number_locked_at(inverse_coord[0], inverse_coord[1], True)

def generate_sudoku_puzzle() -> SudokuPuzzle:
    """
    Generates a random SudokuPuzzle.

    Precondition: None
    Postcondition: None

    Return - A randomly generated SudokuPuzzle.
    """

    puzzle: SudokuPuzzle = SudokuPuzzle()

    _generate_diagonal(puzzle)
    _generate_cells(puzzle)
    _set_default_cells(puzzle)

    for row in puzzle._numbers:
        print(" ".join(map(str, row)))

    return puzzle
