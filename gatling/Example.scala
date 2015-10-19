package com.bernie.test

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._

class Example extends Simulation {
  val uri = "http://gatling.io"
  object Request1{
    val method_1 = exec(http("method_1").get(uri + "/docs/2.1.7/advanced_tutorial.html")).pause(5)
  }
  val method_2 = tryMax(2){
    exec(http("method_2")
    .get(uri + "/docs/2.1.7/session/session_api.html#id2")
    .check(status.is(200))
    .check(status.in(201,202))
    .check(bodyString.is("1234"))
    ).pace(5)
    }.exitHereIfFailed
  val method_3 = exec(http("method_3").get(uri + "/docs/2.0.0-RC2/general/scenario.html")).pause(1,10)

  val httpConf = http
    .baseURL("http://gatling.io") // Here is the root for all relative URLs
    .acceptHeader("text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8") // Here are the common headers
    .doNotTrackHeader("1")
    .acceptLanguageHeader("en-US,en;q=0.5")
    .acceptEncodingHeader("gzip, deflate")
    .userAgentHeader("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:16.0) Gecko/20100101 Firefox/16.0")

  val headers_10 = Map("Content-Type" -> "application/x-www-form-urlencoded") // Note the headers specific to a given request

  var state = true
  var switch = 3
  val scn = scenario("Condition")
    .doIf(state)(exec(method_3))
    .doIfOrElse(state)(exec(Request1.method_1))(exec(method_2))
    .doIfEqualsOrElse("123","121ss3"){exec(Request1.method_1)}{exec(method_2)}
    .doSwitch(switch)(1 -> exec(Request1.method_1), 2 -> exec(method_2))
    .doSwitchOrElse(switch)(1->exec(Request1.method_1), 2-> exec(method_2))(exec(method_3))
    // .randomSwitch(20->exec(Request1.method_1), 80->exec(method_2))  error
    // .randomSwitchOrElse(20->exec(Request1.method_1), 80->exec(method_2)){exec(method_3)}  error
    .uniformRandomSwitch(exec(Request1.method_1), exec(method_2))
    .roundRobinSwitch(exec(Request1.method_1), exec(method_2))

    var ids = Seq(1,2,3)
    val scn2 = scenario("loop")
      .repeat(5){exec(Request1.method_1)}
      .during(30){exec(Request1.method_1)}
      .foreach(ids, "id"){exec(Request1.method_1)}
      .forever("forever"){exec(Request1.method_1)}
      .asLongAs(state){exec(method_2)}

    var scn3 = scenario("group")
    .group("Group 1"){exec(Request1.method_1, method_2)}
    // only one group in a single scenario
    // .group("Group 2"){exec(Reqeust2.method_2, method_3)}  wrong

  setUp(
    scn.inject(atOnceUsers(10)).protocols(httpConf),
    scn2.inject(atOnceUsers(2)).protocols(httpConf),
    scn3.inject(atOnceUsers(10)).protocols(httpConf),
    scn.inject(
      nothingFor(4),
      atOnceUsers(5),
      rampUsers(10) over(5),
      constantUsersPerSec(20) during(10),
      constantUsersPerSec(20) during(10) randomized,
      rampUsersPerSec(10) to(20) during(20 minutes),
      rampUsersPerSec(10) to(20) during(20 minutes) randomized,
      heavisideUsers(1000) over(20 seconds),
      splitUsers(1000) into(rampUsers(10) over(10 seconds)) separatedBy(10 seconds),
      splitUsers(1000) into(rampUsers(10) over(10 seconds)) separatedBy(atOnceUsers(30))
    )
    .protocols(httpConf)
  ).throttle(
    reachRps(100) in (10 seconds),
    holdFor(2 hours),
    jumpToRps(50),
    holdFor(2 hours)
  )
  .assertions(global.responseTime.max.lessThan(100))
  .assertions(forAll.failedRequests.percent.lessThan(5))
  .assertions(details("search"/"index").failedRequests.percent.is(0))
  .assertions(details("details").requestsPerSec.between(10, 100))
}