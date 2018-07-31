package com.bernie.gatling

import java.text.SimpleDateFormat
import java.util.Calendar
import java.util.UUID.randomUUID

import io.gatling.core.Predef.{exec, _}
import io.gatling.http.Predef._
import io.gatling.core.scenario.Simulation

object tools{
  def getVin(): String = {
    return randomUUID().toString.replace("-", "").substring(0, 13).toUpperCase()
  }

  def getCalculateRequest(insurer:String): Unit ={

  }
}


class DimInsurance extends Simulation{
  val dateFormatter: SimpleDateFormat = new SimpleDateFormat("YYYY-MM-dd 00:00")
  val dateFormatter2: SimpleDateFormat = new SimpleDateFormat("YYYY-MM-dd")
  val dateFormatter3: SimpleDateFormat = new SimpleDateFormat("YYYY-12-31")

  val httpProtocol = http
    .baseURL("https://dimsit.insaic.com")
    .inferHtmlResources()
    .acceptHeader("application/json, text/javascript, */*; q=0.01")
    .acceptEncodingHeader("gzip, deflate")
    .acceptLanguageHeader("zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7")
    .userAgentHeader("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")

  var headers_0 = Map(
    "Content-Type" -> "application/json; charset=UTF-8",
    "Origin" -> "https://dimsit.insaic.com",
    "X-Requested-With" -> "XMLHttpRequest")

  var login = exec(http("get_captcha")
      .post("/dim-api/captcha/dfrrdi")
      .headers(headers_0)
      .check(status.is(200)))
    .exec(http("login")
      .post("/dim-api/login")
      .headers(headers_0)
      .body(StringBody("""{"userCode":"dfrrdi","password":"Pass1234","captcha":""}"""))
      .check(status.is(200)))

  var queryVehicleModel = exec(http("query_vehicle_model")
    .post("/dim-api/common/vehicles")
    .headers(headers_0)
    .body(StringBody("""{"modelName": "大众汽车SVW73010FK轿车", "insurer": "cpic", "pageNumber": "0", "pageSize": "10"}"""))
    .check(status.is(200)))

  var getDealers = exec(http("get_dealers")
    .post("/dim-api/common/dealers")
    .headers(headers_0)
    .body(StringBody("""{"dealerCodes":"","brandCode":"","marketingCode":""}"""))
    .check(status.is(200)))

  var getAgreements = exec(http("get_agreements")
    .post("/dim-api/common/agreements")
    .headers(headers_0)
    .body(StringBody("""{"dealerCode":"VW01240","mfrDealerCode":null,"dealerName":"台湾测试","province":"710000","city":"710100","address":null,"brandCode":"Roewe-MG","manufactory":"SAIC","canInputCtpModelName":null,"insurers":[],"loanNo":null,"phone":null}"""))
    .check(status.is(200)))

  var getCoverages = exec(http("get_coverages")
      .post("/dim-api/policy/coverages")
      .headers(headers_0)
      .body(StringBody(s"""{"agreementCode":"DGXY160637JXS","insurerCode":"cpic","dealerCode":"VW01240","insuredMode":"STANDARD","insurer":"cpic","orgCode":"insaic","agentCode":"COMPANY_DIRECT","agentName":"","channelCode":"123123","inputMode":null,"marketingId":null,"auto2015Flag":null,"showPilot":null,"agreementType":"INSAIC","channelType":"COMPANY_DIRECT","manufacturer":"SAIC","province":"710000"}""")))

  var getLoanOrganization = exec(http("get_loan_organization")
    .post("/dim-api/loan/organization")
    .headers(headers_0)
    .body(StringBody(s"""{"dealerCode":"VW01240","insurer":"cpic"}"""))
    .check(status.is(200)))

  var getGpicHandler = exec(http("get_handler")
    .post("/dim-api/policy/gpic/handler")
    .headers(headers_0)
    .body(StringBody("""{"province":"710000","dealerCode":"VW01240","insurer":"gpic","agreementType":"DEALER","agreementCode":"DGXY160249JXS"}""")))



  object AutoInsurance{

    var debug = true
    var startDate = Calendar.getInstance()
    startDate.add(Calendar.DATE, 1)
    var sStartDate = dateFormatter.format(startDate.getTime())

    var endDate = Calendar.getInstance()
    endDate.add(Calendar.DATE, 1)
    endDate.add(Calendar.YEAR, 1)
    var sEndDate = dateFormatter.format(endDate.getTime())

    var sRegisterDate = dateFormatter2.format(Calendar.getInstance().getTime())

    var sPayStartDate = dateFormatter2.format(Calendar.getInstance().getTime())
    var sPayEndDate = dateFormatter3.format(Calendar.getInstance().getTime())

//    val vin = randomUUID().toString.replace("-", "").substring(0, 13).toUpperCase()
    var calculateRequest_cpic =
      s"""
      {"lastBizPolicyNo":"","lastCtpPolicyNo":"","lastBizStartDate":"","lastBizEndDate":"","lastCtpStartDate":"","lastCtpEndDate":"","lastInsurer":"","inputId":"","inputMode":null,"insuredMode":"STANDARD","insurerCode":"cpic","agreementCode":"DGXY160637JXS","marketingId":null,"dealerCode":"VW01240","dealerInfo":{"dealerCode":"VW01240","mfrDealerCode":null,"dealerName":"台湾测试","province":"710000","city":"710100","address":null,"brandCode":"Roewe-MG","manufactory":"SAIC","canInputCtpModelName":null,"insurers":null,"loanNo":null,"phone":null},"orderNo":"","bizStartDate":"$sStartDate","ctpStartDate":"$sStartDate","bizEndDate":"$sEndDate","ctpEndDate":"$sEndDate","loanSerialNo":"","isSelectedCTP":1,"bizActualDiscount":"1.000000","insuredVehicle":{"licenseNo":"","fuelType":"","seatCount":"7","emptyWeight":"1620","carryingWeight":0,"exhaustScale":"2975","vin":"LSJA%s","makeDate":"","engineNo":"67D8G7","vehicleVariety":"","insurercode":"","modelCode":"DZAAAD0132","modelName":"大众汽车SVW73010FK轿车","brandCode":"","seriesCode":null,"packageId":"","productId":"","prodcutName":"","packageName":"","countryNature":"JOINT","deductionDueCode":"0","purchasePrice":"312800","currentValue":"312800.00","chgOwnerDate":"","crossProvinceYear":"","registerDate":"$sRegisterDate","abs_flag":"","usage":"PERSON","loanOrganization":"","cars_type":null,"riskType":"","productStatus":"","remark":"","seatMin":null,"seatMax":null,"horsePower":null,"air_bag_count":null,"tonCount":null,"factory":"","seriesName":"帕萨特","theft_proof":null,"vehicleAlias":"新帕萨特3.0L DSG旗舰尊享版","unifiedModelCode":null,"transmissionType":"","licenseType":null,"purchasePriceTax":"","carKind":"","carYear":"2013","completemassMax":null,"completemassMin":null,"insurerCode":null,"comCode":"","licenseColor":"BLUE","runMiles":null,"runAreaCode":null,"brandName":"上汽大众","powerScale":"","chgOwnerFlag":null,"loanVehicleFlag":"","vehicleTypeDescription":null,"certificateDate":null,"certificateType":"","getCertificateNo":"","carProofDate":"","searchSequenceNo":null,"actualValue":"","carCheckStatus":null,"manufacturer":"","industryModelCode":"","industryModelName":"","brand":"","lastYearProvince":null,"familyName":"帕萨特","transferRegisterDate":"","ctpModelName":""},"partyes":{"owner":{"certiEndDate":"2099-12-31","name":"加特林","nature":"OWNER","certificateType":"ID_CARD","certificateNo":"110101199901014791","mobile":"13800138000","phoneNumber":"","address":"上海市静安区开开大厦","email":"","vehicleOwnerNature":"PERSON","vehicleRelationship":"","postcode":"","organizationType":"","contactName":"","organizationPhone":"","birthDate":"","gender":""},"applicant":{"certiEndDate":"2099-12-31","name":"加特林","nature":"APPLICANT","certificateType":"ID_CARD","certificateNo":"110101199901014791","mobile":"13800138000","phoneNumber":"","address":"上海市静安区开开大厦","email":"","vehicleOwnerNature":"","vehicleRelationship":"OWNER","postcode":"","organizationType":"","contactName":"","organizationPhone":"","birthDate":"","gender":""},"insured":{"certiEndDate":"2099-12-31","name":"加特林","nature":"INSURED","certificateType":"ID_CARD","certificateNo":"110101199901014791","mobile":"13800138000","phoneNumber":"","address":"上海市静安区开开大厦","email":"","vehicleOwnerNature":"","vehicleRelationship":"OWNER","postcode":"","organizationType":"","contactName":"","organizationPhone":"","birthDate":"","gender":""},"claimer":{"certiEndDate":"2099-12-31","name":"加特林","nature":"CLAIMER","certificateType":"ID_CARD","certificateNo":"110101199901014791","mobile":"13800138000","phoneNumber":"","address":"上海市静安区开开大厦","email":"","vehicleOwnerNature":"","vehicleRelationship":"OWNER","postcode":"","organizationType":"","contactName":"","organizationPhone":"","birthDate":"","gender":""}},"coverages":[{"code":"DAMAGE_LOSS","name":"机动车损失险","sumInsured":"312800","quantity":""},{"code":"DAMAGE_LOSS_EXEMPT_CLAUSE","name":"机动车损失险不计免赔特约条款","sumInsured":"","quantity":""},{"code":"THIRD_PARTY","name":"第三者责任险","sumInsured":"500000","quantity":""},{"code":"THIRD_PARTY_EXEMPT_CLAUSE","name":"第三者责任险不计免赔特约条款","sumInsured":"","quantity":""},{"code":"INCAR_DRIVER","name":"车上人员责任险（司机）","sumInsured":"20000","quantity":""},{"code":"INCAR_DRIVER_EXEMPT_CLAUSE","name":"车上司机责任险不计免赔特约条款","sumInsured":"","quantity":""},{"code":"INCAR_PASSENGER","name":"车上人员责任险（乘客）","sumInsured":"20000","quantity":"6"},{"code":"INCAR_PASSENGER_EXEMPT_CLAUSE","name":"车上乘客责任险不计免赔特约条款","sumInsured":"","quantity":""}],"premiumFloating":{},"businessType":"AUTO_NEW","rcdUnpolicyRequestMO":null,"vehicleTax":{"taxType":"COMPLETE","payStartDate":"$sPayStartDate","payEndDate":"$sPayEndDate","taxAbateType":"","taxAbateReason":"","taxAbateProportion":"","taxAbateAmount":"","dutyPaidProofNo":"(151)粤地证06066608","taxComCode":"","taxComName":"","taxAuthCode":""},"platformCode":"","salePerson":null,"bizInsuranceQueryCode":"","ctpInsuranceQueryCode":"","disputeResolveType":"LAWSUIT","arbitrationOrganization":"","invoiceType":"COMMON","instalmentYear":"","marketingCode":"","remarks":"","insurer":"cpic","orgCode":"insaic","agentCode":"COMPANY_DIRECT","agentName":"","channelCode":"123123","auto2015Flag":null,"showPilot":null,"agreementType":"INSAIC","channelType":"COMPANY_DIRECT","mfrDealerCode":null,"dealerName":"台湾测试","province":"710000","city":"710100","address":null,"brandCode":"Roewe-MG","manufactory":"SAIC","canInputCtpModelName":null,"insurers":null,"loanNo":null,"phone":null,"newEquipmentMOs":[],"appointDrivers":[],"tags":[],"ctpSpecialClauses":[],"bizSpecialClauses":[],"ePolicyFlag":"N","eInvoiceFlag":"N"}
    """
    var calculateRequest_paic =
      s"""
       {"lastBizPolicyNo":"","lastCtpPolicyNo":"","lastBizStartDate":"","lastBizEndDate":"","lastCtpStartDate":"","lastCtpEndDate":"","lastInsurer":"","inputId":"","inputMode":null,"insuredMode":"STANDARD","insurerCode":"paic","agreementCode":"DGXY160511JXS","marketingId":null,"dealerCode":"VW01240","dealerInfo":{"dealerCode":"VW01240","mfrDealerCode":null,"dealerName":"台湾测试","province":"710000","city":"710100","address":null,"brandCode":"Roewe-MG","manufactory":"SAIC","canInputCtpModelName":null,"insurers":null,"loanNo":null,"phone":null},"orderNo":"","bizStartDate":"$sStartDate","ctpStartDate":"$sStartDate","bizEndDate":"$sEndDate","ctpEndDate":"$sEndDate","loanSerialNo":"","isSelectedCTP":1,"bizActualDiscount":"","insuredVehicle":{"licenseNo":"","fuelType":"","seatCount":"5","emptyWeight":"1860.0","carryingWeight":"","exhaustScale":"3564.000","vin":"LSJB%s","makeDate":"","engineNo":"23432432","vehicleVariety":"","insurercode":"","modelCode":"KDAALD0005","modelName":"凯迪拉克SGM7367ATA轿车","brandCode":"","seriesCode":null,"packageId":"","productId":"","prodcutName":"","packageName":"","countryNature":"JOINT","deductionDueCode":"0","purchasePrice":"","currentValue":"0","chgOwnerDate":"","crossProvinceYear":"","registerDate":"$sRegisterDate","abs_flag":"","usage":"PERSON","loanOrganization":"","cars_type":null,"riskType":"","productStatus":"","remark":"","seatMin":null,"seatMax":null,"horsePower":null,"air_bag_count":null,"tonCount":null,"factory":"","seriesName":"上海通用凯迪拉克XTS","theft_proof":null,"vehicleAlias":"凯迪拉克XTS 36S AT铂金版","unifiedModelCode":null,"transmissionType":"","licenseType":null,"purchasePriceTax":"","carKind":"","carYear":"2013","completemassMax":null,"completemassMin":null,"insurerCode":null,"comCode":"","licenseColor":"BLUE","runMiles":null,"runAreaCode":null,"brandName":"上海通用凯迪拉克","powerScale":"","chgOwnerFlag":null,"loanVehicleFlag":"","vehicleTypeDescription":null,"certificateDate":null,"certificateType":"","getCertificateNo":"","carProofDate":"","searchSequenceNo":null,"actualValue":"","carCheckStatus":null,"manufacturer":"","industryModelCode":"","industryModelName":"","brand":"","lastYearProvince":null,"familyName":"上海通用凯迪拉克XTS","transferRegisterDate":"","ctpModelName":""},"partyes":{"owner":{"certiEndDate":"2099-12-31","name":"加特林","nature":"OWNER","certificateType":"ID_CARD","certificateNo":"110101199901014791","mobile":"13800138000","phoneNumber":"","address":"上海市静安区","email":"","vehicleOwnerNature":"PERSON","vehicleRelationship":"","postcode":"","organizationType":"","contactName":"","organizationPhone":"","birthDate":"","gender":""},"applicant":{"certiEndDate":"2099-12-31","name":"加特林","nature":"APPLICANT","certificateType":"ID_CARD","certificateNo":"110101199901014791","mobile":"13800138000","phoneNumber":"","address":"上海市静安区","email":"","vehicleOwnerNature":"","vehicleRelationship":"OWNER","postcode":"","organizationType":"","contactName":"","organizationPhone":"","birthDate":"","gender":""},"insured":{"certiEndDate":"2099-12-31","name":"加特林","nature":"INSURED","certificateType":"ID_CARD","certificateNo":"110101199901014791","mobile":"13800138000","phoneNumber":"","address":"上海市静安区","email":"","vehicleOwnerNature":"","vehicleRelationship":"OWNER","postcode":"","organizationType":"","contactName":"","organizationPhone":"","birthDate":"","gender":""}},"coverages":[{"code":"DAMAGE_LOSS","name":"机动车损失险","sumInsured":"","quantity":""},{"code":"DAMAGE_LOSS_EXEMPT_CLAUSE","name":"机动车损失险不计免赔特约条款","sumInsured":"","quantity":""},{"code":"THIRD_PARTY","name":"第三者责任险","sumInsured":"500000","quantity":""},{"code":"THIRD_PARTY_EXEMPT_CLAUSE","name":"第三者责任险不计免赔特约条款","sumInsured":"","quantity":""},{"code":"INCAR_DRIVER","name":"车上人员责任险（司机）","sumInsured":"20000","quantity":""},{"code":"INCAR_DRIVER_EXEMPT_CLAUSE","name":"车上司机责任险不计免赔特约条款","sumInsured":"","quantity":""},{"code":"INCAR_PASSENGER","name":"车上人员责任险（乘客）","sumInsured":"20000","quantity":"4"},{"code":"INCAR_PASSENGER_EXEMPT_CLAUSE","name":"车上乘客责任险不计免赔特约条款","sumInsured":"","quantity":""}],"premiumFloating":{},"businessType":"AUTO_NEW","rcdUnpolicyRequestMO":null,"vehicleTax":{"taxType":"","payStartDate":"$sPayStartDate","payEndDate":"$sPayEndDate","taxAbateType":"","taxAbateReason":"","taxAbateProportion":"","taxAbateAmount":"","dutyPaidProofNo":"","taxComCode":"","taxComName":"","taxAuthCode":""},"platformCode":"","salePerson":null,"bizInsuranceQueryCode":"","ctpInsuranceQueryCode":"","disputeResolveType":"LAWSUIT","arbitrationOrganization":"","invoiceType":"COMMON","instalmentYear":"","marketingCode":"","remarks":"","insurer":"paic","orgCode":"71000000","agentCode":"234324324","agentName":"","channelCode":"1231231","auto2015Flag":null,"showPilot":null,"agreementType":"INSAIC","channelType":"PROFESSIONAL_AGENT","mfrDealerCode":null,"dealerName":"台湾测试","province":"710000","city":"710100","address":null,"brandCode":"Roewe-MG","manufactory":"SAIC","canInputCtpModelName":null,"insurers":null,"loanNo":null,"phone":null,"newEquipmentMOs":[],"appointDrivers":[],"tags":[],"ctpSpecialClauses":[],"bizSpecialClauses":[],"ePolicyFlag":"N","eInvoiceFlag":"N"}
     """
    var calculateRequest_gpic =
      s"""
         {"lastBizPolicyNo":"","lastCtpPolicyNo":"","lastBizStartDate":"","lastBizEndDate":"","lastCtpStartDate":"","lastCtpEndDate":"","lastInsurer":"","inputId":"","inputMode":null,"insuredMode":"STANDARD","insurerCode":"gpic","agreementCode":"DGXY160249JXS","marketingId":null,"dealerCode":"VW01240","dealerInfo":{"dealerCode":"VW01240","mfrDealerCode":null,"dealerName":"台湾测试","province":"710000","city":"710100","address":null,"brandCode":"Roewe-MG","manufactory":"SAIC","canInputCtpModelName":null,"insurers":null,"loanNo":null,"phone":null},"orderNo":"","bizStartDate":"$sStartDate","ctpStartDate":"$sStartDate","bizEndDate":"$sEndDate","ctpEndDate":"$sEndDate","loanSerialNo":"","isSelectedCTP":1,"bizActualDiscount":"","insuredVehicle":{"licenseNo":"","fuelType":"","seatCount":"5","emptyWeight":"1860","carryingWeight":null,"exhaustScale":"3564","vin":"LSJC%s","makeDate":"","engineNo":"23432432","vehicleVariety":"","insurercode":"","modelCode":"KDAALD0005","modelName":"凯迪拉克SGM7367ATA轿车","brandCode":"","seriesCode":null,"packageId":"","productId":"","prodcutName":"","packageName":"","countryNature":"JOINT","deductionDueCode":"0","purchasePrice":"0.00","currentValue":"","chgOwnerDate":"","crossProvinceYear":"","registerDate":"$sRegisterDate","abs_flag":"","usage":"PERSON","loanOrganization":"","cars_type":null,"riskType":"","productStatus":"","remark":"","seatMin":null,"seatMax":null,"horsePower":null,"air_bag_count":null,"tonCount":null,"factory":"","seriesName":"上海通用凯迪拉克XTS","theft_proof":null,"vehicleAlias":"凯迪拉克XTS 36S AT铂金版","unifiedModelCode":null,"transmissionType":"","licenseType":null,"purchasePriceTax":"","carKind":"","carYear":"2013","completemassMax":null,"completemassMin":null,"insurerCode":null,"comCode":"","licenseColor":"BLUE","runMiles":null,"runAreaCode":null,"brandName":"上海通用凯迪拉克","powerScale":"","chgOwnerFlag":null,"loanVehicleFlag":"","vehicleTypeDescription":null,"certificateDate":null,"certificateType":"","getCertificateNo":"","carProofDate":"","searchSequenceNo":null,"actualValue":"","carCheckStatus":null,"manufacturer":"","industryModelCode":"","industryModelName":"","brand":"","lastYearProvince":null,"familyName":"上海通用凯迪拉克XTS","transferRegisterDate":"","ctpModelName":""},"partyes":{"owner":{"certiEndDate":"2099-12-31","name":"加特林","nature":"OWNER","certificateType":"ID_CARD","certificateNo":"110101199901014791","mobile":"13800138000","phoneNumber":"","address":"上海市静安区","email":"","vehicleOwnerNature":"PERSON","vehicleRelationship":"","postcode":"","organizationType":"","contactName":"","organizationPhone":"","birthDate":"","gender":""},"applicant":{"certiEndDate":"2099-12-31","name":"加特林","nature":"APPLICANT","certificateType":"ID_CARD","certificateNo":"110101199901014791","mobile":"13800138000","phoneNumber":"","address":"上海市静安区","email":"","vehicleOwnerNature":"","vehicleRelationship":"OWNER","postcode":"","organizationType":"","contactName":"","organizationPhone":"","birthDate":"","gender":""},"insured":{"certiEndDate":"2099-12-31","name":"加特林","nature":"INSURED","certificateType":"ID_CARD","certificateNo":"110101199901014791","mobile":"13800138000","phoneNumber":"","address":"上海市静安区","email":"","vehicleOwnerNature":"","vehicleRelationship":"OWNER","postcode":"","organizationType":"","contactName":"","organizationPhone":"","birthDate":"","gender":""}},"coverages":[{"code":"DAMAGE_LOSS","name":"机动车损失险","sumInsured":"","quantity":""},{"code":"DAMAGE_LOSS_EXEMPT_CLAUSE","name":"机动车损失险不计免赔特约条款","sumInsured":"","quantity":""},{"code":"THIRD_PARTY","name":"第三者责任险","sumInsured":"500000","quantity":""},{"code":"THIRD_PARTY_EXEMPT_CLAUSE","name":"第三者责任险不计免赔特约条款","sumInsured":"","quantity":""},{"code":"INCAR_DRIVER","name":"车上人员责任险（司机）","sumInsured":"20000","quantity":""},{"code":"INCAR_DRIVER_EXEMPT_CLAUSE","name":"车上司机责任险不计免赔特约条款","sumInsured":"","quantity":""},{"code":"INCAR_PASSENGER","name":"车上人员责任险（乘客）","sumInsured":"20000","quantity":"4"},{"code":"INCAR_PASSENGER_EXEMPT_CLAUSE","name":"车上乘客责任险不计免赔特约条款","sumInsured":"","quantity":""}],"premiumFloating":{},"businessType":"AUTO_NEW","rcdUnpolicyRequestMO":null,"vehicleTax":{"taxType":"","payStartDate":"$sPayStartDate","payEndDate":"$sPayEndDate","taxAbateType":"","taxAbateReason":"","taxAbateProportion":"","taxAbateAmount":"","dutyPaidProofNo":"","taxComCode":"","taxComName":"","taxAuthCode":""},"platformCode":"","salePerson":null,"bizInsuranceQueryCode":"","ctpInsuranceQueryCode":"","disputeResolveType":"LAWSUIT","arbitrationOrganization":"","invoiceType":"COMMON","instalmentYear":"","marketingCode":"","remarks":"","insurer":"gpic","orgCode":"insaic","agentCode":"gpic","agentName":"","channelCode":"123","auto2015Flag":null,"showPilot":null,"agreementType":"DEALER","channelType":"DEALER_AGENT","mfrDealerCode":null,"dealerName":"台湾测试","province":"710000","city":"710100","address":null,"brandCode":"Roewe-MG","manufactory":"SAIC","canInputCtpModelName":null,"insurers":null,"loanNo":null,"phone":null,"newEquipmentMOs":[],"appointDrivers":[],"tags":[],"ctpSpecialClauses":[],"bizSpecialClauses":[],"handler1Code":"","ePolicyFlag":"N","eInvoiceFlag":"N"}
       """
    var calculateRequest_picc =
      s"""
         {"lastBizPolicyNo":"","lastCtpPolicyNo":"","lastBizStartDate":"","lastBizEndDate":"","lastCtpStartDate":"","lastCtpEndDate":"","lastInsurer":"","inputId":"","inputMode":null,"insuredMode":"STANDARD","insurerCode":"picc","agreementCode":"DGXY160269JXS","marketingId":null,"dealerCode":"VW01255","dealerInfo":{"dealerCode":"VW01255","mfrDealerCode":null,"dealerName":"香港测试","province":"810000","city":null,"address":null,"brandCode":"MG","manufactory":"SAIC","canInputCtpModelName":null,"insurers":null,"loanNo":null,"phone":null},"orderNo":"","bizStartDate":"$sStartDate","ctpStartDate":"$sStartDate","bizEndDate":"$sEndDate","ctpEndDate":"$sEndDate","loanSerialNo":"","isSelectedCTP":1,"bizActualDiscount":"","insuredVehicle":{"licenseNo":"","fuelType":"","seatCount":"7","emptyWeight":"1620.0","carryingWeight":"","exhaustScale":"2975.000","vin":"LSJD%s","makeDate":"","engineNo":"2432423","vehicleVariety":"","insurercode":"","modelCode":"DZAAAD0132","modelName":"大众汽车SVW73010FK轿车","brandCode":"","seriesCode":null,"packageId":"","productId":"","prodcutName":"","packageName":"","countryNature":"JOINT","deductionDueCode":"0","purchasePrice":"","currentValue":"0","chgOwnerDate":"","crossProvinceYear":"","registerDate":"$sRegisterDate","abs_flag":"","usage":"PERSON","loanOrganization":"","cars_type":null,"riskType":"","productStatus":"","remark":"","seatMin":null,"seatMax":null,"horsePower":null,"air_bag_count":null,"tonCount":null,"factory":"","seriesName":"帕萨特","theft_proof":null,"vehicleAlias":"新帕萨特3.0L DSG旗舰尊享版","unifiedModelCode":null,"transmissionType":"","licenseType":null,"purchasePriceTax":"","carKind":"","carYear":"2013","completemassMax":null,"completemassMin":null,"insurerCode":null,"comCode":"","licenseColor":"BLUE","runMiles":null,"runAreaCode":null,"brandName":"上汽大众","powerScale":"","chgOwnerFlag":null,"loanVehicleFlag":"","vehicleTypeDescription":null,"certificateDate":null,"certificateType":"","getCertificateNo":"","carProofDate":"","searchSequenceNo":null,"actualValue":"","carCheckStatus":null,"manufacturer":"","industryModelCode":"","industryModelName":"","brand":"","lastYearProvince":null,"familyName":"帕萨特","transferRegisterDate":"","ctpModelName":""},"partyes":{"owner":{"certiEndDate":"2099-12-31","name":"加特林","nature":"OWNER","certificateType":"ID_CARD","certificateNo":"110101199901014791","mobile":"13800138000","phoneNumber":"","address":"上海市静安区","email":"","vehicleOwnerNature":"PERSON","vehicleRelationship":"","postcode":"","organizationType":"","contactName":"","organizationPhone":"","birthDate":"","gender":""},"applicant":{"certiEndDate":"2099-12-31","name":"加特林","nature":"APPLICANT","certificateType":"ID_CARD","certificateNo":"110101199901014791","mobile":"13800138000","phoneNumber":"","address":"上海市静安区","email":"","vehicleOwnerNature":"","vehicleRelationship":"OWNER","postcode":"","organizationType":"","contactName":"","organizationPhone":"","birthDate":"","gender":""},"insured":{"certiEndDate":"2099-12-31","name":"加特林","nature":"INSURED","certificateType":"ID_CARD","certificateNo":"110101199901014791","mobile":"13800138000","phoneNumber":"","address":"上海市静安区","email":"","vehicleOwnerNature":"","vehicleRelationship":"OWNER","postcode":"","organizationType":"","contactName":"","organizationPhone":"","birthDate":"","gender":""}},"coverages":[{"code":"DAMAGE_LOSS","name":"机动车损失险","sumInsured":"","quantity":""},{"code":"DAMAGE_LOSS_EXEMPT_CLAUSE","name":"机动车损失险不计免赔特约条款","sumInsured":"","quantity":""},{"code":"THIRD_PARTY","name":"第三者责任险","sumInsured":"1000000","quantity":""},{"code":"THIRD_PARTY_EXEMPT_CLAUSE","name":"第三者责任险不计免赔特约条款","sumInsured":"","quantity":""},{"code":"INCAR_DRIVER","name":"车上人员责任险（司机）","sumInsured":"100000","quantity":""},{"code":"INCAR_DRIVER_EXEMPT_CLAUSE","name":"车上司机责任险不计免赔特约条款","sumInsured":"","quantity":""},{"code":"INCAR_PASSENGER","name":"车上人员责任险（乘客）","sumInsured":"100000","quantity":"6"},{"code":"INCAR_PASSENGER_EXEMPT_CLAUSE","name":"车上乘客责任险不计免赔特约条款","sumInsured":"","quantity":""}],"premiumFloating":{},"businessType":"AUTO_NEW","rcdUnpolicyRequestMO":null,"vehicleTax":{"taxType":"","payStartDate":"$sPayStartDate","payEndDate":"$sPayEndDate","taxAbateType":"","taxAbateReason":"","taxAbateProportion":"","taxAbateAmount":"","dutyPaidProofNo":"","taxComCode":"","taxComName":"","taxAuthCode":""},"platformCode":"","salePerson":null,"bizInsuranceQueryCode":"","ctpInsuranceQueryCode":"","disputeResolveType":"LAWSUIT","arbitrationOrganization":"","invoiceType":"COMMON","instalmentYear":"","marketingCode":"","remarks":"","insurer":"picc","orgCode":"new_insaic","agentCode":"213","agentName":"","channelCode":"FW78","auto2015Flag":null,"showPilot":null,"agreementType":"DEALER","channelType":"DEALER_BROKER","mfrDealerCode":null,"dealerName":"香港测试","province":"810000","city":null,"address":null,"brandCode":"MG","manufactory":"SAIC","canInputCtpModelName":null,"insurers":null,"loanNo":null,"phone":null,"newEquipmentMOs":[],"appointDrivers":[],"tags":[],"ctpSpecialClauses":[],"bizSpecialClauses":[],"ePolicyFlag":"N","eInvoiceFlag":"N"}
       """

    def calculateAndSubmit(calculateRequest:String, dealerCode:String) =
//      exec(session => {
//        session.set("vin", tools.getVin())
//        session
//      }).
      exec(http("calculate")
        .post("/dim-api/policy/calc")
        .headers(headers_0)
        .body(StringBody(calculateRequest.format(tools.getVin())))
        .check(status.is(200))
        .check(jsonPath("$").saveAs("resp"))
        .check(jsonPath("$.result.orderNo").saveAs("orderNo"))
      ).exec(session => {
        val resp = session.get("resp")
        val orderNo = session.get("orderNo")
        if(debug){
          println(resp)
        }
        session
      })
      .exec(http("preview")
        .post("/dim-api/policy/insure/${orderNo}")
        .headers(headers_0)
        .check(status.is(200))
        .check(jsonPath("$").saveAs("previewResp")))
      .doIf(debug){exec(session => {
        val previewResp = session.get("previewResp")
        println("previewResp-------------")
        println(previewResp)
        session
      })}
      .exec(http("submit")
        .post("/dim-api/policy/submit")
        .headers(headers_0)
        .body(StringBody("""{"orderNo":"${orderNo}","orders":[],"ctpSpecialClauses":[],"bizSpecialClauses":[],"salePerson":null,"tags":[],"dealerCode":"%s","bizInsuranceQueryCode":"","ctpInsuranceQueryCode":"","nonAutoPolicy":null}""".format(dealerCode)))
          .check(status.is(200)))
      .doIf(debug){exec(session => {
        val submitResp = session.get("submitResp")
        println("submitResp-------------")
        println(submitResp)
        session
      })}
  }

  val scn = scenario("auto-insurance")
    .exec(login)
    .exec(getDealers)
    .exec(getAgreements)
    .exec(getCoverages)
    .exec(getLoanOrganization)
    .exec(getGpicHandler)
    .exec(queryVehicleModel)
      .during(5){exec(AutoInsurance.calculateAndSubmit(AutoInsurance.calculateRequest_cpic, "VW01240"))}
//    .exec(AutoInsurance.calculateAndSubmit(AutoInsurance.calculateRequest_cpic, "VW01240"))
//    .randomSwitch(0.25 -> exec(AutoInsurance.calculateAndSubmit(AutoInsurance.calculateRequest_cpic, "VW01240")),
//      0.25 -> exec(AutoInsurance.calculateAndSubmit(AutoInsurance.calculateRequest_gpic, "VW01240")),
//      0.25 -> exec(AutoInsurance.calculateAndSubmit(AutoInsurance.calculateRequest_paic, "VW01240")),
//      0.25 -> exec(AutoInsurance.calculateAndSubmit(AutoInsurance.calculateRequest_picc, "VW01255")))


  setUp(scn.inject(
//      nothingFor(1),
      atOnceUsers(1))
    .protocols(httpProtocol))
}
