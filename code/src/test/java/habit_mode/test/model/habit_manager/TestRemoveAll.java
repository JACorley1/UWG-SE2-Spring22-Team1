package habit_mode.test.model.habit_manager;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.ArrayList;
import java.util.List;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.HabitManager;

class TestRemoveAll {
    @Test
	void testWhenRemovingAllHabitsInTheManager() {
		Habit habit1 = new Habit("Hello!", Frequency.DAILY);
        Habit habit2 = new Habit("Bye!", Frequency.DAILY);

        List<Habit> habits = new ArrayList<Habit>();
        HabitManager manager = new HabitManager();

        habits.add(habit1);
        habits.add(habit2);
        manager.addAll(habits);

        boolean result = manager.removeAll(habits);

        assertAll(
            () -> {assertTrue(result, "Checking that the result is correct when the manager removes all of the habits.");},
            () -> {assertEquals(0, manager.size(), "Checking that the size of the manager is correct after testing.");}
        );
	}

    @Test 
    void testWhenRemovingAllButOneHabitInTheManager() {
        Habit habit1 = new Habit("Hello!", Frequency.DAILY);
        Habit habit2 = new Habit("Bye!", Frequency.DAILY);
        Habit habit3 = new Habit("Hi!", Frequency.WEEKLY);
        List<Habit> habits = new ArrayList<Habit>();
        HabitManager manager = new HabitManager();
        habits.add(habit3);
        habits.add(habit2);
        habits.add(habit1);
        manager.addAll(habits);
        habits.remove(habit3);

        boolean result = manager.removeAll(habits);

        assertAll(
            () -> {assertTrue(result, "Checking that the result is correct when the manager removes some of the habits.");},
            () -> {assertEquals(1, manager.size(), "Checking that the size of the manager is correct after testing.");}
        );
    }

    @Test
    void testRemovingACollectionOfHabitsWhenTheManagerIsEmpty() {
        Habit habit1 = new Habit("Hello!", Frequency.DAILY);
        Habit habit2 = new Habit("Bye!", Frequency.DAILY);
        Habit habit3 = new Habit("Hi!", Frequency.WEEKLY);
        List<Habit> habits = new ArrayList<Habit>();
        HabitManager manager = new HabitManager();
        habits.add(habit3);
        habits.add(habit2);
        habits.add(habit1);

        boolean result = manager.removeAll(habits);

        assertAll(
            () -> {assertFalse(result, "Checking that the result is correct when the manager doesn't remove any of the habits.");},
            () -> {assertEquals(0, manager.size(), "Checking that the size of the manager is still correct after testing.");}
        );
    }

	@Test
	void testWhenRemovingANullCollectionOfHabits() {
        HabitManager manager = new HabitManager();

		assertThrows(
			IllegalArgumentException.class, 
			()->{
				manager.removeAll(null);
			}
		);
	}
}