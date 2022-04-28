package habit_mode.test.model.serverservercommunicator;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import habit_mode.model.sudoku.SudokuPuzzle;
import habit_mode.model.ServerServerCommunicator;

public class TestUpdateSudokuPuzzle {
    @Test
    void testUpdatePuzzle() {
        TrueMockServer server = new TrueMockServer(5556);
        ServerServerCommunicator communicator = new ServerServerCommunicator("tcp://*:5556");
        server.start();
        SudokuPuzzle puzzle = communicator.generateSudokuPuzzle();

        communicator.updateSudokuPuzzle(puzzle);
        int size = communicator.getSudokuPuzzle().getNumbers().length;

        assertEquals(puzzle.getNumbers().length, size);
    }
    
}
