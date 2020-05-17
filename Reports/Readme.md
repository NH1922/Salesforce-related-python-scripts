# Custom Report Types Mapped Names

I had set up a custom report type on the Opportunity object where I had changed what the fields were displayed as for many fields. Later I was required to document the actual Label names for these fields and their corresponding API names. This script does exactly that. 

For this script, two things are needed 
1. An export of the custom report type
2. Saved HTML page of the object on which the report is made in salesforce classic. (Switch to classic -> fields of the object -> save page as) 

Set the variables 'FILE_NAME'(report type) and 'FIELDS_PAGE'(html page) at line 6 and 8 and run the script. 
A csv file (name specified at line 7) will be generated containing the mapping. 

Before running the script, install the requirements specified in requirements.txt
