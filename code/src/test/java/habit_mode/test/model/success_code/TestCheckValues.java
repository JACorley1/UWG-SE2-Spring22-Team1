package habit_mode.test.model.success_code;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import habit_mode.model.SuccessCode;

public class TestCheckValues {
    @Test
    void testValidObjectOKAYSuccessCode() {
        Object doble = 0.0;
        SuccessCode code = SuccessCode.checkValues(doble);
        assertEquals(SuccessCode.OKAY, code);
    }

    @Test
    void testInvalidObjects() {
        Object notDoble = 10;
        SuccessCode code1 = SuccessCode.checkValues(notDoble);
        SuccessCode code2 = SuccessCode.checkValues(null);

        assertEquals(SuccessCode.UNKNOWN_ERROR, code1);
        assertEquals(SuccessCode.UNKNOWN_ERROR, code2);
    }
}

