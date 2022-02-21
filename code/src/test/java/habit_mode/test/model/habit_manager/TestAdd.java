package habit_mode.test.model.habit_manager;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.HabitManager;

class TestAdd {
    @Test
	void testAddWithValidHabit() {
		Habit habit = new Habit("Hello!", Frequency.DAILY);
        HabitManager manager = new HabitManager();

        boolean result = manager.add(habit);

        assertAll(
            () -> {assertTrue(result, "Check if return is correct");},
            () -> {assertTrue(manager.contains(habit), "Check if habit was added");}
        );
	}

    @Test
    void testAddWithAValidHabitAndIndex() {
        Habit habit = new Habit("Hello!", Frequency.DAILY);
        HabitManager manager = new HabitManager();

        manager.add(0, habit);
        int result = manager.size();
        assertAll(
            () -> {assertEquals(1, result, "Check if the result is correct");},
            () -> {assertTrue(manager.contains(habit), "Check if habit was added");}
        );
    }

    @Test
    void testAddWhenTheIndexIsTheSizeOfTheManager() {
        Habit habit1 = new Habit("Hello!", Frequency.DAILY);
        Habit habit2 = new Habit("Bye!", Frequency.DAILY);
        HabitManager manager = new HabitManager();
        manager.add(habit1);

        manager.add(manager.size(), habit2);

        int result = manager.size();

        assertAll(
            () -> {assertEquals(2, result, "Check if the result is correct");},
            () -> {assertTrue(manager.contains(habit2), "Check if habit was added");}
        );
    }

    @Test
    void testAddWhenTheIndexIsLessThanZero() {
        HabitManager manager = new HabitManager();
        Habit habit = new Habit("Hello!", Frequency.DAILY);

		assertThrows(
			IllegalArgumentException.class, 
			()->{
				manager.add(-1, habit);
			}
		);
    }

    @Test
    void testAddWhenTheIndexIsGreaterThanTheSizeOfTheManager() {
        HabitManager manager = new HabitManager();
        Habit habit = new Habit("Hello!", Frequency.DAILY);

		assertThrows(
			IllegalArgumentException.class, 
			()->{
				manager.add(2, habit);
			}
		);
    }

	@Test
	void testAddWhenTheHabitIsNull() {
        HabitManager manager = new HabitManager();

		assertThrows(
			IllegalArgumentException.class, 
			()->{
				manager.add(null);
			}
		);
	}
}
