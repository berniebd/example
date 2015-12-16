# -*- encoding:utf-8 -*-
from dubbo_client import ApplicationConfig, ZookeeperRegistry, DubboClient

__author__ = 'bida'

if __name__ == '__main__':
    config = ApplicationConfig('consumer-of-helloworld-app')

    registry = ZookeeperRegistry('127.0.0.1:20880', config)
    service_interface = 'com.bernie.DemoService'
    service_provider = DubboClient(service_interface, registry, version='2.5.3')
    print service_provider.sayHello(u'bernie')