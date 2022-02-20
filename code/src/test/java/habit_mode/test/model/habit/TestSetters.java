package habit_mode.test.model.habit;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;

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
		assertEquals(true, habit.isComplete(), "Checking that the completion status was changed to true");
	
		habit.toggleCompletionStatus();
		assertEquals(false, habit.isComplete(), "Checking that the completion status was changed to false");
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