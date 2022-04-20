package habit_mode.view.codebehind;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.geometry.Pos;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.scene.text.Font;
import javafx.stage.Stage;
import javafx.scene.Node;




public class SudokuScreenCodeBehind {

    @FXML
    private ResourceBundle resources;

    @FXML
    private URL location;

    @FXML
    private Label noSelectedHabitLabel;

    @FXML
    private Button habitListButton;

    @FXML
    private Button settingsButton;

    @FXML
    private Label coinsLabel;

    @FXML
    private Button backButton;

    @FXML
    private Label sudokuScreenLabel;

    @FXML
    private Button sudokuButton;

    @FXML
    private Button oneButton;

    @FXML
    private Button twoButton;

    @FXML
    private Button threeButton;

    @FXML
    private Button fourButton;

    @FXML
    private Button fiveButton;

    @FXML
    private Button sixButton;

    @FXML
    private Button sevenButton;

    @FXML
    private Button eightButton;

    @FXML
    private Button nineButton;
    
    @FXML
    private GridPane sudokuPane;

    private TextField[][] sudokuBoard;
    @FXML
    void backButtonClicked(ActionEvent event) {

    }

    @FXML
    void habitButtonClicked(ActionEvent event) throws IOException {

        Parent loader = FXMLLoader.load(getClass().getResource("HabitScreen.fxml"));

        Scene scene = new Scene(loader);

        Stage app_stage = (Stage) ((Node) event.getSource()).getScene().getWindow();

        app_stage.setScene(scene); 

        app_stage.show();
        
    }

    @FXML
    void numberButtonClicked(ActionEvent event) {

    }

    @FXML
    void settingsButtonClicked(ActionEvent event) {

    }

    @FXML
    void sudokuButtonSelected(ActionEvent event) {

    }

    @FXML
    void initialize() {
        this.sudokuBoard = new TextField[9][9];
        assert this.noSelectedHabitLabel != null : "fx:id=\"noSelectedHabitLabel\" was not injected: check your FXML file 'SudokuScreen.fxml'.";
        assert this.habitListButton != null : "fx:id=\"habitListButton\" was not injected: check your FXML file 'SudokuScreen.fxml'.";
        assert this.settingsButton != null : "fx:id=\"settingsButton\" was not injected: check your FXML file 'SudokuScreen.fxml'.";
        assert this.coinsLabel != null : "fx:id=\"coinsLabel\" was not injected: check your FXML file 'SudokuScreen.fxml'.";
        assert this.backButton != null : "fx:id=\"backButton\" was not injected: check your FXML file 'SudokuScreen.fxml'.";
        assert this.sudokuScreenLabel != null : "fx:id=\"sudokuScreenLabel\" was not injected: check your FXML file 'SudokuScreen.fxml'.";
        assert this.sudokuButton != null : "fx:id=\"sudokuButton\" was not injected: check your FXML file 'SudokuScreen.fxml'.";
        assert this.oneButton != null : "fx:id=\"oneButton\" was not injected: check your FXML file 'SudokuScreen.fxml'.";
        assert this.twoButton != null : "fx:id=\"twoButton\" was not injected: check your FXML file 'SudokuScreen.fxml'.";
        assert this.threeButton != null : "fx:id=\"threeButton\" was not injected: check your FXML file 'SudokuScreen.fxml'.";
        assert this.fourButton != null : "fx:id=\"fourButton\" was not injected: check your FXML file 'SudokuScreen.fxml'.";
        assert this.fiveButton != null : "fx:id=\"fiveButton\" was not injected: check your FXML file 'SudokuScreen.fxml'.";
        assert this.sixButton != null : "fx:id=\"sixButton\" was not injected: check your FXML file 'SudokuScreen.fxml'.";
        assert this.sevenButton != null : "fx:id=\"sevenButton\" was not injected: check your FXML file 'SudokuScreen.fxml'.";
        assert this.eightButton != null : "fx:id=\"eightButton\" was not injected: check your FXML file 'SudokuScreen.fxml'.";
        assert this.nineButton != null : "fx:id=\"nineButton\" was not injected: check your FXML file 'SudokuScreen.fxml'.";
        this.addTextFields();

    }

    void addTextFields() {
        for (int row = 0; row < 9; row++) {
            for (int column = 0; column < 9; column++) {
                TextField field = new TextField();
                field.setPrefHeight(50);
                field.setPrefWidth(50);
                field.setAlignment(Pos.CENTER);
                field.setFont(Font.font(20));
                this.sudokuBoard[row][column] = field;
                this.sudokuPane.add(field, row, column);
            }
        }
    }
}


