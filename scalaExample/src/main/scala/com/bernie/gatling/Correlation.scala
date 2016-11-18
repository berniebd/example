package com.bernie.gatling

import io.gatling.core.Predef._
import io.gatling.http.Predef._

class Correlation extends Simulation {

  val httpProtocol = http
    .baseURL("http://10.3.254.23:8080").virtualHost()


  val uri1 = "http://10.3.254.23:8080/dangwebx"

  val scn = scenario("Correlation")
    .exec(http("get_user_info")
      .get("http://10.3.254.23:8080/dangwebx/loginController.do?gotologin")
      .check(regex("用户名\" iscookie=\"true\" value=\"(.*)\" nullmsg")
        .saveAs("username"))
      .check(regex("密码\" value=\"(.*)\" nullmsg")
        .saveAs("password")))
      .exec(http("login")
        .post("http://10.3.254.23:8080/dangwebx/security_check_")
        .formParam("username_", "${username}")
        .formParam("password_", "${password}")
        .formParam("userKey", "D1B5CC2FE46C4CC983C073BCA897935608D926CD32992B5900")
        .formParam("randCode", "1234")
        .check(substring("操作成功").find.exists)
      )

  setUp(scn.inject(atOnceUsers(1))).protocols(httpProtocol)
}