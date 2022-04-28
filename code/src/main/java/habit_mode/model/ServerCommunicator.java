package habit_mode.model;

import java.util.List;

import habit_mode.model.sudoku.SudokuPuzzle;

/** 
 * Contains the base functionality for communicating with the server.
 * 
 * @author  Team 1
 * @version Spring 2022
 */
public abstract class ServerCommunicator {

    /**
     * Adds a set of valid user credentials to the registry.
     * 
     * @precondition username != null && !username.isBlank() && password != null && !password.isBlank() &&
     *               email != null && !email.isBlank()
     * @postcondition tbd 
     * 
     * @param username The username to be registered in the registry. 
     * @param password The password to be associated with the given username.
     * @param email The email address associated with the given credentials.
     * 
     * @return A SuccessCode determined by response from server: 0 if successful, 10-12 if request breaks,
     *         20 if username is taken, 21 if username is invalid, 22 if password is invalid, 23 if email
     *         is invalid, or 15 if an unknown error occurs. 
     */
    public abstract SuccessCode registerCredentials(String username, String password, String email);

    /** 
     * Checks with the server whether a specified username and password pair is valid.
     * 
     * @precondition username != null && !username.isBlank() && password != null && !password.isBlank()
     * @postcondition None
     * 
     * @param username The specified username.
     * @param password The specified password.
     * 
     * @return A SuccessCode determined by response from server: 0 if successful, 10-13 if request breaks,
     *         30 if username or password are invalid, or 15 if an unknown error occurs. 
     */
    public abstract SuccessCode validateLogin(String username, String password);

    /** 
     * Retrieves the user's current coin count from the server.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return The user's current coin count.
     */
    public abstract int getCoins();

    /** 
     * Retrieves a list of the user's habits from the server.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return A list of the user's habits.
     */
    public abstract List<Habit> getHabits();

    /** 
     * Retrieves the user's active game of Sudoku from the server.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return The user's active game if one exists, otherwise null.
     */
    public abstract SudokuPuzzle getSudokuPuzzle();

    /**
     * Generates a new puzzle for the user on Server side and returns it.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return A new puzzle for the user.
     */
    public abstract SudokuPuzzle generateSudokuPuzzle();

    /** 
     * Requests that the server sets the user's wallet to have a specified number of coins.
     * 
     * @precondition amount >= 0
     * @postcondition this.getCoins() == amount
     * 
     * @param amount The new number of coins.
     * @return [true] iff the amount was successfully removed, otherwise [false].
     */
    public abstract boolean setCoins(int amount);

    /** 
     * Adds a new habit to the user's habit list on the server.
     * 
     * @precondition habit != null && habit has not already been added
     * @postcondition this.getHabits().contains(habit)
     * 
     * @param habit The new habit to add.
     * @return A SuccessCode determined by response from server: 0 if successful, 10-13 if request breaks,
     *         50 if habit does not exist, or 15 if an unknown error occurs.
     */
    public abstract SuccessCode addHabit(Habit habit);

    /** 
     * Adds a habit to the user's habit list on the server.
     * 
     * @precondition habit != null
     * @postcondition !this.getHabits().contains(habit)
     * 
     * @param habit The specified habit to remove. 
     * @return A SuccessCode determined by response from server: 0 if successful, 10-13 if request breaks,
     *         50 if habit does not exist, or 15 if an unknown error occurs. 
     */
    public abstract SuccessCode removeHabit(Habit habit);

    /** 
     * Marks a specified habit as completed on the server.
     * 
     * @precondition habit != null
     * @postcondition None
     * 
     * @param habit The specified habit to mark as completed.
     * @return A SuccessCode determined by response from server: 0 if successful, 10-13 if request breaks,
     *         50 if habit does not exist, or 15 if an unknown error occurs.
     */
    public abstract SuccessCode completeHabit(Habit habit);

    /** 
     * Updates the puzzle state saved on the server.
     * 
     * @precondition puzzle != null
     * @postcondition this.getSudokuPuzzle().Equals(puzzle)
     * 
     * @param puzzle The current puzzle state.
     * @return A SuccessCode determined by response from server: 0 if successful, 10-13 if request breaks,
     *         or 15 if an unknown error occurs.
     */
    public abstract SuccessCode updateSudokuPuzzle(SudokuPuzzle puzzle);

    /**
     * Requests a hint from the server. 
     * 
     * @precondition none
     * @postcondition none
     * 
     * @return values An array of 4 integers where each index corresponds to number, row, column, coins respectively.
     */
    public abstract int[] buyHint();
    
}
