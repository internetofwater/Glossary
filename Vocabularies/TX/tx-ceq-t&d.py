#Date Created: 01/03/2020
#Purpose: To extract text from html file (website) and export to xlsx file.
#Notes: # TCEQ terms & definitions.



#Needed Modules
############################################################################
import requests #to pull info from an html site
from bs4 import BeautifulSoup #to parse and sort html information
import pandas as pd # parsing data and creating dataframes
import os
import openpyxl

# Todo: Change working directory depending on working machine
workingDir="/Users/augustus/Desktop/WSWC/IoW/Vocabularies/TX/"
os.chdir(workingDir)


#Retrieving html Information
############################################################################
result = requests.get("https://www.tceq.texas.gov/remediation/superfund/glossary.html")  #linking to website and creating source.
html = result.content  # store the page content
soup = BeautifulSoup(html, 'html.parser')  #create a beautifulSoup obect based on the source variable.


#Storage Variables
############################################################################
lst1 = []  # empty list for all text storage
lst2 = []


#Gathering Data

if result.status_code == 200:  # a valuve of 200 indicates yes, a 403 forbidden means no.
    print("Success. Website is accessible.")

    neededclass = soup.find(id ="parent-fieldname-text") # TCEQ specific: Finding all 'p' tag items only within the id "maincontent"
    for dt in neededclass.find_all('dt'):  # change tag information here
        lst1.append(dt.text) # return text only and append empty list with findings

    for id in neededclass.find_all(id = "wetland"):
        lst1.append(id.text)


    for dd in neededclass.find_all('dd'):
        lst2.append(dd.text)


    df1 = pd.DataFrame({'Term':lst1})
    df1.loc[138] = "wetland" # add row manually rather than finagle around with the entire dataframe

    df2 = pd.DataFrame({"Definition":lst2})
    df2.drop(df2[df2['Definition'] == '\n\n'].index, inplace=True)
    df2.drop(df2[df2['Definition'] == ''].index, inplace=True)
    df2.reset_index(inplace=True)


    glossary = pd.merge(left = df1, right=df2, left_index=True, right_index=True)  # merge dataframes on index


    # Cleaning Text
    ############################################################################
    print("Cleaning text.")
    # OWRB Specific:  split on " - ".  Spaces are neccessary to include defs with '-' in them.  Ex "Off-bank"
    glossary.drop(columns='index', axis= 0, inplace=True)



    # Exporting Text to xlsx file.
    ############################################################################
    print("Exporting data to xlsx.")

    #export DataFrame to excel.xlsx format

    glossary.to_excel('tx-ceq-t&d-export.xlsx')
    print("Glossary exported!")


else:
    print("Error. Website is not accessible.")


print("Code Complete.")