package habit_mode.test.model.habit_manager;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.HabitManager;

class TestGet {
    @Test
    void testWhenIndexIsValid() {
        Habit habit = new Habit("Hello!", Frequency.DAILY);
        HabitManager manager = new HabitManager();
        manager.add(habit);
        
        Habit result = manager.get(0);

        assertAll(
            () -> {assertEquals(result, habit, "Check if return is correct.");},
            () -> {assertTrue(manager.contains(habit), "Check if habit is still in the manager.");}
        );
    }

    @Test
    void testWhenTheManagerIsEmpty() {
        HabitManager manager = new HabitManager();
        assertThrows(
            IllegalArgumentException.class, 
            ()->{
                manager.get(0);
            }
        );
    }

    @Test
    void testWhenTheIndexIsLessThanZero() {
        HabitManager manager = new HabitManager();
        Habit habit = new Habit("Hello!", Frequency.DAILY);
        manager.add(habit);
        assertThrows(
            IllegalArgumentException.class, 
            ()->{
                manager.get(-1);
            }
        );
    }

    @Test
    void testWhenTheIndexIsGreaterThanTheIndicesOfTheManager() {
        HabitManager manager = new HabitManager();
        Habit habit = new Habit("Hello!", Frequency.DAILY);
        manager.add(habit);
        assertThrows(
            IllegalArgumentException.class, 
            ()->{
                manager.get(1);
            }
        );
    }
}
