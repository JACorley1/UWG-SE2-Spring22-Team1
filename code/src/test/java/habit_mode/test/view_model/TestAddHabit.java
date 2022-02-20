package habit_mode.test.view_model;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.view_model.HabitViewModel;

class TestAddHabit {
	@Test
	void testAddHabitWithValidPropertyValues() {
        HabitViewModel viewModel = new HabitViewModel();
		String testString = "Hello!";
        viewModel.habitNameProperty().set(testString);
		viewModel.frequencyProperty().set(Frequency.WEEKLY);

        viewModel.addHabit();

		assertEquals(1, viewModel.habitListProperty().getValue().size(), "Checking that the habit was added to the list");
	}

	@Test
	void testAddHabitWithNullStringProperty() {
		HabitViewModel viewModel = new HabitViewModel();
		viewModel.habitNameProperty().set(null);
		viewModel.frequencyProperty().set(Frequency.MONTHLY);
		assertThrows(
			IllegalArgumentException.class, 
			()->{
				viewModel.addHabit();
			}
		);
	}

	@Test
	void testAddHabitWithEmptyStringProperty() {
		HabitViewModel viewModel = new HabitViewModel();
		viewModel.habitNameProperty().set("");
		viewModel.frequencyProperty().set(Frequency.MONTHLY);
		assertThrows(
			IllegalArgumentException.class, 
			()->{
				viewModel.addHabit();
			}
		);
	}
}