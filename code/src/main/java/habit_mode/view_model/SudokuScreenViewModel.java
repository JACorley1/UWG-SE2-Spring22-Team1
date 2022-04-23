package habit_mode.view_model;

import habit_mode.model.ServerCommunicator;
import habit_mode.model.ServerServerCommunicator;



public class SudokuScreenViewModel {
    private ServerCommunicator serverCommunicator;
    
    public SudokuScreenViewModel() {
        this.serverCommunicator = new ServerServerCommunicator();
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
