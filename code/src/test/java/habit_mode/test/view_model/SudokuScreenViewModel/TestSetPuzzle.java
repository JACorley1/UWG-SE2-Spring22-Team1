package habit_mode.test.view_model.SudokuScreenViewModel;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import habit_mode.model.local_implementation.LocalServerCommunicator;
import habit_mode.model.sudoku.SudokuPuzzle;
import habit_mode.view_model.SudokuScreenViewModel;

public class TestSetPuzzle {

    @Test
    void testSetSudokuPuzzle() {
        SudokuScreenViewModel vm = new SudokuScreenViewModel();
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
        vm.setPuzzle(puzzle);

        assertEquals(puzzle, vm.getPuzzle());
        
    }
    
}
