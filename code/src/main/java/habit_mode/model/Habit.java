package habit_mode.model;

import javafx.beans.property.BooleanProperty;
import javafx.beans.property.SimpleBooleanProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.StringProperty;

/** 
 * The habit class.
 * 
 * @author	Team 1
 * @version Spring 2022
 */
public class Habit {
    public static final String NULL_TEXT_ERROR = "text for the habit cannot be null";
    public static final String EMPTY_TEXT_ERROR = "text for the habit cannot be empty";

    private StringProperty textProperty;
    private BooleanProperty completionProperty;
    private Frequency completionFrequency;
    private int id = 0;

    /** 
     * Creates a new habit.
     * 
     * @precondition text != null && text != string.isEmpty();
     * @postcondition this.getText() == text && this.isComplete() == false && this.getFrequency() == frequency;
     * 
     * @param text The text to display for the habit.
     * @param frequency How frequently the habit should be completed.
     */
    public Habit(String text, Frequency frequency) {
        this.checkString(text);
        this.textProperty = new SimpleStringProperty(text);
        this.completionProperty = new SimpleBooleanProperty(false);
        this.completionFrequency = frequency;
    }

    /** 
     * Gets the completion status of the habit.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return the completion status of the habit.
     */
    public boolean isComplete() {
        return this.completionProperty.get();
    }

    /** 
     * Gets the id of the habit. Is 0 unless set.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return the id of the habit
     */
    public int getId() {
        return this.id;
    }

    /**
     * Gets the property for the habit text.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return The text property.
     */
    public StringProperty textProperty() {
        return this.textProperty;
    }

    /**
     * Gets the property for the habit's completion status.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return The completion property.
     */
    public BooleanProperty completionProperty() {
        return this.completionProperty;
    }

    /** 
     * Gets the text of the habit.
     *
     * @precondition None
     * @postcondition None
     * 
     * @return The text of the habit.
     */
    public String getText() {
        return this.textProperty.get();
    }

    /** 
     * Gets the completion frequency of the habit.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return The completion frequency of the habit.
     */
    public Frequency getFrequency() {
        return this.completionFrequency;
    }

    
    /** 
     * Sets the id of the habit
     * 
     * @precondition none
     * @postcondition this.getId() == id;
     * 
     * @param id The habit id.
     */
    public void setId(int id) {
        this.id = id;
    }

    /** 
     * Sets the completion frequency of the habit to the desired frequency.
     * 
     * @precondition none
     * @postcondition this.getFrequency() == frequency;
     * 
     * @param frequency How frequently the habit should be completed.
     */
    public void setFrequency(Frequency frequency) {
        this.completionFrequency = frequency;
    }

    private void checkString(String string) {
        if (string == null) {
            throw new IllegalArgumentException(NULL_TEXT_ERROR);
        }
        if (string.isEmpty()) {
            throw new IllegalArgumentException(EMPTY_TEXT_ERROR);
        }
    }

    @Override
    public String toString() {
        return this.textProperty.get();
    }

    @Override
    public boolean equals(Object other) {
        if (!(other instanceof Habit)) {
            return false;
        }

        Habit otherHabit = (Habit) other;
        return this.getText().equals(otherHabit.getText()) && this.completionFrequency == otherHabit.completionFrequency;
    }

    @Override
    public int hashCode() {
        return super.hashCode();
    }
}
