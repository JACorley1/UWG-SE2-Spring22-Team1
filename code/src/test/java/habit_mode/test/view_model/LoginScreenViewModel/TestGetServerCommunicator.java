package habit_mode.test.view_model.LoginScreenViewModel;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import habit_mode.model.ServerCommunicator;
import habit_mode.model.local_implementation.LocalServerCommunicator;
import habit_mode.view_model.LoginScreenViewModel;

public class TestGetServerCommunicator {
    @Test
    void testGetServerCommunicator() {
        LoginScreenViewModel viewModel = new LoginScreenViewModel(true);
        ServerCommunicator serverCommunicator = new LocalServerCommunicator();

        viewModel.setServerCommunicator(serverCommunicator);
        assertEquals(serverCommunicator, viewModel.getServerCommunicator(), "Check if the server communicator is correct.");
    }
}
