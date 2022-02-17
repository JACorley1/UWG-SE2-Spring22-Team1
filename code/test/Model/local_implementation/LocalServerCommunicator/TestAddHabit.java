package code.test.Model.local_implementation.LocalServerCommunicator;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

import code.model.Frequency;
import code.model.Habit;
import code.model.local_implementation.LocalServerCommunicator;

public class TestAddHabit {
    @Test
    void testAddOneHabit() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        Habit habit = new Habit("habit", Frequency.DAILY);

        boolean result = communicator.addHabit(habit);
        assertAll(
            () -> {assertTrue(result, "Check if return is correct");},
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
            () -> {assertTrue(communicator.addHabit(habit1), "Check if return for first habit is correct");},
            () -> {assertTrue(communicator.addHabit(habit2), "Check if return for second habit is correct");},
            () -> {assertTrue(communicator.getHabits().contains(habit1), "Check if first habit was added");},
            () -> {assertTrue(communicator.getHabits().contains(habit2), "Check if second habit was added");}
        );
    }

    @Test
    void testAddNullHabit() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        
        assertThrows(
            IllegalArgumentException.class,
            () -> {communicator.addHabit(null);},
            "Check if exception is thrown when adding a null habit."
        );
    }

    @Test
    void testAddDuplicateHabit() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        Habit habit = new Habit("Habit", Frequency.DAILY);
        communicator.addHabit(habit);
        
        assertFalse(communicator.addHabit(habit), "Check if false is returned when adding a duplicate habit.");
    }
}
