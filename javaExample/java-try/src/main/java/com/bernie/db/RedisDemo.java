package com.bernie.db;

import redis.clients.jedis.Jedis;

/**
 * Created by bernie on 9/30/15.
 */
public class RedisDemo {
    public static void main(String[] args) {
        Jedis jedis = new Jedis("localhost");
        String name = jedis.get("name");
        System.out.println(name);
    }
}
