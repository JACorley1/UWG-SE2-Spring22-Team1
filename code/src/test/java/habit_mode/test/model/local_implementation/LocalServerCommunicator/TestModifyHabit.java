package habit_mode.test.model.local_implementation.LocalServerCommunicator;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.SuccessCode;
import habit_mode.model.local_implementation.LocalServerCommunicator;

public class TestModifyHabit {
    @Test
    void testModifyHabit() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        Habit habit = new Habit("habit", Frequency.DAILY);

        communicator.addHabit(habit);
        habit.textProperty().set("new habit");
        habit.setFrequency(Frequency.WEEKLY);

        assertAll(
            () -> {assertEquals(communicator.modifyHabit(habit), SuccessCode.OKAY, "Check if return is correct");},
            () -> {assertEquals(communicator.getHabits().get(0).textProperty().get(), "new habit");},
            () -> {assertEquals(communicator.getHabits().get(0).getFrequency(), Frequency.WEEKLY);}
        );
    }

    @Test
    void testModifyNullHabit() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();

        assertEquals(SuccessCode.INVALID_HABIT_NAME, communicator.modifyHabit(null));
    }

    @Test
    void testModifyHabitNotFound() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        Habit habit = new Habit("habit", Frequency.DAILY);

        communicator.addHabit(habit);
        habit.setId(1);
        habit.textProperty().set("new habit");
        habit.setFrequency(Frequency.WEEKLY);

        assertEquals(SuccessCode.NO_HABIT_FOUND, communicator.modifyHabit(habit));
    }
}
