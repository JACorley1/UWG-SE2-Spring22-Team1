package habit_mode.model.local_implementation;

import java.util.HashMap;
import java.util.List;

import habit_mode.model.Habit;
import habit_mode.model.HabitManager;
import habit_mode.model.ServerCommunicator;
import habit_mode.model.SuccessCode;
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

    private static final String NEGATIVE_COIN_AMOUNT = "coins must not be negative";
    private static final String USERNAME = "username";
    private static final String PASSWORD = "password";
    private static final String EMAIL = "email";

    private static int coins = 0;
    private static HabitManager habits = new HabitManager();
    private static SudokuPuzzle storedPuzzle = null;
    private static boolean receivedBonus = false;
    private static HashMap<String, String> registry = new HashMap<String, String>();
    private static SuccessCode successCode;

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
    public SuccessCode validateLogin(String username, String password) {
        successCode = SuccessCode.OKAY;

        if (username == null || username.isBlank() || !registry.containsValue(username) || password == null
            || password.isBlank() || !registry.containsValue(password)) {
            successCode = SuccessCode.INVALID_LOGIN_CREDENTIALS;
        }

        return successCode;
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
    public SuccessCode addHabit(Habit habit) {
        if (habit == null) {
            successCode = SuccessCode.INVALID_HABIT_NAME;
            return successCode;
        }


        Habit clonedHabit = new Habit(habit.getText(), habit.getFrequency());
        clonedHabit.completionProperty().set(habit.isComplete());
        habits.add(clonedHabit);
        successCode = SuccessCode.OKAY;

        return successCode;
    }

    @Override
    public SuccessCode removeHabit(Habit habit) {
        if (habit == null) {
            successCode = SuccessCode.INVALID_HABIT_NAME;
            return successCode;
        }
        if (!habits.contains(habit)) {
            successCode = SuccessCode.NO_HABIT_FOUND;
            return successCode;
        }

        habits.remove(habit);
        successCode = SuccessCode.OKAY;
        return successCode;
    }

    @Override
    public SuccessCode completeHabit(Habit habit) {
        if (habit == null) {
            successCode = SuccessCode.INVALID_HABIT_NAME;
            return successCode;
        }
        if (!habits.contains(habit)) {
            successCode = SuccessCode.NO_HABIT_FOUND;
            return successCode;
        }

        Habit storedHabit = this.getServerSideHabit(habit);

        if (storedHabit.isComplete()) {
            successCode = SuccessCode.OKAY;
            return successCode;
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
        successCode = SuccessCode.OKAY;
        return successCode;
    }

    @Override
    public SuccessCode updateSudokuPuzzle(SudokuPuzzle puzzle) {
        LocalServerCommunicator.storedPuzzle = puzzle;
        successCode = SuccessCode.OKAY;
        return successCode;
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
    public SuccessCode registerCredentials(String username, String password, String email) {
        if (username == null || username.isBlank()) {
            successCode = SuccessCode.INVALID_USERNAME;
        } else if (password == null || password.isBlank()) {
            successCode = SuccessCode.INVALID_PASSWORD;
        } else if (email == null || email.isBlank()) {
            successCode = SuccessCode.INVALID_EMAIL;
        } else if (registry.containsValue(username)) {
            successCode = SuccessCode.USERNAME_ALREADY_EXISTS;
        } else {
            successCode = SuccessCode.OKAY;
            registry.put(USERNAME, username);
            registry.put(PASSWORD, password);
            registry.put(EMAIL, email);
        }
        return successCode;
    }

    @Override
    public SudokuPuzzle generateSudokuPuzzle() {
        return null;
    }
}
