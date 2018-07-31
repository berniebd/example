# -*- encoding:utf-8 -*-
import os

import sys
import xlrd
from lxml import etree

__author__ = 'bida'

if __name__ == '__main__':
    # xls_path = u'e:\\version.xls'
    xls_path = sys.argv[1]
    version = os.path.basename(xls_path).split('.')[0]
    xml_path = os.path.join(os.path.dirname(xls_path), version + '.xml')

    root = etree.Element('testsuite')
    root.set('name', version)

    table = xlrd.open_workbook(xls_path)

    for sheet in table.sheets():
        testsuite = etree.Element('testsuite')
        testsuite.attrib['name'] = sheet.name
        steps = None
        for i in range(1, sheet.nrows):
            if sheet.row(i)[0].value != '':
                testcase = etree.SubElement(testsuite, 'testcase')
                testcase.attrib['name'] = sheet.row(i)[0].value

                importance = etree.SubElement(testcase, 'importance')
                importance.text = isinstance(sheet.row(i)[1].value, float) and str(int(sheet.row(i)[1].value)) or \
                                  sheet.row(i)[1].value

                summary = etree.SubElement(testcase, 'summary')
                summary.text = sheet.row(i)[2].value

                preconditions = etree.SubElement(testcase, 'preconditions')
                preconditions.text = sheet.row(i)[3].value

                steps = etree.Element('steps')

            step = etree.SubElement(steps, 'step')

            step_number = etree.SubElement(step, 'step_number')
            step_number.text = '1'
            # step_number.text = isinstance(sheet.row(i)[4].value, float) and str(int(sheet.row(i)[4].value)) or \
            #                    sheet.row(i)[4].value

            actions = etree.SubElement(step, 'actions')
            actions.text = sheet.row(i)[4].value

            expectedresults = etree.SubElement(step, 'expectedresults')
            expectedresults.text = sheet.row(i)[5].value

            if sheet.row(i)[0].value != '' and sheet.row(i - 1)[0].value != '':
                testcase.append(steps)
            if i == sheet.nrows - 1:
                testcase.append(steps)

        root.append(testsuite)

    # with open(xml_path, 'w') as f:
    #     # f.write(etree.tostring(root, xml_declaration=True, pretty_print=True, encoding='utf-8'))
    #     f.write(etree.tostring(root))

    tree = etree.ElementTree(root)
    tree.write(xml_path, pretty_print=True, xml_declaration=True, encoding='utf-8')
