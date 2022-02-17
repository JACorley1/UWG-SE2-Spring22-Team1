package code.view;

import java.net.URL;
import java.util.ResourceBundle;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;

public class HabitScreenCodeBehind {

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
    private Label moneyLabel;

    @FXML
    private Button backButton;

    @FXML
    private Label habitScreenLabel;

    @FXML
    private ListView<?> habitListViewtha;

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

    @FXML
    void initialize() {
        assert sudokuButton != null : "fx:id=\"sudokuButton\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert habitListButton != null : "fx:id=\"habitListButton\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert settingsButton != null : "fx:id=\"settingsButton\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert moneyLabel != null : "fx:id=\"moneyLabel\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert backButton != null : "fx:id=\"backButton\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert habitScreenLabel != null : "fx:id=\"habitScreenLabel\" was not injected: check your FXML file 'HabitScreen.fxml'.";
        assert habitListViewtha != null : "fx:id=\"habitListViewtha\" was not injected: check your FXML file 'HabitScreen.fxml'.";

    }
}