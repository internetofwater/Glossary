#Date Created: 01/27/2020
#Purpose: To extract text from html file (website) and export to xlsx file.
#Notes: # WA ePermit glossary.



#Needed Modules
############################################################################
import requests #to pull info from an html site
from bs4 import BeautifulSoup #to parse and sort html information
import pandas as pd # parsing data and creating dataframes
import os
import openpyxl

workingDir="/Users/joseph/Desktop/WSWC/IoW/Vocabularies/WA/"
os.chdir(workingDir)


#Retrieving html Information
############################################################################
result = requests.get("https://www.epermitting.wa.gov/site/alias__resourcecenter/2485/default.aspx")  #linking to website and creating source.
html = result.content  # store the page content
soup = BeautifulSoup(html, 'lxml')  #create a beautifulSoup obect based on the source variable.


#Storage Variables
############################################################################
lst1 = []
lst2 = []
lst3 = []
li_tag = ""
mit = 'Mitigation'


#Gathering Data
###########################################################################
if result.status_code == 200:  # a valuve of 200 indicates yes, a 403 forbidden means no.
    print("Success. Website is accessible.")

    neededclass = soup.find(class_ = "zen-main")  # ID-WRB specific. Finding all 'tr' tag items within tr tags to seperate term from
                                                    # definition.
    for p in neededclass.find_all('p'):
        lst1.append(p.text)


    for strong in neededclass.find_all('strong'):
        lst2.append(strong.text)
        #lst2.append(term.text)
        #definition = p.find('br')
        #lst2.append(definition.text)

    glossary = pd.DataFrame(lst1)
    terms = pd.DataFrame(lst2)


    # Cleaning Text
    ############################################################################
    print("Cleaning text.")
    # ID DEQ Specific.

    # remove first row
    glossary.drop([28, 40, 50, 57, 58, 59], inplace=True)
    glossary.reset_index(inplace=True)

    glossary = pd.merge(left=terms, right=glossary, left_index=True, right_index=True)
    glossary.rename(columns={'0_x': 'Term', '0_y': 'Definition'}, inplace=True)  # rename columns to match Template

    for i, row in glossary.iterrows():
        x = row['Term']
        y = row['Definition']
        glossary.at[i, 'Definition'] = y.replace(x, "")

    glossary.drop(['index'], axis=1, inplace=True)
    glossary.set_index('Term', inplace=True)


    # manually add lists to csv as 'mitigation' and 'NEPA' contain lists in a seperate tag.


    # Exporting Text to xlsx file.
    ############################################################################
    print("Exporting data to xlsx.")

    #export DataFrame to xlsx

    glossary.to_excel('wa-epermit-g-export.xlsx')



else:
    print("Error. Website is not accessible.")


print("Code Complete.")