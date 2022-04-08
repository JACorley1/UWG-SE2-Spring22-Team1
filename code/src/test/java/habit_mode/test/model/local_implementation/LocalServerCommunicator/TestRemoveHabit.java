package habit_mode.test.model.local_implementation.LocalServerCommunicator;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.SuccessCode;
import habit_mode.model.local_implementation.LocalServerCommunicator;

public class TestRemoveHabit {
    @Test
    void testRemoveOneHabit() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        Habit habit = new Habit("habit", Frequency.DAILY);

        communicator.addHabit(habit);

        assertAll(
            () -> {assertEquals(communicator.removeHabit(habit), SuccessCode.OKAY, "Check if return is correct");},
            () -> {assertFalse(communicator.getHabits().contains(habit), "Check if habit was removed");}
        );
    }

    @Test
    void testRemoveManyHabits() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        Habit habit1 = new Habit("habit1", Frequency.DAILY);
        Habit habit2 = new Habit("habit2", Frequency.DAILY);
        communicator.addHabit(habit1);
        communicator.addHabit(habit2);

        assertAll(
            () -> {assertEquals(communicator.removeHabit(habit1), SuccessCode.OKAY, "Check if return for first habit is correct");},
            () -> {assertEquals(communicator.removeHabit(habit2), SuccessCode.OKAY, "Check if return for second habit is correct");},
            () -> {assertFalse(communicator.getHabits().contains(habit1), "Check if first habit was removed");},
            () -> {assertFalse(communicator.getHabits().contains(habit2), "Check if second habit was removed");}
        );
    }

    @Test
    void testRemoveNullHabit() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        
        assertEquals(SuccessCode.INVALID_HABIT_NAME, communicator.removeHabit(null));
    }

    @Test
    void testRemoveHabitTwice() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        Habit habit = new Habit("Habit", Frequency.DAILY);
        communicator.addHabit(habit);
        communicator.removeHabit(habit);
        
        assertEquals(communicator.removeHabit(habit), SuccessCode.NO_HABIT_FOUND, "Check if false is returned when removing a duplicate twice.");
    }

    @Test
    void testRemoveHabitFromEmptyList() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        Habit habit = new Habit("Habit", Frequency.DAILY);
        
        assertEquals(communicator.removeHabit(habit), SuccessCode.NO_HABIT_FOUND, "Check if false is returned when removing from an empty list.");
    }
}
