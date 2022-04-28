package habit_mode.test.model.serverservercommunicator;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import habit_mode.model.sudoku.SudokuPuzzle;
import habit_mode.model.ServerServerCommunicator;

public class TestGetSudokuPuzzle {
    @Test
    void testGetPuzzle() {
        TrueMockServer server = new TrueMockServer(5554);
        server.start();
        ServerServerCommunicator communicator = new ServerServerCommunicator("tcp://*:5554");
        SudokuPuzzle puzzle = communicator.generateSudokuPuzzle();
        SudokuPuzzle puzzle1 = communicator.getSudokuPuzzle();

        assertEquals(puzzle.getNumbers().length, puzzle1.getNumbers().length);
    }
}
