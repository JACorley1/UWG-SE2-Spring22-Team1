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

	@FXML
    private Button sudokuButton;
    @FXML
    private Button habitListButton;
    @FXML
    private Button settingsButton;
    @FXML
    private Label moneyLabel;
    @FXML
    private Button backButton;
    @FXML
    private Label habitScreenLabel;
    @FXML
    private ListView<?> habitListViewtha;


	/** Creates a new habit
	 * @precondition: string != null && string != string.isEmpty()
	 * @postcondition: this.getText() = string, this.getCompletionStatus() = false, this.getFrequency() = frequency;
	 */
	public HabitViewModel () {
		
	}

	@FXML
    void backButtonClicked(ActionEvent event) {

    }

    @FXML
    void habitListButtonSelected(ActionEvent event) {

    }

    @FXML
    void settingsButtonClicked(ActionEvent event) {

    }

    @FXML
    void sudokuButtonSelected(ActionEvent event) {

    }
}