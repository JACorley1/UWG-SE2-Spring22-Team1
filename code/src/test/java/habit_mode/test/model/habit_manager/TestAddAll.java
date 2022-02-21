package habit_mode.test.model.habit_manager;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.ArrayList;
import java.util.List;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.HabitManager;

class TestAddAll {
    @Test
	void testWhenAddingValidHabitsInTheManager() {
		Habit habit1 = new Habit("Hello!", Frequency.DAILY);
        Habit habit2 = new Habit("Bye!", Frequency.DAILY);

        List<Habit> habits = new ArrayList<Habit>();
        HabitManager manager = new HabitManager();

        habits.add(habit1);
        habits.add(habit2);

        boolean result = manager.addAll(habits);

        assertAll(
            () -> {assertTrue(result, "Checking that the result is correct when the manager adds all of the habits.");},
            () -> {assertEquals(2, manager.size(), "Checking that the size of the manager is correct after testing.");}
        );
	}

    @Test 
    void testAddAllWithAValidCollectionAndIndex() {
        Habit habit1 = new Habit("Hello!", Frequency.DAILY);
        Habit habit2 = new Habit("Bye!", Frequency.DAILY);
        Habit habit3 = new Habit("Hi!", Frequency.WEEKLY);
        List<Habit> habits = new ArrayList<Habit>();
        HabitManager manager = new HabitManager();

        manager.add(habit3);
        habits.add(habit2);
        habits.add(habit1);

        boolean result = manager.addAll(0, habits);

        assertAll(
            () -> {assertTrue(result, "Checking that the result is correct when the manager adds all of the habits.");},
            () -> {assertEquals(3, manager.size(), "Checking that the size of the manager is correct after testing.");}
        );
    }

    @Test
    void testWhenTheIndexIsGreaterThanTheSizeOfTheManager() {
        HabitManager manager = new HabitManager();
        List<Habit> habits = new ArrayList<Habit>();

		assertThrows(
			IllegalArgumentException.class, 
			()->{
				manager.addAll(1, habits);
			}
		);
    }

    @Test
    void testWhenTheIndexIsLessThanZero() {
        HabitManager manager = new HabitManager();
        List<Habit> habits = new ArrayList<Habit>();

		assertThrows(
			IllegalArgumentException.class, 
			()->{
				manager.addAll(-1, habits);
			}
		);
    }

    @Test
    void testWhenAddingANullCollectionOfHabitsWithAValidIndex() {
        HabitManager manager = new HabitManager();

		assertThrows(
			IllegalArgumentException.class, 
			()->{
				manager.addAll(0, null);
			}
		);
    }

	@Test
	void testWhenAddingANullCollectionOfHabits() {
        HabitManager manager = new HabitManager();

		assertThrows(
			IllegalArgumentException.class, 
			()->{
				manager.addAll(null);
			}
		);
	}
}
