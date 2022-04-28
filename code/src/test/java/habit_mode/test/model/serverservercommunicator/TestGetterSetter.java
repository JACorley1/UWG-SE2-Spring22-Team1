package habit_mode.test.model.serverservercommunicator;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

import habit_mode.model.ServerServerCommunicator;

public class TestGetterSetter {
    @Test
    void testGetGson() {
        ServerServerCommunicator communicator = new ServerServerCommunicator("tcp://*:5551");
        assertTrue(communicator.getGson() != null);
    }

    @Test
    void testGetJsonMessage() {
        ServerServerCommunicator communicator = new ServerServerCommunicator("tcp://*:5551");
        assertTrue(communicator.getJsonMessage() == null);
    }

    @Test
    void testGetSocket() {
        ServerServerCommunicator communicator = new ServerServerCommunicator("tcp://*:5551");
        assertTrue(communicator.getSocket() != null);
    }

    @Test
    void testGetContext() {
        ServerServerCommunicator communicator = new ServerServerCommunicator("tcp://*:5551");
        assertTrue(communicator.getContext() != null);
    }

    @Test
    void testSetToken() {
        ServerServerCommunicator communicator = new ServerServerCommunicator("tcp://*:5551");
        communicator.setToken("token");
        assertEquals("token", communicator.getToken());
    }
}
