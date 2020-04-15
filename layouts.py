import os
import xml.etree.ElementTree as ET


LAYOUT_FOLDER = 'D:\Quick Scripts\Layouts'
OUTPUT_FOLDER = 'D:\Quick Scripts\OutputLayout'


def fix_layouts(filename):
    ET.register_namespace('', 'http://soap.sforce.com/2006/04/metadata')
    tree = ET.parse(os.path.join(LAYOUT_FOLDER,filename))
    root = tree.getroot()
    sections = root.findall('{http://soap.sforce.com/2006/04/metadata}layoutSections')
    for section in sections:
        label = section.find('{http://soap.sforce.com/2006/04/metadata}label').text
        if 'Insurance' not in label:
            style = section.find('{http://soap.sforce.com/2006/04/metadata}style')
            style.text = 'TwoColumnsLeftToRight'
    tree.write(os.path.join(OUTPUT_FOLDER,filename), encoding='UTF-8', xml_declaration=True)
        

if __name__ == '__main__':
    files = next(os.walk(LAYOUT_FOLDER))[2]
    for file in files:
        fix_layouts(file)
    