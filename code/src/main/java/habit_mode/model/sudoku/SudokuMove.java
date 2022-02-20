package habit_mode.model.sudoku;

/**
 * The soduku move class
 * 
 * @author Matthew Thompson
 * @version spring 2022
 */
public class SudokuMove {
    private int column;
    private int row;
    private int prevNumber;

    /**
     * Sudoku move constructor
     * 
     * @param column     the column
     * @param row        the row
     * @param prevNumber the previous number
     * @precondition column >= 0 && row >= 0 && prevNumber >= 0
     * @postcondition this.column = column && this.row = row && this.prevNumber = prevNumber
     */
    public SudokuMove(int column, int row, int prevNumber) {
        this.checkConstructor(column, row, prevNumber);
        this.column = column;
        this.row = row;
        this.prevNumber = prevNumber;
    }

    private void checkConstructor(int column, int row, int prevNumber) {
        if (column < 0) {
            throw new IllegalArgumentException("column cannot be less than 0");
        }
        if (column > 8) {
            throw new IllegalArgumentException("column must be less than or equal to 8");
        }
        if (row < 0) {
            throw new IllegalArgumentException("row must be between 0 and 8");
        }
        if (row > 8) {
            throw new IllegalArgumentException("row must be less than or equal to 8");
        }
        if (prevNumber < 0) {
            throw new IllegalArgumentException("column can not be less than 0 and 9");
        }
        if (prevNumber > 9) {
            throw new IllegalArgumentException("column must be less than or equal to 9");
        }
    }

    /**
     * gets the column for the move
     * @precondition none
     * @postcondition none
     * @return the column
     */
    public int getColumn() {
        return this.column;
    }

    /**
     * gets the row for the move
     * @precondition none
     * @postcondition none
     * @return the row
     */
    public int getRow() {
        return this.row;
    }

    /**
     * gets the previous number for the move
     * @precondition none
     * @postcondition none
     * @return the previous number
     */
    public int getPrevNumber() {
        return this.prevNumber;
    }

}
