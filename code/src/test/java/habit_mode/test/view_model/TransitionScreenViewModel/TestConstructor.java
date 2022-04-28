package habit_mode.test.view_model.TransitionScreenViewModel;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import habit_mode.model.ServerServerCommunicator;
import habit_mode.view_model.TransitionScreenViewModel;

public class TestConstructor {

    @Test
    void testDefaultConstructor() {
        TransitionScreenViewModel vm = new TransitionScreenViewModel();

        assertEquals(new ServerServerCommunicator().getClass(), vm.getServerCommunicator().getClass());
    }
    
}
