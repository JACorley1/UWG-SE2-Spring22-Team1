package habit_mode.test.model.local_implementation.LocalServerCommunicator;

import org.junit.jupiter.api.Test;

import habit_mode.model.local_implementation.LocalServerCommunicator;

public class TestGetSudokuPuzzle {
    @Test
    void testGetPuzzle() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        communicator.getSudokuPuzzle();
    }
}
