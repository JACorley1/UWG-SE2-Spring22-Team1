package habit_mode.test.model.habit;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import habit_mode.model.Frequency;
import habit_mode.model.Habit;

class TestConstructor {
	@Test
	void test2ParamConstructorWithValidParameters() {
		String testString = "Hello!";
		Habit habit = new Habit(testString, Frequency.DAILY);
		
		assertAll(
			()->{assertEquals(false, habit.isComplete(), "checking completion status");},
			()->{assertEquals(Frequency.DAILY, habit.getFrequency(), "checking completion frequency");},
			()->{assertEquals(testString, habit.getText(), "checking the habits text");}
		);
	}

	@Test
	void test2ParamConstructorWithNullString() {
		assertThrows(
			IllegalArgumentException.class, 
			()->{
				new Habit(null, Frequency.WEEKLY);
			}
		);
	}

	@Test
	void test2ParamConstructorWithEmptyString() {
		assertThrows(
			IllegalArgumentException.class, 
			()->{
				new Habit("", Frequency.MONTHLY);
			}
		);
	}
}
