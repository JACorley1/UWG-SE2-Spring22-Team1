package habit_mode.test.model.habit_manager;

import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.HabitManager;

class TestLastIndexOf {
    @Test
    void testLastIndexOfWithTheHabitInTheManager() {
        Habit habit = new Habit("Hello!", Frequency.DAILY);
        HabitManager manager = new HabitManager();
        manager.add(habit);

        int result = manager.lastIndexOf(habit);

        assertTrue(result == 0, "Check if return is correct.");
    }

    @Test
    void testLastIndexOfWithoutTheHabitInTheManager() {
        Habit habit = new Habit("Hello!", Frequency.DAILY);
        HabitManager manager = new HabitManager();

        int result = manager.lastIndexOf(habit);

        assertTrue(result == -1, "Check if return is correct.");
    }

    @Test
    void testLastIndexOfWhenTheHabitIsNull() {
        HabitManager manager = new HabitManager();

        assertThrows(
            IllegalArgumentException.class, 
            ()->{
                manager.lastIndexOf(null);
            }
        );
    }
}
