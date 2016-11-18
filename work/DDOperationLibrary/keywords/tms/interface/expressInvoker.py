# -*- encoding:utf-8 -*-
from DDOperationLibrary.parameters.tms import tmsBase
from pykafka import KafkaClient

from keywords.tms.base.baseInfo import BaseInfo
from keywords.tms.tmsKafkaClient import TmsKafkaClient
from parameters.tms import expressInvokerMessage
from parameters.tms.tmsBase import KafkaTopics

__author__ = 'bida'


class ExpressInvoker:
    def __init__(self):
        pass

    @classmethod
    def feedback_instorage(cls, distributor_id='', order_ids=[]):
        """
        快递接口反馈运单入库
        :param distributor_id:
        :param order_ids:
        """
        print u'*' * 20 + u'快递接口反馈运单入库'
        item = expressInvokerMessage.express_feedback_instock_item.replace('${express_id}', distributor_id)
        items = ''
        for order_id in order_ids:
            items += item.replace('${order_id}', order_id)
            items += ','

        client = KafkaClient(hosts=tmsBase.kafka_client)
        topic = client.topics[KafkaTopics.EXPRESS.value]
        msg = expressInvokerMessage.express_feedback_instock.replace('${items}', items[:-1])
        # print msg
        with topic.get_producer() as producer:
            producer.produce(msg)

    @classmethod
    def feedback_outstorage(cls, distributor_id='', order_ids=[]):
        """
        快递接口反馈运单出库
        :param distributor_id:
        :param order_ids:
        """
        print u'*' * 20 + u'快递接口反馈运单出库'
        item = expressInvokerMessage.express_feedback_out_of_stock_item.replace('${express_id}', distributor_id)
        items = ''
        for order_id in order_ids:
            items += item.replace('${order_id}', order_id)
            items += ','

        client = KafkaClient(hosts=tmsBase.kafka_client)
        topic = client.topics[KafkaTopics.EXPRESS.value]
        msg = expressInvokerMessage.express_feedback_out_of_stock.replace('${items}', items[:-1])
        # print msg
        with topic.get_producer() as producer:
            producer.produce(msg)

    @classmethod
    def feedback_delivery_result(cls, distributor_id='', order_ids=[], feedback_status='6302'):
        """
        快递接口反馈运单配送结果
        :param distributor_id:
        :param order_ids:
        :param feedback_status: 6301 配送在途；6302 配送成功；6303 配送失败
        """
        print u'*' * 20 + u'快递接口反馈运单配送结果'
        item = expressInvokerMessage.express_feedback_delivery_result_item \
            .replace('${express_id}', distributor_id) \
            .replace('${feedback_status}', feedback_status)
        if feedback_status == '6303':
            item = item.replace('${reason}', '查无此人')
        else:
            item = item.replace('${reason}', '')
        items = ''
        for order_id in order_ids:
            items += item.replace('${order_id}', order_id)
            items += ','

        client = KafkaClient(hosts=tmsBase.kafka_client)
        topic = client.topics[KafkaTopics.EXPRESS.value]
        msg = expressInvokerMessage.express_feedback_delivery_result.replace('${items}', items[:-1])
        # print msg
        with topic.get_producer() as producer:
            producer.produce(msg)

    @classmethod
    def feedback_logistics_log(cls, distributor_id='', order_ids=[]):
        """
        快递接口反馈运单物流信息
        :param distributor_id:
        :param order_ids:
        """
        print u'*' * 20 + u'快递接口反馈运单物流信息'
        item = expressInvokerMessage.express_feedback_logistics_log_item \
            .replace('${express_id}', distributor_id)
        items = ''
        for order_id in order_ids:
            items += item.replace('${order_id}', order_id)
            items += ','

        client = KafkaClient(hosts=tmsBase.kafka_client)
        topic = client.topics[KafkaTopics.EXPRESS.value]
        msg = expressInvokerMessage.express_feedback_logistics_log.replace('${items}', items[:-1])
        # print msg
        with topic.get_producer() as producer:
            producer.produce(msg)
