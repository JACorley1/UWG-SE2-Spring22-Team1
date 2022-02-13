package code.test.testHabit;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import code.model.Habit;
import code.model.Frequency;

class TestSetters {
	@Test
	void testSetFrequency() {
		Habit habit = new Habit("Hello!", Frequency.DAILY);

        	habit.setFrequency(Frequency.WEEKLY);

        	assertEquals(Frequency.WEEKLY, habit.getFrequency(), "Checking that the frequency is set");
	}

    @Test
	void testToggleCompletionStatusWhenFalse() {
		Habit habit = new Habit("Hello!", Frequency.DAILY);

        	habit.toggleCompletionStatus();
        	assertEquals(true, habit.getCompletionStatus(), "Checking that the completion status was changed to true");
        
        	habit.toggleCompletionStatus();
        	assertEquals(false, habit.getCompletionStatus(), "Checking that the completion status was changed to false");
	}

    
    @Test
	void testSetTextWithValidString() {
		Habit habit = new Habit("Hello!", Frequency.DAILY);

        	habit.setText("GoodBye!");

        	assertEquals("GoodBye!", habit.getText(), "Checking that the text is set");
	}

	@Test
	void testSetTextWithEmptyString() {
        	Habit habit = new Habit("Hello!", Frequency.DAILY);
		assertThrows(
						IllegalArgumentException.class, 
						()->{
							habit.setText("");
						}
					);
	}

    @Test
	void testSetTextWithNullString() {
        	Habit habit = new Habit("Hello!", Frequency.DAILY);
		assertThrows(
						IllegalArgumentException.class, 
						()->{
							habit.setText(null);
						}
					);
	}
}