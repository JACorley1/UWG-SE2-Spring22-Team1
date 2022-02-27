package habit_mode.test.model.habit;

import static org.junit.jupiter.api.Assertions.assertNotEquals;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;

public class TestHashCode {
    @Test
    void testTeoSimilarHabitsAreDifferent() {
        Habit habit1 = new Habit("habit", Frequency.DAILY);
        Habit habit2 = new Habit("habit", Frequency.DAILY);

        assertNotEquals(habit1.hashCode(), habit2.hashCode());
    }
}
