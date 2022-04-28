package habit_mode.test.model.serverservercommunicator;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import habit_mode.model.ServerCommunicator;
import habit_mode.model.ServerServerCommunicator;

public class TestBuyHint {
    @Test
    void testBuyingHint() {
        TrueMockServer server = new TrueMockServer(5557);
        ServerCommunicator communicator = new ServerServerCommunicator("tcp://*:5557");
        server.start();

        int[] hint = communicator.buyHint();

        assertEquals(4, hint.length);
    }
}
