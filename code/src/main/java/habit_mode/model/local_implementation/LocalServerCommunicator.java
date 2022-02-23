package habit_mode.model.local_implementation;

import java.util.ArrayList;
import java.util.List;

import habit_mode.model.Habit;
import habit_mode.model.ServerCommunicator;
import habit_mode.model.SudokuPuzzle;

/** Stores server information locally, allowing for easy testing without the need of a live server.
 *  All instances access the same static information, as though communicating with the same server.
 *  To clear the information for unit testing, please use LocalServerCommunicator::reset().
 * 
 * @author    Team 1
 * @version Spring 2022
 */
public class LocalServerCommunicator extends ServerCommunicator {
    private static final String NULL_USERNAME_ERROR = "username must not be null";
    private static final String BLANK_USERNAME_ERROR = "username must not be blank";
    private static final String NULL_PASSWORD_ERROR = "password must not be null";
    private static final String BLANK_PASSWORD_ERROR = "password must not be blank";
    private static final String NULL_HABIT_ERROR = "habit must not be null";
    private static final String NEGATIVE_COIN_AMOUNT = "coins must not be negative";

    private static int coins = 0;
    private static SudokuPuzzle puzzle = null;
    private static List<Habit> habits = new ArrayList<>();

    public static void reset() {
        coins = 0;
        puzzle = null;
        habits.clear();
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
        return coins;
    }

    @Override
    public List<Habit> getHabits() {
        return habits;
    }

    @Override
    public SudokuPuzzle getSudokuPuzzle() {
        return puzzle;
    }

    @Override
    public boolean addHabit(Habit habit) {
        if (habit == null) {
            throw new IllegalArgumentException(NULL_HABIT_ERROR);
        }
        if (habits.contains(habit)) {
            return false;
        }

        habits.add(habit);
        return true;
    }

    @Override
    public boolean removeHabit(Habit habit) {
        if (habit == null) {
            throw new IllegalArgumentException(NULL_HABIT_ERROR);
        }
        if (!habits.contains(habit)) {
            return false;
        }

        habits.remove(habit);
        return true;
    }

    @Override
    public boolean completeHabit(Habit habit) {
        if (habit == null) {
            throw new IllegalArgumentException(NULL_HABIT_ERROR);
        }
        if (!habits.contains(habit)) {
            return false;
        }

        //Ensures that we edit the habit stored in the "server" when the "server" and the client 
        //have different objects
        int index = habits.indexOf(habit);
        Habit storedHabit = habits.get(index);

        if (storedHabit.isComplete()) {
            return false;
        }

        storedHabit.toggleCompletionStatus();
        return true;
    }

    @Override
    public boolean updateSudokuPuzzle(SudokuPuzzle puzzle) {
        LocalServerCommunicator.puzzle = puzzle;
        return true;
    }

    @Override
    public boolean setCoins(int amount) {
        if (amount < 0) {
            throw new IllegalArgumentException(NEGATIVE_COIN_AMOUNT);
        }

        coins = amount;
        return true;
    }
}
