package habit_mode.test.model.habit;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;
import javafx.beans.property.StringProperty;

class TestGettersAndSetters {
    @Test
    void testSetFrequency() {
        Habit habit = new Habit("Hello!", Frequency.DAILY);

        habit.setFrequency(Frequency.WEEKLY);

        assertEquals(Frequency.WEEKLY, habit.getFrequency(), "Checking that the frequency is set");
    }
    
    @Test
    void testTextProperty() {
        Habit habit = new Habit("Hello!", Frequency.DAILY);

        StringProperty property = habit.textProperty();
        property.set("Habit");

        assertEquals("Habit", habit.getText(), "Checking that the text is set");
    }
    
    @Test
    void testsetId() {
        Habit habit = new Habit("Hello!", Frequency.DAILY);

        habit.setId(5);
        assertEquals(5, habit.getId(), "Checking that the id is set");
    }
}
