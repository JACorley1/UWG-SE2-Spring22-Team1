package habit_mode.test.model.local_implementation.LocalServerCommunicator;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import habit_mode.model.SuccessCode;
import habit_mode.model.local_implementation.LocalServerCommunicator;

public class TestUpdateSudokuPuzzle {
    @Test
    void testUpdatePuzzle() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        
        assertEquals(communicator.updateSudokuPuzzle(null), SuccessCode.OKAY, "Checks if the puzzle was updated");
    }
}
