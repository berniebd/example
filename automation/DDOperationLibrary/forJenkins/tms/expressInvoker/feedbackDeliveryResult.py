# -*- encoding:utf-8 -*-
import sys
# reload(sys)
# sys.setdefaultencoding('gbk')
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..\\..\\..\\'))
from keywords.tms.base.baseInfo import BaseInfo
from keywords.tms.interface.expressInvoker import ExpressInvoker


if __name__ == '__main__':
    distributor_id = str(BaseInfo.get_distributor_or_subdistributor_id(short_name=sys.argv[1].decode('gbk')))
    ExpressInvoker.feedback_delivery_result(distributor_id=distributor_id,
                                            order_ids=sys.argv[2].split(','),
                                            feedback_status=sys.argv[3])