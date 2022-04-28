package habit_mode.view_model;

import habit_mode.model.ServerCommunicator;
import habit_mode.model.ServerServerCommunicator;

public class TransitionScreenViewModel {

    private ServerCommunicator serverCommunicator;
    
    /** 
     * Creates a new LoginScreenViewModel.
     * 
     * @precondition: None
     * @postcondition: this.serverCommunicator() != null
     */
    public TransitionScreenViewModel() {
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
    
}
