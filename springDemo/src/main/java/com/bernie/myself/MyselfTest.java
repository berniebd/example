package com.bernie.myself;

import static org.junit.Assert.*;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import java.sql.Array;

@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(classes = MyselfConfig.class)
public class MyselfTest {
    @Autowired
    public StaticCfg sc;

    @Autowired
    public StaticCfg sc2;

    @Test
    public void nameShouldBe() throws CloneNotSupportedException {
        assertEquals("bernie", sc.name);
        assertEquals(1, sc.age);
        assertEquals(true, sc.isMale);
        int[] scores = {99, 98, 97};
        System.out.println(sc.toString());
        System.out.println(sc2.toString());
        assertArrayEquals(scores, sc.scores);
        assertEquals(sc, sc2);
        System.out.println(sc.name);
        StaticCfg sc3 = (StaticCfg)sc.clone();
        sc2.setName("Tom");
        System.out.println(sc.name);
        System.out.println(sc3.name);
        System.out.println(sc3.toString());
        assertEquals(sc, sc3);
    }
}
