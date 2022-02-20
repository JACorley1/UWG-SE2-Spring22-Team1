package habit_mode.model;

/** The habit class
 * 
 * @author	CS 3212
 * @version Spring 2022
 */
public class Habit {
	public static final String NULL_TEXT_ERROR = "text for the habit cannot be null";
	public static final String EMPTY_TEXT_ERROR = "text for the habit cannot be empty";
	private String text;
	private boolean complete;
	private Frequency completionFrequency;

	/** Creates a new habit.
	 * 
	 * @precondition text != null && text != string.isEmpty()
	 * @postcondition this.getText() = text, this.isComplete() = false, this.getFrequency() = frequency;
	 * 
	 * @param text The text to display for the habit.
	 * @param frequency How frequently the habit should be completed.
	 */
	public Habit(String text, Frequency frequency) {
		this.checkString(text);
		this.text = text;
		this.complete = false;
		this.completionFrequency = frequency;
	}

	/** Gets the text of the habit.
	 * 
	 * @precondition None
	 * @postcondition None
	 * 
	 * @return The text of the habit
	 */
	public String getText() {
		return this.text;
	}

	/** Gets the completion status of the habit.
	 * 
	 * @precondition None
	 * @postcondition None
	 * 
	 * @return the completion status of the habit.
	 */
	public boolean isComplete() {
		return this.complete;
	}

	/** Gets the completion frequency of the habit
	 * 
	 * @precondition none
	 * @postcondition none
	 * 
	 * @return the completion frequency of the habit
	 */
	public Frequency getFrequency() {
		return this.completionFrequency;
	}

	/** Sets the completion frequency of the habit to the desired frequency
	 * 
	 * @precondition none
	 * @postcondition this.getFrequency() = frequency
	 * 
	 * @param frequency How frequently the habit should be completed.
	 */
	public void setFrequency(Frequency frequency) {
		this.completionFrequency = frequency;
	}

	/** Sets the text for the habit with the text provided
	 * 
	 * @precondition text != string.isEmpty() && text != null
	 * @postcondition this.getText() = string;
	 * 
	 * @param text The display text for the habit.
	 */
	public void setText(String text) {
		this.checkString(text);
		this.text = text;
	}

	/** Toggles the completion status of the habit
	 * 
	 * @precondition none
	 * @postcondition this.isComplete() == !this.isComplete()@pre
	 */
	public void toggleCompletionStatus() {
		this.complete = !this.complete;
	}

	private void checkString(String string) {
		if (string == null) {
			throw new IllegalArgumentException(NULL_TEXT_ERROR);
		}
		if (string.isEmpty()) {
			throw new IllegalArgumentException(EMPTY_TEXT_ERROR);
		}
	}
}
