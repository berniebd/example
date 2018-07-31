package com.bernie.gatling


import io.gatling.core.Predef.{exec, _}
import io.gatling.core.scenario.Simulation
import io.gatling.http.Predef._
import scala.concurrent.duration._

class BI extends Simulation {
	val debug = true
  val url = "http://10.134.111.171"
	val httpProtocol = http
		.baseURL(url)
		.inferHtmlResources()
		.acceptHeader("application/json")
		.acceptEncodingHeader("gzip, deflate")
		.acceptLanguageHeader("zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7")
		.userAgentHeader("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36")

	val headers_0 = Map(
		"Content-Type" -> "application/json",
		"Origin" -> url)

	val login = exec(http("login")
			.post("/api/user/login")
			.headers(headers_0)
			.body(StringBody("""{"email":"devereader@insaic.com","password":"123456","rememberMe":false}"""))
			.check(jsonPath("$..csrfToken").saveAs("csrfToken"))
		)

	val sgmDealer = csv("sgmDealer.csv").circular
	val svwDealer = csv("svwDealer.csv").queue

	val svwQuery =  exec(login)
		.repeat(10) {
			exec().feed(svwDealer).
			exec(http("svw_get_308")
				.get("/api/dash/report/get?trigger=User&reportId=308")
				.headers(Map("Accept" -> "*/*", "X-CSRFToken" -> "${csrfToken}"))
				.check(bodyString.saveAs("svw_get_308")))
			.exec(http("svw_getDashboards_308")
				.get("/api/dash/report/getDashboards?trigger=User&reportId=308")
				.headers(Map("Accept" -> "*/*", "X-CSRFToken" -> "${csrfToken}")))
			.exec(http("svw_getExtractStatus_166")
				.get("/api/dash/dataModel/getExtractStatus?trigger=User&dataModelId=166")
				.headers(Map("Accept" -> "*/*", "X-CSRFToken" -> "${csrfToken}")))
			.exec(http("svw_getExtractStatus_164")
				.get("/api/dash/dataModel/getExtractStatus?trigger=User&dataModelId=164")
				.headers(Map("Accept" -> "*/*", "X-CSRFToken" -> "${csrfToken}")))
			.exec(http("svw_getExtractStatus_162")
				.get("/api/dash/dataModel/getExtractStatus?trigger=User&dataModelId=162")
				.headers(Map("Accept" -> "*/*", "X-CSRFToken" -> "${csrfToken}")))
			.exec(http("svw_getQuery_1")
				.post("/api/dash/component/getQuery?trigger=User")
				.headers(Map("Content-Type" -> "application/json", "Origin" -> url, "X-CSRFToken" -> "${csrfToken}"))
				.body(RawFileBody("bi/svw_body_1.txt")))
			.exec(http("svw_getQuery_2")
				.post("/api/dash/component/getQuery?trigger=User")
				.headers(Map("Content-Type" -> "application/json", "Origin" -> url, "X-CSRFToken" -> "${csrfToken}"))
				.body(RawFileBody("bi/svw_body_2.txt")))
			.exec(http("svw_getQuery_3")
				.post("/api/dash/component/getQuery?trigger=User")
				.headers(Map("Content-Type" -> "application/json", "Origin" -> url, "X-CSRFToken" -> "${csrfToken}"))
				.body(RawFileBody("bi/svw_body_3.txt")))
			.exec(http("svw_getQuery_4")
				.post("/api/dash/component/getQuery?trigger=User")
				.headers(Map("Content-Type" -> "application/json", "Origin" -> url, "X-CSRFToken" -> "${csrfToken}"))
				.body(RawFileBody("bi/svw_body_4.txt")))
			.exec(http("svw_getDimensionMembers_1")
				.post("/api/dash/component/getDimensionMembers?trigger=User")
				.headers(Map("Content-Type" -> "application/json", "Origin" -> url, "X-CSRFToken" -> "${csrfToken}"))
				.body(RawFileBody("bi/svw_body_5.txt")))
			.exec(http("svw_getDimensionMembers_2")
				.post("/api/dash/component/getDimensionMembers?trigger=User")
				.headers(Map("Content-Type" -> "application/json", "Origin" -> url, "X-CSRFToken" -> "${csrfToken}"))
				.body(RawFileBody("bi/svw_body_6.txt")))
			.exec(http("svw_trackevent")
				.post("/api/dash/trackevent?trigger=User")
				.headers(Map("Content-Type" -> "application/json", "Origin" -> url, "X-CSRFToken" -> "${csrfToken}"))
				.body(RawFileBody("bi/svw_body_7.txt")))
		}


	val sgmQuery = exec(login)
		.feed(sgmDealer)
		.repeat(5){
			exec(http("sgm_get_293")
				.get("/api/dash/report/get?trigger=User&reportId=293")
				.headers(Map("Accept" -> "*/*","X-CSRFToken" -> "${csrfToken}")))
			.exec(http("sgm_getDashboards_293")
				.get("/api/dash/report/getDashboards?trigger=User&reportId=293")
				.headers(Map("Accept" -> "*/*","X-CSRFToken" -> "${csrfToken}")))
			.exec(http("sgm_getExtractStatus_135")
				.get("/api/dash/dataModel/getExtractStatus?trigger=User&dataModelId=135")
				.headers(Map("Accept" -> "*/*","X-CSRFToken" -> "${csrfToken}")))
			.exec(http("sgm_getExtractStatus_153")
				.get("/api/dash/dataModel/getExtractStatus?trigger=User&dataModelId=153")
				.headers(Map("Accept" -> "*/*","X-CSRFToken" -> "${csrfToken}")))
			.exec(http("sgm_getExtractStatus_132")
				.get("/api/dash/dataModel/getExtractStatus?trigger=User&dataModelId=132")
				.headers(Map("Accept" -> "*/*","X-CSRFToken" -> "${csrfToken}")))
			.exec(http("sgm_getExtractStatus_152")
				.get("/api/dash/dataModel/getExtractStatus?trigger=User&dataModelId=152")
				.headers(Map("Accept" -> "*/*","X-CSRFToken" -> "${csrfToken}")))
			.exec(http("sgm_getExtractStatus_134")
				.get("/api/dash/dataModel/getExtractStatus?trigger=User&dataModelId=134")
				.headers(Map("Accept" -> "*/*","X-CSRFToken" -> "${csrfToken}")))
			.exec(http("sgm_getExtractStatus_130")
				.get("/api/dash/dataModel/getExtractStatus?trigger=User&dataModelId=130")
				.headers(Map("Accept" -> "*/*","X-CSRFToken" -> "${csrfToken}")))
			.exec(http("sgm_getExtractStatus_136")
				.get("/api/dash/dataModel/getExtractStatus?trigger=User&dataModelId=136")
				.headers(Map("Accept" -> "*/*","X-CSRFToken" -> "${csrfToken}")))
			.exec(http("sgm_getExtractStatus_133")
				.get("/api/dash/dataModel/getExtractStatus?trigger=User&dataModelId=133")
				.headers(Map("Accept" -> "*/*","X-CSRFToken" -> "${csrfToken}")))
			.exec(http("sgm_getQuery_1")
				.post("/api/dash/component/getQuery?trigger=User")
				.headers(Map("Content-Type" -> "application/json","Origin" -> url,"X-CSRFToken" -> "${csrfToken}"))
				.body(RawFileBody("bi/sgm_body_1.txt")))
			.exec(http("sgm_getQuery_2")
				.post("/api/dash/component/getQuery?trigger=User")
				.headers(Map("Content-Type" -> "application/json","Origin" -> url,"X-CSRFToken" -> "${csrfToken}"))
				.body(RawFileBody("bi/sgm_body_2.txt")))
			.exec(http("sgm_getQuery_3")
				.post("/api/dash/component/getQuery?trigger=User")
				.headers(Map("Content-Type" -> "application/json","Origin" -> url,"X-CSRFToken" -> "${csrfToken}"))
				.body(RawFileBody("bi/sgm_body_3.txt")))
			.exec(http("sgm_getQuery_4")
				.post("/api/dash/component/getQuery?trigger=User")
				.headers(Map("Content-Type" -> "application/json","Origin" -> url,"X-CSRFToken" -> "${csrfToken}"))
				.body(RawFileBody("bi/sgm_body_4.txt")))
			.exec(http("sgm_getQuery_5")
				.post("/api/dash/component/getQuery?trigger=User")
				.headers(Map("Content-Type" -> "application/json","Origin" -> url,"X-CSRFToken" -> "${csrfToken}"))
				.body(RawFileBody("bi/sgm_body_5.txt")))
			.exec(http("sgm_getQuery_6")
				.post("/api/dash/component/getQuery?trigger=User")
				.headers(Map("Content-Type" -> "application/json","Origin" -> url,"X-CSRFToken" -> "${csrfToken}")))
			.exec(http("sgm_getQuery_7")
				.post("/api/dash/component/getQuery?trigger=User")
				.headers(Map("Content-Type" -> "application/json","Origin" -> url,"X-CSRFToken" -> "${csrfToken}"))
				.body(RawFileBody("bi/sgm_body_7.txt")))
			.exec(http("sgm_getQuery_8")
				.post("/api/dash/component/getQuery?trigger=User")
				.headers(Map("Content-Type" -> "application/json","Origin" -> url,"X-CSRFToken" -> "${csrfToken}"))
				.body(RawFileBody("bi/sgm_body_8.txt"))
				.check(bodyString.saveAs("getQuery_sgm_8")))
			.exec(http("sgm_getDimensionMembers_1")
				.post("/api/dash/component/getDimensionMembers?trigger=User")
				.headers(Map("Content-Type" -> "application/json","Origin" -> url,"X-CSRFToken" -> "${csrfToken}"))
				.body(RawFileBody("bi/sgm_body_9.txt"))
				.check(bodyString.saveAs("getDimensionMembers_sgm_1")))
			.exec(http("sgm_getDimensionMembers_2")
				.post("/api/dash/component/getDimensionMembers?trigger=User")
				.headers(Map("Content-Type" -> "application/json","Origin" -> url,"X-CSRFToken" -> "${csrfToken}"))
				.body(RawFileBody("bi/sgm_body_10.txt")))
			.exec(http("sgm_trackevent")
				.post("/api/dash/trackevent?trigger=User")
				.headers(Map("Content-Type" -> "application/json","Origin" -> url,"X-CSRFToken" -> "${csrfToken}"))
				.body(RawFileBody("bi/sgm_body_11.txt")))
		}

	val sgmScn = scenario("sgmQuery").exec(sgmQuery).pace(2,5).rendezVous(5)
	val svwScn = scenario("svwQuery").exec(svwQuery).pace(2,5).rendezVous(5)

	setUp(
		svwScn.inject(
			atOnceUsers(1)
			,rampUsers(4) over(2)
		)
			.protocols(httpProtocol),
//		sgmScn.inject(atOnceUsers(1)).protocols(httpProtocol)
	).throttle(
		holdFor(40 seconds)
	).maxDuration(1 minutes)
//		svwScn.inject(atOnceUsers(1)))
//	 .protocols(httpProtocol)
}