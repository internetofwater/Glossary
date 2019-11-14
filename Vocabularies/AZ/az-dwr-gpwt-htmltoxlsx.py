#Date Created: 11/14/2019
#Purpose: To extract text from html file (website) and export to xlsx file.
#Notes: # Arizona Department of Water Resrouces Groundwater Permitting and Wells Terminology.
        # ADWR-GWPWT Specific.  Term names have tag of h3 only, term def needed a class search.
        # Gather text. Separate text into name&Abbr and def lists.  Separate name&Abbr into name and Abbr lists.


#Needed Modules
############################################################################
import requests  #to pull info from an html site
from bs4 import BeautifulSoup  #to parse and sort html information
import pandas as pd  # parsing data and creating dataframes


#Retrieving html Information
############################################################################
result = requests.get("https://new.azwater.gov/permitting-wells/terminology")  #linking to website and creating source.
html = result.content #store the page content
soup = BeautifulSoup(html, 'html.parser') #create a beautifulSoup obect based on the source variable.


#Storage Variables
############################################################################
s1 = ''  # empty string
s2 = ''  # empty string
lst0 = []  # empty list
lst1 = []  # empty list for term name
lst2 = []  # empty list for term abbreviation
lst3 = []  # empty list for term def


#Gathering Data
###########################################################################
if result.status_code == 200:  #a valuve of 200 indicates yes, a 403 forbidden means no.
    print("Success. Website is accessible.")

    for h3_tag in soup.find_all('h3'):  # ADWR-GWPWT specific. Term Name and Abbreviation info has 'h3' tags only.
        s1 = h3_tag.text  # removes the tag, returns the texts only.
        lst1.append(s1.strip())  # append empty list with findings. Strip excess white space.

    for div_tag in soup.find_all('div', class_="accordion-content"):  # ADWR-GWPWT specific. Term Definition info has 'div' tags, narrow search to those with accordion-content class.
        s2 = div_tag.text  # removes the tag, returns the texts only.
        lst3.append(s2.strip())  # append empty list with findings. Strip excess white space.


    # Cleaning Text
    ############################################################################
    print("Cleaning text.")

    # ADWR-GWPWT Specific.

    # # Creating Term Name lst1 and Abbreviation lst2.
    # # Search for items in '( )', split out.  If no, fill with blank.
    for i, s in enumerate(lst1):
        if '(' in s:
            lst1[i] = s.split('(')[0].title()  # Term Name. Capitalize first char of each word.
            lst2.append(s[s.find("(") + 1:s.find(")")].upper())  # Term Abbreviation.  Make all upper case.
        else:
            lst1[i] = s.title()
            lst2.append("")

    # Clean Term Def lst3.
    # Checking and adding missing '.' at end of the definition string.
    for i, s in enumerate(lst3):
        if str(s).endswith("."):
            lst3[i] = s  # do nothing
        else:
            lst3[i] = s + "."  # add .
    # Checking and capitalizing the first character of the definition string.
    for i, s in enumerate(lst3):
        if s[0].isupper():
            lst3[i] = s  # do nothing
        else:
            lst3[i] = s.capitalize()  # capitalize first char


    # Exporting Text to xlsx file.
    ############################################################################
    print("Exporting data to xlsx.")

    # Create DataFrame from available list.
    df0 = pd.DataFrame(lst0)  # All text
    df1 = pd.DataFrame(lst1)  # Term Name
    df2 = pd.DataFrame(lst2)  # Term Abbreviation
    df3 = pd.DataFrame(lst3)  # Term Definition

    #Export DataFrames to xlsx
    with pd.ExcelWriter('ADWR Groundwater Permitting Wells Terminology.xlsx') as writer:  #Name of xlsx file.
        df0.to_excel(writer, sheet_name='alltext')
        df1.to_excel(writer, sheet_name='termname')
        df2.to_excel(writer, sheet_name='terabbr')
        df3.to_excel(writer, sheet_name='termdef')


else:  #A valuve of 200 indicates yes, a 403 forbidden means no.
    print("Error.  Website is not accessible.")


print("Code Complete.")