package habit_mode.test.view_model.HabitViewModel;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import habit_mode.model.local_implementation.LocalServerCommunicator;
import habit_mode.view_model.HabitViewModel;

class TestAddHabit {
    @Test
    void testAddDailyHabitWithValidPropertyValues() {
        HabitViewModel viewModel = new HabitViewModel(new LocalServerCommunicator());
        String testString = "Hello!";
        viewModel.habitNameProperty().set(testString);
        viewModel.dailySelectedProperty().set(true);

        viewModel.addHabit();

        assertEquals(1, viewModel.habitListProperty().getValue().size(), "Checking that the habit was added to the list");
    }

    @Test
    void testAddWeeklyHabitWithValidPropertyValues() {
        HabitViewModel viewModel = new HabitViewModel(new LocalServerCommunicator());
        String testString = "Hello!";
        viewModel.habitNameProperty().set(testString);
        viewModel.weeklySelectedProperty().set(true);

        viewModel.addHabit();

        assertEquals(1, viewModel.habitListProperty().getValue().size(), "Checking that the habit was added to the list");
    }

    @Test
    void testAddMonthlyHabitWithValidPropertyValues() {
        HabitViewModel viewModel = new HabitViewModel(new LocalServerCommunicator());
        String testString = "Hello!";
        viewModel.habitNameProperty().set(testString);
        viewModel.monthlySelectedProperty().set(true);

        viewModel.addHabit();

        assertEquals(1, viewModel.habitListProperty().getValue().size(), "Checking that the habit was added to the list");
    }

    @Test
    void testAddHabitWithNullStringProperty() {
        HabitViewModel viewModel = new HabitViewModel(new LocalServerCommunicator());
        viewModel.habitNameProperty().set(null);

        assertAll(
            () -> {
                assertThrows(
                    IllegalArgumentException.class, 
                    ()->{ viewModel.addHabit(); }
                );
            },
            () -> {
                assertTrue(viewModel.errorVisibleProperty().get(), 
                "Check if the error text is displayed.");
            },
            () -> {
                assertFalse(viewModel.popupVisibleProperty().get(), 
                "Check if the popup is not displayed.");
            }
        );
    }

    @Test
    void testAddHabitWithEmptyStringProperty() {
        HabitViewModel viewModel = new HabitViewModel(new LocalServerCommunicator());
        viewModel.habitNameProperty().set("");

        assertAll(
            () -> {
                assertThrows(
                    IllegalArgumentException.class, 
                    ()->{ viewModel.addHabit(); }
                );
            },
            () -> {
                assertTrue(viewModel.errorVisibleProperty().get(), 
                "Check if the error text is displayed.");
            },
            () -> {
                assertFalse(viewModel.popupVisibleProperty().get(), 
                "Check if the popup is not displayed.");
            }
        );
    }
}