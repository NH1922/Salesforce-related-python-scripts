import xml.etree.ElementTree as ET 
import csv

vrules = []

if __name__ == '__main__':
    tree = ET.parse('Opportunity.object')   
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
            
            
        