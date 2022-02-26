package habit_mode.model.sudoku;

import java.util.Stack;

/**
 * Stores information about the state of a puzzle, including the placement of numbers, the default
 * solution, and which numbers are provided at the start of the puzzle.
 * 
 * @author Team 1
 * @version Spring 2022
 */
public class SudokuPuzzle {
    public static final int PUZZLE_SIZE = 9;

    private int[][] numbers;
    private boolean[][] numberLocks;
    private int[][] defaultAnswer;
    private int selectedNumber;
    private Stack<SudokuMove> moveHistory;

    /**
     * Default Constructor
     * 
     * @precondition None
     * @postcondition this.getNumbers() == new int[9][9] && this.gtNumberLocks() == new boolean[9][9] && 
     *                this.getDefaultAnswer() == new int[9][9] && this.getSelectedNumber() == -1 && 
     *                this.moveHistory == new Stack<SudokuMove>()
     */
    public SudokuPuzzle() {
        this.numbers = new int[PUZZLE_SIZE][PUZZLE_SIZE];
        this.numberLocks = new boolean[PUZZLE_SIZE][PUZZLE_SIZE];
        this.defaultAnswer = new int[PUZZLE_SIZE][PUZZLE_SIZE];
        this.selectedNumber = -1;
        this.moveHistory = new Stack<SudokuMove>();
    }

    /**
     * Gets the numbers.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return The numbers matrix.
     */
    public int[][] getNumbers() {
        return this.numbers;
    }

    /**
     * Gets the move history.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return The move history.
     */
    public Stack<SudokuMove> getMoveHistory() {
        return this.moveHistory;
    }

    /**
     * Gets the selected number.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return The selected number.
     */
    public int getSelectedNumber() {
        return this.selectedNumber;
    }

    /**
     * Gets the number at specified location.
     * 
     * @precondition column >= 0 && column < PUZZLE_SIZE && row >= 0 && row < PUZZLE_SIZE
     * @postcondition None
     * 
     * @param column The column.
     * @param row    The row.
     * @return The number at specified position.
     */
    public int getNumber(int column, int row) {
        this.checkColumnAndRow(column, row);
        return this.numbers[row][column];
    }

    private void checkColumnAndRow(int column, int row) {
        if (column < 0) {
            throw new IndexOutOfBoundsException("column can not be less than 0");
        }
        if (row < 0) {
            throw new IndexOutOfBoundsException("row can not be less than 0");
        }
    }

    /**
     * Gets the number locks.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return The number lock matrix.
     */
    public boolean[][] getNumberLocks() {
        return this.numberLocks;
    }

    /**
     * Gets the default answer.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return The default answer.
     */
    public int[][] getDefaultAnswer() {
        return this.defaultAnswer;
    }

    /**
     * Sets the number at the specified point.
     * 
     * @precondition value >= 0 && value < PUZZLE_SIZE && column >= 0 && column < PUZZLE_SIZE && 
     *               row >= 0 && row < PUZZLE_SIZE
     * @postcondition this.getNumber(row, column) == value
     * 
     * @param value The value being set to the specified position.
     * @param column The column to be set.
     * @param row The row to be set.
     */
    public void setNumber(int value, int column, int row) {
        this.checkNumber(value);
        this.checkColumnAndRow(column, row);
        this.numbers[row][column] = value;
    }

    /**
     * Sets the lock at the specified point.
     * 
     * @precondition column >= 0 && column < PUZZLE_SIZE && row >= 0 && row < PUZZLE_SIZE
     * @postcondition this.isNumberLocked(column, row) == lock
     * 
     * @param lock The boolean for the numberlock to be set.
     * @param column The column to be set.
     * @param row The row to be set.
     */
    public void setNumberLock(boolean lock, int column, int row) {
        this.checkColumnAndRow(column, row);
        this.numberLocks[row][column] = lock;
    }

    /**
     * Sets the selected number.
     * 
     * @precondition number >= 0 && number <= 9
     * @postcondition this.getSelectedNumber() == number
     * 
     * @param number
     */
    public void setSelectedNumber(int number) {
        this.checkNumber(number);
        this.selectedNumber = number;
    }

    private void checkNumber(int number) {
        if (number < 0) {
            throw new IllegalArgumentException("number cannot be less than 0");
        }
        if (number > 9) {
            throw new IllegalArgumentException("number cannot be greater than 9");
        }
    }

    /**
     * Checks to see if game is comple.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return [true] iff the game has been completed, otherwise [false]
     */
    public boolean isComplete() {
        return this.numbers.equals(this.defaultAnswer);
    }

    /**
     * Checks to see if number is locked.
     * 
     * @precondition column >= 0 && column < PUZZLE_SIZE && row >= 0 && row < PUZZLE_SIZE
     * @postcondition None
     * 
     * @param column The column to be set.
     * @param row The row to be set.
     * @return true or false depending on locked state.
     */
    public boolean isNumberLocked(int column, int row) {
        this.checkColumnAndRow(column, row);
        return this.numberLocks[row][column];
    }

    /**
     * Gets the answer for the specified position.
     * 
     * @precondition column >= 0 && column < PUZZLE_SIZE && row >= 0 && row < PUZZLE_SIZE
     * @postcondition None
     * 
     * @param column The column to be set.
     * @param row The row to be set.
     * @return The answer for the coord.
     */
    public int getAnswerForPosition(int column, int row) {
        this.checkColumnAndRow(column, row);
        return this.defaultAnswer[row][column];
    }
}
