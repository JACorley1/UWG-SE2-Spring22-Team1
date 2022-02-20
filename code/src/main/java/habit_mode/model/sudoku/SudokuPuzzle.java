package habit_mode.model.sudoku;

import java.util.Stack;

/**
 * Sudoku puzzle class
 * 
 * @author Matthew Thompson
 * @version spring 2022
 */
public class SudokuPuzzle {

    private int[][] numbers;
    private boolean[][] numberLocks;
    private int[][] defaultAnswer;
    private int selectedNumber;
    private Stack<SudokuMove> moveHistory;

    /**
     * Default Constructor
     * @precondition none
     * @postcondition this.numbers = new int[9][9] && this.numberLocks = new boolean[9][9] && this.defaultAnswer = new int[9][9] && this.selectedNumber = -1 && this.moveHistory = new Stack<SudokuMove>()
     */
    public SudokuPuzzle() {
        this.numbers = new int[9][9];
        this.numberLocks = new boolean[9][9];
        this.defaultAnswer = new int[9][9];
        this.selectedNumber = -1;
        this.moveHistory = new Stack<SudokuMove>();
    }

    /**
     * Gets the numbers
     * @precondition none
     * @postcondition none
     * @return this.numbers
     */
    public int[][] getNumbers() {
        return this.numbers;
    }

    /**
     * Gets the move history
     * @precondition none
     * @postcondition none
     * @return this.moveHistory
     */
    public Stack<SudokuMove> getMoveHistory() {
        return this.moveHistory;
    }

    /**
     * Gets the selected number
     * @precondition none
     * @postcondition none
     * @return selected number
     */
    public int getSelectedNumber() {
        return this.selectedNumber;
    }

    /**
     * Gets the number at specified location
     * 
     * @param column the column
     * @param row    the row
     * @precondition 0 <= column <= 8 && 0 <= row <= 8
     * @return number at specified position
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
     * Gets the number locks
     * @precondition none
     * @postcondition none
     * @return this.numberLocks
     */
    public boolean[][] getNumberLock() {
        return this.numberLocks;
    }

    /**
     * Gets the default answer
     * @precondition none
     * @postcondition none
     * @return default answer
     */
    public int[][] getDefaultAnswer() {
        return this.defaultAnswer;
    }

    /***
     * sets the number at the specified point
     * 
     * @param value
     * @param column
     * @param row
     * @precondition 0 <= value <= 9 && 0 <= column <= 8 && 0 <= row <= 8
     * @postcondition this.numbers[row][column] = value
     */
    public void setNumber(int value, int column, int row) {
        this.checkNumber(value);
        this.checkColumnAndRow(column, row);
        this.numbers[row][column] = value;
    }

    /***
     * sets the lock at the specified point
     * 
     * @param lock
     * @param column
     * @param row
     * @precondition column >= 0 && row >= 0
     * @postcondition this.numberLocks[row][column] = lock
     */
    public void setNumberLock(boolean lock, int column, int row) {
        this.checkColumnAndRow(column, row);
        this.numberLocks[row][column] = lock;
    }

    /***
     * sets the selected number
     * @precondition number >= 0 && number <= 9
     * @postcondition this.selectedNumber = number
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

    /***
     * Checks to see if game is comple
     * @precondition none
     * @postcondition none
     * @return true or false depending on state of the game
     */
    public boolean isComplete() {
        return this.numbers.equals(this.defaultAnswer);
    }

    /***
     * checks to see if number is locked
     * 
     * @param column
     * @param row
     * @precondition 0 <= column <= 8 && 0 <= row <= 8
     * @postcondition none
     * @return true or false depending on locked state
     */
    public boolean isNumberLocked(int column, int row) {
        this.checkColumnAndRow(column, row);
        return this.numberLocks[row][column];
    }

    /***
     * gets the answer for the specified position
     * 
     * @param column
     * @param row
     * @precondition 0 <= column <= 8 && 0 <= row <= 8
     * @postcondition none
     * @return the answer for the coord
     */
    public int getAnswerForPosition(int column, int row) {
        this.checkColumnAndRow(column, row);
        return this.defaultAnswer[row][column];
    }
}
