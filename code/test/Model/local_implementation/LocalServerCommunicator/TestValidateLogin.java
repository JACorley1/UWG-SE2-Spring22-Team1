package code.test.Model.local_implementation.LocalServerCommunicator;


import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.Test;

import code.model.local_implementation.LocalServerCommunicator;

public class TestValidateLogin {
    @Test
    void testValidInformation() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        String username = "username";
        String password = "password";

        boolean result = communicator.validateLogin(username, password);

        assertTrue(result, "Check if the result is correct.");
    }

    @Test
    void testNullUsername() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        String username = null;
        String password = "password";

        assertThrows(
            IllegalArgumentException.class, 
            () -> {communicator.validateLogin(username, password);},
            "Check if an exception is thrown when the username is null."
        );
    }

    @Test
    void testEmptyUsername() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        String username = "";
        String password = "password";

        assertThrows(
            IllegalArgumentException.class, 
            () -> {communicator.validateLogin(username, password);},
            "Check if an exception is thrown when the username is empty."
        );
    }

    @Test
    void testBlankUsername() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        String username = "     ";
        String password = "password";

        assertThrows(
            IllegalArgumentException.class, 
            () -> {communicator.validateLogin(username, password);},
            "Check if an exception is thrown when the username is blank."
        );
    }

    @Test
    void testNullPassword() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        String username = "username";
        String password = null;

        assertThrows(
            IllegalArgumentException.class, 
            () -> {communicator.validateLogin(username, password);},
            "Check if an exception is thrown when the password is null."
        );
    }

    @Test
    void testEmptyPassword() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        String username = "username";
        String password = "";

        assertThrows(
            IllegalArgumentException.class, 
            () -> {communicator.validateLogin(username, password);},
            "Check if an exception is thrown when the password is empty."
        );
    }

    @Test
    void testBlankPassword() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        String username = "username";
        String password = "     ";

        assertThrows(
            IllegalArgumentException.class, 
            () -> {communicator.validateLogin(username, password);},
            "Check if an exception is thrown when the password is blank."
        );
    }
}
