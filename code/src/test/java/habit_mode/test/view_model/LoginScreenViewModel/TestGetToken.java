package habit_mode.test.view_model.LoginScreenViewModel;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import habit_mode.model.ServerCommunicator;
import habit_mode.model.ServerServerCommunicator;
import habit_mode.view_model.LoginScreenViewModel;

public class TestGetToken {

    @Test
    void testGetAuthenticationToken() {
        LoginScreenViewModel vm = new LoginScreenViewModel();
        ((ServerServerCommunicator) vm.getServerCommunicator()).setToken("token");

        assertEquals("token", vm.getAuthenticationToken());
    }
    
}
