import unittest

from backend.sudoku_puzzle import SudokuPuzzle, PUZZLE_SIZE

class TestGetSetNumberAt(unittest.TestCase):    
    """
    Tests for the SudokuPuzzle's number getters and setters.

    @author Team 1
    @version Spring 2022
    """

    def test_set_number(self):
        """
        Checks if a number is set and get correctly.
        """
        puzzle = SudokuPuzzle()
        puzzle.set_number_at(0, 0, 1)

        self.assertEqual(puzzle.get_number_at(0, 0), 1, "Check if the number was set correctly")
    
    def test_set_number_row_too_low(self):
        """
        Checks if an error is raised when the row is below 0.
        """
        puzzle = SudokuPuzzle()
        with self.assertRaises(IndexError):
            puzzle.set_number_at(-1, 0, 1)
    
    def test_set_number_row_too_high(self):
        """
        Checks if an error is raised when the row is at or above the puzzle size.
        """
        puzzle = SudokuPuzzle()
        with self.assertRaises(IndexError):
            puzzle.set_number_at(PUZZLE_SIZE, 0, 1)
    
    def test_set_number_invalid_row_type(self):
        """
        Checks if an error is raised when the row is not an integer.
        """
        puzzle = SudokuPuzzle()
        with self.assertRaises(TypeError):
            puzzle.set_number_at("0", 0, 1)
    
    def test_set_number_col_too_low(self):
        """
        Checks if an error is raised when the column is below 0.
        """
        puzzle = SudokuPuzzle()
        with self.assertRaises(IndexError):
            puzzle.set_number_at(0, -1, 1)
    
    def test_set_number_col_too_high(self):
        """
        Checks if an error is raised when the column is at or above the puzzle size.
        """
        puzzle = SudokuPuzzle()
        with self.assertRaises(IndexError):
            puzzle.set_number_at(0, PUZZLE_SIZE, 1)
    
    def test_set_number_invalid_col_type(self):
        """
        Checks if an error is raised when the column is not an integer.
        """
        puzzle = SudokuPuzzle()
        with self.assertRaises(TypeError):
            puzzle.set_number_at(0, "0", 1)
    
    def test_set_number_too_low(self):
        """
        Checks if an error is raised when the number is below 0.
        """
        puzzle = SudokuPuzzle()
        with self.assertRaises(Exception):
            puzzle.set_number_at(0, 0, -1)
    
    def test_set_number_too_high(self):
        """
        Checks if an error is raised when the number is above the puzzle size.
        """
        puzzle = SudokuPuzzle()
        with self.assertRaises(Exception):
            puzzle.set_number_at(0, 0, PUZZLE_SIZE + 1)

    def test_set_number_invalid_type(self):
        """
        Checks if an error is raised when the number is not an integer.
        """
        puzzle = SudokuPuzzle()
        with self.assertRaises(TypeError):
            puzzle.set_number_at(0, 0, "1")