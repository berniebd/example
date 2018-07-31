package com.bernie.gatling

import io.gatling.core.Predef.{exec, _}
import io.gatling.core.scenario.Simulation
import io.gatling.http.Predef._
import scala.concurrent.duration._

import scala.language.postfixOps

class zhongan extends Simulation {
  val url = "http://112.65.104.117:7443"
	val httpProtocol = http
		.baseURL(url)
//		.inferHtmlResources()
//		.acceptHeader("application/json")
		.acceptEncodingHeader("gzip, deflate")
		.acceptLanguageHeader("zh-CN")
//		.userAgentHeader("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36")


	val users = csv("zhongan.csv").queue

	val seckill = exec()
		.feed(users).
		exec(http("/banma/home")
			.get("/banma/home?authcode=${authcode}&vin=${vin}")
			.headers(Map("Accept" -> "text/html,application/xhtml+xml,application/xml;q=0.9,*.*;q=0.8")))
		.exec(http("/auth/banma")
			.post("/h5-api/banma/auth/banma")
			.headers(Map("Content-Type" -> "application/json;charset=UTF-8"))
			.body(StringBody("""{"vin":"${vin}","authCode":"${authcode}"}""")))
		.exec(http("/order/hasBought")
			.post("/h5-api/banma/order/hasBought/${vin}")
			.headers(Map("Content-Type" -> "application/json;charset=UTF-8"))
			.body(StringBody("""{}""")))
		.exec(http("/ubi/day-driving-behavior")
			.post("/h5-api/banma/ubi/day-driving-behavior")
			.headers(Map("Content-Type" -> "application/json;charset=UTF-8"))
			.body(StringBody("""{"date":"20180510","vin":"${vin}"}""")))
		.exec(http("/order/status")
			.post("/h5-api/banma/order/status/${vin}")
			.headers(Map("Content-Type" -> "application/json;charset=UTF-8"))
			.body(StringBody("""{}""")))
		.exec(http("/coupon/myCoupon")
			.post("/h5-api/banma/coupon/myCoupon")
			.headers(Map("Content-Type" -> "application/json;charset=UTF-8"))
			.body(StringBody("""{"vin":"${vin}"}""")))
		.exec(http("/ubi/balanceAndScratch")
			.post("/h5-api/banma/ubi/balanceAndScratch")
			.headers(Map("Content-Type" -> "application/json;charset=UTF-8"))
			.body(StringBody("""{"vin":"${vin}"}""")))
		.exec(http("/ubi/trip-label")
			.post("/h5-api/banma/ubi/trip-label/${vin}")
			.headers(Map("Content-Type" -> "application/json;charset=UTF-8"))
			.body(StringBody("""{}""")))
		.exec(http("/campaign/status")
			.post("/h5-api/banma/campaign/status/${campaignNo}")
			.headers(Map("Content-Type" -> "application/json;charset=UTF-8"))
			.body(StringBody("""{}""")))
		.exec(http("/campaign/purchasedUsers")
			.post("/h5-api/banma/campaign/purchasedUsers/${campaignNo}")
			.headers(Map("Content-Type" -> "application/json;charset=UTF-8"))
			.body(StringBody("""{}""")))
		.exec(http("/campaign/buy")
			.post("/h5-api/banma/campaign/buy")
			.headers(Map("Content-Type" -> "application/json;charset=UTF-8"))
			.body(StringBody("""{"mobileNo":"${mobile}","campaignNo":"${campaignNo}","name":"${name}","address":"${address}"}""")))


	val scn = scenario("seckill").exec(seckill)

	setUp(
		scn.inject(
			atOnceUsers(1)
//			,rampUsers(4) over(2)
		)
			.protocols(httpProtocol)
	).maxDuration(20 minutes)
//		svwScn.inject(atOnceUsers(1)))
//	 .protocols(httpProtocol)
}