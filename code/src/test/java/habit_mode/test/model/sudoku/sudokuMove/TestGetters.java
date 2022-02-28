package habit_mode.test.model.sudoku.sudokuMove;

import org.junit.jupiter.api.Test;

import habit_mode.model.sudoku.SudokuMove;

public class TestGetters {
    @Test
    void testGetColumn() {
        SudokuMove move = new SudokuMove(1, 1, 1);
        move.getColumn();
    }

    @Test
    void testGetRow() {
        SudokuMove move = new SudokuMove(1, 1, 1);
        move.getRow();
    }

    @Test
    void testGetPrevNumber() {
        SudokuMove move = new SudokuMove(1, 1, 1);
        move.getPrevNumber();
    }
}
