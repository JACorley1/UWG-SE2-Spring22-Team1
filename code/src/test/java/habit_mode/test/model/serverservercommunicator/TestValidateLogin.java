package habit_mode.test.model.serverservercommunicator;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import habit_mode.model.ServerCommunicator;
import habit_mode.model.ServerServerCommunicator;
import habit_mode.model.SuccessCode;

public class TestValidateLogin {
    @Test
    void testValidCredentials(){
        ServerCommunicator communicator = new ServerServerCommunicator();
        
        communicator.registerCredentials("username", "password", "email");

        SuccessCode code = communicator.validateLogin("username", "password");

        assertEquals(SuccessCode.OKAY, code);

    }
}
