#Date Created: 03/25/2020
#Purpose: To extract text from html file (website) and export to xlsx file.
#Notes: # MT DNRC State Water Plan glossary.


#Needed Modules
############################################################################
from docx import *
import os
import pandas as pd

workingDir="/Users/augustus/Desktop/WSWC/IoW/Vocabularies/MT/"
os.chdir(workingDir)


#Retrieving Document
############################################################################
document = Document('2015_mt-water-plan.docx')


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

data.drop(72, inplace=True)

# Iterate over rows in data DataFrame and split on ' – '
for i, row in data.iterrows():
    x = row['glossary'].split(' – ')
    glossary = glossary.append({'Term':x[0], 'Definition':x[1]}, ignore_index=True) # Append split values to glossary dataframe
                                                                                    # with positional arguments

# Cleaning Text
############################################################################
# Strip leading and trailing whitespace
stripped = pd.Series(glossary['Term'].values)  # Convert Keyword column to Pandas Series
stripped = stripped.str.strip()  # Use Series.str.strip() to strip leading and trailing whitespace
glossary = glossary.assign(Term=stripped)

stripped = pd.Series(glossary['Definition'].values)
stripped = stripped.str.strip()
glossary = glossary.assign(Definition=stripped)


# Exporting Text to xlsx file.
############################################################################
print("Exporting data to xlsx.")

#export DataFrame to xlsx

glossary.to_excel('mt-dnrc-g.xlsx')



print('done')

