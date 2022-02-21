package habit_mode.test.model.habit_manager;

import static org.junit.jupiter.api.Assertions.*;
import java.util.Iterator;
import java.util.ListIterator;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.HabitManager;

class TestIterator {
	@Test
	void testIterator() {
        HabitManager manager = new HabitManager();

        Iterator<Habit> result = manager.iterator();

		assertFalse(result.equals(manager.iterator()), "Checking that the manager returns different iterators.");
	}

    @Test
    void testListIterator() {
        HabitManager manager = new HabitManager();

        ListIterator<Habit> result = manager.listIterator();
        
		assertFalse(result.equals(manager.listIterator()), "Checking that the manager returns different list iterators.");
    }

    @Test
    void testListIteratorWithAValidIndex() {
		Habit habit1 = new Habit("Hello!", Frequency.DAILY);
        Habit habit2 = new Habit("Bye!", Frequency.DAILY);
        HabitManager manager = new HabitManager();
        manager.add(habit1);
        manager.add(habit2);

        ListIterator<Habit> result = manager.listIterator(0);
        
		assertFalse(result.equals(manager.listIterator(0)), "Checking that the manager returns different list iterators.");
    }

    @Test
    void testListIteratorWhenIndexIsLessThanZero() {
        HabitManager manager = new HabitManager();
        Habit habit = new Habit("Hello!", Frequency.DAILY);
        manager.add(habit);

		assertThrows(
			IllegalArgumentException.class, 
			()->{
				manager.listIterator(-1);
			}
		);
    }

    @Test
    void testListIteratorWhenIndexIsGreaterThanTheSizeOfTheManager() {
        HabitManager manager = new HabitManager();
        Habit habit = new Habit("Hello!", Frequency.DAILY);
        manager.add(habit);
        
		assertThrows(
			IllegalArgumentException.class, 
			()->{
				manager.listIterator(2);
			}
		);
    }
}