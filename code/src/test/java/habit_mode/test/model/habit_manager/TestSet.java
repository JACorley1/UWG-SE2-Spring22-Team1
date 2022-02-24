package habit_mode.test.model.habit_manager;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.HabitManager;

class TestSet {
    @Test
    void testWhenSettingAValidHabitAndIndexInTheManager() {
        Habit habit1 = new Habit("Hello!", Frequency.DAILY);
        Habit habit2 = new Habit("Bye!", Frequency.DAILY);

        HabitManager manager = new HabitManager();

        manager.add(habit1);
        manager.add(habit2);

        Habit result = manager.set(0, habit2);

        assertAll(
            () -> {assertEquals(result, habit1, "Checking that the result is correct when the manager sets the habit.");},
            () -> {assertEquals(habit2, manager.get(0), "Checking that the Habit is correctly set after testing.");}
        );
    }

    @Test
    void testWhenTheIndexIsGreaterThanTheIndicesOfTheManager() {
        HabitManager manager = new HabitManager();
        Habit habit = new Habit("Hello!", Frequency.DAILY);
        assertThrows(
            IllegalArgumentException.class, 
            ()->{
                manager.set(1, habit);
            }
        );
    }

    @Test
    void testWhenTheIndexIsLessThanZero() {
        HabitManager manager = new HabitManager();
        Habit habit = new Habit("Hello!", Frequency.DAILY);
        assertThrows(
            IllegalArgumentException.class, 
            ()->{
                manager.set(-1, habit);
            }
        );
    }

    @Test
    void testWhenSettingANullHabitWithAValidIndex() {
        HabitManager manager = new HabitManager();
        Habit habit1 = new Habit("Hello!", Frequency.DAILY);
        manager.add(habit1);
        assertThrows(
            IllegalArgumentException.class, 
            ()->{
                manager.set(0, null);
            }
        );
    }
}
