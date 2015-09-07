package com.bernie.kafka;


import kafka.javaapi.producer.Producer;
import kafka.producer.KeyedMessage;
import kafka.producer.ProducerConfig;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Properties;
import java.util.concurrent.ExecutionException;

/**
 * Created by bida on 2015/9/1.
 */
public class KafkaProducerTry {
    private void sendMessage(){
        Properties props = new Properties();

        props.put("metadata.broker.list", "10.3.254.16:9092");
        props.put("serializer.class", "kafka.serializer.StringEncoder");
        props.put("key.serializer.class", "kafka.serializer.StringEncoder");
        props.put("request.required.acks", "-1");

        Producer<String, String>  producer = new Producer<String, String>(new ProducerConfig(props));

        SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");

        producer.send(new KeyedMessage<String, String>("test", format.format(new Date())));

        producer.close();
    }

    public static void main(String[] args) throws ExecutionException, InterruptedException {
        KafkaProducerTry kafkaProducerTry = new KafkaProducerTry();
        kafkaProducerTry.sendMessage();
    }
}
