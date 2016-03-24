from keywords.tms.rainbow.deliveryAction import DeliveryAction
from keywords.tms.rainbow.rainbowFlow import RainbowFlow
from keywords.tms.rainbow.rainbowUtil import RainbowUtil
from keywords.tms.rainbow.refundAction import RefundAction

__author__ = 'bida'


class Rainbow(
    DeliveryAction,
    RainbowUtil,
    RainbowFlow,
    RefundAction
):
    def __init__(self):
        pass
