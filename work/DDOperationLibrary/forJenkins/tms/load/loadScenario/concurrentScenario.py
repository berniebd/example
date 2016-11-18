# -*- encoding:utf-8 -*-
import threading

from forJenkins.tms.load.loadKeywords.performanceScenario import continually_create_self_operated_order

__author__ = 'bida'

if __name__ == '__main__':
    threads = []
    for i in range(2):
        threads.append(threading.Thread(target=continually_create_self_operated_order,
                                        args=(0.5, str(i + 1), '20')))
        # threads.append(threading.Thread(target=continually_create_change_and_refund_order,
        #                                 args=(0.5, str(i + 21), '20')))
        # threads.append(threading.Thread(target=continually_create_merchant_order,
        #                                 args=(0.5, str(i + 31), '20')))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()