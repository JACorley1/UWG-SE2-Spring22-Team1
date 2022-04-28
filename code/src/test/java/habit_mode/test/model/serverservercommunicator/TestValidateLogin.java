package habit_mode.test.model.serverservercommunicator;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import habit_mode.model.ServerCommunicator;
import habit_mode.model.ServerServerCommunicator;
import habit_mode.model.SuccessCode;

public class TestValidateLogin {
    @Test
    void testValidCredentials(){
        ServerCommunicator communicator = new ServerServerCommunicator("tcp://*:5555");

        TrueMockServer server = new TrueMockServer(5555);
        server.start();
        
        communicator.registerCredentials("username", "password", "email");

        SuccessCode code = communicator.validateLogin("username", "password");
        server.interrupt();
        assertEquals(SuccessCode.OKAY, code);

    }
}
