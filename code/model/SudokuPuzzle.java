import java.util.Stack;
import code.model.*;

/**
 * Sudoku puzzle class
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
        this.selectedNumber = null;
        this.moveHistory = new Stack<SudokuMove>();
    }

    /**
     * Gets the numbers
     * 
     * @return this.numbers
     */
    public int[][] getNumber() {
        return this.numbers;
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
        this.numbers[column][row] = value;
    }

    /***
     * sets the lock at the specified point
     * 
     * @param lock
     * @param column
     * @param row
     */
    public void setNumberLock(boolean lock, int column, int row) {
        this.numberLocks[column][row] = lock;
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
        return false;
    }

    /***
     * gets the answer for the specified position
     * 
     * @param column
     * @param row
     * @return the answer for the coord
     */
    public int getAnswerForPosition(int column, int row) {
        return null;
    }
}
