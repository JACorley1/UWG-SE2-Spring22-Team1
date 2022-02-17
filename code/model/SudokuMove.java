/**
 * The soduku move class
 *
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
     */
    public SudokuMove(int column, int row, int prevNumber) {
        this.column = column;
        this.row = row;
        this.prevNumber = prevNumber;
    }

    /**
     * gets the column for the move
     * 
     * @return the column
     */
    public int getColumn() {
        return this.column;
    }

    /**
     * gets the row for the move
     * 
     * @return the row
     */
    public int getRow() {
        return this.row;
    }

    /**
     * gets the previous number for the move
     * 
     * @return the previous number
     */
    public int getPrevNumber() {
        return this.prevNumber;
    }
}
