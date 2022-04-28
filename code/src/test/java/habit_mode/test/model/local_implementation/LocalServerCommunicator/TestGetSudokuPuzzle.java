package habit_mode.test.model.local_implementation.LocalServerCommunicator;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import habit_mode.model.local_implementation.LocalServerCommunicator;
import habit_mode.model.sudoku.SudokuPuzzle;

public class TestGetSudokuPuzzle {
    @Test
    void testNullPuzzle() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        communicator.getSudokuPuzzle();

        assertEquals(communicator.generateSudokuPuzzle(), communicator.getStoredPuzzle());
    }

    @Test
    void testGetPuzzle() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        int[][] board = { 
            { 8, 9, 2, 0, 0, 0, 0, 8, 6 },
            { 0, 0, 3, 0, 2, 7, 0, 5, 9 },
            { 0, 5, 1, 3, 0, 6, 0, 2, 4 },
            { 2, 6, 0, 9, 7, 3, 8, 4, 1 },
            { 4, 0, 9, 5, 0, 1, 2, 0, 3 },
            { 3, 1, 7, 4, 0, 2, 9, 6, 5 },
            { 0, 3, 6, 7, 0, 8, 5, 0, 2 },
            { 0, 7, 0, 2, 0, 0, 6, 0, 0 },
            { 0, 2, 0, 6, 0, 0, 4, 0, 0 } 
        };
        boolean[][] numberLocks = { 
            { true, true, true, false, false, false, false, true, true },
            { false, false, true, false, true, true, false, true, true },
            { false, true, true, true, false, true, false, true, true },
            { true, true, false, true, true, true, true, true, true },
            { true, false, true, true, false, true, true, false, true },
            { true, true, true, true, false, true, true, true, true },
            { false, true, true, true, false, true, true, false, true },
            { false, true, false, true, false, false, true, false, false },
            { false, true, false, true, false, false, true, false, false } 
        };
        SudokuPuzzle puzzle = new SudokuPuzzle(board, numberLocks);
        communicator.setStorePuzzle(puzzle);
        communicator.getSudokuPuzzle();

        assertEquals(puzzle, communicator.getStoredPuzzle());
    }


}
