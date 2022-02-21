package habit_mode.test.model.habit_manager;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.HabitManager;

class TestContains {
	@Test
	void testWithTheHabitInTheManager() {
		Habit habit = new Habit("Hello!", Frequency.DAILY);
        HabitManager manager = new HabitManager();
        manager.add(habit);

        boolean result = manager.contains(habit);

		assertEquals(true, result, "Checking that the manager does contain the habit.");
	}

    @Test
	void testWithTheHabitNotInTheManager() {
		Habit habit = new Habit("Hello!", Frequency.DAILY);
        HabitManager manager = new HabitManager();

        boolean result = manager.contains(habit);

        assertEquals(false, result, "Checking that the manager does not contain the habit.");
	}

	@Test
	void testWhenTheHabitToCheckIsNull() {
        HabitManager manager = new HabitManager();
		assertThrows(
			IllegalArgumentException.class, 
			()->{
				manager.contains(null);
			}
		);
	}
}
