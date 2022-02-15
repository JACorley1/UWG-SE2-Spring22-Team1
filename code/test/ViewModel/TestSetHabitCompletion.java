package code.test.ViewModel;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import edu.westga.cs3212.habit_mode.model.Habit;
import edu.westga.cs3212.habit_mode.model.Frequency;
import code.viewModel.HabitViewModel;

class TestSetHabitCompletion {
	@Test
	void testSetHabitCompletionWithAValueSelected() {
        HabitViewModel viewModel = new HabitViewModel();
		String testString = "Hello!"
        this.viewModel.habitNameProperty().set(testString);
		this.viewModel.frequencyProperty().set(Frequency.WEEKLY)
        this.viewModel.addHabit();
        this.viewModel.selectedHabitProperty().set(this.viewModel.habitListProperty().getValue().get(0);)

        this.viewModel.setHabitCompletion();

        assertEquals(true, this.viewModel.selectedHabitProperty.isComplete(), "Checking that the completion state of the selected habit was changed");
	}

    @Test
	void testSetHabitCompletionWithNoValueSelected() {
		HabitViewModel viewModel = new HabitViewModel();
		this.viewModel.frequencyProperty().set(Frequency.MONTHLY);
        this.viewModel.habitNameProperty().set("Test");
        this.viewModel.addHabit();

		assertThrows(
						IllegalArgumentException.class, 
						()->{
							this.viewModel.setHabitCompletion();
						}
					);
	}

    @Test
	void testSetHabitCompletionWithEmptyCollection() {
		HabitViewModel viewModel = new HabitViewModel();
        Habit selectedHabit = new Habit("TestHabit", Frequency.DAILY);
        this.viewModel.selectedHabitProperty().set(selectedHabit);
         
		assertThrows(
						IllegalArgumentException.class, 
						()->{
							this.viewModel.setHabitCompletion();
						}
					);
	}
}