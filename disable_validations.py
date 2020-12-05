'''
Disable validation rules in the object file

Came accross a situation where I had to merge some validation rules with the ones present on a github Repository. 
Didn't want to sit and manually merge so wrote this script. 

OBJECT_FILE : File containing the retrieved object
VALIDATIONS_FILE : File containing list of validation rules to be deactivated. Each rule on a new line

Stores the output as "Output.xml" on path specified at line 28 
'''

from lxml import etree
import os

OBJECT_FILE = r'D:\Salesforce Workspace\SalesforceScripts\Object\Opportunity.object'
VALIDATIONS_FILE = r'D:\Salesforce Workspace\SalesforceScripts\Object\validations.txt'


def parse_object(validations):
    tree = etree.parse(OBJECT_FILE)
    root = tree.getroot()
    ns = {'default': root.nsmap[None]}
    for validation in root.xpath('.//default:validationRules', namespaces=ns):
        if validation.find('.//default:fullName', namespaces=ns).text in validations:
            print(validation.find('.//default:active', namespaces=ns).text)
            validation.find('.//default:active', namespaces=ns).text = 'false'
    etree.ElementTree(root).write(r'D:\Salesforce Workspace\SalesforceScripts\Object\Output.xml',
                                  xml_declaration=True, encoding='UTF-8', pretty_print=True)


def read_validations():
    with open(VALIDATIONS_FILE) as fp:
        validations = fp.read().split('\n')
    return validations


if __name__ == "__main__":
    validations = read_validations()
    print(validations)
    parse_object(validations)
