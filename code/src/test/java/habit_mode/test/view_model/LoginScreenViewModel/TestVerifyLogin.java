package habit_mode.test.view_model.LoginScreenViewModel;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import habit_mode.model.SuccessCode;
import habit_mode.view_model.LoginScreenViewModel;
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.StringProperty;

public class TestVerifyLogin {
    @Test
    void testValidLogin() {
        LoginScreenViewModel viewModel = new LoginScreenViewModel(true);
        StringProperty usernameProperty = new SimpleStringProperty();
        StringProperty passwordProperty = new SimpleStringProperty();

        viewModel.usernameProperty().bindBidirectional(usernameProperty);
        viewModel.passwordProperty().bindBidirectional(passwordProperty);

        usernameProperty.setValue("username");
        passwordProperty.setValue("password");

        viewModel.getServerCommunicator().registerCredentials("username", "password", "email");

        assertEquals(SuccessCode.OKAY, viewModel.validateLogin(), "Check if the login credentials are correctly verified");
    }

    @Test
    void testBlankUsername() {
        LoginScreenViewModel viewModel = new LoginScreenViewModel(true);
        StringProperty usernameProperty = new SimpleStringProperty();
        StringProperty passwordProperty = new SimpleStringProperty();

        viewModel.usernameProperty().bindBidirectional(usernameProperty);
        viewModel.passwordProperty().bindBidirectional(passwordProperty);

        usernameProperty.setValue("");
        passwordProperty.setValue("password");

        assertEquals(SuccessCode.INVALID_LOGIN_CREDENTIALS, viewModel.validateLogin());

    }

    @Test
    void testBlankPassword() {
        LoginScreenViewModel viewModel = new LoginScreenViewModel(true);
        StringProperty usernameProperty = new SimpleStringProperty();
        StringProperty passwordProperty = new SimpleStringProperty();

        viewModel.usernameProperty().bindBidirectional(usernameProperty);
        viewModel.passwordProperty().bindBidirectional(passwordProperty);

        usernameProperty.setValue("username");
        passwordProperty.setValue("");

        assertEquals(SuccessCode.INVALID_LOGIN_CREDENTIALS, viewModel.validateLogin());
    }
}
