package habit_mode.view_model;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.HabitManager;
import javafx.beans.property.ListProperty;
import javafx.beans.property.ObjectProperty;
import javafx.beans.property.SimpleListProperty;
import javafx.beans.property.SimpleObjectProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.StringProperty;
import javafx.collections.FXCollections;

/** 
 * The habitViewModel class.
 * 
 * @author    Team 1
 * @version Spring 2022
 */
public class HabitViewModel {
    private ObjectProperty<Frequency> frequencyProperty;
    private ObjectProperty<Habit> selectedHabitProperty;
    private ListProperty<Habit> habitListProperty;
    private StringProperty habitNameProperty;

    /** 
     * Creates a new habit view model.
     * 
     * @precondition: None.
     * @postcondition: this.frequencyProperty() == new SimpleObjectProperty<Frequency>(), this.habitNameProperty() == new SimpleStringProperty(""), 
     * 				         this.habitListProperty() == FXCollections.observableArrayList(new HabitManager());
     */
    public HabitViewModel() {
        this.frequencyProperty = new SimpleObjectProperty<Frequency>();
        this.selectedHabitProperty = new SimpleObjectProperty<Habit>();
        this.habitNameProperty =  new SimpleStringProperty("");
        this.habitListProperty = new SimpleListProperty<Habit>(FXCollections.observableArrayList(new HabitManager()));
    }

    /** 
     * Adds a habit to the system.
     * 
     * @precondition this.habitNameProperty.getValue() != null || "";
     * @postcondition this.habitListProperty().getValue().size() == this.habitListProperty().getValue().size() @pre + 1;
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

    /** 
     * Sets the targeted habits completion status.
     * 
     * @precondition !this.habitListProperty().getValue().isEmpty() && this.selectedHabitProperty().getValue() != null;
     * @postcondition this.selectedHabitProperty.getValue().toggleCompletionStatus() == !this.selectedHabitProperty().getValue().toggleCompletionStatus() @pre;
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
  
    /** 
     * The frequency property.
     * 
     * @precondition None.
     * @postcondition None.
     * 
     * @return The frequency property.
     */
    public ObjectProperty<Frequency> frequencyProperty() {
        return this.frequencyProperty;
    }

    /** 
     * The selected habit property.
     * 
     * @precondition None.
     * @postcondition None.
     * 
     * @return The selected habit property.
     */
    public ObjectProperty<Habit> selectedHabitProperty() {
        return this.selectedHabitProperty;
    }

    /** 
     * The habit list property.
     * 
     * @precondition None.
     * @postcondition None.
     *  
     * @return The habit list property.
     */
    public ListProperty<Habit> habitListProperty() {
        return this.habitListProperty;
    }

    /** 
     * The habit name property.
     * 
     * @precondition None.
     * @postcondition None.
     * 
     * @return The habit name property.
     */
    public StringProperty habitNameProperty() {
        return this.habitNameProperty;
    }
}