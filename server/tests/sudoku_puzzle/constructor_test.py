import unittest

from backend.sudoku_puzzle import SudokuPuzzle, PUZZLE_SIZE

class TestConstructor(unittest.TestCase):    
    """
    Tests for the SudokuPuzzle constructor.

    @author Team 1
    @version Spring 2022
    """

    def test_valid_constructor(self):
        """
        Checks if the constructor sets the default values correctly.
        """
        puzzle = SudokuPuzzle()

        for row in range(PUZZLE_SIZE):
            for col in range(PUZZLE_SIZE):
                self.assertEqual(puzzle.get_solution_at(row, col), 0, "Check if the solution is empty")
                self.assertEqual(puzzle.get_number_at(row, col), 0, "Check if the puzzle is empty")
                self.assertFalse(puzzle.is_number_locked_at(row, col), "Check if the puzzle is not locked")
