package habit_mode.test.model.local_implementation.LocalServerCommunicator;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.SuccessCode;
import habit_mode.model.local_implementation.LocalServerCommunicator;

public class TestAddHabit {
    @Test
    void testAddOneHabit() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        Habit habit = new Habit("habit", Frequency.DAILY);

        SuccessCode result = communicator.addHabit(habit);
        assertAll(
            () -> {assertEquals(result, SuccessCode.OKAY, "Check method returns properly.");},
            () -> {assertTrue(communicator.getHabits().contains(habit), "Check if habit was added");}
        );
    }

    @Test
    void testAddManyHabits() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        Habit habit1 = new Habit("habit1", Frequency.DAILY);
        Habit habit2 = new Habit("habit2", Frequency.DAILY);

        assertAll(
            () -> {assertEquals(communicator.addHabit(habit1), SuccessCode.OKAY, "Check if return for first habit is correct");},
            () -> {assertEquals(communicator.addHabit(habit2), SuccessCode.OKAY, "Check if return for second habit is correct");},
            () -> {assertTrue(communicator.getHabits().contains(habit1), "Check if first habit was added");},
            () -> {assertTrue(communicator.getHabits().contains(habit2), "Check if second habit was added");}
        );
    }

    @Test
    void testAddNullHabit() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        
        assertEquals(SuccessCode.INVALID_HABIT_NAME, communicator.addHabit(null));
    }

}
