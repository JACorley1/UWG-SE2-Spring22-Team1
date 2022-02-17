package code.test.Model.local_implementation.LocalServerCommunicator;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.Test;

import code.model.Frequency;
import code.model.Habit;
import code.model.local_implementation.LocalServerCommunicator;

public class TestCompleteHabit {
    @Test
    void testCompleteSingleHabit() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        Habit habit = new Habit("habit", Frequency.DAILY);

        communicator.addHabit(habit);

        assertAll(
            () -> {assertTrue(communicator.completeHabit(habit), "Check if return is correct");},
            () -> {assertTrue(habit.isComplete(), "Check if habit was completed");}
        );
    }

    @Test
    void testCompletingHabitNotAdded() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        Habit habit = new Habit("habit", Frequency.DAILY);

        assertAll(
            () -> {assertFalse(communicator.completeHabit(habit), "Check if return is correct");},
            () -> {assertFalse(habit.isComplete(), "Check if habit was not completed");}
        );
    }

    @Test
    void testCompletingAlreadyCompletedHabit() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        Habit habit = new Habit("habit", Frequency.DAILY);

        communicator.addHabit(habit);
        communicator.completeHabit(habit);

        assertAll(
            () -> {assertFalse(communicator.completeHabit(habit), "Check if return is correct");},
            () -> {assertTrue(habit.isComplete(), "Check if habit was not completed");}
        );
    }

    @Test
    void testCompletingNullHabit() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();

        assertThrows(
            IllegalArgumentException.class,
            () -> {communicator.completeHabit(null);},
            "Check is exception is thrown when completing a null habit."
        );
    }
}
