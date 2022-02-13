package code.viewModel

/** The habitViewModel class
 * 
 * @author	CS 3212
 * @version Spring 2022
 */
public class HabitViewModel {
    private ObjectProperty<Frequency> frequencyProperty;
	private ListProperty<Habit> habitList;
	private StringProperty habitNameProperty;
	/** Creates a new habit
	 * @precondition: string != null && string != string.isEmpty()
	 * @postcondition: this.getText() = string, this.getCompletionStatus() = false, this.getFrequency() = frequency;
	 */
	public HabitViewModel () {

	}
}