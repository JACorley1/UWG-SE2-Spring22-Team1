package habit_mode.test.view_model.HabitViewModel;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.local_implementation.LocalServerCommunicator;
import habit_mode.view_model.HabitViewModel;

public class TestUpdateHabit {
    @Test
    void testUpdateHabitWithNewTextAndFrequency() {
        HabitViewModel viewModel = new HabitViewModel(new LocalServerCommunicator());
        String testString = "Hello!";
        viewModel.habitNameProperty().set(testString);
        viewModel.dailySelectedProperty().set(true);

        viewModel.addHabit();
        viewModel.dailySelectedProperty().set(false);

        viewModel.selectedHabitProperty().set(viewModel.habitListProperty().get(0));
        testString = "Goodbye!";
        viewModel.removeHabitNameProperty().set(testString);
        viewModel.removeWeeklySelectedProperty().set(true);
        viewModel.updateHabit(0);

        assertEquals(testString, viewModel.habitListProperty().get(0).getText(), "Checking that the text of the habit was updated to the list");
        assertEquals(Frequency.WEEKLY, viewModel.habitListProperty().get(0).getFrequency(), "Checking that the Frequency of the habit was updated to the list");
        assertEquals(1, viewModel.habitListProperty().size(), "Checking that the original size of the habit list is still the same after updating a habit.");
    }

    @Test
    void testWhenIndexIsGreaterThanTheSizeOfTheHabitList() {
        HabitViewModel viewModel = new HabitViewModel(new LocalServerCommunicator());       
        String testString = "Hello!";
        viewModel.habitNameProperty().set(testString);
        viewModel.dailySelectedProperty().set(true);
        viewModel.addHabit();
        assertThrows(
            IllegalArgumentException.class, 
            ()->{
                viewModel.updateHabit(1);
            }
        );
    }
}
