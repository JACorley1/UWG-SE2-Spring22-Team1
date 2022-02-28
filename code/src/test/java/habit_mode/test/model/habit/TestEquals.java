package habit_mode.test.model.habit;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotEquals;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;

public class TestEquals {
    @Test
    void testSimilarHabits() {
        Habit habit1 = new Habit("habit", Frequency.DAILY);
        Habit habit2 = new Habit("habit", Frequency.DAILY);

        assertEquals(habit1, habit2, "Check if two similar habits are equal.");
    }

    @Test
    void testDifferentText() {
        Habit habit1 = new Habit("habit", Frequency.DAILY);
        Habit habit2 = new Habit("habit1", Frequency.DAILY);

        assertNotEquals(habit1, habit2, "Check if two different habits are not equal.");
    }

    @Test
    void testDifferentFrequency() {
        Habit habit1 = new Habit("habit", Frequency.WEEKLY);
        Habit habit2 = new Habit("habit", Frequency.DAILY);

        assertNotEquals(habit1, habit2, "Check if two different habits are not equal.");
    }

    @Test
    void testEqualsNull() {
        Habit habit1 = new Habit("habit", Frequency.DAILY);
        Habit habit2 = null;

        assertNotEquals(habit1, habit2, "Check if two different habits are not equal.");
    }
}
