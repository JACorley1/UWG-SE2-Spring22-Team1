package habit_mode.test.model.local_implementation.LocalServerCommunicator;

import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

import habit_mode.model.local_implementation.LocalServerCommunicator;

public class TestUpdateSudokuPuzzle {
    @Test
    void testUpdatePuzzle() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        
        assertTrue(communicator.updateSudokuPuzzle(null), "Checks if the puzzle was updated");
    }
}
