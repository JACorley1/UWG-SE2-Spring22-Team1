package habit_mode.test.view_model.HabitViewModel;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.view_model.HabitViewModel;

class TestRemoveHabit {
    @Test
    void testRemoveDailyHabitParameterWithValidPropertyValues() {
        HabitViewModel viewModel = new HabitViewModel();
        String testString = "Hello!";
        viewModel.habitNameProperty().set(testString);
        viewModel.dailySelectedProperty().set(true);
        viewModel.addHabit();
        Habit habit = new Habit(testString, Frequency.DAILY);
        
        viewModel.removeHabit(habit);

        assertEquals(0, viewModel.habitListProperty().getValue().size(), "Checking that the habit was removed to the list");
        

    }

    @Test
    void testRemoveWeeklyHabitParameterWithValidPropertyValues() {
        HabitViewModel viewModel = new HabitViewModel();
        String testString = "Hello!";
        viewModel.habitNameProperty().set(testString);
        viewModel.weeklySelectedProperty().set(true);
        viewModel.addHabit();
        Habit habit = new Habit(testString, Frequency.WEEKLY);
        
        viewModel.removeHabit(habit);

        assertEquals(0, viewModel.habitListProperty().getValue().size(), "Checking that the habit was removed to the list");
        
    }

    @Test
    void testRemoveMonthlyHabitParameterWithValidPropertyValues() {
        HabitViewModel viewModel = new HabitViewModel();
        String testString = "Hello!";
        viewModel.habitNameProperty().set(testString);
        viewModel.monthlySelectedProperty().set(true);
        viewModel.addHabit();
        Habit habit = new Habit(testString, Frequency.MONTHLY);
        
        viewModel.removeHabit(habit);

        assertEquals(0, viewModel.habitListProperty().getValue().size(), "Checking that the habit was removed to the list");
        
    }


    @Test
    void testRemoveHabitWithNullStringProperty() {
        HabitViewModel viewModel = new HabitViewModel();
        viewModel.removeHabitNameProperty().set(null);

        assertAll(
                () -> {
                    assertThrows(
                            IllegalArgumentException.class,
                            () -> {
                                viewModel.removeHabit();
                            });
                },
                () -> {
                    assertTrue(viewModel.errorVisibleProperty().get(),
                            "Check if the error text is displayed.");
                },
                () -> {
                    assertFalse(viewModel.popupVisibleProperty().get(),
                            "Check if the popup is not displayed.");
                });
    }

    @Test
    void testRemoveNullHabit() {
        HabitViewModel viewModel = new HabitViewModel();
        assertAll(
                () -> {
                    assertThrows(
                            IllegalArgumentException.class,
                            () -> {
                                viewModel.removeHabit(null);
                            });
                },
                () -> {
                    assertFalse(viewModel.popupVisibleProperty().get(),
                            "Check if the popup is not displayed.");
                });
    }

    @Test
    void testRemoveWeeklyHabitWithValidPropertyValues() {
        HabitViewModel viewModel = new HabitViewModel();
        String testString = "Hello!";
        viewModel.habitNameProperty().set(testString);
        viewModel.weeklySelectedProperty().set(true);
        viewModel.addHabit();
        viewModel.removeHabitNameProperty().set(testString);
        viewModel.removeWeeklySelectedProperty().set(true);

        viewModel.removeHabit();

        assertEquals(0, viewModel.habitListProperty().getValue().size(), "Checking that the habit was removed to the list");
    }


    @Test
    void testRemoveDailyHabitWithValidPropertyValues() {
        HabitViewModel viewModel = new HabitViewModel();
        String testString = "Hello!";
        viewModel.habitNameProperty().set(testString);
        viewModel.dailySelectedProperty().set(true);
        viewModel.addHabit();
        viewModel.removeHabitNameProperty().set(testString);
        viewModel.removeDailySelectedProperty().set(true);

        viewModel.removeHabit();

        assertEquals(0, viewModel.habitListProperty().getValue().size(), "Checking that the habit was removed to the list");
    }

}
