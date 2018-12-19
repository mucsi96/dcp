package hu.mucsi;

import org.junit.Test;

import static org.junit.Assert.*;

public class MainTest {
    @Test
    public void testApp() {
        int[] numbers = { 10, 15, 3, 7 };
        boolean result = Main.canAddUp(numbers, 17);
        assertTrue(result);
    }
}
