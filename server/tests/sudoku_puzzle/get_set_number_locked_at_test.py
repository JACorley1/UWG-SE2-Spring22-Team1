import unittest

from backend.sudoku_puzzle import SudokuPuzzle, PUZZLE_SIZE

class TestGetSetNumberAt(unittest.TestCase):    
    """
    Tests for the SudokuPuzzle's number lock getters and setters.

    @author Team 1
    @version Spring 2022
    """
    def test_set_number_locked(self):
        """
        Checks if a number lock is set and get correctly.
        """
        puzzle = SudokuPuzzle()
        puzzle.set_number_locked_at(0, 0, True)

        self.assertEqual(puzzle.is_number_locked_at(0, 0), True, "Check if the number lock was set correctly")
    
    def test_set_number_locked_row_too_low(self):
        """
        Checks if an error is raised when the row is below 0.
        """
        puzzle = SudokuPuzzle()
        with self.assertRaises(IndexError):
            puzzle.set_number_locked_at(-1, 0, True)
    
    def test_set_number_locked_row_too_high(self):
        """
        Checks if an error is raised when the row is at or above the puzzle size.
        """
        puzzle = SudokuPuzzle()
        with self.assertRaises(IndexError):
            puzzle.set_number_locked_at(PUZZLE_SIZE, 0, True)
    
    def test_set_number_locked_invalid_row_type(self):
        """
        Checks if an error is raised when the row is not an integer.
        """
        puzzle = SudokuPuzzle()
        with self.assertRaises(TypeError):
            puzzle.set_number_locked_at("0", 0, True)
    
    def test_set_number_locked_col_too_low(self):
        """
        Checks if an error is raised when the column is below 0.
        """
        puzzle = SudokuPuzzle()
        with self.assertRaises(IndexError):
            puzzle.set_number_locked_at(0, -1, True)

    def test_set_number_locked_col_too_high(self):
        """
        Checks if an error is raised when the column is at or above the puzzle size.
        """
        puzzle = SudokuPuzzle()
        with self.assertRaises(IndexError):
            puzzle.set_number_locked_at(0, PUZZLE_SIZE, True)
    
    def test_set_number_locked_invalid_col_type(self):
        """
        Checks if an error is raised when the column is not an integer.
        """
        puzzle = SudokuPuzzle()
        with self.assertRaises(TypeError):
            puzzle.set_number_locked_at("0", 0, True)
    
    def test_set_number_locked_invalid_type(self):
        """
        Checks if an error is raised when the number lock is not a boolean.
        """
        puzzle = SudokuPuzzle()
        with self.assertRaises(TypeError):
            puzzle.set_number_locked_at(0, 0, "True")