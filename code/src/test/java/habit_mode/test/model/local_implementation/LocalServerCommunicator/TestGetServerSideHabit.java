package habit_mode.test.model.local_implementation.LocalServerCommunicator;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotEquals;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.local_implementation.LocalServerCommunicator;

public class TestGetServerSideHabit {
    @Test
    void testHabitExists() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        Habit habit = new Habit("habit", Frequency.DAILY);

        communicator.addHabit(habit);
        Habit serverHabit = communicator.getServerSideHabit(habit);

        assertEquals(habit, serverHabit);
    }

    @Test
    void testHabitDoesNotExist() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        Habit habit = new Habit("habit", Frequency.DAILY);

        Habit serverHabit = communicator.getServerSideHabit(habit);

        assertNotEquals(habit, serverHabit);
    }
}
