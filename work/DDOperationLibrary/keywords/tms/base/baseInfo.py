# -*- encoding:utf-8 -*-
import chardet
import demjson
import sys
# reload(sys)
# sys.setdefaultencoding('gbk')
from keywords.tms.tmsLogin import TmsLogin
from parameters.tms import tmsBase
from utilities.httpRequest import HttpRequest

__author__ = 'bida'


class BaseInfo:
    def __init__(self):
        pass

    @classmethod
    def get_distributor_or_subdistributor_id(cls, account='ADMIN', short_name=''):
        distributor_id = cls.get_distributor_id(distributor_short_name=short_name) != 0 \
                         and cls.get_distributor_id(distributor_short_name=short_name) \
                         or cls.get_subdistributor_id(subdistributor_short_name=short_name)[1]
        return distributor_id

    @classmethod
    def get_distributor(cls, account='ADMIN', short_name=''):
        """
        根据简称获取配送商，或配送商分公司id
        :param account:
        :param short_name:
        """
        distributor_id = cls.get_distributor_id(distributor_short_name=short_name) != 0 \
                         and cls.get_distributor_id(distributor_short_name=short_name) \
                         or cls.get_subdistributor_id(subdistributor_short_name=short_name)
        return distributor_id

    @classmethod
    def get_distributor_id(cls, account='ADMIN', distributor_code='', distributor_short_name=''):
        print u'*' * 20 + u'获取配送商id'
        url = tmsBase.base_url + '/tms/base/baseDistributionTraderController.do?datagrid&field=id,supportService,companyNo,companyShortName,companyName,provinceTxt,cityTxt,areaTxt,streetTxt,companyAddress,contactPerson,contactNumber,serviceTel,website,email,supportService4,supportService5,supportService6,supportService1,supportService2,supportService3,alicode,comment,status,chinesename,updateTime,updateTime_begin,updateTime_end,'
        resp = HttpRequest.post_request(TmsLogin.get_session(account), url,
                                        data={'companyNo': distributor_code, 'companyShortName': distributor_short_name,
                                              'page': 1, 'rows': 10})
        print resp
        obj = demjson.decode(resp)
        if obj['total'] == 0:
            print u'*' * 20 + u'无符合条件的配送商'
            return 0
        else:
            distributor_id = obj['rows'][0]['id']
            print u'distributor_id: ' + distributor_id
            return distributor_id

    @classmethod
    def get_subdistributor_id(cls, account='ADMIN', subdistributor_short_name=''):
        print u'-' * 20 + u'获取配送商分公司及总公司id'
        url = tmsBase.base_url + '/tms/base/baseDistributionTraderSubController.do?datagrid&field=id,parentId,parentName,no,companyShortName,provinceTxt,cityTxt,areaTxt,streetTxt,companyAddress,contactPerson,contactPhone,email,comment,status,chinesename,updateTime,updateTime_begin,updateTime_end,'
        resp = HttpRequest.post_request(TmsLogin.get_session(account), url,
                                        data={'companyShortName': subdistributor_short_name, 'page': 1, 'rows': 10})
        print resp
        obj = demjson.decode(resp)
        if obj['total'] == 0:
            print u'-' * 20 + u'无符合条件的配送商分公司'
            return 0
        else:
            distributor_id = obj['rows'][0]['id']
            parent_distributor_id = obj['rows'][0]['parentId']
            print 'sub_distributor_id: ' + distributor_id
            print 'parent_distributor_id: ' + parent_distributor_id
            return parent_distributor_id, distributor_id

if __name__ == '__main__':
    print BaseInfo.get_distributor_or_subdistributor_id(short_name='上海分公司（ZFTest004）')