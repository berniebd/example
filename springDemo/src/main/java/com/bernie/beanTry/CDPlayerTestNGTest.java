package com.bernie.beanTry;

import org.testng.Assert;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.testng.AbstractTestNGSpringContextTests;
import org.testng.annotations.Test;

@Test
@ContextConfiguration(classes = CDPlayerConfig.class)
public class CDPlayerTestNGTest extends AbstractTestNGSpringContextTests{
    @Autowired
    CompactDisc cd;

    @Test
    void testCdShouldNotNull(){
        System.out.println(cd.toString());
        Assert.assertNotNull(cd);
    }
}
