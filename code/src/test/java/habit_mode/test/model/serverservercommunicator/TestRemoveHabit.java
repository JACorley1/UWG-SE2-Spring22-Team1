package habit_mode.test.model.serverservercommunicator;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.List;
import java.util.Random;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.ServerCommunicator;
import habit_mode.model.ServerServerCommunicator;

public class TestRemoveHabit {
    @Test
    void testOneHabit(){
        ServerCommunicator communicator = new ServerServerCommunicator("tcp://*:5553");
        TrueMockServer server = new TrueMockServer(5553);
        server.start();
        Random rand = new Random();
        String username = rand.nextInt() + "";
        communicator.registerCredentials(username, "password", "email");

        communicator.validateLogin(username, "password");
        Habit habit = new Habit("text", Frequency.DAILY);
        communicator.addHabit(habit);
        communicator.removeHabit(habit);

        List<Habit> habits = communicator.getHabits();
        server.interrupt();
        assertEquals(0, habits.size());
    }
}
