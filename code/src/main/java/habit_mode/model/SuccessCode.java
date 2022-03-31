package habit_mode.model;

/**
 * The enum SuccessCode.
 * 
 * @author Team 1
 * @version Spring 2022
 */
public enum SuccessCode {
    OKAY(0), 
    MISSING_REQUEST_TYPE(10), 
    UNSUPPORT_REQUEST_TYPE(11),
    MALFORMED_REQUEST_TYPE(12), 
    USER_NOT_FOUND(13), 
    INVALID_AUTH_TOKEN(14), 
    UNKNOWN_ERROR(15), 
    USERNAME_ALREADY_EXISTS(20), 
    INVALID_USERNAME(21), 
    INVALID_PASSWORD(22), 
    INVALID_EMAIL(23), 
    INVALID_LOGIN_CREDENTIALS(30), 
    UNKNOWN_FIELD_NAME(40), 
    NO_FIELDS_PROVIDED(41),
    INVALID_HABIT_NAME(50), 
    INVALID_HABIT_FREQUENCY(51), 
    NO_HABIT_FOUND(52);

    private final int code;

    /**
     * The constructor for SuccessCode.
     * 
     * @precondition none
     * @postcondition this.getCode == value
     * 
     * @param value The integer value associated with each code. 
     */
    SuccessCodes(int value) {
        this.code = value;
    }

    /**
     * Gets the integer associated with the given success code.
     * 
     * @return code The SuccessCode represented as an integer.
     */
    public int getCode() {
        return this.code;
    }
}
