'''
Required Fields Finder

Finds all required fields for all page layouts inside a folder
'''

import os
import csv
from lxml import etree

layout_folder = r'D:\Quick Scripts\Layouts'
required_fields = []
required_behavior = 'Required'

def parse_xml(filename):
    tree = etree.parse(filename)
    root = tree.getroot()
    ns = {'default': root.nsmap[None]}
    fields = []
    for item in root.xpath('.//default:layoutItems', namespaces=ns):
        behavior = item.find('.//default:behavior', namespaces=ns)
        field = item.find('.//default:field', namespaces=ns)
        #print(field.text)
        if not behavior is None and behavior.text == required_behavior:
            fields.append(field.text)
    print(fields)
    return fields

# def search_fields(object):
#     for item in req_fields:
#         if(item['object']==object):
#             return required_fields[object]

def update_fields(object,fields):
    flag = False
    for item in required_fields:
        if item['object'] == object:
            item['fields'] = item['fields'].union(set(fields))
            flag = True
    if not flag:
        required_fields.append({'object':object,'fields':set(fields)})


if __name__ == '__main__':
    files = next(os.walk(layout_folder))[2]
    for file in files:
        update_fields(file.split('-')[0],parse_xml(os.path.join(layout_folder,file)))
        #fields = parse_xml(os.path.join(layout_folder,file))
        # next(item for item in required_fields if required_fields['Object']==file.split('-')[0])
        #required_fields[file.split('-')[0]] = required_fields[file.split('-')[0]].union(set(fields))
    with open('required_fields.csv', 'w', encoding='utf8', newline='') as output_file:
        fc = csv.DictWriter(output_file, fieldnames=required_fields[0].keys(),)
        fc.writeheader()
        fc.writerows(required_fields)
    print(required_fields)