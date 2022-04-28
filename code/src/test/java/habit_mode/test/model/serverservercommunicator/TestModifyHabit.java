package habit_mode.test.model.serverservercommunicator;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Random;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.ServerCommunicator;
import habit_mode.model.ServerServerCommunicator;
import habit_mode.model.SuccessCode;

public class TestModifyHabit {
    @Test
    public void testModifyHabit() {
        TrueMockServer server = new TrueMockServer(5558);
        server.start();
        ServerCommunicator communicator = new ServerServerCommunicator("tcp://*:5558");
        Random rand = new Random();
        String username = rand.nextInt() + "";
        Habit habit = new Habit("text", Frequency.DAILY);

        communicator.registerCredentials(username, "password", "email");
        communicator.validateLogin(username, "password");
        communicator.addHabit(habit);

        assertEquals(SuccessCode.OKAY, communicator.modifyHabit(habit));
    }
}
