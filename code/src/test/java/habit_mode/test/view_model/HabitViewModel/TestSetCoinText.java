package habit_mode.test.view_model.HabitViewModel;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import habit_mode.model.ServerCommunicator;
import habit_mode.model.local_implementation.LocalServerCommunicator;
import habit_mode.view_model.HabitViewModel;

public class TestSetCoinText {

    @Test
    void testSetHabitCompletionWithAValueSelected() {
        HabitViewModel viewModel = new HabitViewModel();
        ServerCommunicator serverCommunicator = new LocalServerCommunicator();
        serverCommunicator.setCoins(10);
        var testString = "Coins: 10";
        assertEquals(
                testString,
                viewModel.setCoinText(),
                "Checking that the string is what is correct value of coins");

    }
}
