package habit_mode.test.model.serverservercommunicator;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.List;
import java.util.Random;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.ServerCommunicator;
import habit_mode.model.ServerServerCommunicator;

public class TestGetHabits {
    @Test
    void testNoHabits(){
        ServerCommunicator communicator = new ServerServerCommunicator("tcp://*:5551");
        TrueMockServer server = new TrueMockServer(5551);
        server.start();
        Random rand = new Random();
        String username = rand.nextInt() + "";
        communicator.registerCredentials(username, "password", "email");

        communicator.validateLogin(username, "password");
        List<Habit> habits = communicator.getHabits();
        server.interrupt();
        assertEquals(0, habits.size());

    }

    @Test
    void testOneHabit(){
        ServerCommunicator communicator = new ServerServerCommunicator("tcp://*:5551");
        TrueMockServer server = new TrueMockServer(5551);
        server.start();
        Random rand = new Random();
        String username = rand.nextInt() + "";
        communicator.registerCredentials(username, "password", "email");

        communicator.validateLogin(username, "password");
        Habit habit = new Habit("tet", Frequency.DAILY);
        communicator.addHabit(habit);

        List<Habit> habits = communicator.getHabits();
        server.interrupt();
        assertEquals(1, habits.size());
        assertEquals(habit, habits.get(0));

    }

    @Test
    void testMultipleHabits(){
        ServerCommunicator communicator = new ServerServerCommunicator("tcp://*:5551");
        TrueMockServer server = new TrueMockServer(5551);
        server.start();
        Random rand = new Random();
        String username = rand.nextInt() + "";
        communicator.registerCredentials(username, "password", "email");

        communicator.validateLogin(username, "password");
        Habit habit1 = new Habit("text", Frequency.DAILY);
        Habit habit2 = new Habit("test", Frequency.DAILY);
        communicator.addHabit(habit1);
        communicator.addHabit(habit2);

        List<Habit> habits = communicator.getHabits();
        server.interrupt();
    
        assertEquals(habit1.getFrequency(), habits.get(0).getFrequency());
        assertEquals(habit2.getFrequency(), habits.get(1).getFrequency());
    }
}
