package code.model;

/** The habit class
 * 
 * @author	CS 3212
 * @version Spring 2022
 */
public class Habit {
	public static final String NULL_TEXT_ERROR = "text for the habit cannot be null";
	public static final String EMPTY_TEXT_ERROR = "text for the habit cannot be empty";
	private String text;
	private boolean isComplete;
	private Frequency completionFrequency;

	/** Creates a new habit
	 * @precondition: string != null && string != string.isEmpty()
	 * @postcondition: this.getText() = string, this.getCompletionStatus() = false, this.getFrequency() = frequency;
	 */
	public Habit (String string, Frequency frequency) {
		this.checkString(string);
		this.text = string;
		this.isComplete = false;
		this.completionFrequency = frequency;
	}

	/**
	 * gets the text of the habit
	 * @precondition: none
	 * @postcondition: none
	 * @return: the text of the habit
	 */
	public String getText() {
		return this.text;
	}

	/** Gets the completion status of the habit 
	 * @precondition: none
	 * @postcondition: none
	 * @return: the completion status of the habit
	 */
	public boolean getCompletionStatus() {
		return this.isComplete;
	}

	/** gets the completion frequency of the habit
	 * @precondition: none
	 * @postcondition: none
	 * @return: the completion frequency of the habit
	 */
	public Frequency getFrequency() {
		return this.completionFrequency;
	}

	/** Sets the completion frequency of the habit to the desired frequency
	 * @precondition: none
	 * @postcondition: this.getFrequency() = frequency
	 */
	public void setFrequency(Frequency frequency) {
		this.completionFrequency = frequency;
	}

	/** Sets the text for the habit with the text provided
	 * @precondition: string != string.isEmpty() && string != null
	 * @postcondition: this.getText() = string;
	 */
	public void setText(String string) {
		this.checkString(string);
		this.text = string;
	}

	/** toggles the completion status of the habit
	 * @precondition: none
	 * @postcondition: this.getIsComplete
	 */
	public void toggleCompletionStatus() {
		if (this.isComplete) {
			this.isComplete = false;
			return;
		} 
		this.isComplete = true;
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
