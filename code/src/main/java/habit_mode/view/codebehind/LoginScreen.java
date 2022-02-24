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
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import javafx.scene.Node;

public class LoginScreen {

    @FXML
    private ResourceBundle resources;

    @FXML
    private URL location;

    @FXML
    private Button loginButton;

    @FXML
    private TextField passwordTextField;

    @FXML
    private TextField userNameTextField;

    @FXML
    void loginButtonPress(ActionEvent event) throws IOException {
        Parent loader = FXMLLoader.load(getClass().getResource("HabitScreen.fxml"));

        Scene scene = new Scene(loader);

        Stage app_stage = (Stage) ((Node) event.getSource()).getScene().getWindow();

        app_stage.setScene(scene); 

        app_stage.show();
    }

    @FXML
    void initialize() {
        assert this.loginButton != null : "fx:id=\"loginButton\" was not injected: check your FXML file 'LoginScreen.fxml'.";
        assert this.passwordTextField != null : "fx:id=\"passwordTextField\" was not injected: check your FXML file 'LoginScreen.fxml'.";
        assert this.userNameTextField != null : "fx:id=\"userNameTextField\" was not injected: check your FXML file 'LoginScreen.fxml'.";

    }

}
