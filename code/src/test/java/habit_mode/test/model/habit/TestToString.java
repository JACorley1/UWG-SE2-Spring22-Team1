package habit_mode.test.model.habit;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;

public class TestToString {
    @Test
    void testToString() {
        Habit habit = new Habit("habit", Frequency.MONTHLY);

        assertEquals("habit", habit.toString());
    }
}
