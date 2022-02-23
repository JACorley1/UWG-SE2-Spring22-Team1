package habit_mode.test.model.habit_manager;

import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.HabitManager;

class TestIndexOf {
    @Test
    void testIndexOfWithTheHabitInTheManager() {
        Habit habit = new Habit("Hello!", Frequency.DAILY);
        HabitManager manager = new HabitManager();
        manager.add(habit);

        int result = manager.indexOf(habit);

        assertTrue(result == 0, "Check if return is correct.");
    }

    @Test
    void testIndexOfWithoutTheHabitInTheManager() {
        Habit habit = new Habit("Hello!", Frequency.DAILY);
        HabitManager manager = new HabitManager();

        int result = manager.indexOf(habit);

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

    @Test
    void testIndexOfWhenTheHabitIsNull() {
        HabitManager manager = new HabitManager();

        assertThrows(
            IllegalArgumentException.class, 
            ()->{
                manager.indexOf(null);
            }
        );
    }
}
