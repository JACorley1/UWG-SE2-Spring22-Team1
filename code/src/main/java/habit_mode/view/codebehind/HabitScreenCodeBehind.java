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
        
        assert addHabitButton != null : "fx:id=\"addHabitButton\" was not injected: check your FXML file 'HabitScreen.fxml'.";
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

        public Item(String name, boolean on) {
            this.setName(name);
            this.setOn(on);
        }

        public final StringProperty nameProperty() {
            return this.name;
        }

        public final String getName() {
            return this.nameProperty().get();
        }

        public final void setName(final String name) {
            this.nameProperty().set(name);
        }

        public final BooleanProperty onProperty() {
            return this.on;
        }

        public final boolean isOn() {
            return this.onProperty().get();
        }

        public final void setOn(final boolean on) {
            this.onProperty().set(on);
        }

        @Override
        public String toString() {
            return this.getName();
        }

    }

}