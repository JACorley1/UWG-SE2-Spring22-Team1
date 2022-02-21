package habit_mode.test.model.habit_manager;

import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;

import habit_mode.model.HabitManager;

class TestRetainAll {
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
