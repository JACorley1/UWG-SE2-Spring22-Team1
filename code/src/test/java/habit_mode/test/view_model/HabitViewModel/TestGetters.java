package habit_mode.test.view_model.HabitViewModel;

import org.junit.jupiter.api.Test;

import habit_mode.view_model.HabitViewModel;

public class TestGetters {
    @Test
    void testDailySelectedProperty() {
        HabitViewModel viewModel = new HabitViewModel();
        viewModel.dailySelectedProperty();
    }

    @Test
    void testWeeklySelectedProperty() {
        HabitViewModel viewModel = new HabitViewModel();
        viewModel.weeklySelectedProperty();
    }

    @Test
    void testMonthlySelectedProperty() {
        HabitViewModel viewModel = new HabitViewModel();
        viewModel.monthlySelectedProperty();
    }

    @Test
    void testCoinsLabelProperty() {
        HabitViewModel viewModel = new HabitViewModel();
        viewModel.coinsLabelProperty();
    }

    @Test
    void testRemoveWeeklySelectedProperty() {
        HabitViewModel viewModel = new HabitViewModel();
        viewModel.removeWeeklySelectedProperty();
    }

    @Test
    void testRemoveDailySelectedProperty() {
        HabitViewModel viewModel = new HabitViewModel();
        viewModel.removeDailySelectedProperty();
    }

    @Test
    void testgetServerCommunicator() {
        HabitViewModel viewModel = new HabitViewModel();
        viewModel.getServerCommunicator();
    }
}
