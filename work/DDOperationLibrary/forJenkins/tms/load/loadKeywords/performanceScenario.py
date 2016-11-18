# -*- encoding:utf-8 -*-
import sys
import os
reload(sys)
sys.setdefaultencoding('gbk')
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..\\..\\..\\..\\'))
from datetime import datetime
from parameters.tms.tmsBase import KafkaTopics
from pykafka import KafkaClient
from parameters.tms import tmsBase
from keywords.tms.interface.innerInvoker import InnerInvoker

__author__ = 'bida'


def continually_create_self_operated_order(minute=1, thread_num='', count=10, interval='0.01'):
    """

    :param count:
    :param minute:持续时间
    :param thread_num: 线程名称
    :param interval: 创建运单时间间隔
    """
    client = KafkaClient(hosts=tmsBase.kafka_client)
    topic = client.topics[KafkaTopics.RAINBOW.value]
    duration = minute * 60
    start_time = datetime.now()
    end_time = datetime.now()
    length = 0

    print 'Thread-%s begin batch create self operated orders' % thread_num
    with topic.get_producer() as producer:
        while (end_time - start_time).seconds < duration:
            length += InnerInvoker.create_self_operated_order(count=count,
                                                              thread_no=thread_num,
                                                              interval=interval,
                                                              producer=producer)[1]
            end_time = datetime.now()
    print 'Thread-%s totally created  %s self operated orders ' % (thread_num, length)


def continually_create_merchant_order(minute=1, thread_num='', count=10, interval='0.01'):
    """

    :param count:
    :param minute:持续时间
    :param thread_num: 线程名称
    :param interval: 创建运单时间间隔
    """
    client = KafkaClient(hosts=tmsBase.kafka_client)
    topic = client.topics[KafkaTopics.RAINBOW.value]
    duration = minute * 60
    start_time = datetime.now()
    end_time = datetime.now()
    length = 0

    print 'Thread-%s begin batch create merchant orders' % thread_num
    with topic.get_producer() as producer:
        while (end_time - start_time).seconds < duration:
            length += InnerInvoker.create_merchant_order(count=count,
                                                         items=10,
                                                         thread_no=thread_num,
                                                         interval=interval,
                                                         producer=producer)[1]
            end_time = datetime.now()
    print 'Thread-%s totally created  %s merchant orders' % (thread_num, length)


def continually_create_change_and_refund_order(minute=1, thread_num='', count=10, interval='0.01'):
    """

    :param count:
    :param minute:持续时间
    :param thread_num: 线程名称
    :param interval: 创建运单时间间隔
    """
    client = KafkaClient(hosts=tmsBase.kafka_client)
    topic = client.topics[KafkaTopics.RAINBOW.value]
    duration = minute * 60
    start_time = datetime.now()
    end_time = datetime.now()
    length = 0

    print 'Thread-%s begin batch create change and refund orders' % thread_num
    with topic.get_producer() as producer:
        while (end_time - start_time).seconds < duration:
            length += InnerInvoker.create_change_and_refund_order(count=count,
                                                                  thread_no=thread_num,
                                                                  interval=interval,
                                                                  producer=producer)[1]
            end_time = datetime.now()
    print 'Thread-%s totally created  %s change and refund orders' % (thread_num, length)
