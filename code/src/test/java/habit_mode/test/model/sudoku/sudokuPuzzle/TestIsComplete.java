package habit_mode.test.model.sudoku.sudokuPuzzle;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import habit_mode.model.sudoku.SudokuPuzzle;

public class TestIsComplete {
    
    @Test
	void testValidPuzzle() {
		SudokuPuzzle puzzle = new SudokuPuzzle();
        int[][] board = { 
		{ 7, 9, 2, 1, 5, 4, 3, 8, 6 },
        	{ 6, 4, 3, 8, 2, 7, 1, 5, 9 },
        	{ 8, 5, 1, 3, 9, 6, 7, 2, 4 },
        	{ 2, 6, 5, 9, 7, 3, 8, 4, 1 },
        	{ 4, 8, 9, 5, 6, 1, 2, 7, 3 },
        	{ 3, 1, 7, 4, 8, 2, 9, 6, 5 },
        	{ 1, 3, 6, 7, 4, 8, 5, 9, 2 },
        	{ 9, 7, 4, 2, 1, 5, 6, 3, 8 },
        	{ 5, 2, 8, 6, 3, 9, 4, 1, 7 } 
	};
        puzzle.setNumbers(board);

		assertTrue(puzzle.isComplete(),"Checking that the answer given is complete");
	}

    @Test
	void testInvalidPuzzle() {
		SudokuPuzzle puzzle = new SudokuPuzzle();
        int[][] board = { 
		{ 7, 9, 2, 1, 5, 4, 3, 8, 6 },
        	{ 6, 4, 3, 8, 2, 7, 1, 5, 9 },
        	{ 8, 5, 1, 3, 9, 6, 7, 2, 4 },
        	{ 2, 6, 5, 9, 7, 3, 8, 4, 1 },
        	{ 6, 8, 9, 5, 6, 1, 2, 7, 3 }, //6 is invalid
        	{ 3, 1, 7, 4, 8, 2, 9, 6, 5 },
        	{ 1, 3, 6, 7, 4, 8, 5, 9, 2 },
        	{ 9, 7, 4, 2, 1, 5, 6, 3, 8 },
        	{ 5, 2, 8, 6, 3, 9, 4, 1, 7 } 
	};
        puzzle.setNumbers(board);

		assertFalse(puzzle.isComplete(),"Checking that the answer given is false");
	}

    @Test
	void testNumbersOutOfBounds() {
		SudokuPuzzle puzzle = new SudokuPuzzle();
        int[][] board = { 
		{ 7, 9, 2, 1, 5, 4, 3, 8, 6 },
        	{ 6, 4, 3, 8, 2, 7, 1, 5, 9 },
        	{ 8, 5, 1, 3, 9, 6, 7, 2, 4 },
        	{ 2, 6, 5, 9, 7, 3, 8, 4, 1 },
        	{ 4, 8, 9, 5, 6, 0, 2, 7, 3 }, //0 is invalid
        	{ 3, 1, 7, 4, 8, 2, 9, 6, 5 },
        	{ 1, 3, 6, 7, 4, 8, 5, 9, 2 },
        	{ 9, 7, 4, 2, 1, 5, 6, 3, 8 },
        	{ 5, 2, 8, 6, 3, 9, 4, 1, 7 } 
	};
        puzzle.setNumbers(board);

		assertFalse(puzzle.isComplete(),"Checking that the answer given is false");
	}
}
