package code.model.sudoku;

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
     * 
     * @return this.numbers
     */
    public int[][] getNumbers() {
        return this.numbers;
    }

    /**
     * Gets the move history
     * 
     * @return this.moveHistory
     */
    public Stack<SudokuMove> getMoveHistory() {
        return this.moveHistory;
    }

    /**
     * Gets the selected number
     * 
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
     * @return number at specified position
     */
    public int getNumber(int column, int row) {
        return this.numbers[row][column];
    }

    /**
     * Gets the number locks
     * 
     * @return this.numberLocks
     */
    public boolean[][] getNumberLock() {
        return this.numberLocks;
    }

    /**
     * Gets the default answer
     * 
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
     */
    public void setNumber(int value, int column, int row) {
        this.numbers[row][column] = value;
    }

    /***
     * sets the lock at the specified point
     * 
     * @param lock
     * @param column
     * @param row
     */
    public void setNumberLock(boolean lock, int column, int row) {
        this.numberLocks[row][column] = lock;
    }

    /***
     * sets the selected number
     * 
     * @param number
     */
    public void setSelectedNumber(int number) {
        this.selectedNumber = number;
    }

    /***
     * Checks to see if game is comple
     * 
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
     * @return true or false depending on locked state
     */
    public boolean isNumberLocked(int column, int row) {
        return this.numberLocks[row][column];
    }

    /***
     * gets the answer for the specified position
     * 
     * @param column
     * @param row
     * @return the answer for the coord
     */
    public int getAnswerForPosition(int column, int row) {
        return this.defaultAnswer[row][column];
    }
}
