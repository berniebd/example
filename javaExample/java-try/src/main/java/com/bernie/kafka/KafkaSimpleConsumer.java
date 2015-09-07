package com.bernie.kafka;

import kafka.consumer.Consumer;
import kafka.consumer.ConsumerConfig;
import kafka.consumer.ConsumerIterator;
import kafka.consumer.KafkaStream;
import kafka.javaapi.consumer.ConsumerConnector;

import java.io.UnsupportedEncodingException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Properties;

/**
 * Created by bida on 2015/9/1.
 */
public class KafkaSimpleConsumer {
    public static void main(String[] args) throws InterruptedException, UnsupportedEncodingException {
        Properties prop = new Properties();
        prop.put("zookeeper.connect", "10.3.254.16:2181");
        prop.put("group.id", "test-group");
        prop.put("zookeeper.session.timeout.ms", "400");
        prop.put("zookeeper.sync.time.ms", "200");
        prop.put("auto.commit.interval.ms", "1000");

        ConsumerConfig consumerConfig = new ConsumerConfig(prop);

        ConsumerConnector consumerConnector = Consumer.createJavaConsumerConnector(consumerConfig);
        Map<String, Integer> topicCountMap = new HashMap<String,Integer>();
        topicCountMap.put("testt", new Integer(1));
        Map<String, List<KafkaStream<byte[], byte[]>>> consumerMap = consumerConnector.createMessageStreams(topicCountMap);
        List<KafkaStream<byte[], byte[]>> streams = consumerMap.get("test");
        for(final KafkaStream stream:streams){
            ConsumerIterator<byte[], byte[]> it = stream.iterator();
            while(it.hasNext()){
                System.out.println(new String(it.next().message()));
            }
        }
    }
}
