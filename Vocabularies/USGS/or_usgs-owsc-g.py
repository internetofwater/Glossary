#Date Created: 01/27/2020
#Purpose: To extract text from html file (website) and export to xlsx file.
#Notes: # OR-USGS glossary.



#Needed Modules
############################################################################
import requests #to pull info from an html site
from bs4 import BeautifulSoup #to parse and sort html information
import pandas as pd # parsing data and creating dataframes
import os
import openpyxl

workingDir="/Users/joseph/Desktop/WSWC/IoW/Vocabularies/ID/"
os.chdir(workingDir)


#Retrieving html Information
############################################################################
result = requests.get("https://or.water.usgs.gov/projs_dir/willgw/glossary.html")  #linking to website and creating source.
html = result.content  # store the page content
soup = BeautifulSoup(html, 'html.parser')  #create a beautifulSoup obect based on the source variable.


#Storage Variables
############################################################################
lst1 = []
lst2 = []
lst3 = []


#Gathering Data
###########################################################################
if result.status_code == 200:  # a valuve of 200 indicates yes, a 403 forbidden means no.
    print("Success. Website is accessible.")

    neededclass = soup.find(id = "mainbody")  # ID-WRB specific. Finding all 'tr' tag items within tr tags to seperate term from
                                              # definition.
    for p in neededclass.find_all('p'):
            lst1.append(p.text)


#    data = {'Terms': lst1, 'Definitions': lst2}
    glossary = pd.DataFrame(lst1)


    # Cleaning Text
    ############################################################################
    print("Cleaning text.")
    # ID DEQ Specific.

    # remove first row
    glossary.drop([0], inplace=True)
    glossary.set_index('Terms', inplace=True)



    # Exporting Text to xlsx file.
    ############################################################################
    print("Exporting data to xlsx.")

    #export DataFrame to xlsx

    glossary.to_excel('id-deq-g-export.xlsx')



else:
    print("Error. Website is not accessible.")


print("Code Complete.")