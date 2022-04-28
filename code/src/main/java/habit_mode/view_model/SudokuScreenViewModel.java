package habit_mode.view_model;

import habit_mode.model.ServerCommunicator;
import habit_mode.model.ServerServerCommunicator;
import habit_mode.model.sudoku.SudokuPuzzle;



/**
 * The view model for the SudokuScreen.
 * 
 * @author Team 1
 * @version Spring 2022
 */
public class SudokuScreenViewModel {
    private ServerCommunicator serverCommunicator;
    private SudokuPuzzle puzzle;
    
    /** 
     * Creates a new LoginScreenViewModel.
     * 
     * @precondition: None
     * @postcondition: this.serverCommunicator() != null
     */
    public SudokuScreenViewModel() {
        this.serverCommunicator = new ServerServerCommunicator();
        this.puzzle = new SudokuPuzzle();

    }

    public SudokuPuzzle getPuzzle() {
        return this.puzzle;
    }

    /**
     * Basic getter for transferring the authentication token.
     * 
     * @return The user's authentication token as a string.
     */
    public String getAuthenticationToken() {
        return ((ServerServerCommunicator) this.serverCommunicator).getToken();
    }

    /**
     * Gets the server communicator.
     * 
     * @precondition None.
     * @postcondition None.
     * 
     * @return the server communicator
     */
    public ServerServerCommunicator getServerCommunicator() {
        return (ServerServerCommunicator) this.serverCommunicator;
    }

    /**
     * Converts the text of the Labels to numbers to store in the numbers matrix for the puzzle
     * 
     * @param text the text to convert
     * @param row the row
     * @param column the column
     */
    public void convertLabelsToPuzzle(String text, int row, int column) {
        this.puzzle.setNumber(Integer.parseInt(text), row, column);
    }

     /**
     * Sets the puzzle.
     * 
     * @precondition None.
     * @postcondition this.puzzle = puzzle.
     * 
     * @param puzzle The puzzle to be set to the viewmodels puzzle.
     */
    public void setPuzzle(SudokuPuzzle puzzle) {
        this.puzzle = puzzle;
    }
}
