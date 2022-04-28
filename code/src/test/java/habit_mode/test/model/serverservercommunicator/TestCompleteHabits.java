package habit_mode.test.model.serverservercommunicator;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.List;
import java.util.Random;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.ServerCommunicator;
import habit_mode.model.ServerServerCommunicator;

public class TestCompleteHabits {
    @Test
    void testOneHabit() {
        TrueMockServer server = new TrueMockServer(5552);
        ServerCommunicator communicator = new ServerServerCommunicator("tcp://*:5552");
        Random rand = new Random();
        String username = rand.nextInt() + "";
        server.start();
        communicator.registerCredentials(username, "password", "email");

        communicator.validateLogin(username, "password");
        Habit habit = new Habit("text", Frequency.DAILY);
        communicator.addHabit(habit);
        communicator.completeHabit(habit);
        int coins = communicator.getCoins();
        List<Habit> habits = communicator.getHabits();
        server.interrupt();
        assertEquals(true, habits.get(0).isComplete());
        assertEquals(70, coins);
    }
}
