import xml.etree.ElementTree as ET
import csv


ns = {'CustomObject':"http://soap.sforce.com/2006/04/metadata"}
filename = 'Opportunity.object'
picklists = []


if __name__=='__main__':
    tree = ET.parse(filename)
    root = tree.getroot()
    for field in root.findall('./CustomObject:fields',ns):
        picklist_vals = []
        if field.find('./CustomObject:valueSet//CustomObject:value',ns) is not None:
            values = field.findall('.//CustomObject:value',ns)
            for value in values:
                picklist_vals.append(value.find('./CustomObject:fullName',ns).text)
            #print(picklist_vals)
            picklists.append({'Field' : field.find('./CustomObject:fullName',ns).text,'Values':picklist_vals})      
    print(picklists)        
            
    with open('picklists.csv', 'w', encoding='utf8', newline='') as output_file:
        fc = csv.DictWriter(output_file, fieldnames=picklists[0].keys(),)
        fc.writeheader()
        fc.writerows(picklists)
    
    