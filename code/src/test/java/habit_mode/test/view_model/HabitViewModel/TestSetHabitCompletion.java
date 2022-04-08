package habit_mode.test.view_model.HabitViewModel;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.local_implementation.LocalServerCommunicator;
import habit_mode.view_model.HabitViewModel;

class TestSetHabitCompletion {
    @Test
    void testSetHabitCompletionWithAValueSelected() {
        LocalServerCommunicator.reset();
        HabitViewModel viewModel = new HabitViewModel(true);        
        String testString = "Hello!";
        viewModel.habitNameProperty().set(testString);

        viewModel.addHabit();
        viewModel.selectedHabitProperty().set(viewModel.habitListProperty().getValue().get(0));

        viewModel.setHabitCompletion(true);
        assertEquals(
            true, 
            viewModel.selectedHabitProperty().getValue().isComplete(), 
            "Checking that the completion state of the selected habit was changed"
        );
    }

    @Test
    void testSetHabitCompletionWithNoValueSelected() {
        LocalServerCommunicator.reset();
        HabitViewModel viewModel = new HabitViewModel(true);        
        viewModel.habitNameProperty().set("Test");
        viewModel.addHabit();

        assertThrows(
            IllegalArgumentException.class, 
            ()->{
                viewModel.setHabitCompletion(true);
            }
        );
    }

    @Test
    void testSetHabitCompletionWithEmptyCollection() {
        LocalServerCommunicator.reset();
        HabitViewModel viewModel = new HabitViewModel(true);        
        Habit selectedHabit = new Habit("TestHabit", Frequency.DAILY);
        viewModel.selectedHabitProperty().set(selectedHabit);
         
        assertThrows(
            IllegalArgumentException.class, 
            ()->{
                viewModel.setHabitCompletion(true);
            }
        );
    }
}