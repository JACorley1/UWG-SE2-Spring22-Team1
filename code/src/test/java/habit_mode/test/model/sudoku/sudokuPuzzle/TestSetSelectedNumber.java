package habit_mode.test.model.sudoku.sudokuPuzzle;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import habit_mode.model.sudoku.SudokuPuzzle;

public class TestSetSelectedNumber {

    @Test
	void testValidSetSelectedNumber() {
		SudokuPuzzle puzzle = new SudokuPuzzle();

		puzzle.setSelectedNumber(5);

		assertEquals(5, puzzle.getSelectedNumber(),"Checking that the selected is set");
	}

	@Test
	void testSetSelectedNumberWithInvalidNumberLowerBound() {
		SudokuPuzzle puzzle = new SudokuPuzzle();
		assertThrows(
			IllegalArgumentException.class, 
			()->{
				puzzle.setSelectedNumber(-1);
			}
		);
	}

	@Test
	void testSetSelectedNumberWithInvalidNumberUpperBound() {
		SudokuPuzzle puzzle = new SudokuPuzzle();
		assertThrows(
			IllegalArgumentException.class, 
			()->{
				puzzle.setSelectedNumber(10);
			}
		);
	}
}
