package habit_mode.test.model.sudoku.sudokuPuzzle;


import static org.junit.jupiter.api.Assertions.*;

import java.util.Stack;

import org.junit.jupiter.api.Test;

import habit_mode.model.sudoku.SudokuPuzzle;
import habit_mode.model.sudoku.SudokuMove;

public class TestConstructor {
	@Test
	void testConstructorWithValidInput() {
		
		SudokuPuzzle puzzle = new SudokuPuzzle();
        int[][] defaultAnswer = new int[9][9];
        int[][] numbers = new int[9][9];
        boolean[][] numberLocks = new boolean[9][9];
        Stack<SudokuMove> moveHistory = new Stack<SudokuMove>();
		
		assertAll(
            ()->{assertEquals(-1, puzzle.getSelectedNumber(), "checking selectedNumber");}
		);
	}
}
