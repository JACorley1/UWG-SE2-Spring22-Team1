import unittest

import backend.sudoku_generator
from backend.sudoku_puzzle import SudokuPuzzle, PUZZLE_SIZE

class TestGenerateSudokuPuzzle(unittest.TestCase):    
    """
    Tests for the SudokuPuzzle constructor.

    @author Team 1
    @version Spring 2022
    """
    def test_generate_puzzle(self):
        """
        Tests if valid puzzles are generated.
        """
        for _ in range(3):
            puzzle: SudokuPuzzle = backend.sudoku_generator.generate_sudoku_puzzle()
            self.assertTrue(puzzle.is_solution_valid(), "Check if the generated puzzle is valid")
            for coords in [(row, col) for row in range(PUZZLE_SIZE) for col in range(PUZZLE_SIZE)]:
                row, col = coords
                lock1 = puzzle.is_number_locked_at(row, col)
                lock2 = puzzle.is_number_locked_at(PUZZLE_SIZE - row - 1, PUZZLE_SIZE - col - 1)
                num_1_shown = puzzle.get_number_at(row, col) != 0
                num_2_shown = puzzle.get_number_at(PUZZLE_SIZE - row - 1, PUZZLE_SIZE - col - 1) != 0
                self.assertTrue(
                    lock1 == lock2 and lock1 == num_1_shown and lock1 == num_2_shown, 
                    "Checks if cells with default values are locked and the puzzle is symetrical"
                )
