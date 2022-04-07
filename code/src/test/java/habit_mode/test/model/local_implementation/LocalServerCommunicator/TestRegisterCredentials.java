package habit_mode.test.model.local_implementation.LocalServerCommunicator;
import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;


import org.junit.jupiter.api.Test;


import habit_mode.model.local_implementation.LocalServerCommunicator;
import habit_mode.model.SuccessCode;
public class TestRegisterCredentials {

    @Test
    void testInvalidUsername(){
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        String username1 = "";
        String password = "123";
        String email = "emailadd";
        SuccessCode code = SuccessCode.INVALID_USERNAME;

        assertAll(
            () -> {assertEquals(code, communicator.registerCredentials(username1, password, email));},
            () -> {assertEquals(code, communicator.registerCredentials(null, password, email));}
        );
    }
    @Test
    void testInvalidPassword(){
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        String username1 = "Admin";
        String password = "";
        String email = "emailadd";
        SuccessCode code = SuccessCode.INVALID_PASSWORD;

        assertAll(
            () -> {assertEquals(code, communicator.registerCredentials(username1, password, email));},
            () -> {assertEquals(code, communicator.registerCredentials(username1, null, email));}
        );
    }
    @Test
    void testInvalidEmail(){
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        String username1 = "Admin";
        String password = "Adin";
        String email = "";
        SuccessCode code = SuccessCode.INVALID_EMAIL;

        assertAll(
            () -> {assertEquals(code, communicator.registerCredentials(username1, password, email));},
            () -> {assertEquals(code, communicator.registerCredentials(username1, password, null));}
        );
    }
    @Test
    void testRepeatedUsernameAndValidUsername(){
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        String username1 = "Admin";
        String password = "Adin";
        String email = "Admin";
        SuccessCode code1 = SuccessCode.USERNAME_ALREADY_EXISTS;
        SuccessCode code2 = SuccessCode.OKAY;

        assertAll(
            () -> {assertEquals(code2, communicator.registerCredentials(username1, password, email));},
            () -> {assertEquals(code1, communicator.registerCredentials(username1, password, email));}
        );
    }
}
    
