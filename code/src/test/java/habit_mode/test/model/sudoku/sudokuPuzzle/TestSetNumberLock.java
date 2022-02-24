package habit_mode.test.model.sudoku.sudokuPuzzle;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import habit_mode.model.sudoku.SudokuPuzzle;
public class TestSetNumberLock {
    
    @Test
	void testValidSetNumberLock() {
		SudokuPuzzle puzzle = new SudokuPuzzle();

		puzzle.setNumberLock(true, 1, 1);

		assertEquals(true, puzzle.isNumberLocked(1, 1),"Checking that the number lock is set");
	}

    @Test
	void testSetNumberLockWithInvalidColumnLowerBound() {
		SudokuPuzzle puzzle = new SudokuPuzzle();
		assertThrows(
			IndexOutOfBoundsException.class, 
			()->{
				puzzle.setNumberLock(false, -1, 1);
			}
		);
	}

    @Test
	void testSetNumberLockWithInvalidColumnUpperBound() {
		SudokuPuzzle puzzle = new SudokuPuzzle();
		assertThrows(
			IndexOutOfBoundsException.class, 
			()->{
				puzzle.setNumberLock(false, 9, 1);
			}
		);
	}

    @Test
	void testSetNumberLockWithInvalidRowLowerBound() {
		SudokuPuzzle puzzle = new SudokuPuzzle();
		assertThrows(
			IndexOutOfBoundsException.class, 
			()->{
				puzzle.setNumberLock(false, 1, -1);
			}
		);
	}

    @Test
	void testSetNumberLockWithInvalidRowUpperBound() {
		SudokuPuzzle puzzle = new SudokuPuzzle();
		assertThrows(
			IndexOutOfBoundsException.class, 
			()->{
				puzzle.setNumberLock(false, 1, 9);
			}
		);
	}
}
