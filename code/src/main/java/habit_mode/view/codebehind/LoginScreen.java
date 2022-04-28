package habit_mode.view.codebehind;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.control.Alert.AlertType;
import javafx.stage.Stage;
import javafx.scene.Node;
import habit_mode.model.SuccessCode;
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
    private Button registerButton;

    @FXML
    private TextField passwordTextField;

    @FXML
    private TextField userNameTextField;

    @FXML
    private TextField emailTextField;

    @FXML
    void loginButtonPress(ActionEvent event) throws IOException {
        try {
            if (this.viewModel.validateLogin() == SuccessCode.OKAY) {
                Parent loader = FXMLLoader.load(getClass().getResource("HabitScreen.fxml"));
                loader.setUserData(this.viewModel.getAuthenticationToken());

                Scene scene = new Scene(loader);

                Stage app_stage = (Stage) ((Node) event.getSource()).getScene().getWindow();
                app_stage.setScene(scene); 

                app_stage.show();
            } else {
                this.presentErrorDialog(this.viewModel.validateLogin());
            } 
        } catch (Exception error) {
            System.out.print(error.getLocalizedMessage());
        }
    }

    @FXML
    void newUserButtonPress(ActionEvent event) {
        this.isUserNew = !this.isUserNew;
        this.toggleEmailVisibility();
        this.toggleButtons();
    }

    @FXML
    void registerButtonPressed(ActionEvent event) throws IOException {
        try {
            if (this.viewModel.registerUser() == SuccessCode.OKAY) {
                this.loginButtonPress(event);
            } else {
                this.presentErrorDialog(this.viewModel.registerUser());
            }
        } catch (Exception error) {
            System.out.print(error.getLocalizedMessage());
        }
    }

    @FXML
    void initialize() {
        this.isUserNew = false;
        this.viewModel = new LoginScreenViewModel();

        this.viewModel.usernameProperty().bindBidirectional(this.userNameTextField.textProperty());
        this.viewModel.passwordProperty().bindBidirectional(this.passwordTextField.textProperty());
        this.viewModel.emailProperty().bindBidirectional(this.emailTextField.textProperty());

        assert this.loginButton != null : "fx:id=\"loginButton\" was not injected: check your FXML file 'LoginScreen.fxml'.";
        assert this.passwordTextField != null : "fx:id=\"passwordTextField\" was not injected: check your FXML file 'LoginScreen.fxml'.";
        assert this.userNameTextField != null : "fx:id=\"userNameTextField\" was not injected: check your FXML file 'LoginScreen.fxml'.";

    }

    private void presentErrorDialog(SuccessCode errorCode) {
        String errorMessage = this.determineErrorMessage(errorCode);
        Alert alert = new Alert(AlertType.ERROR);
        alert.setTitle("An error has occurred.");
        alert.setHeaderText("The following issue has occurred:");
        alert.setContentText(errorMessage);
        alert.showAndWait();
        return;
    }

    private String determineErrorMessage(SuccessCode errorCode) {
        
        switch (errorCode) {
            case INVALID_LOGIN_CREDENTIALS:
                return "The login credentials provided are invalid, please try again or register a new account.";
            case UNKNOWN_ERROR:
                return "An Unknown Error has occurred. Please try again.";
            case USERNAME_ALREADY_EXISTS:
                return "The username you entered is already in use. Please try again or login.";
            case USER_NOT_FOUND:
                return "Account not found with given credentials. Please try again or Create an account.";
            case INVALID_PASSWORD:
                return "The password entered is invalid. Please try a different one.";
            case INVALID_EMAIL:
                return "The email entered is invalid. Please try a different one.";
            case INVALID_USERNAME:
                return "The username entered is invalid. Please try a different one.";
            default:
                return "Unknown Error has occurred. Please try again.";
        }
    }

    private void toggleEmailVisibility() {
        this.emailLabel.setVisible(!this.emailLabel.isVisible());
        this.emailTextField.setVisible(!this.emailTextField.isVisible());
    }

    private void toggleButtons() {
        this.loginButton.setVisible(!this.isUserNew);
        this.loginButton.setDisable(this.isUserNew);

        this.registerButton.setVisible(this.isUserNew);
        this.registerButton.setDisable(!this.isUserNew);

        if (!this.isUserNew) {
            this.newUserButton.setText("New User?");
        } else {
            this.newUserButton.setText("Cancel");
        }
    }
}
