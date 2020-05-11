# Title: Nebraska - Department of Natural Resources - INSIGHT
# Created by: Joseph Brewer, WSWC
# Date Created: 05/11/2020
# Purpose: To extract text from html file (website) and export to xlsx file.
# Notes:


#Needed Modules
############################################################################
import requests #to pull info from an html site
from bs4 import BeautifulSoup #to parse and sort html information
import pandas as pd # parsing data and creating dataframes
import os
import openpyxl

workingDir="/Users/augustus/Desktop/WSWC/IoW/Vocabularies/NE/"
os.chdir(workingDir)


#Retrieving html Information
############################################################################
result = requests.get("https://nednr.nebraska.gov/insight/terminology.html")  #linking to website and creating source.
html = result.content  # store the page content
soup = BeautifulSoup(html, 'html.parser')  #create a beautifulSoup obect based on the source variable.


#Storage Variables
############################################################################
lst1 = []
lst2 =[]
glossary = pd.DataFrame(columns=['Term', 'Definition'])


#Gathering Data
###########################################################################
if result.status_code == 200:  # a valuve of 200 indicates yes, a 403 forbidden means no.
    print("Success. Website is accessible.")

    neededclass = soup.find(class_ = "terminologyTable")  # NM-WRRI specific:
    x = 0
    for tr in neededclass.find_all('tr'):
        x = 0
        for td in tr.find_all('td'):
            if x == 0:
                print(td.text)
                lst1.append(td.text)
               # data=data.append({'term': td.text}, ignore_index=True)
                x+=1
            elif x == 1:
                print(td.text)
                lst2.append(td.text)
                #data=data.append({'definition':td.text}, ignore_index=True)

    data = {'Term': lst1, 'Definition': lst2}
    glossary = pd.DataFrame(data)


    # drop empty rows




    # Cleaning Text
    ############################################################################
    # Need to removr \r\n and replace with spaces in Terms
    stripped = pd.Series(glossary['Term'].values)  # Convert Keyword column to Pandas Series
    stripped = stripped.str.replace('\r\n', ' ') # Use Series.str.replace() to replace \r\n with space
    glossary = glossary.assign(Term=stripped)

    # Repeat for Definition
    stripped = pd.Series(glossary['Definition'].values)  # Convert Keyword column to Pandas Series
    stripped = stripped.str.replace('\r\n', ' ')  # Use Series.str.replace() to replace \r\n with space
    glossary = glossary.assign(Definition=stripped)



    # Exporting Text to xlsx file.
    ############################################################################
    print("Exporting data to xlsx.")

    #export DataFrame to xlsx

    glossary.to_excel('ne-dnr-insight_t-export.xlsx')



else:
    print("Error. Website is not accessible.")


print("Code Complete.")