#Date Created: 10/28/2019
#Purpose: To extract text from html file (website) and export to xlsx file.
#Notes: # UDWQ glossary.
        # Easier to grab specific text, then split name and definition information into two separate lists.


#Needed Modules
############################################################################
import requests #to pull info from an html site
from bs4 import BeautifulSoup #to parse and sort html information
import pandas as pd # parsing data and creating dataframes


#Retrieving html Information
############################################################################
result = requests.get("https://deq.utah.gov/water-quality/glossary-utah-ground-water-quality-protection-program#Pollutant")  #linking to website and creating source.
html = result.content  # store the page content
soup = BeautifulSoup(html, 'html.parser')  #create a beautifulSoup obect based on the source variable.


#Storage Variables
############################################################################
s1 = ''  # empty string
lst1 = []  # empty list for all text storage
lst2 = []  # empty list for term name storage
lst3 = []  # empty list for term def storage


#Gathering Data
###########################################################################
if result.status_code == 200:  # a valuve of 200 indicates yes, a 403 forbidden means no.
    print("Success. Website is accessible.")

    neededclass = soup.find(class_="entry-content")  # UDWQ specific. Finding all 'li' tag items only within the class_"entry-content"
    for li_tag in neededclass.find_all('li'):  # change tag information here
        s1 = li_tag.text  # removes the tag, returns the texts only.
        lst1.append(s1)  # append empty list with findings


    # Cleaning Text
    ############################################################################
    print("Cleaning text.")
    # UDWQ Specific.
        # Skipping N/A Elements.
        # Seperating out Term Name from Term Definitions.

    for i in lst1:
        if 'N/A' in i:  #UDWQ glossary specific
            continue
        if "\n" in i:  #UDWQ glossary specific
            lst2.append(i.split("\n")[0])  # index 0 is the term name
            lst3.append(i.split("\n")[1])  # index 1 is the term def
        else:  # If not noted, just append to list. Will fix by hand in excel later.
            lst2.append(i)
            lst3.append(i)


    # Exporting Text to xlsx file.
    ############################################################################
    print("Exporting data to xlsx.")

    # Create DataFrame from available list.
    df1 = pd.DataFrame(lst2)
    df2 = pd.DataFrame(lst3)

    #export DataFrames to xlsx
    with pd.ExcelWriter('Utah Water Quality Terms and Defs.xlsx') as writer:  #Name of xlsx file.
        df1.to_excel(writer, sheet_name='termname')
        df2.to_excel(writer, sheet_name='termdef')


else:
    print("Error. Website is not accessible.")


print("Code Complete.")