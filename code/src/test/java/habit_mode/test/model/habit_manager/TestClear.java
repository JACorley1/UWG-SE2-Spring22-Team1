package habit_mode.test.model.habit_manager;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.HabitManager;

class TestClear {
    @Test
    void testWhenManagerHasHabits() {
        HabitManager manager = new HabitManager();
		Habit habit1 = new Habit("Hello!", Frequency.DAILY);
        Habit habit2 = new Habit("Bye!", Frequency.DAILY);
        manager.add(habit1);
        manager.add(habit2);

        manager.clear();

        assertEquals(0, manager.size(), "checking that the manager clears all habits from it.");
    }

    @Test
    void testWhenManagerIsEmpty() {
        HabitManager manager = new HabitManager();

        manager.clear();

        assertEquals(0, manager.size(), "checking to make sure nothing happens.");
    }
}
