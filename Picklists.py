'''
Picklists value finder

Script finds all the picklist values for a given object

Retrieve the custom fields of an object using ANT migration tool or workbench.
Specifiy the object for which you wish to retrieve the picklist values.
Set 'filename' to point to the file. (full path of the file)
In this example, the script tries to find picklist values for the Opportunity object.

Output is stored in 'picklists.csv'. Customize the filename and path at line 40

'''

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
    
    