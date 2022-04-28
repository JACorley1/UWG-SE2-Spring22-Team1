package habit_mode.test.view_model.SudokuScreenViewModel;

import org.junit.jupiter.api.Test;


import habit_mode.view_model.SudokuScreenViewModel;

public class TestGetters {
    @Test
    void testDailySelectedProperty() {
        SudokuScreenViewModel viewModel = new SudokuScreenViewModel();
        viewModel.getServerCommunicator();
    }

    @Test
    void testWeeklySelectedProperty() {
        SudokuScreenViewModel viewModel = new SudokuScreenViewModel();
        viewModel.getAuthenticationToken();
    }
}
