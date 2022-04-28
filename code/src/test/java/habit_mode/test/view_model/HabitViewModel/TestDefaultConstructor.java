package habit_mode.test.view_model.HabitViewModel;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;


import habit_mode.model.ServerServerCommunicator;
import habit_mode.view_model.HabitViewModel;


public class TestDefaultConstructor {
    @Test
    void TestDefaultConstructor() {
        HabitViewModel viewModel = new HabitViewModel();
        assertEquals(ServerServerCommunicator.class, viewModel.getServerCommunicator().getClass());
    }
}
