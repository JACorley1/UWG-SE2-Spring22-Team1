import unittest
import random
import backend.sudoku_generator
from backend.sudoku_puzzle import SudokuPuzzle, PUZZLE_SIZE

class TestIsSolutionValid(unittest.TestCase):    
    """
    Tests for the SudokuPuzzle's unlock_random_hint method

    @author Team 1
    @version Spring 2022
    """
    def test_get_single_hint(self):
        """
        Tests if a single hint is unlocked when running the method once
        """
        random.seed(0)
        puzzle = SudokuPuzzle()

        coords = [(row, col) for row in range(PUZZLE_SIZE) for col in range(PUZZLE_SIZE)]
        puzzle.unlock_random_hint()
        locked_cells = list(filter(lambda coord: puzzle.number_locks[coord[0]][coord[1]], coords))

        self.assertTrue(
            len(locked_cells) == 1, 
            "Check if there is only one locked cell."
        )
        for row, col in locked_cells:
            self.assertEqual(
                puzzle.numbers[row][col], puzzle.solution[row][col],
                "Check id the numbers at all locked coordinates equal the solution"
            )
    
    def test_get_many_hints(self):
        """
        Tests if many hints are unlocked when running the method many times
        """
        random.seed(0)
        puzzle = SudokuPuzzle()

        coords = [(row, col) for row in range(PUZZLE_SIZE) for col in range(PUZZLE_SIZE)]
        for _ in range(10):
            puzzle.unlock_random_hint()
        new_locked_cells = list(filter(lambda coord: puzzle.number_locks[coord[0]][coord[1]], coords))

        self.assertTrue(
            len(new_locked_cells) == 10, 
            "Check if the length of the number_locks array is increased by 1."
        )
        for row, col in new_locked_cells:
            self.assertEqual(
                puzzle.numbers[row][col], puzzle.solution[row][col],
                "Check id the numbers at all locked coordinates equal the solution"
                )

    def test_get_hints_for_generated_puzzle(self):
        """
        Tests if many hints are unlocked when running the method many times on a puzzle that has been generated
        """
        random.seed(0)
        puzzle = backend.sudoku_generator.generate_sudoku_puzzle()

        coords = [(row, col) for row in range(PUZZLE_SIZE) for col in range(PUZZLE_SIZE)]
        old_locked_cells = list(filter(lambda coord: puzzle.number_locks[coord[0]][coord[1]], coords))
        for _ in range(10):
            puzzle.unlock_random_hint()
        new_locked_cells = list(filter(lambda coord: puzzle.number_locks[coord[0]][coord[1]], coords))

        self.assertTrue(
            len(new_locked_cells) == len(old_locked_cells) + 10, 
            "Check if the length of the number_locks array is increased by 10."
        )
        for row, col in new_locked_cells:
            self.assertEqual(
                puzzle.numbers[row][col], puzzle.solution[row][col],
                "Check id the numbers at all locked coordinates equal the solution"
                )
    
    def test_get_hint_for_fully_locked_puzzle(self):
        """
        Tests if None is returned when the puzzle is fully locked
        """
        puzzle = SudokuPuzzle()
        puzzle._number_locks = [[True] * PUZZLE_SIZE] * PUZZLE_SIZE

        self.assertIsNone(puzzle.unlock_random_hint(), "Check if None is returned when the puzzle is fully locked.")