package habit_mode.model.sudoku;

/**
 * The soduku move class
 * 
 * @author Team 1
 * @version Spring 2022
 */
public class SudokuMove {

    public static final int PUZZLE_SIZE = 9;
    public static final int MIN_INDEX = 0;
    public static final int MAX_INDEX = 8;
    public static final int MAX_VALUE = 9;

    private int column;
    private int row;
    private int prevNumber;

    /**
     * Sudoku move constructor.
     * 
     * @precondition column >= 0 && row >= 0 && prevNumber >= 0
     * @postcondition this.getColumn() == column && this.getRow() == row &&
     *                this.getPrevNumber() == prevNumber
     * 
     * @param column     the column
     * @param row        the row
     * @param prevNumber the previous number
     */
    public SudokuMove(int column, int row, int prevNumber) {
        this.checkConstructor(column, row, prevNumber);
        this.column = column;
        this.row = row;
        this.prevNumber = prevNumber;
    }

    private void checkConstructor(int column, int row, int prevNumber) {
        if (column < MIN_INDEX) {
            throw new IndexOutOfBoundsException("column cannot be less than 0");
        }
        if (column > MAX_INDEX) {
            throw new IndexOutOfBoundsException("column must be less than or equal to 8");
        }
        if (row < MIN_INDEX) {
            throw new IndexOutOfBoundsException("row must be between 0 and 8");
        }
        if (row > MAX_INDEX) {
            throw new IndexOutOfBoundsException("row must be less than or equal to 8");
        }
        if (prevNumber < MIN_INDEX) {
            throw new IllegalArgumentException("column can not be less than 0 and 9");
        }
        if (prevNumber > MAX_VALUE) {
            throw new IllegalArgumentException("column must be less than or equal to 9");
        }
    }

    /**
     * Gets the column for the move.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return The column.
     */
    public int getColumn() {
        return this.column;
    }

    /**
     * Gets the row for the move.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return The row.
     */
    public int getRow() {
        return this.row;
    }

    /**
     * Gets the previous number for the move.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return The previous number.
     */
    public int getPrevNumber() {
        return this.prevNumber;
    }

}
