package habit_mode.test.view_model.LoginScreenViewModel;

import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

import habit_mode.view_model.LoginScreenViewModel;
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.StringProperty;

public class TestVerifyLogin {
    @Test
    void testValidLogin() {
        LoginScreenViewModel viewModel = new LoginScreenViewModel();
        StringProperty usernameProperty = new SimpleStringProperty();
        StringProperty passwordProperty = new SimpleStringProperty();

        viewModel.usernameProperty().bindBidirectional(usernameProperty);
        viewModel.passwordProperty().bindBidirectional(passwordProperty);

        usernameProperty.setValue("username");
        passwordProperty.setValue("password");

        assertTrue(viewModel.validateLogin(), "Check if the login credentials are correctly verified");
    }

    @Test
    void testBlankUsername() {
        LoginScreenViewModel viewModel = new LoginScreenViewModel();
        StringProperty usernameProperty = new SimpleStringProperty();
        StringProperty passwordProperty = new SimpleStringProperty();

        viewModel.usernameProperty().bindBidirectional(usernameProperty);
        viewModel.passwordProperty().bindBidirectional(passwordProperty);

        usernameProperty.setValue("");
        passwordProperty.setValue("password");

        assertThrows(
            IllegalArgumentException.class,
            () -> {viewModel.validateLogin();},
            "Check if an exception is thrown when the username is blank."
        );
    }

    @Test
    void testBlankPassword() {
        LoginScreenViewModel viewModel = new LoginScreenViewModel();
        StringProperty usernameProperty = new SimpleStringProperty();
        StringProperty passwordProperty = new SimpleStringProperty();

        viewModel.usernameProperty().bindBidirectional(usernameProperty);
        viewModel.passwordProperty().bindBidirectional(passwordProperty);

        usernameProperty.setValue("username");
        passwordProperty.setValue("");

        assertThrows(
            IllegalArgumentException.class,
            () -> {viewModel.validateLogin();},
            "Check if an exception is thrown when the password is blank."
        );
    }
}
