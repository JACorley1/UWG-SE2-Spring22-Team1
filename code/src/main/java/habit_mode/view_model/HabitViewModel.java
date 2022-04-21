package habit_mode.view_model;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.ServerCommunicator;
import habit_mode.model.ServerServerCommunicator;
import habit_mode.model.SuccessCode;
import habit_mode.model.local_implementation.LocalServerCommunicator;
import javafx.beans.property.BooleanProperty;
import javafx.beans.property.ListProperty;
import javafx.beans.property.ObjectProperty;
import javafx.beans.property.SimpleBooleanProperty;
import javafx.beans.property.SimpleListProperty;
import javafx.beans.property.SimpleObjectProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.StringProperty;
import javafx.collections.FXCollections;

/**
 * The habitViewModel class.
 * 
 * @author Team 1
 * @version Spring 2022
 */
public class HabitViewModel {
    private ServerCommunicator serverCommunicator;
    private BooleanProperty dailySelectedProperty;
    private BooleanProperty weeklySelectedProperty;
    private BooleanProperty monthlySelectedProperty;
    private BooleanProperty popupVisibleProperty;
    private BooleanProperty errorVisibleProperty;
    private StringProperty habitNameProperty;
    private StringProperty coinsLabelProperty;
    private ObjectProperty<Habit> selectedHabitProperty;
    private ListProperty<Habit> habitListProperty;
    private BooleanProperty removeDailySelectedProperty;
    private BooleanProperty removeWeeklySelectedProperty;
    private StringProperty removeHabitNameProperty;

    /**
     * Creates a new habit view model.
     * 
     * @precondition: None.
     * @postcondition: this.frequencyProperty() == new
     *                 SimpleObjectProperty<Frequency>(), this.habitNameProperty()
     *                 == new SimpleStringProperty(""),
     *                 this.habitListProperty() ==
     *                 FXCollections.observableArrayList(new HabitManager());
     */
    public HabitViewModel() {
        this.serverCommunicator = new ServerServerCommunicator();
        this.dailySelectedProperty = new SimpleBooleanProperty();
        this.weeklySelectedProperty = new SimpleBooleanProperty();
        this.monthlySelectedProperty = new SimpleBooleanProperty();
        this.removeDailySelectedProperty = new SimpleBooleanProperty();
        this.removeWeeklySelectedProperty = new SimpleBooleanProperty();
        this.popupVisibleProperty = new SimpleBooleanProperty();
        this.errorVisibleProperty = new SimpleBooleanProperty();
        this.selectedHabitProperty = new SimpleObjectProperty<Habit>();
        this.habitNameProperty = new SimpleStringProperty("");
        this.removeHabitNameProperty = new SimpleStringProperty("");
        this.coinsLabelProperty = new SimpleStringProperty("");
        this.habitListProperty = new SimpleListProperty<Habit>(FXCollections.observableArrayList());
    }

    /**
     * A special constructor for use during tests.
     * 
     * @precondition none
     * @postcondition this.serverCommunicator.getClass().equals(LocalServerCommunicator.class) &&
     *                this.frequencyProperty() == new
     *                SimpleObjectProperty<Frequency>(), this.habitNameProperty()
     *                == new SimpleStringProperty(""),
     *                this.habitListProperty() ==
     *                FXCollections.observableArrayList(new HabitManager());
     * 
     * @param dummy A boolean value that exists to allow constructor overloading.
     */
    public HabitViewModel(boolean dummy) {
        this.serverCommunicator = new LocalServerCommunicator();
        this.dailySelectedProperty = new SimpleBooleanProperty();
        this.weeklySelectedProperty = new SimpleBooleanProperty();
        this.monthlySelectedProperty = new SimpleBooleanProperty();
        this.removeDailySelectedProperty = new SimpleBooleanProperty();
        this.removeWeeklySelectedProperty = new SimpleBooleanProperty();
        this.popupVisibleProperty = new SimpleBooleanProperty();
        this.errorVisibleProperty = new SimpleBooleanProperty();
        this.selectedHabitProperty = new SimpleObjectProperty<Habit>();
        this.habitNameProperty = new SimpleStringProperty("");
        this.removeHabitNameProperty = new SimpleStringProperty("");
        this.coinsLabelProperty = new SimpleStringProperty("");
        this.habitListProperty = new SimpleListProperty<Habit>(FXCollections.observableArrayList());
    }

    /**
     * Adds a habit to the system.
     * 
     * @precondition this.habitNameProperty.getValue() != null || "";
     * @postcondition this.habitListProperty().getValue().size() ==
     *                this.habitListProperty().getValue().size() @pre + 1;
     */
    public void addHabit() {
        if (this.habitNameProperty.getValue() == null) {
            this.errorVisibleProperty.set(true);
            throw new IllegalArgumentException(Habit.NULL_TEXT_ERROR);
        }
        if (this.habitNameProperty.getValue().isEmpty()) {
            this.errorVisibleProperty.set(true);
            throw new IllegalArgumentException(Habit.EMPTY_TEXT_ERROR);
        }

        Habit habit = new Habit(this.habitNameProperty.getValue(), this.determineFrequency());
        if (this.serverCommunicator.addHabit(habit) == SuccessCode.OKAY) {
            this.habitListProperty.add(habit);
            this.closePopup();
        }

    }

    

     /**
     * Gets the server communicator.
     * 
     * @precondition None.
     * @postcondition None.
     * 
     * @return the server communicator
     */
    public ServerCommunicator getServerCommunicator() {
        return this.serverCommunicator;
    }
    /**
     * Removes a habit from the system
     * 
     * @precondition this.habitNameProperty.getValue() != null;
     * @postcondition this.habitListProperty().getValue().size() ==
     *                this.habitListProperty().getValue().size() @pre - 1;
     */
    public void removeHabit() {
        if (this.removeHabitNameProperty.getValue() == null) {
            this.errorVisibleProperty.set(true);
            throw new IllegalArgumentException(Habit.NULL_TEXT_ERROR);
        }
        Habit removedHabit = null;
        for (Habit habit : this.habitListProperty) {

            if (habit.getText() == this.removeHabitNameProperty.getValue() && habit.getFrequency() == this.determineRemoveFrequency()) {
                removedHabit = habit;
            }
        }
        if (this.serverCommunicator.removeHabit(removedHabit) == SuccessCode.OKAY) {
            this.habitListProperty.remove(removedHabit);
            this.closePopup();
        }

    }

     /**
     * Removes a habit from the system
     * 
     * @precondition habitToRemove != null;
     * @postcondition this.habitListProperty().getValue().size() ==
     *                this.habitListProperty().getValue().size() @pre - 1;
     * 
     * @param habitToRemove the habit to remove.
     */
    public void removeHabit(Habit habitToRemove) {
        if (habitToRemove == null) {
            throw new IllegalArgumentException("habit can't be null");
        }
        if (this.serverCommunicator.removeHabit(habitToRemove) == SuccessCode.OKAY) {
            this.habitListProperty.remove(habitToRemove);
            this.closePopup();
        }

    }

    /**
     * Updates the currently selected habit
     * 
     * @precondition index >= 0 & index < this.habitListProperty().getValue().size();
     * @postcondition this.selectedHabitProperty().getText() == this.removeHabitNameProperty()
     *                this.selectedHabitProperty().getFrequency() == the selected frequency property;
     * 
     * @param index the index of the habit to update.
     */
    public void updateHabit(int index) {
        if (index < 0) {
            throw new IllegalArgumentException("the index cannot be less than 0");
        }
        if (index > this.habitListProperty.getValue().size()) {
            throw new IllegalArgumentException("the index cannot be greater than the size of the habit list");
        }
        Habit updatedHabit = new Habit(this.removeHabitNameProperty().getValue(), this.determineRemoveFrequency());
        this.removeHabit(this.habitListProperty.getValue().get(index));
        this.habitListProperty.getValue().add(index, updatedHabit);
        this.getServerCommunicator().addHabit(updatedHabit);
    }

     /**
     * Gets the currently selected frequency.
     * 
     * @precondition none
     * @postcondition none
     * 
     * @return Frequency.
     */
    public Frequency determineFrequency() {
        if (this.dailySelectedProperty.getValue()) {
            return Frequency.DAILY;
        }
        if (this.weeklySelectedProperty.getValue()) {
            return Frequency.WEEKLY;
        }
        return Frequency.MONTHLY;
    }

    /**
     * Gets the currently selected remove frequency.
     * 
     * @precondition none
     * @postcondition none
     * 
     * @return Frequency.
     */
    public Frequency determineRemoveFrequency() {
        if (this.removeDailySelectedProperty.getValue()) {
            return Frequency.DAILY;
        }
        if (this.removeWeeklySelectedProperty.getValue()) {
            return Frequency.WEEKLY;
        }
        return Frequency.MONTHLY;
    }

    /**
     * Closes the add habit popup window, hides the error message, and resets all of
     * its values
     * to default.
     * 
     * @precondition None
     * @postcondition this.dailySelectedProperty().getValue() &&
     *                !this.weeklySelectedProperty().getValue() &&
     *                !this.weeklySelectedProperty().getValue() &&
     *                !this.errorVisibleProperty().getValue() &&
     *                !this.popupVisibleProperty().getValue() &&
     *                this.habitNameProperty().getValue().equals("")
     */
    public void closePopup() {
        this.errorVisibleProperty.set(false);
        this.popupVisibleProperty.set(false);
        this.habitNameProperty.set("");
    }

    /**
     * Sets the targeted habits completion status.
     * 
     * @precondition !this.habitListProperty().getValue().isEmpty() &&
     *               this.selectedHabitProperty().getValue() != null;
     * @postcondition this.selectedHabitProperty.getValue().toggleCompletionStatus()
     *                ==
     *                !this.selectedHabitProperty().getValue().toggleCompletionStatus() @pre;
     * 
     * @param status The completion status of the currently selected habit.
     */
    public void setHabitCompletion(boolean status) {
        if (this.habitListProperty.getValue().isEmpty()) {
            throw new IllegalArgumentException("Cannot modify a value that does not exist in an empty list.");
        }
        if (this.selectedHabitProperty.getValue() == null) {
            throw new IllegalArgumentException("Cannot change the completion status of a null habit.");
        }

        this.selectedHabitProperty.getValue().completionProperty().set(status);
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
     * The remove daily selected property.
     * 
     * @precondition None.
     * @postcondition None.
     * 
     * @return The remove daily selected property.
     */
    public BooleanProperty removeDailySelectedProperty() {
        return this.removeDailySelectedProperty;
    }

     /**
     * The remove weekly selected property.
     * 
     * @precondition None.
     * @postcondition None.
     * 
     * @return The remove weekly selected property.
     */
    public BooleanProperty removeWeeklySelectedProperty() {
        return this.removeWeeklySelectedProperty;
    }

    /**
     * The visible property for the add habit popup.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return The visible property for the add habit popup.
     */
    public BooleanProperty popupVisibleProperty() {
        return this.popupVisibleProperty;
    }

    /**
     * The visible property for the error label.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return The visible property for the error label.
     */
    public BooleanProperty errorVisibleProperty() {
        return this.errorVisibleProperty;
    }

    /**
     * The selected property for the daily radio button.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return The selected property for the daily radio button.
     */
    public BooleanProperty dailySelectedProperty() {
        return this.dailySelectedProperty;
    }

    /**
     * The selected property for the weekly radio button.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return The selected property for the weekly radio button.
     */
    public BooleanProperty weeklySelectedProperty() {
        return this.weeklySelectedProperty;
    }

    /**
     * The selected property for the monthly radio button.
     * 
     * @precondition None
     * @postcondition None
     * 
     * @return The selected property for the monthly radio button.
     */
    public BooleanProperty monthlySelectedProperty() {
        return this.monthlySelectedProperty;
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

    /**
     * The remove habit name property.
     * 
     * @precondition None.
     * @postcondition None.
     * 
     * @return The remove habit name property.
     */
    public StringProperty removeHabitNameProperty() {
        return this.removeHabitNameProperty;
    }

    /**
     * The habit name property.
     * 
     * @precondition None.
     * @postcondition None.
     * 
     * @return The habit name property.
     */
    public StringProperty coinsLabelProperty() {
        return this.coinsLabelProperty;
    }

    /**
     * Send the completed habit to the server.
     * 
     * @precondition habit != null;
     * @postcondition this.coinsLabelProperty.getValue == "Coins: " +
     *                this.serverCommunicator.getCoins();
     * 
     * @param habit the habit being sent.
     */
    public void sendCompletedHabit(Habit habit) {
        if (habit == null) {
            throw new IllegalArgumentException("habit cannot be null");
        }
        if (this.serverCommunicator.completeHabit(habit) == SuccessCode.OKAY) {
            this.coinsLabelProperty.setValue("Coins: " + this.serverCommunicator.getCoins());
        }
    }

}