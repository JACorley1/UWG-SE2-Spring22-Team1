import unittest

from backend.sudoku_puzzle import SudokuPuzzle, PUZZLE_SIZE

class TestIsNumberValidAt(unittest.TestCase):    
    """
    Tests for the SudokuPuzzle's is_number_valid_at method.

    @author Team 1
    @version Spring 2022
    """
    def test_valid_number(self):
        """
        Tests if a number is valid for a specified cell when the entire number is empty.
        """
        puzzle = SudokuPuzzle()

        self.assertTrue(puzzle.is_number_valid_at(0, 0, 1), "Check if a valid number is valid")

    def test_number_on_same_number(self):
        """
        Tests if a number is valid when placed on itself.
        """
        puzzle = SudokuPuzzle()

        puzzle.set_number_at(0, 0, 1)

        self.assertTrue(puzzle.is_number_valid_at(0, 0, 1), "Check if a valid number is valid")


    def test_number_already_on_row(self):
        """
        Tests if the currect value is returned when the number is already on the row.
        """
        puzzle = SudokuPuzzle()

        puzzle.set_number_at(0, 0, 1)

        self.assertFalse(puzzle.is_number_valid_at(1, 0, 1), "Check if a valid number is invalid")
    
    def test_number_already_on_col(self):
        """
        Tests if the currect value is returned when the number is already on the column.
        """
        puzzle = SudokuPuzzle()

        puzzle.set_number_at(0, 0, 1)

        self.assertFalse(puzzle.is_number_valid_at(0, 1, 1), "Check if a valid number is invalid")
    
    def test_number_already_in_square(self):
        """
        Tests if the currect value is returned when the number is already in the square.
        """
        puzzle = SudokuPuzzle()

        puzzle.set_number_at(0, 0, 1)

        self.assertFalse(puzzle.is_number_valid_at(1, 1, 1), "Check if a valid number is invalid")
    
    def test_col_too_low(self):
        """
        Tests if an error is raised when the column is below 0.
        """
        puzzle = SudokuPuzzle()
        with self.assertRaises(IndexError):
            puzzle.is_number_valid_at(-1, 0, 1)
    
    def test_col_too_high(self):
        """
        Tests if an error is raised when the column is at or above the puzzle size.
        """
        puzzle = SudokuPuzzle()
        with self.assertRaises(IndexError):
            puzzle.is_number_valid_at(PUZZLE_SIZE, 0, 1)
    
    def test_invalid_col_type(self):
        """
        Tests if an error is raised when the column is not an integer.
        """
        puzzle = SudokuPuzzle()
        with self.assertRaises(TypeError):
            puzzle.is_number_valid_at("0", 0, 1)
    
    def test_row_too_low(self):
        """
        Tests if an error is raised when the row is below 0.
        """
        puzzle = SudokuPuzzle()
        with self.assertRaises(IndexError):
            puzzle.is_number_valid_at(0, -1, 1)
    
    def test_row_too_high(self):
        """
        Tests if an error is raised when the row is at or above the puzzle size.
        """
        puzzle = SudokuPuzzle()
        with self.assertRaises(IndexError):
            puzzle.is_number_valid_at(0, PUZZLE_SIZE, 1)
    
    def test_invalid_row_type(self):
        """
        Tests if an error is raised when the row is not an integer.
        """
        puzzle = SudokuPuzzle()
        with self.assertRaises(TypeError):
            puzzle.is_number_valid_at(0, "0", 1)
    
    def test_number_too_low(self):
        """
        Tests if an error is raised when the number is below 0.
        """
        puzzle = SudokuPuzzle()
        with self.assertRaises(Exception):
            puzzle.is_number_valid_at(0, 0, -1)
    
    def test_number_too_high(self):
        """
        Tests if an error is raised when the number is above the puzzle size.
        """
        puzzle = SudokuPuzzle()
        with self.assertRaises(Exception):
            puzzle.is_number_valid_at(0, 0, PUZZLE_SIZE + 1)

    def test_invalid_number_type(self):
        """
        Tests if an error is raised when the number is not an integer.
        """
        puzzle = SudokuPuzzle()
        with self.assertRaises(TypeError):
            puzzle.is_number_valid_at(0, 0, "1")
