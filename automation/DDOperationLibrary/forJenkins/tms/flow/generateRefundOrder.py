# -*- encoding:utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..\\..\\..\\'))
from keywords.tms.billing.billingFlow import BillingFlow

if __name__ == '__main__':
    BillingFlow.billing_return_refund(account='ADMIN', order_nos=sys.argv[1].split(','))
