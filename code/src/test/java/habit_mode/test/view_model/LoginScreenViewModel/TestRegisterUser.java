package habit_mode.test.view_model.LoginScreenViewModel;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import habit_mode.model.SuccessCode;
import habit_mode.view_model.LoginScreenViewModel;
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.StringProperty;

public class TestRegisterUser {
    @Test
    void testValidCredentials() {
        LoginScreenViewModel viewModel = new LoginScreenViewModel();
        StringProperty usernameProperty = new SimpleStringProperty();
        StringProperty passwordProperty = new SimpleStringProperty();
        StringProperty emailProperty = new SimpleStringProperty();

        viewModel.usernameProperty().bindBidirectional(usernameProperty);
        viewModel.passwordProperty().bindBidirectional(passwordProperty);
        viewModel.emailProperty().bindBidirectional(emailProperty);

        usernameProperty.setValue("test");
        passwordProperty.setValue("password");
        emailProperty.setValue("email@gmail.com");

        SuccessCode result = viewModel.registerUser();

        assertEquals(SuccessCode.OKAY, result, "Check if the registration credentials are correctly processed.");
    }

    @Test
    void testInvalidkUsername() {
        LoginScreenViewModel viewModel = new LoginScreenViewModel();
        StringProperty usernameProperty = new SimpleStringProperty();
        StringProperty passwordProperty = new SimpleStringProperty();
        StringProperty emailProperty = new SimpleStringProperty();

        viewModel.usernameProperty().bindBidirectional(usernameProperty);
        viewModel.passwordProperty().bindBidirectional(passwordProperty);
        viewModel.emailProperty().bindBidirectional(emailProperty);

        usernameProperty.setValue("");
        passwordProperty.setValue("password");
        emailProperty.setValue("email@gmail.com");

        SuccessCode result = viewModel.registerUser();

        assertEquals(SuccessCode.INVALID_USERNAME, result);

    }

    @Test
    void testInvalidPassword() {
        LoginScreenViewModel viewModel = new LoginScreenViewModel();
        StringProperty usernameProperty = new SimpleStringProperty();
        StringProperty passwordProperty = new SimpleStringProperty();
        StringProperty emailProperty = new SimpleStringProperty();

        viewModel.usernameProperty().bindBidirectional(usernameProperty);
        viewModel.passwordProperty().bindBidirectional(passwordProperty);
        viewModel.emailProperty().bindBidirectional(emailProperty);

        usernameProperty.setValue("username");
        passwordProperty.setValue("");
        emailProperty.setValue("email@gmail.com");

        SuccessCode result = viewModel.registerUser();

        assertEquals(SuccessCode.INVALID_PASSWORD, result);
    }

    @Test
    void testInvalidEmail() {
        LoginScreenViewModel viewModel = new LoginScreenViewModel();
        StringProperty usernameProperty = new SimpleStringProperty();
        StringProperty passwordProperty = new SimpleStringProperty();
        StringProperty emailProperty = new SimpleStringProperty();

        viewModel.usernameProperty().bindBidirectional(usernameProperty);
        viewModel.passwordProperty().bindBidirectional(passwordProperty);
        viewModel.emailProperty().bindBidirectional(emailProperty);

        usernameProperty.setValue("username");
        passwordProperty.setValue("password");
        emailProperty.setValue("");

        SuccessCode result = viewModel.registerUser();

        assertEquals(SuccessCode.INVALID_EMAIL, result);
    }

    @Test
    void testUsernameAlredyInUse() {
        LoginScreenViewModel viewModel = new LoginScreenViewModel();
        StringProperty usernameProperty = new SimpleStringProperty();
        StringProperty passwordProperty = new SimpleStringProperty();
        StringProperty emailProperty = new SimpleStringProperty();

        viewModel.usernameProperty().bindBidirectional(usernameProperty);
        viewModel.passwordProperty().bindBidirectional(passwordProperty);
        viewModel.emailProperty().bindBidirectional(emailProperty);

        usernameProperty.setValue("username");
        passwordProperty.setValue("password");
        emailProperty.setValue("email@gmail.com");
        viewModel.registerUser();

        usernameProperty.setValue("username");
        passwordProperty.setValue("password2");
        emailProperty.setValue("email2@gmail.com");
        SuccessCode result = viewModel.registerUser();

        assertEquals(SuccessCode.USERNAME_ALREADY_EXISTS, result);
    }
}
