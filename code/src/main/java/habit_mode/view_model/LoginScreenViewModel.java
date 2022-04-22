package habit_mode.view_model;

import habit_mode.model.ServerCommunicator;
import habit_mode.model.ServerServerCommunicator;
import habit_mode.model.SuccessCode;
import habit_mode.model.local_implementation.LocalServerCommunicator;
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.StringProperty;

/**
 * The view model for the LoginScreen.
 * 
 * @author Team 1
 * @version Spring 2022
 */
public class LoginScreenViewModel {
    private static final String NULL_SERVER_COMMUNICATOR_ERROR = "serverCommunicator must not be null";

    private ServerCommunicator serverCommunicator;
    private StringProperty usernameProperty;
    private StringProperty passwordProperty;
    private StringProperty emailProperty;

    /** 
     * Creates a new LoginScreenViewModel.
     * 
     * @precondition: None
     * @postcondition: this.usernameProperty() != null && 
     *                 this.passwordProperty() != null &&
     *                 this.serverCommunicator() != null
     */
    public LoginScreenViewModel() {
        this.serverCommunicator = new ServerServerCommunicator();
        this.usernameProperty = new SimpleStringProperty();
        this.passwordProperty = new SimpleStringProperty();
        this.emailProperty = new SimpleStringProperty();
    }

    /**
     * A special constructor for use during tests.
     * 
     * @precondition none
     * @postcondition this.serverCommunicator.getClass().equals(LocalServerCommunicator.class) &&
     *                this.usernameProperty() != null && 
     *                this.passwordProperty() != null &&
     *                this.serverCommunicator() != null
     * 
     * @param dummy A boolean value that exists to allow constructor overloading.
     */
    public LoginScreenViewModel(boolean dummy) {
        this.serverCommunicator = new LocalServerCommunicator();
        this.usernameProperty = new SimpleStringProperty();
        this.passwordProperty = new SimpleStringProperty();
        this.emailProperty = new SimpleStringProperty();
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
     * Validates the login information.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return A SuccessCode determined by response from server: 0 if successful, 10-13 if request breaks,
     *         30 if username or password are invalid, or 15 if an unknown error occurs.
     */
    public SuccessCode validateLogin() {
        SuccessCode result = this.serverCommunicator.validateLogin(this.usernameProperty.getValue(), this.passwordProperty.getValue());
        return result;
    }

    /**
     * Gets the username property.
     * 
     * @return The username property.
     */
    public StringProperty usernameProperty() {
        return this.usernameProperty;
    }

    /**
     * Gets the password property.
     * 
     * @return The password property.
     */
    public StringProperty passwordProperty() {
        return this.passwordProperty;
    }

    /**
     * Gets the email property.
     * 
     * @return The email property.
     */
    public StringProperty emailProperty() {
        return this.emailProperty;
    }

    /**
     * Sets the server communicator.
     * 
     * @precondition serverCommunicator != null
     * @postcondition this.getServerCommunicator() == serverCommunicator
     * 
     * @param serverCommunicator The new ServerCommuincator.
     */
    public void setServerCommunicator(ServerCommunicator serverCommunicator) {
        if (serverCommunicator == null) {
            throw new IllegalArgumentException(NULL_SERVER_COMMUNICATOR_ERROR);
        }

        this.serverCommunicator = serverCommunicator;
    }

    /**
     * Gets the server communicator.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return The server communicator.
     */
    public ServerCommunicator getServerCommunicator() {
        return this.serverCommunicator;
    }

    /**
     * Registers the user's credentials into the server
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return  OKAY(0) if everything works fine, USERNAME_ALREADY_EXISTS(20) if the username is already in use
     *          INVALID_USERNAME(21) if the username is invalid, INVALID_PASSWORD(22) if the password is Invalid
     *          INVALID_EMAIL(23) if the email entered is invalid.
     */
    public SuccessCode registerUser() {
        return this.serverCommunicator.registerCredentials(this.usernameProperty.getValue(), this.passwordProperty.getValue(), this.emailProperty.getValue());
    }
}
