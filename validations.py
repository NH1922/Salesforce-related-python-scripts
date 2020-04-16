'''
Validation Rule Finder

Script finds all the validation rules and their error messages based on the condition set.

Retrieve the validation rules using ant migration tool or workbench.
Specifiy the filename of the retrieved object in 'filename' variable.

In this example, the script tries to find validation rules written on Opportunity object that
fires on update i.e contains 'NOT(ISNEW())' in the formula of the rule.

Output is stored in 'validations_update.csv'. Customize the filename and path at line 40

'''

import xml.etree.ElementTree as ET
import csv

vrules = []
filename = 'Opportunity.object'


if __name__ == '__main__':
    tree = ET.parse(filename)
    root = tree.getroot()
    for child in root:
        # print(child.find('{http://soap.sforce.com/2006/04/metadata}errorConditionFormula'))
        formula = child.find('{http://soap.sforce.com/2006/04/metadata}errorConditionFormula').text
        if not formula is None and 'NOT(ISNEW())' in formula:
            print(formula)
            rules = {}
            rules['Full name'] = child.find('{http://soap.sforce.com/2006/04/metadata}fullName').text
            rules['Error Message'] = child.find('{http://soap.sforce.com/2006/04/metadata}errorMessage').text
            vrules.append(rules)
    print(vrules)
    with open('validations_update.csv', 'w', encoding='utf8', newline='') as output_file:
        fc = csv.DictWriter(output_file, fieldnames=vrules[0].keys(),)
        fc.writeheader()
        fc.writerows(vrules)
            
            
        