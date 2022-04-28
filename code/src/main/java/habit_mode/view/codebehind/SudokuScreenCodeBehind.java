package habit_mode.view.codebehind;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

import habit_mode.view_model.SudokuScreenViewModel;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.Background;
import javafx.scene.layout.BackgroundFill;
import javafx.scene.layout.CornerRadii;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.scene.text.TextAlignment;
import javafx.stage.Stage;
import javafx.scene.Node;
import habit_mode.model.ServerServerCommunicator;
import habit_mode.model.sudoku.SudokuPuzzle;



/**
 * The class SudokuScreenCodeBehind.
 * 
 * @author Team 1
 * @version Spring 2022
 */
public class SudokuScreenCodeBehind {

    @FXML
    private AnchorPane mainPane;

    @FXML
    private ResourceBundle resources;

    @FXML
    private URL location;

    @FXML
    private Label winLabel;

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

    private Pane[][] sudokuBoard;

    @FXML
    private Button eraseButton;

    @FXML
    private Button hintButton;

    private SudokuScreenViewModel viewModel;

    private static Button mostRecentlySelectedButton;
    
    private SudokuPuzzle puzzle;

    private static Pane mostRecentlySelectedPane;

    @FXML
    void hintButtonClicked(ActionEvent event) {
        if (this.viewModel.getServerCommunicator().getCoins() - 20 > 0) {
            int[] hint = this.viewModel.getServerCommunicator().buyHint();
            int number = hint[0];
            int row = hint[1];
            int col = hint[2];
            int coins = hint[3];
            this.viewModel.getServerCommunicator().setCoins(coins);
            Pane pane = this.sudokuBoard[row][col];
            Label label = (Label) pane.getChildren().get(0);
            pane.disableProperty().set(true);
            label.setText(String.valueOf(number));
            this.coinsLabel.setText(String.valueOf("Coins: " + this.viewModel.getServerCommunicator().getCoins()));
        }
    }

    @FXML
    void eraseButtonClicked(ActionEvent event) {

    }

    @FXML
    void backButtonClicked(ActionEvent event) {

    }

    @FXML
    void habitButtonClicked(ActionEvent event) throws IOException {
        for (int row = 0; row < 9; row++) {
            for (int column = 0; column < 9; column++) {
                Label label = (Label) this.sudokuBoard[row][column].getChildren().get(0);
                if (!label.getText().isEmpty()) {
                    this.viewModel.convertLabelsToPuzzle(label.getText(), row, column);
                }
            }
        }
        this.viewModel.getServerCommunicator().updateSudokuPuzzle(this.viewModel.getPuzzle());
        Parent loader = FXMLLoader.load(getClass().getResource("HabitScreen.fxml"));
        loader.setUserData(this.viewModel.getAuthenticationToken());

        Scene scene = new Scene(loader);

        Stage app_stage = (Stage) ((Node) event.getSource()).getScene().getWindow();
        app_stage.setScene(scene); 

        app_stage.show();

        
    }

    @FXML
    void numberButtonClicked(ActionEvent event) {
        Button number = (Button) event.getSource();
        mostRecentlySelectedButton = number;
        

    }

    @FXML
    void settingsButtonClicked(ActionEvent event) {

    }

    @FXML
    void sudokuButtonSelected(ActionEvent event) {

    }

    @FXML
    void initialize() {
        this.viewModel = new SudokuScreenViewModel();
        this.sudokuBoard = new Pane[9][9];
        mostRecentlySelectedPane = this.sudokuBoard[0][0];
        mostRecentlySelectedButton = null;
        assert this.winLabel != null : "fx:id=\"winLabel\" was not injected: check your FXML file 'SudokuScreen.fxml'.";
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
        this.setUpPanes();

    }

    @FXML
    void mouseEvent(MouseEvent event) {
        for (int row = 0; row < 9; row++) {
            for (int column = 0; column < 9; column++) {
                Label label = (Label) this.sudokuBoard[row][column].getChildren().get(0);
                if (!label.getText().isEmpty()) {
                    this.viewModel.convertLabelsToPuzzle(label.getText(), row, column);
                    if (this.viewModel.getPuzzle().isComplete()) {
                        this.winLabel.setVisible(true);
                    }
                }
            }
        }
    }

    private void setUpPanes() {
        this.mainPane.sceneProperty().addListener((obs, wasNull, exists) -> {
            if (this.mainPane.sceneProperty().isNotNull().get()) {
                ((ServerServerCommunicator) this.viewModel.getServerCommunicator()).setToken((String) this.mainPane.getScene().getRoot().getUserData());
                this.puzzle = this.viewModel.getServerCommunicator().getSudokuPuzzle();
                this.viewModel.setPuzzle(this.viewModel.getServerCommunicator().getSudokuPuzzle());
                this.coinsLabel.setText("Coins: " + String.valueOf(this.viewModel.getServerCommunicator().getCoins()));
                this.addPanes();
            }
        });
    }
    


    private void addPanes() {
        for (int row = 0; row < 9; row++) {
            for (int column = 0; column < 9; column++) {
                Pane pane = new Pane();
                Label label = new Label();
                               
                label.alignmentProperty().set(Pos.CENTER);
                label.setFont(Font.font(15));
                if (this.puzzle.getNumber(row, column) != 0) {
                    label.setText(String.valueOf(this.puzzle.getNumber(row, column)));
                    if (this.viewModel.getPuzzle().isNumberLocked(row, column)) {
                        pane.disableProperty().set(true);
                    }
                }
                this.setLabelsAndPanes(pane, label);
                EventHandler<MouseEvent> eventHandler = new EventHandler<MouseEvent>() { 
                    @Override 
                    public void handle(MouseEvent event) { 
                            SudokuScreenCodeBehind.mostRecentlySelectedPane = (Pane) event.getSource();
                            var list = SudokuScreenCodeBehind.mostRecentlySelectedPane.getChildren();
                            Label label = (Label) list.get(0);
                            if (SudokuScreenCodeBehind.mostRecentlySelectedButton != null) {
                            label.setText(SudokuScreenCodeBehind.mostRecentlySelectedButton.getText());
                            }
                        }
                    };
                pane.setOnMouseClicked(eventHandler);
                this.setSudokuPane(row, column, pane);
            }
        }
    }

    private void setSudokuPane(int row, int column, Pane pane) {
        this.sudokuPane.setLayoutX(50);
        this.sudokuBoard[row][column] = pane;
        this.sudokuPane.setHgap(15);
        this.sudokuPane.setVgap(30);              
        this.sudokuPane.add(pane, row, column);
    }

    private void setLabelsAndPanes(Pane pane, Label label) {
        label.textAlignmentProperty().set(TextAlignment.CENTER);
        label.layoutXProperty().bind(pane.widthProperty().subtract(label.widthProperty()).divide(2));
        label.layoutYProperty().bind(pane.heightProperty().subtract(label.heightProperty()).divide(2));
        pane.getChildren().add(label);
        pane.setBackground(new Background(new BackgroundFill(Color.web("#D3D3D3"), CornerRadii.EMPTY, Insets.EMPTY)));
        pane.setStyle("-fx-border-color: black");
        pane.setMinHeight(35);
        pane.setMinWidth(35);
    }

  
}


