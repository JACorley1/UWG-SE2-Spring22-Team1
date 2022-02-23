package habit_mode.test.view_model;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.view_model.HabitViewModel;

class TestSetHabitCompletion {
    @Test
    void testSetHabitCompletionWithAValueSelected() {
        HabitViewModel viewModel = new HabitViewModel();
        String testString = "Hello!";
        viewModel.habitNameProperty().set(testString);
        viewModel.frequencyProperty().set(Frequency.WEEKLY);
        viewModel.addHabit();
        viewModel.selectedHabitProperty().set(viewModel.habitListProperty().getValue().get(0));

        viewModel.setHabitCompletion();

        assertEquals(true, viewModel.selectedHabitProperty().getValue().isComplete(), "Checking that the completion state of the selected habit was changed");
    }

    @Test
    void testSetHabitCompletionWithNoValueSelected() {
        HabitViewModel viewModel = new HabitViewModel();
        viewModel.frequencyProperty().set(Frequency.MONTHLY);
        viewModel.habitNameProperty().set("Test");
        viewModel.addHabit();

        assertThrows(
                        IllegalArgumentException.class, 
                        ()->{
                            viewModel.setHabitCompletion();
                        }
                    );
    }

    @Test
    void testSetHabitCompletionWithEmptyCollection() {
        HabitViewModel viewModel = new HabitViewModel();
        Habit selectedHabit = new Habit("TestHabit", Frequency.DAILY);
        viewModel.selectedHabitProperty().set(selectedHabit);
         
        assertThrows(
                        IllegalArgumentException.class, 
                        ()->{
                            viewModel.setHabitCompletion();
                        }
                    );
    }
}