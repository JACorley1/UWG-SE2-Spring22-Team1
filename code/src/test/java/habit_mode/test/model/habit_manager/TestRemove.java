package habit_mode.test.model.habit_manager;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.HabitManager;

class TestRemove {
    @Test
    void testRemoveWithTheHabitInTheManager() {
        Habit habit = new Habit("Hello!", Frequency.DAILY);
        HabitManager manager = new HabitManager();
        manager.add(habit);

        boolean result = manager.remove(habit);

        assertAll(
            () -> {assertTrue(result, "Check if return is correct.");},
            () -> {assertTrue(!manager.contains(habit), "Check if habit was removed.");}
        );
    }

    @Test
    void testRemoveWithoutTheHabitInTheManager() {
        Habit habit = new Habit("Hello!", Frequency.DAILY);
        HabitManager manager = new HabitManager();

        boolean result = manager.remove(habit);

        assertAll(
            () -> {assertTrue(!result, "Check if return is correct.");},
            () -> {assertTrue(!manager.contains(habit), "Check that the habit is not in the manager.");}
        );
    }

    @Test
    void testRemoveWithValidIndex() {
        Habit habit = new Habit("Hello!", Frequency.DAILY);
        HabitManager manager = new HabitManager();
        manager.add(habit);

        Habit result = manager.remove(0);

        assertAll(
            () -> {assertTrue(result == habit, "Check if return is correct.");},
            () -> {assertTrue(!manager.contains(habit), "Check that the habit is not in the manager.");}
        );
    }

    @Test
    void testWhenIndexIsGreaterThanTheIndicesOfTheManager() {
        HabitManager manager = new HabitManager();
        Habit habit = new Habit("Hello!", Frequency.DAILY);
        manager.add(habit);

        assertThrows(
            IllegalArgumentException.class, 
            ()->{
                manager.remove(manager.size());
            }
        );
    }

    @Test
    void testWhenIndexIsLessThanZero() {
        HabitManager manager = new HabitManager();
        
        assertThrows(
            IllegalArgumentException.class, 
            ()->{
                manager.remove(-1);
            }
        );
    }

    @Test
    void testRemoveWhenTheHabitIsNull() {
        HabitManager manager = new HabitManager();

        assertThrows(
            IllegalArgumentException.class, 
            ()->{
                manager.remove(null);
            }
        );
    }
}
