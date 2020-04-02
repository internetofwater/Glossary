#Date Created: 01/27/2020
#Purpose: To extract text from html file (website) and export to xlsx file.
#Notes: # IDDEQ glossary.



#Needed Modules
############################################################################
import requests #to pull info from an html site
from bs4 import BeautifulSoup #to parse and sort html information
import pandas as pd # parsing data and creating dataframes
import os
import openpyxl

workingDir="/Users/augustus/Desktop/WSWC/IoW/Vocabularies/ID/"
os.chdir(workingDir)


#Retrieving html Information
############################################################################
result = requests.get("https://www.deq.idaho.gov/glossary/")  #linking to website and creating source.
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

    neededclass = soup.find(id = "content")  # ID-WRB specific. Finding all 'tr' tag items within tr tags to seperate term from
                                      # definition.
    for twentyeighty in neededclass.find_all(class_ = "2080"):
        for dt in twentyeighty.find_all('dt'):
            lst1.append(dt.text)

        for dd in twentyeighty.find_all('dd'):
            lst2.append(dd.text)

    data = {'Terms': lst1, 'Definitions': lst2}
    glossary = pd.DataFrame(data)


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