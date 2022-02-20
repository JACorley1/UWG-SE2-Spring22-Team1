package habit_mode.test.model.sudoku.sudokuPuzzle;


import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import habit_mode.model.sudoku.SudokuPuzzle;

public class TestConstructor {
	@Test
	void testConstructorWithValidInput() {
		
		SudokuPuzzle puzzle = new SudokuPuzzle();
		
		assertAll(()->{assertEquals(-1, puzzle.getSelectedNumber(), "checking selectedNumber");}
		);
	}
}
