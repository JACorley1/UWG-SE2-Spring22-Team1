package habit_mode.test.model.habit_manager;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.ArrayList;
import java.util.List;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.HabitManager;

class TestContainsAll {
    @Test
    void testWithAllOfTheHabitsInTheManager() {
        Habit habit1 = new Habit("Hello!", Frequency.DAILY);
        Habit habit2 = new Habit("Bye!", Frequency.DAILY);

        List<Habit> habits = new ArrayList<Habit>();
        HabitManager manager = new HabitManager();

        habits.add(habit1);
        habits.add(habit2);
        manager.add(habit1);
        manager.add(habit2);

        boolean result = manager.containsAll(habits);

        assertTrue(result, "Checking that the result is correct when the manager contains all of the habits.");
    }

    @Test
    void testWithOneHabitNotInTheManager() {
        Habit habit1 = new Habit("Hello!", Frequency.DAILY);
        Habit habit2 = new Habit("Bye!", Frequency.DAILY);

        List<Habit> habits = new ArrayList<Habit>();
        HabitManager manager = new HabitManager();

        habits.add(habit1);
        habits.add(habit2);
        manager.add(habit1);

        boolean result = manager.containsAll(habits);

        assertFalse(result, "Checking that the manager responds correctly to it not containing the habit.");
    }

    @Test
    void testWhenTheHabitToCheckIsNull() {
        HabitManager manager = new HabitManager();
        assertThrows(
            IllegalArgumentException.class, 
            ()->{
                manager.containsAll(null);
            }
        );
    }
}
