package com.bernie.mvcTry;

import static org.junit.Assert.*;
import org.junit.Test;

public class HomeControllerTest {
    @Test
    public void testHomePage() throws Exception{
        HomeController controller = new HomeController();
        assertEquals("home", controller.home());
    }
}
