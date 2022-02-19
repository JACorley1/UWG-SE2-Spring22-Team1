package habit_mode.test.model.local_implementation.LocalServerCommunicator;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.local_implementation.LocalServerCommunicator;

public class TestRemoveHabit {
    @Test
    void testRemoveOneHabit() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        Habit habit = new Habit("habit", Frequency.DAILY);

        communicator.addHabit(habit);

        assertAll(
            () -> {assertTrue(communicator.removeHabit(habit), "Check if return is correct");},
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
            () -> {assertTrue(communicator.removeHabit(habit1), "Check if return for first habit is correct");},
            () -> {assertTrue(communicator.removeHabit(habit2), "Check if return for second habit is correct");},
            () -> {assertFalse(communicator.getHabits().contains(habit1), "Check if first habit was removed");},
            () -> {assertFalse(communicator.getHabits().contains(habit2), "Check if second habit was removed");}
        );
    }

    @Test
    void testRemoveNullHabit() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        
        assertThrows(
            IllegalArgumentException.class,
            () -> {communicator.removeHabit(null);},
            "Check if exception is thrown when removing a null habit."
        );
    }

    @Test
    void testRemoveHabitTwice() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        Habit habit = new Habit("Habit", Frequency.DAILY);
        communicator.addHabit(habit);
        
        assertFalse(communicator.addHabit(habit), "Check if false is returned when removing a duplicate twice.");
    }

    @Test
    void testRemoveHabitFromEmptyList() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        Habit habit = new Habit("Habit", Frequency.DAILY);
        
        assertFalse(communicator.removeHabit(habit), "Check if false is returned when removing from an empty list.");
    }
}
