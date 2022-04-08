package habit_mode.test.view_model.LoginScreenViewModel;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import habit_mode.model.ServerCommunicator;
import habit_mode.model.ServerServerCommunicator;
import habit_mode.model.local_implementation.LocalServerCommunicator;
import habit_mode.view_model.LoginScreenViewModel;

public class TestDefaultConstructor {
    @Test
    void TestDefaultConstructor() {
        LoginScreenViewModel viewModel = new LoginScreenViewModel();
        assertEquals(ServerServerCommunicator.class, viewModel.getServerCommunicator().getClass());
    }
}

