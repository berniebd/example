# -*- encoding:utf-8 -*-
from time import sleep

from keywords.tms.base.baseInfo import BaseInfo
from keywords.tms.express import ExpressDeliveryAction
from keywords.tms.express.expressReturndAction import ExpressReturnAction
from keywords.tms.interface.expressInvoker import ExpressInvoker
from keywords.tms.interface.innerInvoker import InnerInvoker
from keywords.tms.rainbow import RefundAction
from parameters.tms import tmsBase
from parameters.tms.tmsBase import DispatchStatus

__author__ = 'bida'


class ExpressFlow():
    def __init__(self):
        pass

    @classmethod
    def express_return_return(cls, order_ids=[], account='EXPRESS', feedback_result=DispatchStatus.SUCCESS.name):
        """
        自营退货运单退货成功退
        :param account:
        :param feedback_result:
        :param order_ids:
        """
        ExpressReturnAction.express_export_pre_return_order(account=account, order_ids=order_ids)
        sleep(tmsBase.wait_time)

        ExpressDeliveryAction.batch_dispatch(account=account, order_ids=order_ids)
        sleep(tmsBase.wait_time)

        ExpressDeliveryAction.batch_feedback(account=account, order_ids=order_ids,
                                             feedback_result=feedback_result)

        if feedback_result == 'FAIL':
            return

        sleep(tmsBase.wait_time)
        ExpressReturnAction.express_confirm_distributor_return(account=account, order_ids=order_ids)
        sleep(tmsBase.wait_time)
        ids = ''
        for order_id in order_ids:
            ids += order_id
            ids += ','
        sleep(tmsBase.wait_time)
        InnerInvoker.wms_return_confirmation(order_ids=ids[:-1], operation='return')

    @classmethod
    def express_return_on_fail(cls, order_ids=[], express_account='EXPRESS',
                               operating_center_account='TIANJINOPERATION'):
        """
        自营运单，换货运单配送失败，配送商退货
        :param operating_center_account:
        :param order_ids:
        :param express_account:
        """
        cls.express_delivery(account=express_account, order_ids=order_ids, target='3',
                             feedback_result=DispatchStatus.FAIL.name)
        RefundAction.return_check_requests(account=operating_center_account, order_ids=order_ids, operate_type='1')
        ExpressReturnAction.express_confirm_distributor_return(account=express_account, order_ids=order_ids)
        sleep(tmsBase.wait_time)
        ids = ''
        for order_id in order_ids:
            ids += order_id
            ids += ','
        sleep(tmsBase.wait_time)
        InnerInvoker.wms_return_confirmation(order_ids=ids, operation='exchange')

    @classmethod
    def express_return_on_success(cls, order_ids=[], express_account='EXPRESS'):
        """
        换货运单换货成功退，配送商退货
        :param order_ids:
        :param express_account:
        """
        cls.express_delivery(account=express_account, order_ids=order_ids, target='3',
                             feedback_result=DispatchStatus.SUCCESS.name)
        sleep(tmsBase.wait_time)
        ExpressReturnAction.express_confirm_distributor_return(account=express_account, order_ids=order_ids)
        ids = ''
        for order_id in order_ids:
            ids += order_id
            ids += ','
        sleep(tmsBase.wait_time)
        InnerInvoker.wms_return_confirmation(order_ids=ids, operation='exchange')

    @classmethod
    def express_delivery(cls, account='AUTOEXPRESS', target='', order_ids=[],
                         feedback_result=DispatchStatus.SUCCESS.name, by='express'):

        """
        快递配送并反馈
        :param feedback_result:
        :param account:
        :param order_ids:
        """
        ExpressDeliveryAction.batch_in_storage(account=account, order_ids=order_ids)
        if target == '1':
            return
        sleep(tmsBase.wait_time)

        ExpressDeliveryAction.batch_dispatch(account=account, order_ids=order_ids)
        if target == '2':
            return
        sleep(tmsBase.wait_time)

        if feedback_result == DispatchStatus.SUCCESS.name:
            if by == 'express':
                ExpressDeliveryAction.batch_feedback(account=account, order_ids=order_ids,
                                                     feedback_result=feedback_result)
            if by == 'pos':
                for order_id in order_ids:
                    InnerInvoker.tms_pos_payment_feedback(order_id)
                    InnerInvoker.tms_pos_signment_feedback(order_id)
        else:
            ExpressDeliveryAction.batch_feedback(account=account, order_ids=order_ids, feedback_result=feedback_result)

    @classmethod
    def express_delivery_api(cls,
                             account='AUTOEXPRESS',
                             target='',
                             order_ids=[],
                             feedback_result='',
                             distributor_short_name=''):

        """
        快递接口配送并反馈
        :param target:
        :param distributor_short_name:
        :param feedback_result:
        :param account:
        :param order_ids:
        """

        distributor_id = str(BaseInfo.get_distributor_or_subdistributor_id(short_name=distributor_short_name))
        ExpressInvoker.feedback_instorage(distributor_id=distributor_id, order_ids=order_ids)
        if target == '1':
            return
        sleep(tmsBase.wait_time)

        ExpressInvoker.feedback_outstorage(distributor_id=distributor_id, order_ids=order_ids)
        if target == '2':
            return
        sleep(tmsBase.wait_time)

        ExpressInvoker.feedback_logistics_log(distributor_id=distributor_id, order_ids=order_ids)
        ExpressInvoker.feedback_delivery_result(distributor_id=distributor_id, order_ids=order_ids,
                                                feedback_status=feedback_result)
