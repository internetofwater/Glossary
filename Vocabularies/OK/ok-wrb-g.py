#Date Created: 12/19/2019
#Purpose: To extract text from html file (website) and export to xlsx file.
#Notes: # OKWRB glossary.



#Needed Modules
############################################################################
import requests #to pull info from an html site
from bs4 import BeautifulSoup #to parse and sort html information
import pandas as pd # parsing data and creating dataframes
import os
import openpyxl

workingDir="/Users/augustus/Desktop/WSWC/IoW/Vocabularies/OK/"
os.chdir(workingDir)


#Retrieving html Information
############################################################################
result = requests.get("https://www.owrb.ok.gov/util/glossary.php")  #linking to website and creating source.
html = result.content  # store the page content
soup = BeautifulSoup(html, 'html.parser')  #create a beautifulSoup obect based on the source variable.


#Storage Variables
############################################################################
lst1 = []  # empty list for all text storage


#Gathering Data
###########################################################################
if result.status_code == 200:  # a valuve of 200 indicates yes, a 403 forbidden means no.
    print("Success. Website is accessible.")

    neededclass = soup.find(class_="centercontent")  # OWRB specific. Finding all 'p' tag items only within the class_"entry-content"
    test = neededclass.find_all('p')
    for p in neededclass.find_all('p'):  # change tag information here
        lst1.append(p.text)  # return text only and append empty list with findings

    glossary = pd.DataFrame(lst1)
    glossary.drop([0], inplace=True)

    # Cleaning Text
    ############################################################################
    print("Cleaning text.")
    # OWRB Specific.
        # Skipping N/A Elements.
        # Seperating out Term Name from Term Definitions.

    glossary = glossary[0].str.split(':', n=1, expand=True)
    glossary.rename(columns={0:'Term', 1:'Definition'}, inplace=True)
    glossary.set_index('Term', inplace=True)
    glossary.drop('-- back to top --', inplace=True)


    # Exporting Text to xlsx file.
    ############################################################################
    print("Exporting data to xlsx.")

    #export DataFrame to xlsx

    glossary.to_excel('ok-wrb-g-export.xlsx')



else:
    print("Error. Website is not accessible.")


print("Code Complete.")