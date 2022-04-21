import unittest

from backend.sudoku_puzzle import SudokuPuzzle

class TestIsSolutionValid(unittest.TestCase):    
    """
    Tests for the SudokuPuzzle's properties

    @author Team 1
    @version Spring 2022
    """

    def test_numbers(self):
        """
        Tests that the numbers property returns the whole numbers array
        """
        puzzle = SudokuPuzzle()
        self.assertEqual(puzzle.numbers, puzzle._numbers, "Check if the numbers property returns the whole numbers array.")
    
    def test_solution(self):
        """
        Tests that the solution property returns the whole solution array
        """
        puzzle = SudokuPuzzle()

        self.assertEqual(puzzle.solution, puzzle._solution, "Check if the solution property returns the whole solution array.")
    
    def test_number_locks(self):
        """
        Tests that the number_locks property returns the whole number_locks array
        """
        puzzle = SudokuPuzzle()

        self.assertEqual(puzzle.number_locks, puzzle._number_locks, "Check if the number_locks property returns the whole number_locks array.")