package habit_mode.view_model;

import habit_mode.model.ServerCommunicator;
import habit_mode.model.ServerServerCommunicator;
import habit_mode.model.sudoku.SudokuPuzzle;



public class SudokuScreenViewModel {
    private ServerCommunicator serverCommunicator;
    private SudokuPuzzle puzzle;
    
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

    public ServerServerCommunicator getServerCommunicator() {
        return (ServerServerCommunicator) this.serverCommunicator;
    }

}
