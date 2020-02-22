#Date Created: 01/27/2020
#Purpose: To extract text from html file (website) and export to xlsx file.
#Notes: # OR-USGS glossary.



#Needed Modules
############################################################################
import requests #to pull info from an html site
from bs4 import BeautifulSoup #to parse and sort html information
import pandas as pd # parsing data and creating dataframes
import os
import numpy as np
import openpyxl

workingDir="/Users/augustus/Desktop/WSWC/IoW/Vocabularies/USGS/"
os.chdir(workingDir)


#Retrieving html Information
############################################################################
result = requests.get("https://or.water.usgs.gov/projs_dir/willgw/glossary.html")  #linking to website and creating source.
html = result.content  # store the page content
soup = BeautifulSoup(html, 'lxml')  #create a beautifulSoup obect based on the source variable.


#Storage Variables
############################################################################
lst1 = []
lst2 = []
lst3 = []


#Gathering Data
###########################################################################
if result.status_code == 200:  # a valuve of 200 indicates yes, a 403 forbidden means no.
    print("Success. Website is accessible.")

    neededclass = soup.find(id = "mainbody")


    for p in neededclass.find_all('p'):
        lst1.append(p.text)

    glossary = pd.DataFrame(lst1)


    # Cleaning Text
    ############################################################################
    print("Cleaning text.")
    # ID DEQ Specific.

    # drop references from end of dataframe
    ref = list(range(436, 472))
    glossary.drop(ref, inplace=True)

    for i, row in glossary.iterrows():
        x = len(row[0])
        y = row[0]
        print(i, x)
        if x <= 4:
            glossary.drop(i, inplace = True)
        elif "|" in y:
            glossary.drop(i, inplace =True)



        print('done')

    glossary = pd.Series(glossary)
    glossary = glossary.str.strip()



    # remove first row
    glossary.drop([0], inplace=True)  # remove first row



    glossary.set_index('Terms', inplace=True)



    # Exporting Text to xlsx file.
    ############################################################################
    print("Exporting data to xlsx.")

    #export DataFrame to xlsx

    glossary.to_excel('id-deq-g-export.xlsx')



else:
    print("Error. Website is not accessible.")


print("Code Complete.")