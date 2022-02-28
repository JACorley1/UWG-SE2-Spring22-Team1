package habit_mode.test.model.local_implementation.LocalServerCommunicator;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

import habit_mode.model.local_implementation.LocalServerCommunicator;

public class TestSetCoins {
    @Test
    void test0Coins() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();
        communicator.setCoins(5);

        assertAll(
            () -> {assertTrue(communicator.setCoins(0), "Check if return is correct");},
            () -> {assertTrue(communicator.getCoins() == 0, "Check if coins are set to 0.");}
        );
    }

    @Test
    void testPositiveCoins() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();

        assertAll(
            () -> {assertTrue(communicator.setCoins(1), "Check if return is correct");},
            () -> {assertTrue(communicator.getCoins() == 1, "Check if coins are set to 0.");}
        );
    }

    @Test
    void testNegativeCoins() {
        LocalServerCommunicator.reset();
        LocalServerCommunicator communicator = new LocalServerCommunicator();

        assertThrows(
            IllegalArgumentException.class, 
            () -> {communicator.setCoins(-1);},
            "Check if an exception is thrown when coins are set to a negative number."
        );
    }
}
