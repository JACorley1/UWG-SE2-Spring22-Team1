package habit_mode.view_model;

import java.util.ArrayList;
import java.util.List;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import javafx.beans.property.ListProperty;
import javafx.beans.property.ObjectProperty;
import javafx.beans.property.SimpleListProperty;
import javafx.beans.property.SimpleObjectProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.StringProperty;
import javafx.collections.FXCollections;

/** The habitViewModel class
 * 
 * @author    Team 1
 * @version Spring 2022
 */
public class HabitViewModel {
    private ObjectProperty<Frequency> frequencyProperty;
    private ObjectProperty<Habit> selectedHabitProperty;
    private ListProperty<Habit> habitListProperty;
    private StringProperty habitNameProperty;

    /** Creates a new habit view model
     * @precondition: none
     * @postcondition: this.frequencyProperty() = new SimpleObjectProperty<Frequency>(), this.habitNameProperty() =  new SimpleStringProperty(""), this.habitListProperty() = 
     */
    public HabitViewModel() {
        this.frequencyProperty = new SimpleObjectProperty<Frequency>();
        this.selectedHabitProperty = new SimpleObjectProperty<Habit>();
        this.habitNameProperty =  new SimpleStringProperty("");
        List<Habit> habitList = new ArrayList<Habit>();
        this.habitListProperty = new SimpleListProperty<Habit>(FXCollections.observableArrayList(habitList));
    }

    /** adds a habit to the system
     * @precondition this.habitNameProperty.getValue() != null || ""
     * @postcondition this.habitListProperty().getValue().size() == this.habitListProperty().getValue().size() @pre + 1
     */
    public void addHabit() {
        if (this.habitNameProperty.getValue() == null) {
            throw new IllegalArgumentException(Habit.NULL_TEXT_ERROR);
        }
        if (this.habitNameProperty.getValue().isEmpty()) {
            throw new IllegalArgumentException(Habit.EMPTY_TEXT_ERROR);
        }

        Habit habit = new Habit(this.habitNameProperty.getValue(), this.frequencyProperty.getValue());
        this.habitListProperty.add(habit);
    }

    /** sets the targeted habits completion status
     * @precondition !this.habitListProperty().getValue().isEmpty() && this.selectedHabitProperty().getValue() != null
     * @postcondition this.selectedHabitProperty.getValue().toggleCompletionStatus() == !this.selectedHabitProperty().getValue().toggleCompletionStatus() @pre
     */
    public void setHabitCompletion() {
        if (this.habitListProperty.getValue().isEmpty()) {
            throw new IllegalArgumentException("Cannot modify a value that does not exist in an empty list.");
        }
        if (this.selectedHabitProperty.getValue() == null) {
            throw new IllegalArgumentException("Cannot change the completion status of a null habit.");
        }
        this.selectedHabitProperty.getValue().toggleCompletionStatus();
    }
  
    /** the frequency property
     * @precondition none
     * @postcondition none
     * @return the frequency property
     */
    public ObjectProperty<Frequency> frequencyProperty() {
        return this.frequencyProperty;
    }

    /** the selected habit property
     * @precondition none
     * @postcondition none
     * @return the selected habit property
     */
    public ObjectProperty<Habit> selectedHabitProperty() {
        return this.selectedHabitProperty;
    }

    /** the habit list property
     * @precondition none
     * @postcondition none 
     * @return the habit list property
     */
    public ListProperty<Habit> habitListProperty() {
        return this.habitListProperty;
    }

    /** the habit name property
     * @precondition none
     * @postcondition none
     * @return the habit name property
     */
    public StringProperty habitNameProperty() {
        return this.habitNameProperty;
    }
}