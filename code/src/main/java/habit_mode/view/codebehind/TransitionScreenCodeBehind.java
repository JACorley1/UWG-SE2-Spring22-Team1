package habit_mode.view.codebehind;

import java.io.IOException;

import habit_mode.view_model.TransitionScreenViewModel;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;
import javafx.scene.Node;
import habit_mode.model.ServerServerCommunicator;

public class TransitionScreenCodeBehind {

    @FXML
    private AnchorPane mainPane;

    @FXML
    private Button habitListButton;

    @FXML
    private Button settingsButton;

    @FXML
    private Button sudokuButton;

    @FXML
    private Button continueSudoku;

    @FXML
    private Button startNewGame;

    private TransitionScreenViewModel viewModel;

    @FXML
    void continueClicked(ActionEvent event) throws IOException {
        Parent loader = FXMLLoader.load(getClass().getResource("SudokuScreen.fxml"));
        loader.setUserData(this.viewModel.getAuthenticationToken());


        Scene scene = new Scene(loader);

        Stage app_stage = (Stage) ((Node) event.getSource()).getScene().getWindow();

        app_stage.setScene(scene); 

        app_stage.show();
    }

    @FXML
    void habitButtonClicked(ActionEvent event) throws IOException {
        Parent loader = FXMLLoader.load(getClass().getResource("HabitScreen.fxml"));
        loader.setUserData(this.viewModel.getAuthenticationToken());


        Scene scene = new Scene(loader);

        Stage app_stage = (Stage) ((Node) event.getSource()).getScene().getWindow();

        app_stage.setScene(scene); 

        app_stage.show();
    }

    @FXML
    void settingsButtonClicked(ActionEvent event) {

    }

    @FXML
    void initialize() {
        this.viewModel = new TransitionScreenViewModel();
        
        assert this.mainPane != null : "fx:id=\"mainPane\" was not injected: check your FXML file 'TransitionScreen.fxml'.";
        assert this.habitListButton != null : "fx:id=\"habitListButton\" was not injected: check your FXML file 'TransitionScreen.fxml'.";
        assert this.settingsButton != null : "fx:id=\"settingsButton\" was not injected: check your FXML file 'TransitionScreen.fxml'.";
        assert this.sudokuButton != null : "fx:id=\"sudokuButton\" was not injected: check your FXML file 'TransitionScreen.fxml'.";
        assert this.continueSudoku != null : "fx:id=\"continueSudoku\" was not injected: check your FXML file 'TransitionScreen.fxml'.";
        assert this.startNewGame != null : "fx:id=\"startNewGame\" was not injected: check your FXML file 'TransitionScreen.fxml'.";
        this.setPaneListener();
        
    }

    @FXML
    void startNewGameClicked(ActionEvent event) throws IOException {
        if (this.viewModel.getServerCommunicator().generateSudokuPuzzle() != null) {
            Parent loader = FXMLLoader.load(getClass().getResource("SudokuScreen.fxml"));
            loader.setUserData(this.viewModel.getAuthenticationToken());

            Scene scene = new Scene(loader);

            Stage app_stage = (Stage) ((Node) event.getSource()).getScene().getWindow();

            app_stage.setScene(scene); 

            app_stage.show();
        }   
    }

    @FXML
    void sudokuButtonSelected(ActionEvent event) throws IOException {
    }

    private void setPaneListener() {
        this.continueSudoku.sceneProperty().addListener((obs, wasNull, exists) -> {
            if (this.continueSudoku.sceneProperty().isNotNull().get()) {
                ((ServerServerCommunicator) this.viewModel.getServerCommunicator()).setToken((String) this.continueSudoku.getScene().getRoot().getUserData());
                if (this.viewModel.getServerCommunicator().getSudokuPuzzle() == null) {
                    this.continueSudoku.disableProperty().set(true);
                } else {
                    this.continueSudoku.disableProperty().set(false);
                }
            }
        });
    }

}