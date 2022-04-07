package habit_mode.model;

/**
 * The enum SuccessCode.
 * 
 * @author Team 1
 * @version Spring 2022
 */
public enum SuccessCode {
    OKAY(0.0), 
    MISSING_REQUEST_TYPE(10.0), 
    UNSUPPORT_REQUEST_TYPE(11.0),
    MALFORMED_REQUEST_TYPE(12.0), 
    USER_NOT_FOUND(13.0), 
    INVALID_AUTH_TOKEN(14.0), 
    UNKNOWN_ERROR(15.0), 
    USERNAME_ALREADY_EXISTS(20.0), 
    INVALID_USERNAME(21.0), 
    INVALID_PASSWORD(22.0), 
    INVALID_EMAIL(23.0), 
    INVALID_LOGIN_CREDENTIALS(30.0), 
    UNKNOWN_FIELD_NAME(40.0), 
    NO_FIELDS_PROVIDED(41.0),
    INVALID_HABIT_NAME(50.0), 
    INVALID_HABIT_FREQUENCY(51.0), 
    NO_HABIT_FOUND(52.0);

    private final double code;

    /**
     * The constructor for SuccessCode.
     * 
     * @precondition none
     * @postcondition this.getCode == value
     * 
     * @param value The integer value associated with each code. 
     */
    SuccessCode(Double value) {
        this.code = value;
    }

    /**
     * Gets the integer associated with the given success code.
     * 
     * @return code The SuccessCode represented as an integer.
     */
    public double getCode() {
        return this.code;
    }

    /**
     * Checks if a given decimal value corresponds with a success code.
     * 
     * @precondition doubl != null && doubl.getClass().equals(Double.class)
     * @postcondition none
     * 
     * @param doubl The doubl to be checked.
     * @return code The SuccessCode associated with the value or UNKNOWN_ERROR if value matches no codes.
     */
    public static SuccessCode checkValues(Object doubl) {

        if (doubl == null || !doubl.getClass().equals(Double.class)) {
            return SuccessCode.UNKNOWN_ERROR;
        }

        for (SuccessCode successCode : SuccessCode.values()) {
            
            Double code = (Double) doubl; 
            if (code == successCode.getCode()) {
                return successCode;
            }
        }
        return SuccessCode.UNKNOWN_ERROR;
    }
}
