package habit_mode.test.model.sudoku.sudokuPuzzle;

import org.junit.jupiter.api.Test;

import habit_mode.model.sudoku.SudokuPuzzle;

public class TestGetters {
    @Test
    void testGetAnswersForPosition() {
        SudokuPuzzle puzzle = new SudokuPuzzle();
        puzzle.getAnswerForPosition(1, 1);
    }

    @Test
    void testGetDefaultAnswer() {
        SudokuPuzzle puzzle = new SudokuPuzzle();
        puzzle.getDefaultAnswer();
    }

    @Test
    void testGetMoveHistory() {
        SudokuPuzzle puzzle = new SudokuPuzzle();
        puzzle.getMoveHistory();
    }

    @Test
    void testGeNumber() {
        SudokuPuzzle puzzle = new SudokuPuzzle();
        puzzle.getNumber(1, 1);
    }

    @Test
    void testGetNumberLocks() {
        SudokuPuzzle puzzle = new SudokuPuzzle();
        puzzle.getNumberLocks();
    }

    @Test
    void testGetNumbers() {
        SudokuPuzzle puzzle = new SudokuPuzzle();
        puzzle.getNumbers();
    }

    @Test
    void testGetSelectedNumber() {
        SudokuPuzzle puzzle = new SudokuPuzzle();
        puzzle.getSelectedNumber();
    }

}
