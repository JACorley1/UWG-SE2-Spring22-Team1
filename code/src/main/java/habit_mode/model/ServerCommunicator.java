package habit_mode.model;

import java.util.List;

import habit_mode.model.sudoku.SudokuPuzzle;

/** Contains the base functionality for communicating with the server.
 * 
 * @author	Team 1
 * @version Spring 2022
 */
public abstract class ServerCommunicator {

    /** Checks with the server whether a specified username and password pair is valid.
     * 
     * @precondition username != null && !username.isBlank() && password != null && !password.isBlank()
     * @postcondition None
     * 
     * @param username The specified username
     * @param password The specified password
     * 
     * @return [true] iff the provided credentials are a valid pair, otherwise [false]
     */
    public abstract boolean validateLogin(String username, String password);

    /** Retrieves the user's current coin count from the server.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return The user's current coin count
     */
    public abstract int getCoins();

    /** Retrieves a list of the user's habits from the server.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return A list of the user's habits
     */
    public abstract List<Habit> getHabits();

    /** Retrieves the user's active game of Sudoku from the server.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return The user's active game if one exists, otherwise null.
     */
    public abstract SudokuPuzzle getSudokuPuzzle();

    /** Requests that the server sets the user's wallet to have a specified number of coins.
     * 
     * @precondition amount >= 0
     * @postcondition this.getCoins() == amount
     * 
     * @param amount The new number of coins.
     * @return [true] iff the amount was successfully removed, otherwise [false].
     */
    public abstract boolean setCoins(int amount);

    /** Adds a new habit to the user's habit list on the server.
     * 
     * @precondition habit != null && habit has not already been added
     * @postcondition this.getHabits().contains(habit)
     * 
     * @param habit The new habit to add.
     * @return [true] iff the habit was successfully added, otherwise [false].
     */
    public abstract boolean addHabit(Habit habit);

    /** Adds a habit to the user's habit list on the server.
     * 
     * @precondition habit != null
     * @postcondition !this.getHabits().contains(habit)
     * 
     * @param habit The specified habit to remove. 
     * @return [true] iff the habit was successfully removed, otherwise [false].
     */
    public abstract boolean removeHabit(Habit habit);

    /** Marks a specified habit as completed on the server.
     * 
     * @precondition habit != null
     * @postcondition None
     * 
     * @param habit The specified habit to mark as completed.
     * @return [true] iff the habit was successfully completed, otherwise [false].
     */
    public abstract boolean completeHabit(Habit habit);

    /** Updates the puzzle state saved on the server.
     * 
     * @precondition puzzle != null
     * @postcondition this.getSudokuPuzzle().Equals(puzzle)
     * 
     * @param puzzle The current puzzle state.
     * @return [true] iff the puzzle was successfully updated, otherwise [false].
     */
    public abstract boolean updateSudokuPuzzle(SudokuPuzzle puzzle);
}
