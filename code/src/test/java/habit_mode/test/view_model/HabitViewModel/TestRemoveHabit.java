package habit_mode.test.view_model.HabitViewModel;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import habit_mode.view_model.HabitViewModel;

class TestRemoveHabit {
    @Test
    void testRemoveDailyHabitWithValidPropertyValues() {
    }

    @Test
    void testRemoveWeeklyHabitWithValidPropertyValues() {
    }

    @Test
    void testRemoveMonthlyHabitWithValidPropertyValues() {
    }

    @Test
    void testRemoveHabitWithNullStringProperty() {
        HabitViewModel viewModel = new HabitViewModel();
        viewModel.selectedHabitProperty().set(null);

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
}
