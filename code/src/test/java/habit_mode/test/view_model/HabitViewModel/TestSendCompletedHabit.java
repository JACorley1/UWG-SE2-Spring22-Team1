package habit_mode.test.view_model.HabitViewModel;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.local_implementation.LocalServerCommunicator;
import habit_mode.view_model.HabitViewModel;

public class TestSendCompletedHabit {

    @Test
    void testSendCompletedHabit() {
        LocalServerCommunicator.reset();
        HabitViewModel viewModel = new HabitViewModel(true);        
        String testString = "Coins: 70";
        Habit habit = new Habit("text", Frequency.MONTHLY);
        viewModel.habitNameProperty().set("text");
        viewModel.addHabit();
        habit.completionProperty().set(true);
        viewModel.sendCompletedHabit(habit);

        assertEquals(testString,
                viewModel.coinsLabelProperty().getValue().toString(),
                "Checking that the string is matched");
    }

    @Test
    void testSendCompletedHabitWithNullHabit() {
        LocalServerCommunicator.reset();
        HabitViewModel viewModel = new HabitViewModel(true);
        assertThrows(
                IllegalArgumentException.class,
                () -> {
                    viewModel.sendCompletedHabit(null);
                });
    }

}