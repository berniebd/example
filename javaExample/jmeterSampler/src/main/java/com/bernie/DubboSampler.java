package com.bernie;

/**
 * Created by bida on 2015/9/2.
 */
public class DubboSampler extends AbstractJavaSamplerClient {
    private SampleResult results = new SamplerResult();

    public Arguments getDefaultParameters(){
        Arguments params = new Arguments();
        params.addArgument("param1", "value1");
        return params;
    }

    public void setupTest(JavaSamplerContext context){
        results = new SamplerResult();
    }

    @Override
    public SamplerResult runText(JavaSamplerContext context){
        return results;
    }

    public void teardownText(JavaSamplerContext context){

    }
}
