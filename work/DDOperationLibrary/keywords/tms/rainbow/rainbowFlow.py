# -*- encoding:utf-8 -*-
from datetime import datetime
from time import sleep
from keywords.tms.rainbow import DeliveryAction
from parameters.tms import tmsBase

__author__ = 'bida'


class RainbowFlow():
    def __init__(self):
        pass

    @classmethod
    def sorting_forward_to_delivery_dealer(cls, account='TIANJINSORTING', order_ids={}, delivery_dealer='',
                                           is_merchant=False, is_packaged=False):
        """
        一般运单出库至配送商
        :param account:
        :param order_ids:
        :param delivery_dealer:
        :param is_merchant:
        :param is_packaged:
        """
        print u'*' * 20 + u'一般运单出库至配送商'
        for order_id in order_ids:
            if u'运单信息不存在' in DeliveryAction.delivery_in_storage(account=account, order_id=order_id):
                raise StandardError(u'运单信息不存在: %s' % order_id)

        if is_merchant:
            for order_id in order_ids:
                DeliveryAction.delivery_weight(account=account, order_no=order_id)

        if is_packaged:
            package_no = datetime.now().strftime('%y%m%d%H%M%S')
            DeliveryAction.delivery_create_package(account=account, package_no=package_no, package_type=2)
            for order_id in order_ids:
                DeliveryAction.delivery_add_order_into_package(account=account, package_no=package_no, package_type=2,
                                                               order_no=order_id)
            DeliveryAction.delivery_confirm_package(account=account, package_no=package_no, package_type=2)

            sleep(tmsBase.wait_time)

            DeliveryAction.delivery_out_storage(account=account, out_company=delivery_dealer, order_no=package_no,
                                                out_order_type=2, out_type=1)
        else:
            for order_id in order_ids:
                DeliveryAction.delivery_out_storage(account=account, out_company=delivery_dealer, order_no=order_id,
                                                    out_order_type=1, out_type=1)

        sleep(tmsBase.wait_time)
        DeliveryAction.delivery_handoff(account=account, out_company=delivery_dealer)
