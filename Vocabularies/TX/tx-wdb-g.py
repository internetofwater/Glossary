#Date Created: 01/23/2020
#Purpose: To extract text from html file (website) and export to xlsx file.
#Notes: # TWDB glossary



#Needed Modules
############################################################################
import requests #to pull info from an html site
from bs4 import BeautifulSoup #to parse and sort html information
import pandas as pd # parsing data and creating dataframes
import os
import openpyxl

# Todo: Change working directory depending on working machine
workingDir="/Users/joseph/Desktop/WSWC/IoW/Vocabularies/TX/"
os.chdir(workingDir)


#Retrieving html Information
############################################################################
result = requests.get("http://www.twdb.texas.gov/waterplanning/data/glossary.asp")  #linking to website and creating source.
html = result.content  # store the page content
soup = BeautifulSoup(html, 'lxml')  #create a beautifulSoup obect based on the source variable.


#Storage Variables
############################################################################
lst1 = []  # empty list for all text storage
lst2 = []


#Gathering Data

if result.status_code == 200:  # a valuve of 200 indicates yes, a 403 forbidden means no.
    print("Success. Website is accessible.")

    neededclass = soup.find(class_ ="definition-list--block") # TCEQ specific: Finding all 'p' tag items only within the id "maincontent"
    for dt in neededclass.find_all('dt'):  # change tag information here
        lst1.append(dt.text) # return text only and append empty list with findings

    for dd in neededclass.find_all("dd"):
        lst2.append(dd.text)


    df1 = pd.DataFrame({'Term':lst1})
    df2 = pd.DataFrame({"Definition":lst2})


    glossary = pd.merge(left = df1, right=df2, left_index=True, right_index=True)  # merge dataframes on index


    # Cleaning Text
    ############################################################################
    print("Cleaning text.")
    # no cleaning required


    # Exporting Text to xlsx file.
    ############################################################################
    print("Exporting data to xlsx.")

    #export DataFrame to excel.xlsx format

    glossary.to_excel('tx-wdb-g-export.xlsx')
    print("Glossary exported!")


else:
    print("Error. Website is not accessible.")


print("Code Complete.")