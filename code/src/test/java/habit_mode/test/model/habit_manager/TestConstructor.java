package habit_mode.test.model.habit_manager;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import habit_mode.model.HabitManager;

class TestConstructor {
	@Test
	void testConstructor() {
        HabitManager manager = new HabitManager();
		
        assertEquals(0, manager.size(), "Ensuring the manager was created");
	}
}
