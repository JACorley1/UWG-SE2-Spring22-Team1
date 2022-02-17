package code.view

import java.net.URL;
import java.util.ResourceBundle;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.image.ImageView;

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
    void loginButtonPress(ActionEvent event) {

    }

    @FXML
    void initialize() {
        assert loginButton != null : "fx:id=\"loginButton\" was not injected: check your FXML file 'LoginScreen.fxml'.";
        assert passwordTextField != null : "fx:id=\"passwordTextField\" was not injected: check your FXML file 'LoginScreen.fxml'.";
        assert userNameTextField != null : "fx:id=\"userNameTextField\" was not injected: check your FXML file 'LoginScreen.fxml'.";

    }

}
