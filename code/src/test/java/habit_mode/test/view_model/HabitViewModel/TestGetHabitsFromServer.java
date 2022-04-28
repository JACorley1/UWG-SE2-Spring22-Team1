package habit_mode.test.view_model.HabitViewModel;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.local_implementation.LocalServerCommunicator;
import habit_mode.view_model.HabitViewModel;

public class TestGetHabitsFromServer {

    @Test
    void testGetNoHabits() {
        LocalServerCommunicator.reset();
        HabitViewModel vm = new HabitViewModel(new LocalServerCommunicator());
        vm.getHabitsFromServer();
        assertEquals(0, vm.habitListProperty().getSize());
        assertEquals(0, vm.completedHabitListProperty().getSize());
    }
    
    @Test
    void testGetCompletedHabits() {
        LocalServerCommunicator.reset();

        HabitViewModel viewModel = new HabitViewModel(new LocalServerCommunicator());      
        String testString = "Hello!";
        viewModel.habitNameProperty().set(testString);

        viewModel.addHabit();
        viewModel.selectedHabitProperty().set(viewModel.habitListProperty().getValue().get(0));

        viewModel.setHabitCompletion(true);
        viewModel.getHabitsFromServer();

        assertEquals(1, viewModel.completedHabitListProperty().getSize());
    }
    
}
