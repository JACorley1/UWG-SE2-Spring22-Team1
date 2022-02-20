package habit_mode.test.model.sudoku.sudokuMove;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import habit_mode.model.sudoku.SudokuMove;

public class TestConstructor {
	@Test
	void testConstructorWithValidInput() {
		
		SudokuMove move = new SudokuMove(1,2,3);
		
		assertAll(
			()->{assertEquals(1, move.getColumn(), "checking column");},
			()->{assertEquals(2, move.getRow(), "checking row");},
			()->{assertEquals(3, move.getPrevNumber(), "checking prevNumver");}
		);
	}

	@Test
	void testConstructorWithInvalidColumnLowerBound() {
		assertThrows(
			IllegalArgumentException.class, 
			()->{
				new SudokuMove(-1, 2, 2);
			}
		);
	}

	@Test
	void testConstructorWithInvalidRowLowerBound() {
		assertThrows(
			IllegalArgumentException.class, 
			()->{
				new SudokuMove(2, -1, 3);
			}
		);
	}

    @Test
	void testConstructorWithInvalidPrevNumberLowerBound() {
		assertThrows(
			IllegalArgumentException.class, 
			()->{
				new SudokuMove(2, 6, -1);
			}
		);
	}

    @Test
	void testConstructorWithInvalidColumnUpperBound() {
		assertThrows(
			IllegalArgumentException.class, 
			()->{
				new SudokuMove(9, 2, 2);
			}
		);
	}

	@Test
	void testConstructorWithInvalidRowUpperBound() {
		assertThrows(
			IllegalArgumentException.class, 
			()->{
				new SudokuMove(2, 9, 3);
			}
		);
	}

    @Test
	void testConstructorWithInvalidPrevNumberUpperBound() {
		assertThrows(
			IllegalArgumentException.class, 
			()->{
				new SudokuMove(2, 6, 10);
			}
		);
	}
}
