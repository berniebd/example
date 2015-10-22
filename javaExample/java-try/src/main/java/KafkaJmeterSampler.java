import kafka.javaapi.producer.Producer;
import kafka.producer.KeyedMessage;
import kafka.producer.ProducerConfig;
import org.apache.jmeter.config.Arguments;
import org.apache.jmeter.protocol.java.sampler.AbstractJavaSamplerClient;
import org.apache.jmeter.protocol.java.sampler.JavaSamplerContext;
import org.apache.jmeter.samplers.SampleResult;

import java.util.Properties;

/**
 * Created by bernie on 10/20/15.
 */
public class KafkaJmeterSampler extends AbstractJavaSamplerClient {
    private SampleResult results;
    private Properties props;
    private Producer<String, String> producer;

    public Arguments getDefaultParameters() {
        Arguments params = new Arguments();
        params.addArgument("broker", "host:port");
        params.addArgument("topic", "");
        params.addArgument("message","");
        params.addArgument("count","1");
        return params;
    }

    @Override
    public void setupTest(JavaSamplerContext context) {
        super.setupTest(context);
        results = new SampleResult();
        props = new Properties();
        props.put("metadata.broker.list", context.getParameter("broker"));
        props.put("serializer.class", "kafka.serializer.StringEncoder");
        props.put("key.serializer.class", "kafka.serializer.StringEncoder");
        props.put("request.required.acks", "-1");

        producer = new Producer<String, String>(new ProducerConfig(props));
        System.out.println("init");
    }

    public SampleResult runTest(JavaSamplerContext javaSamplerContext) {
        results.sampleStart();
        for(int i = 0;i < javaSamplerContext.getIntParameter("count");i++){
            producer.send(new KeyedMessage<String, String>(javaSamplerContext.getParameter("topic"),
                    javaSamplerContext.getParameter("message")));
        }
        results.setResponseMessage("success");
        results.sampleEnd();
        results.setSuccessful(true);
        results.setResponseCodeOK();
        return results;
    }

    @Override
    public void teardownTest(JavaSamplerContext context) {
        producer.close();
    }
}
