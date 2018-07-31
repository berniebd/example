# -*- encoding:utf-8 -*-
from lxml import etree
from lxml.etree import QName, Element, SubElement

__author__ = 'bida'


class XMLNamespace(object):
    soapenv = 'http://schemas.xmlsoap.org/soap/envelope/'
    ns = 'http://service.front.sinosoft.com'
    ax213 = 'http://busInterface.front.sinosoft.com/xsd'
    ax215 = 'http://dto.front.sinosoft.com/xsd'
    ax216 = 'http://common.dto.front.sinosoft.com/xsd'
    # ax216_resposne = 'ax216:TxInsuranceResponseEhm'
    # ax216_response_extension = 'ax216:TxInsuranceResponseExtensionEhm'
    ax219 = 'http://out.vehicleModelQuery.dto.front.sinosoft.com/xsd'
    xsi = 'http://busInterface.front.sinosoft.com/xsd'
    # type = 'http://busInterface.front.sinosoft.com/xsd'


if __name__ == '__main__':
    envelope = Element(QName(XMLNamespace.soapenv, 'Envelope'), nsmap={'soapenv': XMLNamespace.soapenv})
    body = SubElement(envelope, QName(XMLNamespace.soapenv, 'Body'))
    queryVehicleModelResponse = SubElement(body, QName(XMLNamespace.ns, 'queryVehicleModelResponse'),
                                           nsmap={'ns': XMLNamespace.ns})
    rreturn = SubElement(queryVehicleModelResponse, QName(XMLNamespace.ns, 'return'),
                         nsmap={'ax213': XMLNamespace.ax213, 'ax215': XMLNamespace.ax215, 'ax216': XMLNamespace.ax216,
                                'ax219': XMLNamespace.ax219, 'xsi': XMLNamespace.xsi},
                         attrib={'xsi:abc': 'ax215:VehicleModelQueryResponse'})
    # rreturn.set('{%s}' % XMLNamespace.ax215, '12334')

    # policySort = SubElement(rreturn, QName(XMLNamespace.ax215, 'policySort'))
    # insurance_response = SubElement(rreturn, QName(XMLNamespace.ax215, 'txInsuranceResponseEhm'),
    #                                 nsmap={'type': XMLNamespace.ax216_resposne})
    # insurance_response_extension = SubElement(rreturn, QName(XMLNamespace.ax215, 'txInsuranceResponseExtensionEhm'),
    #                                           nsmap={'type': XMLNamespace.ax216_response_extension})
    # policySort = SubElement(rreturn, QName(XMLNamespace.ax215, 'vehicleModelDataArr'))

    print(etree.tostring(envelope))
