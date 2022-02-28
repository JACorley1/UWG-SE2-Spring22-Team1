package habit_mode.test.model.sudoku.sudokuPuzzle;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import habit_mode.model.sudoku.SudokuPuzzle;
public class TestSetNumber {
    
    @Test
	void testValidSetNumber() {
		SudokuPuzzle puzzle = new SudokuPuzzle();

		puzzle.setNumber(3, 1, 1);

		assertEquals(3, puzzle.getNumber(1, 1),"Checking that the number is set");
	}

    @Test
	void testSetNumberWithInvalidValueLowerBound() {
		SudokuPuzzle puzzle = new SudokuPuzzle();
		assertThrows(
			IllegalArgumentException.class, 
			()->{
				puzzle.setNumber(-1, 1, 1);
			}
		);
	}

    @Test
	void testSetNumberWithInvalidValueUpperBound() {
		SudokuPuzzle puzzle = new SudokuPuzzle();
		assertThrows(
			IllegalArgumentException.class, 
			()->{
				puzzle.setNumber(10, 1, 1);
			}
		);
	}

    @Test
	void testSetNumberWithInvalidColumnUpperBound() {
		SudokuPuzzle puzzle = new SudokuPuzzle();
		assertThrows(
			IndexOutOfBoundsException.class, 
			()->{
				puzzle.setNumber(8, 9, 1);
			}
		);
	}

    @Test
	void testSetNumberWithInvalidColumnLowerBound() {
		SudokuPuzzle puzzle = new SudokuPuzzle();
		assertThrows(
			IndexOutOfBoundsException.class, 
			()->{
				puzzle.setNumber(4, -1, 1);
			}
		);
	}

    @Test
	void testSetNumberWithInvalidRowUpperBound() {
		SudokuPuzzle puzzle = new SudokuPuzzle();
		assertThrows(
			IndexOutOfBoundsException.class, 
			()->{
				puzzle.setNumber(8, 3, 9);
			}
		);
	}

    @Test
	void testSetNumberWithInvalidRowLowerBound() {
		SudokuPuzzle puzzle = new SudokuPuzzle();
		assertThrows(
			IndexOutOfBoundsException.class, 
			()->{
				puzzle.setNumber(3, 3, -1);
			}
		);
	}
}
