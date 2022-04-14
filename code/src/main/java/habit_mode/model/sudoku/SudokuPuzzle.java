package habit_mode.model.sudoku;

import java.util.Arrays;
import java.util.Stack;

/**
 * Stores information about the state of a puzzle, including the placement of
 * numbers, the default
 * solution, and which numbers are provided at the start of the puzzle.
 * 
 * @author Team 1
 * @version Spring 2022
 */
public class SudokuPuzzle {
    public static final int PUZZLE_SIZE = 9;
    public static final int MIN_INDEX = 0;
    public static final int MAX_INDEX = 8;

    private int[][] numbers;
    private boolean[][] numberLocks;
    private int[][] defaultAnswer;
    private int selectedNumber;
    private Stack<SudokuMove> moveHistory;

    /**
     * Default Constructor
     * 
     * @precondition None
     * @postcondition this.getNumbers() == new int[PUZZLE_SIZE][PUZZLE_SIZE] &&
     *                this.gtNumberLocks() ==
     *                new boolean[PUZZLE_SIZE][PUZZLE_SIZE] &&
     *                this.getDefaultAnswer() == new int[PUZZLE_SIZE][PUZZLE_SIZE]
     *                &&
     *                this.getSelectedNumber() == -1 &&
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
     * @precondition column >= MIN_INDEX && column < MAX_INDEX && row >= MIN_INDEX
     *               && row < MAX_INDEX
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
        if (column < MIN_INDEX) {
            throw new IndexOutOfBoundsException("column can not be less than 0");
        }
        if (column > MAX_INDEX) {
            throw new IndexOutOfBoundsException("column can not be more than 8");
        }
        if (row > MAX_INDEX) {
            throw new IndexOutOfBoundsException("row can not be more than 8");
        }
        if (row < MIN_INDEX) {
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
     * @precondition value >= MIN_INDEX && value < PUZZLE_SIZE && column >=
     *               MIN_INDEX &&
     *               column <
     *               PUZZLE_SIZE &&
     *               row >= MIN_INDEX && row < PUZZLE_SIZE
     * @postcondition this.getNumber(row, column) == value
     * 
     * @param value  The value being set to the specified position.
     * @param column The column to be set.
     * @param row    The row to be set.
     */
    public void setNumber(int value, int column, int row) {
        this.checkNumber(value);
        this.checkColumnAndRow(column, row);
        this.numbers[row][column] = value;
    }

    /**
     * Sets the numbers matrix
     * 
     * 
     * @postcondition this.numbers == puzzle
     * 
     * @param puzzle  The puzzle being set to numbers
     *
     */
    public void setNumbers(int[][] puzzle) {
        this.numbers = puzzle;
    }

    /**
     * Sets the lock at the specified point.
     * 
     * @precondition column >= MIN_INDEX && column < MAX_INDEX && row >= MIN_INDEX
     *               && row < MAX_INDEX
     * @postcondition this.isNumberLocked(column, row) == lock
     * 
     * @param lock   The boolean for the numberlock to be set.
     * @param column The column to be set.
     * @param row    The row to be set.
     */
    public void setNumberLock(boolean lock, int column, int row) {
        this.checkColumnAndRow(column, row);
        this.numberLocks[row][column] = lock;
    }

    /**
     * Sets the selected number.
     * 
     * @precondition number >= MIN_INDEX && number <= PUZZLE_SIZE
     * @postcondition this.getSelectedNumber() == number
     * 
     * @param number
     */
    public void setSelectedNumber(int number) {
        this.checkNumber(number);
        this.selectedNumber = number;
    }

    private void checkNumber(int number) {
        if (number < MIN_INDEX) {
            throw new IllegalArgumentException("number cannot be less than 0");
        }
        if (number > PUZZLE_SIZE) {
            throw new IllegalArgumentException("number cannot be greater than 9");
        }
    }

    /**
     * Checks to see if game is complete.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return [true] iff the game has been completed, otherwise [false]
     */
    public boolean isComplete() {
       
        if (!this.isinRange(this.numbers)) {
            return false;
        } 

      boolean[] unique = new boolean[PUZZLE_SIZE + 1];
 
       if (!this.checkUniqueValues(unique)) {
        return false;
       }
        for (int i = 0; i < PUZZLE_SIZE - 2; i += 3) {

            for (int j = 0; j < PUZZLE_SIZE - 2; j += 3) {

                Arrays.fill(unique, false);
                for (int k = 0; k < 3; k++) {
                    for (int e = 0; e < 3; e++) {
                        
                        int x = i + k;
                        int y = j + e;
                        int value = this.numbers[x][y];
                        if (unique[value]) {
                            return false;
                        }
                        unique[value] = true;
                    }
                }
            }
        }
    
        return true;


    }


    private boolean checkUniqueValues(boolean[] unique) {
        for (int i = 0; i < PUZZLE_SIZE; i++) {
            Arrays.fill(unique, false);

            for (int j = 0; j < PUZZLE_SIZE; j++) {
                int value = this.numbers[i][j];
                if (unique[value]) {
                    return false;
                }
                unique[value] = true;
            }
        }
        for (int i = 0; i < PUZZLE_SIZE; i++) {
            Arrays.fill(unique, false);
    
            for (int j = 0; j < PUZZLE_SIZE; j++) {

                int value = this.numbers[j][i];

                if (unique[value]) {
                    return false;
                }
                unique[value] = true;
            }
        }
        return true;
    }
    private boolean isinRange(int[][] puzzle) {
        for (int i = 0; i < PUZZLE_SIZE; i++) {
            for (int j = 0; j < PUZZLE_SIZE; j++) {
                
            
                if (puzzle[i][j] <= 0 || puzzle[i][j] > 9) {
                    return false;
                }
            }
        }
    return true;
    }


    /**
     * Checks to see if number is locked.
     * 
     * @precondition column >= MIN_INDEX && column < PUZZLE_SIZE && row >= MIN_INDEX
     *               && row < PUZZLE_SIZE
     * @postcondition None
     * 
     * @param column The column to be set.
     * @param row    The row to be set.
     * @return true or false depending on locked state.
     */
    public boolean isNumberLocked(int column, int row) {
        this.checkColumnAndRow(column, row);
        return this.numberLocks[row][column];
    }

    /**
     * Gets the answer for the specified position.
     * 
     * @precondition column >= MIN_INDEX && column < PUZZLE_SIZE && row >= MIN_INDEX
     *               && row < PUZZLE_SIZE
     * @postcondition None
     * 
     * @param column The column to be set.
     * @param row    The row to be set.
     * @return The answer for the coord.
     */
    public int getAnswerForPosition(int column, int row) {
        this.checkColumnAndRow(column, row);
        return this.defaultAnswer[row][column];
    }

}
