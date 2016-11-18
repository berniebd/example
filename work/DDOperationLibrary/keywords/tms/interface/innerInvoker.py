# encoding=utf-8
from datetime import datetime, timedelta
from time import sleep
from pykafka import KafkaClient
from keywords.tms.base.baseInfo import BaseInfo
from parameters.tms import tmsBase, innerInvokerMessage
from parameters.tms.tmsBase import KafkaTopics

__author__ = 'bida'


def _generate_order_id():
    return datetime.now().strftime('%y%m%d%H%M%S%f')[:-3]


class InnerInvoker:
    def __init__(self):
        pass

    @classmethod
    def payment_zhifubao_notice(cls, order_id, pay_status='1'):
        """
        支付系统支付宝支付通知
        :param order_id:
        :param pay_status: 1，已支付；0，未支付。
        """
        print u'*' * 20 + u'支付系统支付宝支付通知'
        msg = innerInvokerMessage.payment_zhifubao_notice.replace('${order_id}', order_id)\
            .replace('${pay_status}', pay_status)
        print msg
        client = KafkaClient(hosts=tmsBase.kafka_client)
        topic = client.topics[KafkaTopics.POS.value]
        with topic.get_producer() as producer:
            producer.produce(msg)

    @classmethod
    def wms_return_confirmation(cls, order_ids, operation='exchange'):
        """
        仓库销退签收确认
        :param operation: exchange;return;exchange_to_return
        :param order_ids:
        """
        print u'*' * 20 + u'仓库销退签收确认'
        print innerInvokerMessage.wms_return_confirmation.decode('utf-8')

        if operation == 'exchange':
            exchange_num = '1'
            return_num = '0'
            last_num = '1'
        if operation == 'return':
            exchange_num = '0'
            return_num = '1'
            last_num = '0'
        if operation == 'exchange_to_return':
            exchange_num = '3'
            return_num = '2'
            last_num = '3'
        msg = innerInvokerMessage.wms_return_confirmation.replace('${exchange_num}', exchange_num)\
            .replace('${return_num}', return_num)\
            .replace('${last_num}', last_num)
        print msg

        client = KafkaClient(hosts=tmsBase.kafka_client)
        topic = client.topics[KafkaTopics.WMS.value]
        g = lambda x: producer.produce(msg.replace('${order_id}', x))
        with topic.get_producer() as producer:
            map(lambda order_id: g(order_id), order_ids.split(','))

    @classmethod
    def create_merchant_order(cls,
                              count=1,
                              items=1,
                              entrepot_id='30',
                              receive_street_id='111010507',
                              send_city='1110105',
                              shipment_type='1',
                              client_order_type='1',
                              distributor='autoexpress',
                              shop_id='0001',
                              pay_id='1',
                              should_receive_payment='56.00',
                              thread_no='',
                              interval='0.001',
                              producer=None):
        """
        创建招商运单
        :param send_city:
        :param should_receive_payment:
        :param pay_id:
        :param shop_id:商户编号
        :param distributor:
        :param client_order_type:
        :param count:消息数
        :param items:每条消息包含运单数
        :param entrepot_id:发货仓库
        :param receive_street_id:收货街道id
        :param shipment_type:配送方式
        :param thread_no:
        :param interval:
        :param producer:
        :return:
        """
        item_msg = innerInvokerMessage.merchant_order_item \
            .replace('${entrepot_id}', entrepot_id) \
            .replace('${receive_street_id}', receive_street_id) \
            .replace('${send_city}', send_city) \
            .replace('${shipment_type}', shipment_type) \
            .replace('${client_order_type}', client_order_type) \
            .replace('${distributor}', str(BaseInfo.get_distributor_or_subdistributor_id(short_name=distributor))) \
            .replace('${shop_id}', shop_id).replace('${pay_id}', pay_id)\
            .replace('${should_receive_payment}', should_receive_payment)

        items_msg = ''
        order_ids = list()
        sleep_time = float(interval)

        if producer is None:
            print item_msg.decode('utf-8')

            client = KafkaClient(hosts=tmsBase.kafka_client)
            topic = client.topics[KafkaTopics.RAINBOW.value]
            with topic.get_producer() as producer:
                for j in range(int(count)):
                    init_id = int(thread_no + _generate_order_id())
                    ids = map(lambda l: str(init_id + l), range(int(items)))

                    for order_id in ids:
                        items_msg += item_msg.replace('${order_id}', order_id)

                    producer.produce(innerInvokerMessage.create_merchant_order.replace('${items_info}', items_msg[:-1]))

                    order_ids += ids
                    sleep(sleep_time * 1000)
        else:
            for j in range(int(count)):
                for i in range(int(items)):
                    order_id = thread_no + _generate_order_id()

                    items_msg += item_msg.replace('${order_id}', order_id)
                    order_ids.append(order_id)
                    sleep(sleep_time)

                producer.produce(innerInvokerMessage.create_merchant_order.replace('${items_info}', items_msg[:-1]))

        print order_ids
        return order_ids, len(order_ids)

    @classmethod
    def create_change_and_refund_order(cls,
                                       count=1,
                                       operate_type='3',
                                       entrepot_id='30',
                                       send_city='1110105',
                                       receive_street_id='111010507',
                                       distributor='autoexpress',
                                       armoney='47.99',
                                       pay_id='1',
                                       shipment_type='1',
                                       thread_no='',
                                       interval='0.001',
                                       producer=None):
        """
        创建退换货运单
        :param pay_id:
        :param thread_no:
        :param count:
        :param operate_type: 3:退货，4:换货
        :param entrepot_id:
        :param receive_street_id:
        :param distributor:
        :param armoney:
        :param interval:
        :param producer:
        :return
        """
        if operate_type == '3':
            exchange_no = '0'
            return_no = '1'
            last_no = '0'
        if operate_type == '4':
            exchange_no = '1'
            return_no = '0'
            last_no = '1'
        if operate_type == 'other':
            operate_type = '10'
            exchange_no = '5'
            return_no = '0'
            last_no = '3'

        msg = innerInvokerMessage.create_change_and_refund_order \
            .replace('${entrepot_id}', entrepot_id) \
            .replace('${receive_street_id}', receive_street_id) \
            .replace('${send_city}', send_city) \
            .replace('${distributor}', str(BaseInfo.get_distributor_or_subdistributor_id(short_name=distributor))) \
            .replace('${armoney}', armoney) \
            .replace('${order_type}', operate_type) \
            .replace('${promise_time}', (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')) \
            .replace('${start_time}', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))\
            .replace('${pay_id}', pay_id)\
            .replace('${shipment_type}', shipment_type)\
            .replace('${exchangeNum}', exchange_no)\
            .replace('${returnNum}', return_no)\
            .replace('${lastNum}', last_no)

        sleep_time = float(interval)
        init_id = int(thread_no + _generate_order_id())
        order_ids = map(lambda i: str(init_id + i), range(int(count)))
        g = lambda i: producer.produce(msg.replace('${order_id}', i))

        if producer is None:
            print msg.decode('utf-8')

            client = KafkaClient(hosts=tmsBase.kafka_client)
            topic = client.topics[KafkaTopics.RAINBOW.value]
            with topic.get_producer() as producer:
                map(lambda x: g(x), order_ids)
        else:
            for order_id in order_ids:
                g(order_id)
                sleep(sleep_time)

        print order_ids
        return order_ids, len(order_ids)

    @classmethod
    def create_self_operated_order(cls,
                                   count=1,
                                   entrepot_id='30',
                                   shipment_type='1',
                                   receive_street_id='111010507',
                                   send_city='1110105',
                                   distributor='autoexpress',
                                   armoney='47.99',
                                   order_type='1',
                                   pay_id='1',
                                   thread_no='',
                                   interval='0.001',
                                   producer=None):

        """
        创建自营运单
        :param pay_id:
        :param order_type:
        :param count:
        :param entrepot_id:
        :param shipment_type:
        :param receive_street_id:
        :param distributor:
        :param armoney:
        :param thread_no:
        :param interval:
        :param producer:
        :return:
        """
        msg = innerInvokerMessage.create_self_operated_order \
            .replace('${entrepot_id}', entrepot_id) \
            .replace('${shipment_type}', shipment_type) \
            .replace('${receive_street_id}', receive_street_id) \
            .replace('${send_city}', send_city) \
            .replace('${distributor}', str(BaseInfo.get_distributor_or_subdistributor_id(short_name=distributor))) \
            .replace('${armoney}', armoney) \
            .replace('${order_type}', order_type)\
            .replace('${pay_id}', pay_id)

        sleep_time = float(interval)

        init_id = int(thread_no + _generate_order_id())
        order_ids = map(lambda i: str(init_id + i), range(int(count)))

        g = lambda x: producer.produce(msg.replace('${order_id}', x))

        if producer is None:
            print msg.decode('utf-8')
            client = KafkaClient(hosts=tmsBase.kafka_client)
            topic = client.topics[KafkaTopics.RAINBOW.value]
            with topic.get_producer() as producer:
                map(lambda i: g(i), order_ids)
        else:
            for order_id in order_ids:
                g(order_id)
                sleep(sleep_time)

        print order_ids
        return order_ids, len(order_ids)
