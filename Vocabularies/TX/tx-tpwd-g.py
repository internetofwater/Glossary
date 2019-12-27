#Date Created: 12/27/2019
#Purpose: To extract text from html file (website) and export to xlsx file.
#Notes: # OKWRB glossary.



#Needed Modules
############################################################################
import requests #to pull info from an html site
from bs4 import BeautifulSoup #to parse and sort html information
import pandas as pd # parsing data and creating dataframes
import os
import openpyxl

workingDir="/Users/joseph/Desktop/WSWC/IoW/Vocabularies/TX/"
os.chdir(workingDir)


#Retrieving html Information
############################################################################
result = requests.get("https://tpwd.texas.gov/landwater/water/habitats/rivers/glossary.phtml")  #linking to website and creating source.
html = result.content  # store the page content
soup = BeautifulSoup(html, 'html.parser')  #create a beautifulSoup obect based on the source variable.


#Storage Variables
############################################################################
lst1 = []  # empty list for all text storage


#Gathering Data
###########################################################################
try:
    #if result.status_code == 200:  # a valuve of 200 indicates yes, a 403 forbidden means no.
    print("Success. Website is accessible.")

    neededclass = soup.find(id ="maincontent")  # TPWD specific: Finding all 'p' tag items only within the id "maincontent"
    for p in neededclass.find_all('p'):  # change tag information here
        lst1.append(p.text)  # return text only and append empty list with findings

    glossary = pd.DataFrame(lst1)  # convert list to dataframe for manipulation
    glossary.drop([0,1,2,424], inplace=True)  # TPWD specific: Drop fluff rows

    # Cleaning Text
    ############################################################################
    print("Cleaning text.")
    # OWRB Specific:  split on " - ".  Spaces are neccessary to include defs with '-' in them.  Ex "Off-bank"
    glossary = glossary[0].str.split(' - ', n=1, expand=True)
    glossary.rename(columns={0:'Term', 1:'Definition'}, inplace=True)  # rename columns to match Template
    glossary.set_index('Term', inplace=True)



    # Exporting Text to xlsx file.
    ############################################################################
    print("Exporting data to xlsx.")

    #export DataFrame to excel.xlsx format

    glossary.to_excel('tx-tpwd-g-export.xlsx')



except:
    print("Error. Website is not accessible.")


print("Code Complete.")