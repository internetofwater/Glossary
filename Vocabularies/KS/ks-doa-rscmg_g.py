# Title: Kansas - Department of Agriculture - River and Stream Corridor Management Guide Glossary
# Created by: Joseph Brewer, WSWC
# Date Created: 05/20/2020
# Purpose: To extract text from html file (website) and export to xlsx file.
# Notes:


#Needed Modules
############################################################################
from docx import *
import os
import pandas as pd
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows

workingDir="/Users/augustus/Desktop/WSWC/IoW/Vocabularies/KS/"
os.chdir(workingDir)


#Retrieving Document
############################################################################
document = Document('ks-doa-rscmg_g.docx')


#Storage Variables
############################################################################
# Create empty dataframes
data = pd.DataFrame(columns=['glossary'])
glossary = pd.DataFrame(columns=['Term', 'Definition'])


#Gathering Data
###########################################################################
# Iterate over paragraghs.  Paragraphs seperated by columns
for para in document.paragraphs:
    data = data.append({'glossary':para.text}, ignore_index=True) # Append text to data DataFrame



# Iterate over rows in data DataFrame and split on ' – '
for i, row in data.iterrows():
    x = row['glossary'].split(' – ')
    if len(x) == 2:
        glossary = glossary.append({'Term':x[0], 'Definition':x[1]}, ignore_index=True) # Append split values to glossary dataframe
                                                                                        # with positional arguments
    else:
        print(x)


# Cleaning Text
############################################################################
# Strip leading and trailing whitespace
stripped = pd.Series(glossary['Term'].values)  # Convert Keyword column to Pandas Series
stripped = stripped.str.strip() # Use Series.str.strip() to strip leading/trailing whitespace
#stripped = stripped.str.capitalize() # Use Series.str.capitalize to capitalize first character of string
glossary = glossary.assign(Term=stripped)

stripped = pd.Series(glossary['Definition'].values)
stripped = stripped.str.strip()
#stripped = stripped.str.capitalize()
glossary = glossary.assign(Definition=stripped)


# Exporting Text to xlsx file.
############################################################################
print("Exporting data to xlsx.")


#export DataFrame to xlsx
glossary.to_excel('ks-doa-rscmg_g_EXPORT.xlsx')  #ToDo: un-comment to run again


print('done')

