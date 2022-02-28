package habit_mode.test.model.habit_manager;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.HabitManager;

class TestIsEmpty {
    @Test
    void testWhenManagerIsEmpty() {
        HabitManager manager = new HabitManager();

        assertTrue(manager.isEmpty(), "Checking that the manager is empty upon creation.");
    }

    @Test
    void testWhenManagerIsNotEmpty() {
        HabitManager manager = new HabitManager();
        Habit habit = new Habit("Habit", Frequency.DAILY);
        manager.add(habit);

        assertFalse(manager.isEmpty(), "Checking that the manager is empty upon creation.");
    }
}
