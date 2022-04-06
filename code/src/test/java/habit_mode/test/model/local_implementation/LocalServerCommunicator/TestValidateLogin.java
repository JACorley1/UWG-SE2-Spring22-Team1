package habit_mode.test.model.local_implementation.LocalServerCommunicator;


import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import habit_mode.model.SuccessCode;
import habit_mode.model.local_implementation.LocalServerCommunicator;

public class TestValidateLogin {
    @Test
    void testValidInformation() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        String username = "username";
        String password = "password";
        communicator.registerCredentials(username, password, "email");
        SuccessCode result = communicator.validateLogin(username, password);

        assertEquals(SuccessCode.OKAY, result, "Check if the result is correct.");
    }

    @Test
    void testNullUsername() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        String username = null;
        String password = "password";

        assertEquals(SuccessCode.INVALID_LOGIN_CREDENTIALS, communicator.validateLogin(username, password));
    }

    @Test
    void testEmptyUsername() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        String username = "";
        String password = "password";

        assertEquals(SuccessCode.INVALID_LOGIN_CREDENTIALS, communicator.validateLogin(username, password));
    }

    @Test
    void testBlankUsername() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        String username = "     ";
        String password = "password";

        assertEquals(SuccessCode.INVALID_LOGIN_CREDENTIALS, communicator.validateLogin(username, password));
    }

    @Test
    void testNullPassword() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        String username = "username";
        String password = null;

        assertEquals(SuccessCode.INVALID_LOGIN_CREDENTIALS, communicator.validateLogin(username, password));
    }

    @Test
    void testEmptyPassword() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        String username = "username";
        String password = "";

        assertEquals(SuccessCode.INVALID_LOGIN_CREDENTIALS, communicator.validateLogin(username, password));
    }

    @Test
    void testBlankPassword() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        String username = "username";
        String password = "     ";

        assertEquals(SuccessCode.INVALID_LOGIN_CREDENTIALS, communicator.validateLogin(username, password));
    }
}
