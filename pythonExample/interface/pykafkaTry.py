# encoding=utf-8
from datetime import datetime
from pykafka import KafkaClient

__author__ = 'bida'

order_id = datetime.now().strftime('%Y%m%d%H%M%S%f')
print order_id

message = '''
{
    "body": {
        "armoney": 47.1,
        "cashs": 0,
        "coupons": 0,
        "couponsMoney": 0,
        "custEmail": "1778651282947901ddmobilphone__user.com",
        "custId": "174115203",
        "custMessage": "",
        "custRequestSenddate": "送货时间不限",
        "custType": "0",
        "deliveryNo": "JJD0615092330681",
        "deliveryStationId": "",
        "erpSendDate": "2015-09-23 23:59:45",
        "expectedDeliveryTimePromise": "2015-09-24 10:47:07",
        "expectedDeliveryTimeStart": null,
        "foodsFee": 52.1,
        "foodsLastFee": 52.1,
        "giftCoupons": 0,
        "mappingTrackingNumber": "",
        "money": 0,
        "orderDate": "2015-09-23 10:46:58",
        "orderId": $orderId$,
        "orderItems": [
            {
                "itemId": 13232913383004,
                "lastNum": 1,
                "productId": 20999128,
                "productName": "窗边的小豆豆",
                "salePrice": 18.4
            },
            {
                "itemId": 13232913383005,
                "lastNum": 1,
                "productId": 21081984,
                "productName": "秘密花园——教育部语文新课标必读丛书(适合小学生阅读)(小书房.世界经典文库)(新版)",
                "salePrice": 9.2
            },
            {
                "itemId": 13232913383003,
                "lastNum": 1,
                "productId": 23605048,
                "productName": "意林作文素材版合订本总第17卷（14年11期下-12期下）",
                "salePrice": 9
            },
            {
                "itemId": 13232913383001,
                "lastNum": 1,
                "productId": 23643240,
                "productName": "【当当出品】假如给我三天光明(新课标)",
                "salePrice": 4.5
            },
            {
                "itemId": 13232913383002,
                "lastNum": 1,
                "productId": 23696692,
                "productName": "【当当出品】城南旧事（新课标）",
                "salePrice": 11
            }
        ],
        "orderSource": "当当自营订单",
        "orderType": "1",
        "ordersErro": "",
        "orgOrderNo": "",
        "packageBarcode": "",
        "packageNum": 1,
        "packagePos": "",
        "packageSpec": "",
        "payId": "1",
        "pointDeductionAmount": 0,
        "rcvStreetId": "121050801",
        "selfServiceId": "0",
        "sendCity": "1420103",
        "sendCompany": "18614",
        "sendFee": 0,
        "shipAddress": "中国湖北武汉市硚口区,汉正街华贸三号楼地龙饰品A22号",
        "shipId": "1",
        "shipName": "汪漫",
        "shipRegion": "4028e0bb4d02c5c6014d02e6d0780001",
        "shipTel": ",17786512829",
        "shipZip": "430000",
        "siteCode": "4028e0894cd57278014cd59724e70001",
        "siteName": "",
        "subOrderId": ""
    },
    "dest": null,
    "sendTime": "2015-10-30 20:50:46",
    "src": null,
    "messageType": null,
    "messageId": "120749c2-956f-4a10-b74b-331e42d51968",
    "messageProcessorName": null
}
'''.replace('$orderId$', order_id)

print message

client = KafkaClient(hosts='10.3.254.26:9092')
topic = client.topics['90001']
with topic.get_producer() as producer:
    producer.produce(message)

# consumer = topic.get_simple_consumer()
# consumer = topic.get_balanced_consumer()
# for message in consumer:
#     if message is not None:
#         print message.offset, message.value