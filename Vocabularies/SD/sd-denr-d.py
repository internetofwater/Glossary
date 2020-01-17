#Date Created: 01/16/2020
#Purpose: To extract text from html file (website) and export to xlsx file.
#Notes: # SDDENR



#Needed Modules
############################################################################
import requests #to pull info from an html site
from bs4 import BeautifulSoup #to parse and sort html information
import pandas as pd # parsing data and creating dataframes
import os
import openpyxl

workingDir="/Users/joseph/Desktop/WSWC/IoW/Vocabularies/SD/"
os.chdir(workingDir)


#Retrieving html Information
############################################################################
result = requests.get("https://denr.sd.gov/des/wr/dictionary.aspx")  #linking to website and creating source.
html = result.content  # store the page content
soup = BeautifulSoup(html, 'lxml')  #create a beautifulSoup obect based on the source variable.


#Storage Variables
############################################################################
lst1 = []  # empty list for all text storage
lst2 = []  # empty list for all text storage


#Gathering Data
###########################################################################
if result.status_code == 200:  # a valuve of 200 indicates yes, a 403 forbidden means no.
    print("Success. Website is accessible.")

    neededclass = soup.find(id ="main")  # SDDENR specific: Finding all 'h4' tag items only within the class "cke_focus"
    for h4 in neededclass.find_all('h4'):  # change tag information here | h4 tags associated with term
        lst1.append(h4.text)  # return text only and append empty list with findings

    for blockquote in neededclass.find_all('blockquote'): # change tag information here | blockquote tags associated with definition
        lst2.append(blockquote.text) # return text only and append empty list with findings

    terms = pd.Series(lst1)  # convert list to dataframe for manipulation
    definitions = pd.Series(lst2)

    # Cleaning Text
    ############################################################################
    print("Cleaning text.")
    # OWRB Specific:  split on " - ".  Spaces are neccessary to include defs with '-' in them.  Ex "Off-bank"
    terms=terms.str.replace('.', '') # strip period of end of terms
    definitions.drop([91, 96, 99, 106, 107, 108, 116, 127, 129, 140, 156, 157, 158, 159], inplace = True) # drop fluff rows

    definitions = definitions.str.replace('\r\n', '')
    definitions = definitions.str.replace('       ', '')

    terms = terms.to_frame() # convert series to dataframes.  Documentation is clearer on merging
    definitions = definitions.to_frame()
    definitions.reset_index(inplace=True)
    glossary = pd.merge(left = terms, right=definitions, left_index=True, right_index=True)
    glossary.rename(columns={'0_x':'Term', '0_y':'Definition'}, inplace=True)  # rename columns to match Template
    glossary.drop(columns='index', axis=0, inplace=True)
    glossary.set_index('Term', inplace=True)




    # Exporting Text to xlsx file.
    ############################################################################
    print("Exporting data to xlsx.")

    #export DataFrame to excel.xlsx format
    glossary.to_excel('sd-denr-d-export.xlsx')





else:
    print("Error. Website is not accessible.")


print("Code Complete.")