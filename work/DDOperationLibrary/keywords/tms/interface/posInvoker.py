# -*- encoding:utf-8 -*-
from parameters.tms import tmsBase
from pykafka import KafkaClient

from parameters.tms import posInvokerMessage
from parameters.tms.tmsBase import KafkaTopics

__author__ = 'bida'


class PosInvoker:
    def __init__(self):
        pass

    @classmethod
    def tms_pos_exceptional_delivery(cls, order_no='', excode=''):
        """
        pos配送异常
        :param excode:
        :param order_no:
        """
        print u'*' * 20 + u'POS配送异常'

        msg = posInvokerMessage.tms_pos_exceptional_delivery.replace('${order_no}', order_no)\
            .replace('$[exCode}', excode)
        # print msg
        client = KafkaClient(hosts=tmsBase.kafka_client)
        topic = client.topics[KafkaTopics.POS.value]
        with topic.get_producer() as producer:
            producer.produce(msg)

    @classmethod
    def tms_pos_payment_reverse(cls, order_no='', reverse_amt='47.9', pay_type='02', reverse_type='01'):
        """
        POS支付冲正
        :param order_no:
        :param reverse_amt:
        :param pay_type:支付类型
        :param reverse_type:冲正类型，01，支付冲正；02，撤销冲正
        """
        message = reverse_type == '01' and u'POS支付冲正' or u'POS撤销冲正'
        print u'*' * 20 + message

        msg = posInvokerMessage.tms_pos_payment_reverse.replace('${order_no}', order_no)\
            .replace('${reverse_amt}', reverse_amt)\
            .replace('${pay_type}', pay_type)\
            .replace('${reverse_type}', reverse_type)
        # print msg
        client = KafkaClient(hosts=tmsBase.kafka_client)
        topic = client.topics[KafkaTopics.POS.value]
        with topic.get_producer() as producer:
            producer.produce(msg)

    @classmethod
    def tms_pos_signment_feedback(cls, order_no):
        """
        POS派件签收结果反馈
        :param order_no:
        """
        print u'*' * 20 + u'POS派件签收结果反馈'
        msg = posInvokerMessage.tms_pos_signment_feedback\
            .replace('${order_no}', order_no)
        # print msg
        client = KafkaClient(hosts=tmsBase.kafka_client)
        topic = client.topics[KafkaTopics.POS.value]
        with topic.get_producer() as producer:
            producer.produce(msg)

    @classmethod
    def tms_pos_cancel_payment(cls, order_no):
        """
         POS撤销支付结果反馈
        :param order_no:
        """
        print u'*' * 20 + u'POS撤销支付结果反馈'
        msg = posInvokerMessage.tms_pos_cancel_payment\
            .replace('${order_no}', order_no)
        # print msg
        client = KafkaClient(hosts=tmsBase.kafka_client)
        topic = client.topics[KafkaTopics.POS.value]
        with topic.get_producer() as producer:
            producer.produce(msg)

    @classmethod
    def tms_pos_payment_feedback(cls, order_no, pay_type, order_payable_amount):
        """
        POS派件支付结果反馈
        :param order_no:
        :param pay_type:01 现金；02 银行卡
        :param order_payable_amount:
        """
        print u'*' * 20 + u'POS派件支付结果反馈'
        msg = posInvokerMessage.tms_pos_payment_feedback\
            .replace('${order_no}', order_no)\
            .replace('${pay_type}', pay_type)\
            .replace('${order_payable_amount}', order_payable_amount)
        # print msg
        client = KafkaClient(hosts=tmsBase.kafka_client)
        topic = client.topics[KafkaTopics.POS.value]
        with topic.get_producer() as producer:
            producer.produce(msg)

