package habit_mode.view.codebehind;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import javafx.scene.Node;

import habit_mode.view_model.LoginScreenViewModel;

/**
 * The class LoginScreen.
 * 
 * @author Team 1
 * @version Spring 2022
 */
public class LoginScreen {

    private boolean isUserNew;

    private LoginScreenViewModel viewModel;

    @FXML
    private Label emailLabel;

    @FXML
    private ResourceBundle resources;

    @FXML
    private URL location;

    @FXML
    private Button loginButton;

    @FXML
    private Button newUserButton;

    @FXML
    private TextField passwordTextField;

    @FXML
    private TextField userNameTextField;

    @FXML
    private TextField emailTextField;

    @FXML
    void loginButtonPress(ActionEvent event) throws IOException {
        try {
            if (this.viewModel.validateLogin()) {
                Parent loader = FXMLLoader.load(getClass().getResource("HabitScreen.fxml"));

                Scene scene = new Scene(loader);

                Stage app_stage = (Stage) ((Node) event.getSource()).getScene().getWindow();

                app_stage.setScene(scene); 

                app_stage.show();
            } else {
                System.out.print("Login failed.");
            } 
        } catch (Exception error) {
            System.out.print(error.getLocalizedMessage());
        }
    }

    @FXML
    void newUserButtonPress(ActionEvent event) throws IOException {
        this.isUserNew = !this.isUserNew;
        this.toggleEmailVisibility();
        this.toggleButtonText();
    }

    @FXML
    void initialize() {
        this.isUserNew = false;
        this.viewModel = new LoginScreenViewModel();

        this.viewModel.usernameProperty().bindBidirectional(this.userNameTextField.textProperty());
        this.viewModel.passwordProperty().bindBidirectional(this.passwordTextField.textProperty());

        assert this.loginButton != null : "fx:id=\"loginButton\" was not injected: check your FXML file 'LoginScreen.fxml'.";
        assert this.passwordTextField != null : "fx:id=\"passwordTextField\" was not injected: check your FXML file 'LoginScreen.fxml'.";
        assert this.userNameTextField != null : "fx:id=\"userNameTextField\" was not injected: check your FXML file 'LoginScreen.fxml'.";

    }

    private void toggleEmailVisibility() {
        this.emailLabel.setVisible(!this.emailLabel.isVisible());
        this.emailTextField.setVisible(!this.emailTextField.isVisible());
    }

    private void toggleButtonText() {
        if (!this.isUserNew) {
            this.loginButton.setStyle("-fx-font-size: 31px; ");
            this.loginButton.setText("Login");
            this.newUserButton.setText("New User?");
        } else {
            this.loginButton.setStyle("-fx-font-size: 22px; ");
            this.loginButton.setText("Register");
            this.newUserButton.setText("Cancel");
        }
    }
}
