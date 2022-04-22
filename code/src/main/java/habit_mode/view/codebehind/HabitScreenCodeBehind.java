package habit_mode.view.codebehind;

import java.net.URL;
import java.util.ArrayList;
import java.util.ResourceBundle;

import javafx.beans.value.ObservableValue;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.control.RadioButton;
import javafx.scene.control.TextField;
import javafx.scene.control.Toggle;
import javafx.scene.control.ToggleGroup;
import javafx.scene.control.cell.CheckBoxListCell;
import javafx.scene.layout.AnchorPane;
import javafx.util.Callback;
import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.ServerServerCommunicator;
import habit_mode.view_model.HabitViewModel;

/**
 * The class HabitScreenCodeBehind.
 * 
 * @author Team 1
 * @version Spring 2022
 */
public class HabitScreenCodeBehind {
    private HabitViewModel viewModel;

    @FXML
    private AnchorPane mainPane;

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
    private Label coinsLabel;

    @FXML
    private Button backButton;

    @FXML
    private Label habitScreenLabel;

    @FXML
    private ListView<Habit> habitListView;

    @FXML
    private Button addHabitButton;

    @FXML
    private AnchorPane addHabitBackgroundAnchorPane;

    @FXML
    private RadioButton dailyRadioButton;

    @FXML
    private ToggleGroup frequencyToggleGroup;

    @FXML
    private RadioButton weeklyRadioButton;

    @FXML
    private RadioButton monthlyRadioButton;

    @FXML
    private Button confirmHabitButton;

    @FXML
    private Button cancelButton;

    @FXML
    private Label habitNameErrorLabel;

    @FXML
    private TextField habitNameTextField;

    @FXML
    private Button removeHabitsButton;

    @FXML
    private AnchorPane removeHabitAnchorPane;

    @FXML
    private RadioButton removeDailyRadioButton;

    @FXML
    private ToggleGroup updateFrequencyToggleGroup;

    @FXML
    private RadioButton removeWeeklyRadioButton;

    @FXML
    private RadioButton removeMonthlyRadioButton;

    @FXML
    private Button updateConfirmButton;

    @FXML
    private Button removeButton;

    @FXML
    private Label updateErrorLabel;

    @FXML
    private Label invalidHabitTextLabel;

    @FXML
    private TextField updateHabitNameTextField;

    @FXML
    private AnchorPane addHabitsAnchorPane;

    @FXML
    private Button removeCancelButton;

    @FXML
    private ListView<Habit> completedHabitListView;

    @FXML
    private AnchorPane completeHabitAnchorPane;

    @FXML
    private Button confirmCompleteHabitButton;

    @FXML
    private Button completeHabitCancelButton;

    @FXML
    private Button sendCompleteHabitsButton;

    @FXML
    private Label noSelectedHabitLabel;

    @FXML
    void removeButtonClicked(ActionEvent event) {
        try {
            this.viewModel.removeHabit(this.habitListView.getSelectionModel().getSelectedItem());
            this.updateHabitNameTextField.clear();
        } catch (Exception err) {
            System.out.println(err.getMessage());
        }

    }

    @FXML
    void removeHabitsButtonClicked(ActionEvent event) {
        if (this.habitListView.getSelectionModel().getSelectedItem() == null) {
            this.noSelectedHabitLabel.setVisible(true);
            this.invalidHabitTextLabel.setVisible(false);
        } else {
            this.noSelectedHabitLabel.setVisible(false);
            this.addHabitBackgroundAnchorPane.setVisible(true);
            this.removeHabitAnchorPane.setVisible(true);
            this.addHabitsAnchorPane.setVisible(false);
            this.completeHabitAnchorPane.setVisible(false);
            this.updateHabitNameTextField.setText(this.habitListView.getSelectionModel().getSelectedItem().getText());
            this.updateFrequencyToggleGroup.selectToggle(this.selectedFrequency());
        }
    }

    @FXML
    void sendCompleteHabitsButtonClicked(ActionEvent event) {
        this.addHabitBackgroundAnchorPane.setVisible(true);
        this.removeHabitAnchorPane.setVisible(false);
        this.addHabitsAnchorPane.setVisible(false);
        this.completeHabitAnchorPane.setVisible(true);
    }

    @FXML
    void confirmUpdateHabitButtonClicked(ActionEvent event) {
        try {
            int index = this.habitListView.getSelectionModel().getSelectedIndex();
            this.viewModel.updateHabit(index);
            this.habitListView.refresh();
            this.addHabitBackgroundAnchorPane.setVisible(false);
            this.removeHabitAnchorPane.setVisible(false);
            this.updateHabitNameTextField.clear();
        } catch (Exception error) {
            this.addHabitBackgroundAnchorPane.setVisible(false);
            this.removeHabitAnchorPane.setVisible(false);
            this.updateHabitNameTextField.clear();
            this.invalidHabitTextLabel.setVisible(true);
        } 
    }

    @FXML
    void confirmCompleteHabitButtonClicked(ActionEvent event) {
        ArrayList<Habit> habits = new ArrayList<Habit>();
        for (Habit item : this.viewModel.habitListProperty().get()) {
            if (item.completionProperty().get()) {
                habits.add(item);
            }
        }

        for (Habit habit : habits) {
            this.viewModel.sendCompletedHabit(habit);
            this.completedHabitListView.getItems().add(habit);
            this.habitListView.getItems().remove(habit);
        }
        this.completeHabitAnchorPane.setVisible(false);
        this.addHabitBackgroundAnchorPane.setVisible(false);
    }



    @FXML
    void addButtonClicked(ActionEvent event) {
        this.addHabitBackgroundAnchorPane.setVisible(true);
        this.addHabitsAnchorPane.setVisible(true);
        this.removeHabitAnchorPane.setVisible(false);
        this.completeHabitAnchorPane.setVisible(false);
    }

    

    @FXML
    void backButtonClicked(ActionEvent event) {

    }

    @FXML
    void cancelButtonClicked(ActionEvent event) {
        this.viewModel.closePopup();
    }

    @FXML
    void confirmHabitButtonClicked(ActionEvent event) {
        try {
            this.viewModel.addHabit();
        } catch (Exception err) {
            System.out.println(err.getMessage());
        }
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

        this.assertFields();

        this.setHabitListeners();
        this.setViewModelBindings();
        this.setPaneListener();
    }

    private void assertFields() {
        assert this.sudokuButton != null
                : "fx:id=\"sudokuButton\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert this.noSelectedHabitLabel != null
                : "fx:id=\"noSelectedHabitLabel\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert this.habitListButton != null
                : "fx:id=\"habitListButton\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert this.settingsButton != null
                : "fx:id=\"settingsButton\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert this.coinsLabel != null
                : "fx:id=\"coinsLabel\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert this.backButton != null
                : "fx:id=\"backButton\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert this.habitScreenLabel != null
                : "fx:id=\"habitScreenLabel\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert this.habitListView != null
                : "fx:id=\"habitListView\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert this.addHabitButton != null
                : "fx:id=\"addHabitButton\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert this.addHabitBackgroundAnchorPane != null
                : "fx:id=\"addHabitBackgroundAnchorPane\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        this.splitAssertFields();
    }

    private void splitAssertFields() {
        assert this.dailyRadioButton != null
                : "fx:id=\"dailyRadioButton\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert this.frequencyToggleGroup != null
                : "fx:id=\"frequencyToggleGroup\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert this.weeklyRadioButton != null
                : "fx:id=\"weeklyRadioButton\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert this.monthlyRadioButton != null
                : "fx:id=\"monthlyRadioButton\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert this.confirmHabitButton != null
                : "fx:id=\"confirmHabitButton\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert this.cancelButton != null
                : "fx:id=\"cancelButton\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert this.habitNameErrorLabel != null
                : "fx:id=\"habitNameErrorLabel\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert this.habitNameTextField != null
                : "fx:id=\"habitNameTextField\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert this.mainPane != null 
                : "fx:id=\"mainPane\" was not injected: check your FXML file 'HabitScreen.fxml'.";
    }

    private void setPaneListener() {
        this.mainPane.sceneProperty().addListener((obs, wasNull, exists) -> {
            if (this.mainPane.sceneProperty().isNotNull().get()) {
                ((ServerServerCommunicator) this.viewModel.getServerCommunicator()).setToken((String) this.mainPane.getScene().getRoot().getUserData());
                this.viewModel.getHabitsFromServer();
                this.viewModel.updateCoins();
            }
        });
    }

    private void setViewModelBindings() {
        this.viewModel.dailySelectedProperty().bindBidirectional(this.dailyRadioButton.selectedProperty());
        this.viewModel.weeklySelectedProperty().bindBidirectional(this.weeklyRadioButton.selectedProperty());
        this.viewModel.monthlySelectedProperty().bindBidirectional(this.monthlyRadioButton.selectedProperty());
        this.viewModel.removeDailySelectedProperty().bindBidirectional(this.removeDailyRadioButton.selectedProperty());
        this.viewModel.removeWeeklySelectedProperty().bindBidirectional(this.removeWeeklyRadioButton.selectedProperty());
        this.viewModel.popupVisibleProperty().bindBidirectional(this.addHabitBackgroundAnchorPane.visibleProperty());
        this.viewModel.errorVisibleProperty().bindBidirectional(this.habitNameErrorLabel.visibleProperty());
        this.viewModel.habitNameProperty().bindBidirectional(this.habitNameTextField.textProperty());
        this.viewModel.removeHabitNameProperty().bindBidirectional(this.updateHabitNameTextField.textProperty());
        this.viewModel.habitListProperty().bindBidirectional(this.habitListView.itemsProperty());
        this.viewModel.completedHabitListProperty().bindBidirectional(this.completedHabitListView.itemsProperty());
        this.viewModel.coinsLabelProperty().bindBidirectional(this.coinsLabel.textProperty());

        
    }

    private void setHabitListeners() {
        for (Habit habit : this.viewModel.habitListProperty()) {
            habit.completionProperty().addListener((obs, wasOn, isNowOn) -> {
                this.viewModel.sendCompletedHabit(habit);
            });

            this.habitListView.getItems().add(habit);
        }

        this.habitListView.setCellFactory(CheckBoxListCell.forListView(new Callback<Habit, ObservableValue<Boolean>>() {
            @Override
            public ObservableValue<Boolean> call(Habit habit) {
                return habit.completionProperty();
            }
        }));
    }

    private Toggle selectedFrequency() {
        Frequency selectedHabitsFrequency = this.habitListView.getSelectionModel().getSelectedItem().getFrequency();
        if (selectedHabitsFrequency == Frequency.DAILY) {
            return this.removeDailyRadioButton;
        }
        if (selectedHabitsFrequency == Frequency.WEEKLY) {
            return this.removeWeeklyRadioButton;
        }
        return this.removeMonthlyRadioButton;
    }
}