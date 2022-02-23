package habit_mode.test.model.habit_manager;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.HabitManager;

class TestToArray {
    @Test
    void testToArrayWithoutParameter() {
        Habit habit = new Habit("Hello!", Frequency.DAILY);
        HabitManager manager = new HabitManager();
        manager.add(habit);

        Object[] result = manager.toArray();

        assertFalse(result.equals(manager.toArray()), "Checking that the manager converts to different arrays.");
    }

    @Test
    void testToArrayWithAValidArrayPassedIn() {
        Object[] array = new Object[1];
        Habit habit = new Habit("Hello!", Frequency.DAILY);
        HabitManager manager = new HabitManager();
        manager.add(habit);

        Object[] result = manager.toArray(array);

        assertTrue(result.equals(manager.toArray(array)), "Checking that the manager converts its value into the specified array.");
    }
}
