# -*- encoding:utf-8 -*-

__author__ = 'bida'

import lxml.etree as ET
import lxml.builder
import glob

dbchangelog = 'http://www.host.org/xmlTry/ns/dbchangelog'
xsi = 'http://www.host.org/2001/XMLSchema-instance'
E = lxml.builder.ElementMaker(
    nsmap={
        None: dbchangelog,
        'xsi': xsi})

ROOT = E.databaseChangeLog
DOC = E.include

# grab all the xmlTry files
files = [DOC(file=f) for f in glob.glob("*.xmlTry")]

the_doc = ROOT(*files)
the_doc.attrib['{{{pre}}}schemaLocation'.format(pre=xsi)] = 'www.host.org/xmlTry/ns/dbchangelog'

print(ET.tostring(the_doc,
                  pretty_print=True, xml_declaration=True, encoding='utf-8'))
