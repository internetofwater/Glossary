# Date Created: 11/18/2019
# Purpose: To extract text from a PDF files retrieve online.
# Notes: # California Water Board
        # Glossary info comes only in PDF format in 26 separate URLs.  Will need to turn pdf's into workable object, then do text extraction.
        # .split("  ") is not perfect here, some items only have 1 space " " separating out name from def.  Will require some manual changes.


# Needed Modules
###########################################################################
import requests  # to pull info from an html site
import io
import PyPDF2 as p2  # to read and handle PDF information
import pandas as pd  # parsing data and creating DataFrames
from string import ascii_lowercase  # to iterate through an alphabetical list


# Storage Variables
############################################################################
list0b = []  # empty list
list1 = []  # empty list for term name
list2 = []  # empty list for term abbreviation
list3 = []  # empty list for term def


# Retrieving HTML PDF Information
############################################################################
for c in ascii_lowercase:  # iterate through an alphabetical list, lower case

    text = "https://www.waterboards.ca.gov/publications_forms/available_documents/water_words/words_" + c + ".pdf"  # html site URL
    r = requests.get(text)  #linking to website and creating source.
    if r.status_code == 200:  # a value of 200 indicates yes, a 403 forbidden means no.
        print(f"Success. Website {c} is accessible.")
        f = io.BytesIO(r.content)  # creating and wrapping byte stream object
        pdfread = p2.PdfFileReader(f)  # reading object

        # Temporary Storage Variables. Will reset with each iteration. Full storage to append to list.
        ############################################################################
        list0 = []  # empty list
        x = 0  # counter for numeric iteration
        pagetext = ''  # empty string
        alltext = ''   # empty string

        # Gathering Data
        ###########################################################################
        while x < pdfread.getNumPages():  # while num is less than the number of pages
            pageinfo = pdfread.getPage(x)  # save pdf page as object
            pagetext = pageinfo.extractText().replace('\n', '').replace('\r', '')  # extract text from pdf object. Remove new lines and tabs.
            alltext = alltext + pagetext  # concatenate text from all pdf pages into one string a storage string for later use
            x = x + 1  # advance counter

        list0 = alltext.split("  ")  # create list from string
        list0b = list0b + list0  # concatenate list later use

    else:  # A value of 200 indicates yes, a 403 forbidden means no.
        print(f"Error. Website {c} is not accessible.")


# Cleaning Text
############################################################################
print("Cleaning text.")

# Creating combined name&abbr list1 and TermDef list3.
# Search name and def divider char, separate using indexing.
for i in list0b:
    if ":" in i:  # AZ glossary specific
        list1.append(i.split(":")[0].title().strip())  # index 0 is the term name
        list3.append(i.split(":")[1].strip())  # index 1 is the term def
    else:  # If not noted, just append to list. Will fix by hand in excel later.
        continue

# Creating Term Name list1 and Abbreviation list2.
# Search for items in '( )', split out.  If no, fill with blank.
for i, s in enumerate(list1):
    if "(" in s:
        list1[i] = s.split("(")[0].title().strip()  # Term Name. Capitalize first char of each word.
        list2.append(s[s.find("(") + 1:s.find(")")].upper())  # Term Abbreviation. Make all upper case.
    else:
        list1[i] = s.title().strip()
        list2.append("")

# Clean Term Def lst3.
# Checking and adding missing '.' at end of the definition string.
for i, s in enumerate(list3):
    if str(s).endswith("."):
        list3[i] = s  # do nothing
    else:
        list3[i] = s + "."  # add .
# Checking and capitalizing the first character of the definition string.
for i, s in enumerate(list3):
    if s[0].isupper():
        list3[i] = s  # do nothing
    else:
        list3[i] = s.capitalize()  # capitalize first char


# Exporting Text to xlsx file
############################################################################
print("Exporting data to xlsx.")

# Create DataFrame from available list.
df0 = pd.DataFrame(list0b)  # All text
df1 = pd.DataFrame(list1)  # Term Name
df2 = pd.DataFrame(list2)  # Term Abbreviation
df3 = pd.DataFrame(list3)  # Term Definition

# Export DataFrames to xlsx
with pd.ExcelWriter('CAL Glossary.xlsx') as writer:  # Name of xlsx file.
    df0.to_excel(writer, sheet_name='alltext')
    df1.to_excel(writer, sheet_name='termname')
    df2.to_excel(writer, sheet_name='terabbr')
    df3.to_excel(writer, sheet_name='termdef')