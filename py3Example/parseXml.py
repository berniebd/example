# encoding=utf-8
# Created by bernie on 6/2/
from xml.etree import ElementTree

if __name__ == '__main__':
    doc = ElementTree.parse('source.xml')
    root = doc.getroot()
    print(root)
    parents = root.findall('parent')
    print(len(parents))
    for son in parents[0].findall('son'):
        print(son.tag)
        print(son.attrib['name'])
        print(son.text)