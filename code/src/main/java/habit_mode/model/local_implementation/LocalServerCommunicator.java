package habit_mode.model.local_implementation;

import java.util.HashMap;
import java.util.List;

import habit_mode.model.Habit;
import habit_mode.model.HabitManager;
import habit_mode.model.ServerCommunicator;
import habit_mode.model.SuccessCodes;
import habit_mode.model.sudoku.SudokuPuzzle;

/**
 * Stores server information locally, allowing for easy testing without the need
 * of a live server.
 * All instances access the same static information, as though communicating
 * with the same server.
 * To clear the information for unit testing, please use
 * LocalServerCommunicator::reset().
 * 
 * @author Team 1
 * @version Spring 2022
 */
public class LocalServerCommunicator extends ServerCommunicator {
    private static final int COMPLETION_REWARD = 20;
    private static final int FULL_COMPLETION_BONUS = 50;

    private static final String NULL_USERNAME_ERROR = "username must not be null";
    private static final String BLANK_USERNAME_ERROR = "username must not be blank";
    private static final String NULL_PASSWORD_ERROR = "password must not be null";
    private static final String BLANK_PASSWORD_ERROR = "password must not be blank";
    private static final String NULL_HABIT_ERROR = "habit must not be null";
    private static final String NEGATIVE_COIN_AMOUNT = "coins must not be negative";
    private static final String USERNAME = "username";
    private static final String PASSWORD = "password";
    private static final String EMAIL = "email";

    private static int coins = 0;
    private static HabitManager habits = new HabitManager();
    private static SudokuPuzzle storedPuzzle = null;
    private static boolean receivedBonus = false;
    private static HashMap<String, String> registry = new HashMap<String, String>();
    private static SuccessCodes successCode;

    /**
     * Resets static fields stored values to their default state.
     * 
     * @precondition None
     * @postcondition LocalServerCommunicator.getCoins() == 0 &&
     *                LocalServerCommunicator.getPuzzle() == null &&
     *                LocalServerCommunicator.getHabits.isEmpty()
     */
    public static void reset() {
        coins = 0;
        storedPuzzle = null;
        habits.clear();
        registry.clear();
        receivedBonus = false;
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
        return storedPuzzle;
    }

    @Override
    public boolean addHabit(Habit habit) {
        if (habit == null) {
            throw new IllegalArgumentException(NULL_HABIT_ERROR);
        }
        if (habits.contains(habit)) {
            return false;
        }

        Habit clonedHabit = new Habit(habit.getText(), habit.getFrequency());
        clonedHabit.completionProperty().set(habit.isComplete());
        habits.add(clonedHabit);

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

        Habit storedHabit = this.getServerSideHabit(habit);

        if (storedHabit.isComplete()) {
            return false;
        }
        storedHabit.completionProperty().set(true);
        coins += COMPLETION_REWARD;

        if (!receivedBonus) {
            var completed = 0;
            for (Habit currHabit : habits) {
                if (currHabit.isComplete()) {
                    completed++;
                }
            }
            if (completed == habits.size()) {
                coins += FULL_COMPLETION_BONUS;
                receivedBonus = true;
            }
        }
        
        return true;
    }

    @Override
    public boolean updateSudokuPuzzle(SudokuPuzzle puzzle) {
        LocalServerCommunicator.storedPuzzle = puzzle;
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

    /**
     * Gets the server-side version of a given Habit.
     * 
     * @param habit The client-side version of a habit
     * @return The server-side version of a habit if it exists, otherwise null.
     */
    public Habit getServerSideHabit(Habit habit) {
        int index = habits.indexOf(habit);

        return index == -1 ? null : habits.get(index);
    }

    @Override
    public SuccessCodes registerCredentials(String username, String password, String email) {
        if (username == null || username.isBlank()) {
            successCode = SuccessCodes.INVALID_USERNAME;
        } else if (password == null || password.isBlank()) {
            successCode = SuccessCodes.INVALID_PASSWORD;
        } else if (email == null || email.isBlank()) {
            successCode = SuccessCodes.INVALID_EMAIL;
        } else if (registry.containsValue(username)) {
            successCode = SuccessCodes.USERNAME_ALREADY_EXISTS;
        } else {
            successCode = SuccessCodes.OKAY;
            registry.put(USERNAME, username);
            registry.put(PASSWORD, password);
            registry.put(EMAIL, email);
        }
        return successCode;
    }
}
