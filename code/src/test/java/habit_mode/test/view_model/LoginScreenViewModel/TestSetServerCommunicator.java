package habit_mode.test.view_model.LoginScreenViewModel;

import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;

import habit_mode.model.local_implementation.LocalServerCommunicator;
import habit_mode.view_model.LoginScreenViewModel;

public class TestSetServerCommunicator {
    @Test
    void testValidServerCommunicator() {
        LoginScreenViewModel viewModel = new LoginScreenViewModel();
        LocalServerCommunicator serverCommunicator = new LocalServerCommunicator();

        viewModel.setServerCommunicator(serverCommunicator);
    }

    @Test
    void testNullServerCommunicator() {
        LoginScreenViewModel viewModel = new LoginScreenViewModel();

        assertThrows(
            IllegalArgumentException.class,
            () -> {viewModel.setServerCommunicator(null);},
            "Check if an exception is thrown when setting the serverCommunicator to null."
        );
    }
}
