package habit_mode.view.codebehind;

import java.net.URL;
import java.util.ResourceBundle;

import javafx.beans.property.BooleanProperty;
import javafx.beans.property.SimpleBooleanProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.StringProperty;
import javafx.beans.value.ObservableValue;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.control.cell.CheckBoxListCell;
import javafx.util.Callback;
import habit_mode.model.Habit;
import habit_mode.view_model.HabitViewModel;

public class HabitScreenCodeBehind {
    private HabitViewModel viewModel;

    @FXML
    private ResourceBundle resources;

    @FXML
    private URL location;

    @FXML
    private Button sudokuButton;

    @FXML
    private Button habitListButton;

    @FXML
    private Button settingsButton;

    @FXML
    private Button addHabitButton;

    @FXML
    private Label moneyLabel;

    @FXML
    private Button backButton;

    @FXML
    private Label habitScreenLabel;

    @FXML
    private ListView<Item> habitListView;

    @FXML
    void addButtonClicked(ActionEvent event) {

    }

    @FXML
    void backButtonClicked(ActionEvent event) {

    }

    @FXML
    void settingsButtonClicked(ActionEvent event) {

    }

    @FXML
    void sudokuButtonSelected(ActionEvent event) {

    }

    @FXML
    void initialize() {
        this.viewModel = new HabitViewModel();
        
        assert this.addHabitButton != null : "fx:id=\"addHabitButton\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert this.sudokuButton != null : "fx:id=\"sudokuButton\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert this.habitListButton != null : "fx:id=\"habitListButton\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert this.settingsButton != null : "fx:id=\"settingsButton\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert this.moneyLabel != null : "fx:id=\"moneyLabel\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert this.backButton != null : "fx:id=\"backButton\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert this.habitScreenLabel != null : "fx:id=\"habitScreenLabel\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert this.habitListView != null : "fx:id=\"habitListView\" was not injected: check your FXML file 'HabitScreen.fxml'.";

        this.setHabitListeners();

    }

    private void setHabitListeners() {
        for (Habit habit : this.viewModel.habitListProperty())  {
            Item item = new Item(habit.getText(), false);

            item.onProperty().addListener((obs, wasOn, isNowOn) -> {
                System.out.println(item.getName() + " changed on state from " + wasOn + " to " + isNowOn);
            });

            this.habitListView.getItems().add(item);
        }

        this.habitListView.setCellFactory(CheckBoxListCell.forListView(new Callback<Item, ObservableValue<Boolean>>() {
            @Override
            public ObservableValue<Boolean> call(Item item) {
                return item.onProperty();
            }
        }));
    }

    /**
     * The static class Item.
     * 
     * @author Team 1
     * @version Spring 2022
     */
    public static class Item {
        private final StringProperty name = new SimpleStringProperty();
        private final BooleanProperty on = new SimpleBooleanProperty();

        /**
         * The 2-parameter constructor for Item
         * 
         * @precondition none
         * @postcondition this.getName() == name, this.isOn() == on
         * 
         * @param name The name to be assigned to the item.
         * @param on   The default on-status of the item.
         */
        public Item(String name, boolean on) {
            this.setName(name);
            this.setOn(on);
        }

        /**
         * Getter for the item's NameProperty.
         * 
         * @return The item's name as a StringProperty.
         */
        public final StringProperty nameProperty() {
            return this.name;
        }

        /**
         * Getter for the item's name.
         * 
         * @return The item's name as a string.
         */
        public final String getName() {
            return this.nameProperty().get();
        }

        /**
         * Setter for the item's NameProperty.
         * 
         * @postcondition this.getName() == name
         * 
         * @param name The name to change the item to. 
         */
        public final void setName(final String name) {
            this.nameProperty().set(name);
        }

        /**
         * Getter for the item's BooleanProperty.
         * 
         * @return A BooleanProperty that represents true if checked or false otherwise.
         */
        public final BooleanProperty onProperty() {
            return this.on;
        }

        /**
         * Getter for the item's on status.
         *  
         * @return True if checked, false otherwise.
         */
        public final boolean isOn() {
            return this.onProperty().get();
        }

        /**
         * Setter for the item's BooleanProperty.
         * 
         * @param on True if checked, false otherwise. 
         */
        public final void setOn(final boolean on) {
            this.onProperty().set(on);
        }

        @Override
        public String toString() {
            return this.getName();
        }

    }

}