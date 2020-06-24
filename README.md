# Salesforce Related Python Scripts
Set of quick and dirty python scripts I wrote to automate certain repetitive  things I had to do in salesforce.

Very often I was required to fetch stuff like list of all required fields on a layout, list of validation rules that were were based on a certain validation rule, find mapped names in a report type. 
Most of these tasks can be done quickly by taking a "retrieve" of the objects, report types etc  and parse the retrieved metadata. 

This repo contains some of those scripts I wrote. These aren't the neatest and most efficient codes but they got the job done for me. Will try and improve them over time.

#### Brief Descriptions  
[picklists.py](https://github.com/NH1922/Salesforce-related-python-scripts/blob/master/Picklists.py) - Find all picklist values for an object

[validations.py](https://github.com/NH1922/Salesforce-related-python-scripts/blob/master/validations.py) - Finds all validation rules for an object based on their error condition formula 

[pagelayout_style_changer.py](https://github.com/NH1922/Salesforce-related-python-scripts/blob/master/pagelayout_style_changer.py) - Sets styles of sections based on the set criteria to Two Columns Left To right for all page layouts in a folder.

[required_fields.py](https://github.com/NH1922/Salesforce-related-python-scripts/blob/master/required_fields.py) - Finds all required fields at page layout levels for objects across all their page layouts. 

[reporttypenames.py](https://github.com/NH1922/Salesforce-related-python-scripts/blob/master/Reports/reporttypenames.py) creates a mapping of fields in a custom report type with their api names and labels. 

[FLS.py](https://github.com/NH1922/Salesforce-related-python-scripts/blob/master/FLS.py) Extracts FLS of a particular object for a profile. 
