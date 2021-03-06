package habit_mode.test.model.local_implementation.LocalServerCommunicator;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.SuccessCode;
import habit_mode.model.local_implementation.LocalServerCommunicator;

public class TestCompleteHabit {
    @Test
    void testCompleteSingleHabit() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        Habit habit = new Habit("habit", Frequency.DAILY);

        communicator.addHabit(habit);
        Habit serverHabit = communicator.getServerSideHabit(habit);

        assertAll(
            () -> {assertEquals(communicator.completeHabit(habit), SuccessCode.OKAY, "Check if return is correct");},
            () -> {assertTrue(serverHabit.isComplete(), "Check if habit was completed");}
        );
    }

    @Test
    void testCompleteManyHabits() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        Habit habit1 = new Habit("habit", Frequency.DAILY);
        Habit habit2 = new Habit("habit2", Frequency.DAILY);

        communicator.addHabit(habit1);
        communicator.addHabit(habit2);
        Habit serverHabit1 = communicator.getServerSideHabit(habit1);
        Habit serverHabit2 = communicator.getServerSideHabit(habit2);

        assertAll(
            () -> {assertEquals(communicator.completeHabit(habit1), SuccessCode.OKAY, "Check if return is correct");},
            () -> {assertEquals(communicator.completeHabit(habit2), SuccessCode.OKAY, "Check if return is correct");},
            () -> {assertTrue(serverHabit1.isComplete(), "Check if habit was completed");},
            () -> {assertTrue(serverHabit2.isComplete(), "Check if habit was completed");}
        );
    }

    @Test
    void testCompleteHabitsAfterEarningBonus() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        Habit habit1 = new Habit("habit", Frequency.DAILY);
        Habit habit2 = new Habit("habit2", Frequency.DAILY);

        communicator.addHabit(habit1);
        communicator.completeHabit(habit1);

        communicator.addHabit(habit2);
        Habit serverHabit1 = communicator.getServerSideHabit(habit1);
        Habit serverHabit2 = communicator.getServerSideHabit(habit2);

        assertAll(
            () -> {assertEquals(communicator.completeHabit(habit2), SuccessCode.OKAY, "Check if return is correct");},
            () -> {assertTrue(serverHabit1.isComplete(), "Check if habit was completed");},
            () -> {assertTrue(serverHabit2.isComplete(), "Check if habit was completed");}
        );
    }

    @Test
    void testCompletingHabitNotAdded() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        Habit habit = new Habit("habit", Frequency.DAILY);

        assertAll(
            () -> {assertEquals(communicator.completeHabit(habit), SuccessCode.NO_HABIT_FOUND, "Check if return is correct");},
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
        Habit serverHabit = communicator.getServerSideHabit(habit);

        assertAll(
            () -> {assertEquals(communicator.completeHabit(habit), SuccessCode.OKAY, "Check if return is correct");},
            () -> {assertTrue(serverHabit.isComplete(), "Check if habit was not completed");}
        );
    }

    @Test
    void testCompletingNullHabit() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();

        assertEquals(SuccessCode.INVALID_HABIT_NAME, communicator.completeHabit(null));
    }
}
