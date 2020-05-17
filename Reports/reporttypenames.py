from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import csv


FILE_NAME = 'Loan_Applications_with_Lookup_fields.reportType'
CSV_NAME = 'Mapping.csv'
FIELDS_PAGE = 'opp.html'


def WriteDictToCSV(csv_file, csv_columns, dict_data):
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
    return


if __name__ == "__main__":
    # Fetch the Display Names from the unpackaged file
    tree = ET.parse(FILE_NAME)
    root = tree.getroot()
    columns = root.findall(
        '*/{http://soap.sforce.com/2006/04/metadata}columns')
    renamed_cols = []
    for element in columns:
        if len(element.getchildren()) == 4:
            renamed_cols.append(element)

    # Parsing the fields page to find the labels
    page = open(FIELDS_PAGE)
    page = page.read()
    soup = BeautifulSoup(page, 'lxml')
    mapping = []
    for column in renamed_cols:
        print('API NAME :'+column[2].text)
        if column[2].text == 'CreatedDate' or 'Account.' in column[2].text or 'Scheme__c.' in column[2].text or 'LocationMaster__c.' in column[2].text or 'SalesExecutive__c' in column[2].text:
            label=''
        else:
            label = soup.find('td', text=column[2].text).find_previous_sibling("th").text
        mapping.append(
            {'Api Name': column[2].text, 'Label': label, 'Mapped Name': column[1].text})

    column_names = ['Api Name','Label','Mapped Name']
    WriteDictToCSV(CSV_NAME,column_names,mapping)
