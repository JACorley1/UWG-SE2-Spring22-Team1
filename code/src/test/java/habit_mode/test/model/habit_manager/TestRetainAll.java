package habit_mode.test.model.habit_manager;

import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertFalse;

import java.util.ArrayList;
import java.util.List;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.HabitManager;

class TestRetainAll {
    @Test 
    void testWhenRetainingAllHabitsInTheManager() {
        Habit habit1 = new Habit("Hello!", Frequency.DAILY);
        Habit habit2 = new Habit("Bye!", Frequency.DAILY);

        List<Habit> habits = new ArrayList<Habit>();
        HabitManager manager = new HabitManager();

        habits.add(habit1);
        habits.add(habit2);
        manager.addAll(habits);

        assertFalse(manager.retainAll(habits), "Ensuring that the list doesn't change when retaining all values in the list.");
    }

    @Test 
    void testWhenRetainingAllButOneHabitInTheManager() {
        Habit habit1 = new Habit("Hello!", Frequency.DAILY);
        Habit habit2 = new Habit("Bye!", Frequency.DAILY);

        List<Habit> habits = new ArrayList<Habit>();
        HabitManager manager = new HabitManager();

        habits.add(habit1);
        habits.add(habit2);
        manager.addAll(habits);
        habits.remove(habit1);

        assertTrue(manager.retainAll(habits), "Ensuring that the list does change when retaining all values in the list.");
    }

    @Test
    void testWhenRetainingANullCollectionOfHabits() {
        HabitManager manager = new HabitManager();

        assertThrows(
            IllegalArgumentException.class, 
            ()->{
                manager.retainAll(null);
            }
        );
    }
}
