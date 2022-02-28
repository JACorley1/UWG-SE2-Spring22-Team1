package habit_mode.test.model.sudoku.sudokuPuzzle;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import habit_mode.model.sudoku.SudokuPuzzle;

public class TestGetAnswerForPosition {
    
    @Test
	void testValidGetAnswerForPosition() {
		SudokuPuzzle puzzle = new SudokuPuzzle();

		puzzle.getAnswerForPosition(1, 1);

		assertEquals(0, puzzle.getAnswerForPosition(1, 1),"Checking that the answer given is correct");
	}

    @Test
	void testGetAnswerForPositionWithInvalidColumnLowerBound() {
		SudokuPuzzle puzzle = new SudokuPuzzle();
		assertThrows(
			IndexOutOfBoundsException.class, 
			()->{
				puzzle.getAnswerForPosition(-1, 1);
			}
		);
	}

    @Test
	void testGetAnswerForPositionWithInvalidColumnUpperBound() {
		SudokuPuzzle puzzle = new SudokuPuzzle();
		assertThrows(
			IndexOutOfBoundsException.class, 
			()->{
				puzzle.getAnswerForPosition(9, 1);
			}
		);
	}

    @Test
	void testGetAnswerForPositionWithInvalidRowLowerBound() {
		SudokuPuzzle puzzle = new SudokuPuzzle();
		assertThrows(
			IndexOutOfBoundsException.class, 
			()->{
				puzzle.getAnswerForPosition(1, -1);
			}
		);
	}

    @Test
	void testGetAnswerForPositionWithInvalidRowUpperBound() {
		SudokuPuzzle puzzle = new SudokuPuzzle();
		assertThrows(
			IndexOutOfBoundsException.class, 
			()->{
				puzzle.getAnswerForPosition(1, 9);
			}
		);
	}
}
