package com.bernie.kafka;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.StringSerializer;

import java.util.Properties;
import java.util.concurrent.ExecutionException;

/**
 * Created by bida on 2015/9/1.
 */
public class KafkaProducerNewTry {
    private void sendMessage() throws ExecutionException, InterruptedException {
        Properties props = new Properties();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "10.3.254.16:9092");
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());

        KafkaProducer<String, String> producer = new KafkaProducer<String, String>(props);

        boolean sync = true;

        ProducerRecord<String, String>  producerRecord = new ProducerRecord<String, String>("test", "value");

        if(sync){
            producer.send(producerRecord).get();
        } else{
            producer.send(producerRecord);
        }

        producer.close();
    }
    public static void main(String[] args){

    }
}
