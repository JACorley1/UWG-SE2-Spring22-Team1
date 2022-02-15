package code.test.ViewModel;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import edu.westga.cs3212.habit_mode.model.Habit;
import edu.westga.cs3212.habit_mode.model.Frequency;
import code.viewModel.HabitViewModel;

class TestAddHabit {
	@Test
	void testAddHabitWithValidPropertyValues() {
        HabitViewModel viewModel = new HabitViewModel();
		String testString = "Hello!"
        this.viewModel.habitNameProperty().set(testString);
		this.viewModel.frequencyProperty().set(Frequency.WEEKLY)

        this.viewModel.addHabit();

		assertEquals(1, this.viewModel.habitListProperty().getValue().size(), "Checking that the habit was added to the list");
	}

	@Test
	void testAddHabitWithNullStringProperty() {
		HabitViewModel viewModel = new HabitViewModel();
		this.viewModel.habitNameProperty().set(null);
		this.viewModel.frequencyProperty().set(Frequency.MONTHLY);
		assertThrows(
						IllegalArgumentException.class, 
						()->{
							this.viewModel.addHabit();
						}
					);
	}

	@Test
	void testAddHabitWithEmptyStringProperty() {
		HabitViewModel viewModel = new HabitViewModel();
		this.viewModel.habitNameProperty().set("");
		this.viewModel.frequencyProperty().set(Frequency.MONTHLY);
		assertThrows(
						IllegalArgumentException.class, 
						()->{
							this.viewModel.addHabit();
						}
					);
	}
}