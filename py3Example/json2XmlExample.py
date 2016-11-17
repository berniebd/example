# -*- encoding:utf-8 -*-
import dicttoxml
__author__ = 'bida'

jo = {
    'head':{
        'partnerCode': 'SAIC',
        'responseCompleteMessageStatus': {
            'messageStatusCode': '000000'
        }
    },
    'body': {
        'QueryVehicleModelResponse':{
            'VehicleModelList':{},
            'deductionDueTaxDate': '2015-09-11'
        }
    }
}


if __name__ == '__main__':
    xml = dicttoxml.dicttoxml(jo, root=True, custom_root='response', attr_type=False)
    print(xml)