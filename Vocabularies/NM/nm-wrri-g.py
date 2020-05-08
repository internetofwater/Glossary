# Title: New Mexico - Oregon USGS - Water Resources Research Institute - NMDSWB Stocks and Fluxes
# Created by: Joseph Brewer, WSWC
# Date Created: 05/8/2020
# Purpose: To extract text from html file (website) and export to xlsx file.
# Notes:


#Needed Modules
############################################################################
import requests #to pull info from an html site
from bs4 import BeautifulSoup #to parse and sort html information
import pandas as pd # parsing data and creating dataframes
import os
import openpyxl

workingDir="/Users/augustus/Desktop/WSWC/IoW/Vocabularies/NM/"
os.chdir(workingDir)


#Retrieving html Information
############################################################################
result = requests.get("https://nmwrri.nmsu.edu/nmdswb-stocks-and-flows/")  #linking to website and creating source.
html = result.content  # store the page content
soup = BeautifulSoup(html, 'html.parser')  #create a beautifulSoup obect based on the source variable.


#Storage Variables
############################################################################
data = pd.DataFrame(columns=['glossary'])
glossary = pd.DataFrame(columns=['Term', 'Definition'])


#Gathering Data
###########################################################################
if result.status_code == 200:  # a valuve of 200 indicates yes, a 403 forbidden means no.
    print("Success. Website is accessible.")

    neededclass = soup.find(class_ = "entry-content cf")  # NM-WRRI specific:

    for p in neededclass.find_all('p'):
        data = data.append({'glossary': p.text}, ignore_index=True)

    # drop empty rows
    data.drop([0,1,14,19,20], inplace=True)




    # Cleaning Text
    ############################################################################
    # Iterate over rows in data DataFrame and split on ' – '
    for i, row in data.iterrows():
        x = row['glossary'].split(' – ')
        if len(x) == 2:
            glossary = glossary.append({'Term': x[0], 'Definition': x[1]},
                                       ignore_index=True)  # Append split values to glossary dataframe
                                                           # with positional arguments
        else:
            print(x)



    # Exporting Text to xlsx file.
    ############################################################################
    print("Exporting data to xlsx.")

    #export DataFrame to xlsx

    glossary.to_excel('nm-wrri-wbc-export.xlsx')



else:
    print("Error. Website is not accessible.")


print("Code Complete.")