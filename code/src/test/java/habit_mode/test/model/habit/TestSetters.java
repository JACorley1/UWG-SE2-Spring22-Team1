package habit_mode.test.model.habit;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;

class TestSetters {
    @Test
    void testSetFrequency() {
        Habit habit = new Habit("Hello!", Frequency.DAILY);

        habit.setFrequency(Frequency.WEEKLY);

        assertEquals(Frequency.WEEKLY, habit.getFrequency(), "Checking that the frequency is set");
    }
}