#Date Created: 12/22/2019
#Purpose: To extract text from html file (website) and export to xlsx file.
#Notes: # IDDWR glossary.



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
result = requests.get("https://idwr.idaho.gov/terminology.html")  #linking to website and creating source.
html = result.content  # store the page content
soup = BeautifulSoup(html, 'html.parser')  #create a beautifulSoup obect based on the source variable.


#Storage Variables
############################################################################
terminology = pd.DataFrame(columns=['Term', 'Definition'])


#Gathering Data
###########################################################################
if result.status_code == 200:  # a valuve of 200 indicates yes, a 403 forbidden means no.
    print("Success. Website is accessible.")

    neededclass = soup.find('tbody')  # ID-WRB specific. Finding all 'tr' tag items within tr tags to seperate term from
                                      # definition.
    for tr in neededclass.find_all('tr'):
        i = 0
        for td in tr.find_all('td'):
            i = i + 1
            x = td.text
            print('success')
            if i == 1:
               terminology = terminology.append({'Term':x}, ignore_index= True)
            else:
                terminology = terminology.append({'Definition': x}, ignore_index=True)

    terminology['Definition'] = terminology['Definition'].shift(-1)
    terminology.dropna(inplace=True)


    # Cleaning Text
    ############################################################################
    print("Cleaning text.")
    # ID DWR Specific.

    # replace two definitions to remove inset figure text
    terminology.set_index('Term', inplace=True)
    terminology.at[
        'Exceedence', 'Definition'] = 'Exceedence is a method describing the percentage of time for which an observed stream flow is greater than or equal to a defined stream flow. Exceedence is used when stream flow data are not normally distributed (such as on a bell-shaped curve). Most streams flows are not normally distributed because high flow events can skew the data making the mean flow greater than the median flow. Low-flow events have high exceedence percentages because, generally, observed flows exceed the low flow. High-flow events have low exceedence percentages because most observed flows are lower than the high-flow levels.'
    terminology.at[
        'Public Land Survey System (PLSS)', 'Definition'] = 'The PLSS is used to describe and divide land in many states in the US. In Idaho, the initial point of the PLSS is near Kuna. From this point, the land is divided into 6×6-mile townships—which are further subdivided into 36 1×1-mile sections containing 640 acres each. One section can be subdivided into quarters which are 160 acres each, and which can be further subdivided into quarter quarters of 40 acres each. Each township is tied to the initial point and is identified by how many townships north or south as well as by how many ranges east or west they are from the initial point.'

    # Exporting Text to xlsx file.
    ############################################################################
    print("Exporting data to xlsx.")

    #export DataFrame to xlsx

    terminology.to_excel('id-dwr-t-export.xlsx')



else:
    print("Error. Website is not accessible.")


print("Code Complete.")