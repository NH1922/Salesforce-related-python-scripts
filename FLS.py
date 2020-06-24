"""
FLS Extractor

Extracts FLS of an object for a profile. 

Switch to classic mode and navigate to profiles and then to the Field Level Security of the desired object. 
Save the page on your local storage. Save the pages of all the objects whose FLS has to be documented in the 
directory specified in variable 'BASE_DIRECTORY' 

Run the script and it will generate the CSV files for each of the oject html saved. 

"""

from bs4 import BeautifulSoup
import os
import csv

BASE_DIRECTORY  = r'C:\Users\nitish_yadav\Desktop\Scripts'  #directory containing saved html pages


def parse_html(filename):
    outputrows = []
    with open(filename) as fp:
        page = fp.read()
    soup = BeautifulSoup(page,'html.parser')
    title = soup.find('h1',class_='pageType').text
    print(title)
    rows = soup.find_all('tr',class_='dataRow')
    for row in rows:
        output = {}
        cols = row.find_all('td',class_='dataCell')
        output['Field Name'] = cols[0].text
        output['Read Access'] = False if cols[2].find('img').get('title') == 'Not Checked' else True
        output['Edit Access'] = False if cols[3].find('img').get('title') == 'Not Checked' else True
        outputrows.append(output)
    output_file = title.split('Field-Level')[0].strip()+'.csv'
    print(output_file)
    with open(output_file, 'w', encoding='utf8', newline='') as output_file:
        fc = csv.DictWriter(output_file, fieldnames=outputrows[0].keys(),)
        fc.writeheader()
        fc.writerows(outputrows)

if __name__ == '__main__':
    files = next(os.walk(BASE_DIRECTORY))[2]
    for filename in files:
        parse_html(os.path.join(BASE_DIRECTORY,filename))