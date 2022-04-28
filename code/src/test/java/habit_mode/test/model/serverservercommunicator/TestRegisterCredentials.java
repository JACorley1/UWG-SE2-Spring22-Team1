package habit_mode.test.model.serverservercommunicator;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Random;

import org.junit.jupiter.api.Test;

import habit_mode.model.SuccessCode;
import habit_mode.model.ServerCommunicator;
import habit_mode.model.ServerServerCommunicator;

public class TestRegisterCredentials {
    @Test
    void testValidCredentials(){
        ServerCommunicator communicator = new ServerServerCommunicator("tcp://*:5550");
        TrueMockServer server = new TrueMockServer(5550);
        server.start();
        Random rand = new Random();

        SuccessCode code = communicator.registerCredentials(rand.nextInt() + "", "password", "email");
        server.interrupt();
        assertEquals(SuccessCode.OKAY, code);

    }
}
