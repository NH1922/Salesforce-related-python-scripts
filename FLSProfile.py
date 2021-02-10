'''
FLSProfile.py

Creates spreadsheets for each profiles with FLS of the fields specified across multiple objects 

1. Take an export of profiles and the fields(required)
2. Set 'PROFILE_FOLDER' to the directory containing the profiles
3. The script will generate a seperate csv for each profile containing all the fields and their acess (Read/Edit/No Access)
'''

from lxml import etree
import os
import csv

PROFILE_FOLDER = r'D:\Salesforce Workspace\SalesforceScripts\profiles'


def get_fls(file,profile):
    tree = etree.parse(file)
    root = tree.getroot()
    ns = {'default': root.nsmap[None]}
    fls = []
    # profile_fls = {}
    for field_permission in root.xpath('.//default:fieldPermissions', namespaces=ns):
        access = {}
        readable = field_permission.find('.//default:readable', namespaces=ns).text.lower()=='true'
        editable = field_permission.find('.//default:editable', namespaces=ns).text.lower() == 'true'
        field = field_permission.find('.//default:field', namespaces=ns)
        print(field.text, '->', readable, '-', editable)
        access['Object'], access['Field'] = field.text.split('.')
        if readable and editable:   
            access['Access']= 'Edit'
        elif readable and not editable:
            access['Access']= 'Read'
        else:
           access['Access']= 'No Access'
        fls.append(access)
    # profile_fls['Profile'] = profile
    # profile_fls['FLS'] = fls
    write_to_csv(profile,fls)
    # return profile_fls

def write_to_csv(output,rows):
    with open(output+'.csv', 'w', encoding='utf8', newline='') as output_file:
        fc = csv.DictWriter(output_file, fieldnames=rows[0].keys(),)
        fc.writeheader()
        fc.writerows(rows)
    
if __name__ == "__main__":
    files = next(os.walk(PROFILE_FOLDER))[2]
    output = []
    for file in files:
        output.append(get_fls(os.path.join(PROFILE_FOLDER,file),file.split('.')[0]))
