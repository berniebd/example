package com.bernie.gatling

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._

/**
 * Created by bida on 2015/10/22.
 */

class Parameterization extends Simulation{
  val uri = "http://gatling.io"

  val httpConf = http
    .baseURL("http://gatling.io") // Here is the root for all relative URLs
    .acceptHeader("text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8") // Here are the common headers
    .doNotTrackHeader("1")
    .acceptLanguageHeader("en-US,en;q=0.5")
    .acceptEncodingHeader("gzip, deflate")
    .userAgentHeader("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:16.0) Gecko/20100101 Firefox/16.0")
    .maxConnectionsPerHost(10)
    .maxConnectionsPerHostLikeFirefox
    .disableClientSharing
    .check(status.is(200))
    .silentURI("https://myCSN/*")

  object Request1{
    val method_1 = exec(http("method_1").get(uri + "/docs/2.1.7/advanced_tutorial.html")).pause(5)
  }

  val scn = scenario("parameterization")
    .exec(feed(csv("gatling/foo.csv").queue)
      .exec(http("post")
        .post("http://10.3.254.23:8080/dangwebx/security_check_")
        .formParam("username_", "${username}")
        .formParam("password_", "${password}")
        .formParam("randCode", "1234")
        .formParam("usreKey", "D1B5CC2FE46C4CC983C073BCA897935608D926CD32992B5900")
        .check(substring("success").find.exists)
        .check(substring("操作成功1").find.exists)
      )
    )

  setUp(scn.inject(atOnceUsers(1)).protocols(httpConf))
}