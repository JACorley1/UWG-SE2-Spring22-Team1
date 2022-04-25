package habit_mode.test.view_model.SudokuScreenViewModel;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;


import habit_mode.view_model.SudokuScreenViewModel;

class TestConvertLabelsToPuzzle {
    @Test
    void testConvertLabelsToPuzzle() {
        
        SudokuScreenViewModel viewModel = new SudokuScreenViewModel();        

        viewModel.convertLabelsToPuzzle("6", 0, 0);

        assertEquals(6, viewModel.getPuzzle().getNumber(0, 0), "Checking that number is set to the correct number");
        assertEquals(0, viewModel.getPuzzle().getNumber(1, 0), "Checking that number is set to the correct number");
        

    }
}