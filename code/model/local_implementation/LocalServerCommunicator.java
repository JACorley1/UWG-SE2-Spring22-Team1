package code.model.local_implementation;

import java.util.ArrayList;
import java.util.List;

import code.model.Habit;
import code.model.ServerCommunicator;
import code.model.SudokuPuzzle;

/** Stores server information locally, allowing for easy testing without the need of a live server.
 *  All instances access the same static information, as though communicating with the same server.
 *  To clear the information for unit testing, please use LocalServerCommunicator::reset().
 * 
 * @author	Team 1
 * @version Spring 2022
 */
public class LocalServerCommunicator extends ServerCommunicator {
    private static String NULL_USERNAME_ERROR = "username must not be null";
    private static String BLANK_USERNAME_ERROR = "username must not be blank";
    private static String NULL_PASSWORD_ERROR = "password must not be null";
    private static String BLANK_PASSWORD_ERROR = "password must not be blank";
    private static String NULL_HABIT_ERROR = "habit must not be null";
    private static String NEGATIVE_COIN_AMOUNT = "coins must not be negative";

    private static int COINS = 0;
    private static SudokuPuzzle PUZZLE = null;
    private static List<Habit> HABITS = new ArrayList<>();

    public static void reset() {
        COINS = 0;
        PUZZLE = null;
        HABITS.clear();
    }
    
	@Override
	public boolean validateLogin(String username, String password) {
        if (username == null) {
            throw new IllegalArgumentException(NULL_USERNAME_ERROR);
        }
        if (username.isBlank()) {
            throw new IllegalArgumentException(BLANK_USERNAME_ERROR);
        }
        if (password == null) {
            throw new IllegalArgumentException(NULL_PASSWORD_ERROR);
        }
        if (password.isBlank()) {
            throw new IllegalArgumentException(BLANK_PASSWORD_ERROR);
        }

		return true;
	}

	@Override
	public int getCoins() {
		return COINS;
	}

	@Override
	public List<Habit> getHabits() {
		return HABITS;
	}

	@Override
	public SudokuPuzzle getSudokuPuzzle() {
		return PUZZLE;
	}

	@Override
	public boolean addHabit(Habit habit) {
        if (habit == null) {
            throw new IllegalArgumentException(NULL_HABIT_ERROR);
        }
        if (HABITS.contains(habit)) {
            return false;
        }

        HABITS.add(habit);
		return true;
	}

	@Override
	public boolean removeHabit(Habit habit) {
        if (habit == null) {
            throw new IllegalArgumentException(NULL_HABIT_ERROR);
        }
        if (!HABITS.contains(habit)) {
            return false;
        }

        HABITS.remove(habit);
		return true;
	}

	@Override
	public boolean completeHabit(Habit habit) {
		if (habit == null) {
            throw new IllegalArgumentException(NULL_HABIT_ERROR);
        }
        if (!HABITS.contains(habit)) {
            return false;
        }

        //Ensures that we edit the habit stored in the "server" when the "server" and the client 
        //have different objects
        int index = HABITS.indexOf(habit);
        Habit storedHabit = HABITS.get(index);

        if (storedHabit.isComplete()) {
            return false;
        }

        storedHabit.toggleCompletionStatus();
        return true;
	}

	@Override
	public boolean updateSudokuPuzzle(SudokuPuzzle puzzle) {
        PUZZLE = puzzle;
		return true;
	}

	@Override
	public boolean setCoins(int amount) {
        if (amount < 0) {
            throw new IllegalArgumentException(NEGATIVE_COIN_AMOUNT);
        }

        COINS = amount;
		return true;
	}
}
