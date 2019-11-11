#Date Created: 10/29/2019
#Purpose: To extract text from html file (website) and export to xlsx file.
#Notes: # WY glossary has poor selection of tags to use
        # have to save combined terms and defintions as a string first, then split into a list


#Needed Modules
import requests #to pull info from an html site
from bs4 import BeautifulSoup #to parse and sort html information
import pandas as pd # parsing data and creating dataframes

#linking to website and creating source.
result = requests.get("http://library.wrds.uwyo.edu/glossary/wrs/wrs01/wrs01-wqt.html")

#use BeautifulSoup to parse and process the source.
html = result.content #store the page content
soup = BeautifulSoup(html, 'html.parser') #create a beautifulSoup obect based on the source variable.


############################################################################
if result.status_code == 200:  #a valuve of 200 indicates yes, a 403 forbidden means no.
############################################################################
    print("Success. Website is accessible.")

    s1 = ''  # empty string
    lst0 = []   # empty list for text storage
    lst1 = []   # empty list for text storage
    lst2 = []   # empty list for term name storage
    lst3 = []   # empty list for term def storage


    for pre_tag in soup.find_all('pre'):
        s1 = pre_tag.text

    lst0 = s1.split('\n\n')

    for i in lst0:  #WY glossary specific. Cleaning text.
        if '\n         ' in i:
            lst1.append(i.replace('\n         ', ' '))
        else:
            continue

    for i in lst1:
        if '* * *' in i:  #WY glossary specific
            continue
        if ' - ' in i:    #WY glossary specific
            lst2.append(i.split(' - ')[0].title())  #index 0 is the term name
            lst3.append(i.split(' - ')[1])  #index 1 is the term def
        else:             #If not noted, just append to list.  Will fix by hand in excel later.
            lst2.append(i)
            lst3.append(i)

    # Create DataFrame from available list.
    df1 = pd.DataFrame(lst1)
    df2 = pd.DataFrame(lst2)
    df3 = pd.DataFrame(lst3)

    print("Exporting data to xlsx.")
    #export DataFrames to xlsx
    with pd.ExcelWriter('Wyoming Water Quality Terms and Defs.xlsx') as writer:  #Name of xlsx file.
        df1.to_excel(writer, sheet_name='text')
        df2.to_excel(writer, sheet_name='termname')
        df3.to_excel(writer, sheet_name='termdef')


############################################################################
else:  #a valuve of 200 indicates yes, a 403 forbidden means no.
############################################################################
    print("Error.  Website is not accessible.")



print("Code Complete.")