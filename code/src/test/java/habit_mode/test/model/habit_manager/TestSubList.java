package habit_mode.test.model.habit_manager;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import java.util.List;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import habit_mode.model.HabitManager;

class TestSubList {
    @Test 
    void testSubListWithAValidRangeOfIndicesInTheManager() {
        Habit habit1 = new Habit("Hello!", Frequency.DAILY);
        Habit habit2 = new Habit("Bye!", Frequency.DAILY);
        Habit habit3 = new Habit("Hi!", Frequency.WEEKLY);
        HabitManager manager = new HabitManager();

        manager.add(habit3);
        manager.add(habit2);
        manager.add(habit1);

        List<Habit> result = manager.subList(0, 2);

        assertEquals(2, result.size(), "Checking that the size of the result is correct after testing.");
    }

    @Test 
    void testSubListWithLowerBoundIndexLessThanZero() {
        Habit habit1 = new Habit("Hello!", Frequency.DAILY);
        Habit habit2 = new Habit("Bye!", Frequency.DAILY);
        Habit habit3 = new Habit("Hi!", Frequency.WEEKLY);
        HabitManager manager = new HabitManager();

        manager.add(habit3);
        manager.add(habit2);
        manager.add(habit1);

        assertThrows(
            IllegalArgumentException.class, 
            ()->{
                manager.subList(-1, 2);
            }
        );
    }

    @Test 
    void testSubListWithUpperBoundIndexGreaterThanTheSizeOfTheManager() {
        Habit habit1 = new Habit("Hello!", Frequency.DAILY);
        Habit habit2 = new Habit("Bye!", Frequency.DAILY);
        Habit habit3 = new Habit("Hi!", Frequency.WEEKLY);
        HabitManager manager = new HabitManager();

        manager.add(habit3);
        manager.add(habit2);
        manager.add(habit1);

        assertThrows(
            IllegalArgumentException.class, 
            ()->{
                manager.subList(0, manager.size() + 1);
            }
        );
    }
}
