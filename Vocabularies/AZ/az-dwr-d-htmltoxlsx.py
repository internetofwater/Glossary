#Date Created: 11/13/2019
#Purpose: To extract text from html file (website) and export to xlsx file.
#Notes: # AZ Department of Water Resources Glossary Information.
        # AZDWR Specific. Glossary Info spread out throughout 8 webpages, will need to exract each one individually and append to same list.


#Needed Modules
############################################################################
import requests #to pull info from an html site
from bs4 import BeautifulSoup #to parse and sort html information
import pandas as pd # parsing data and creating dataframes


#Storage Variables
############################################################################
lst1 = []  # empty list
lst1a = []  # empty list for term name
lst1b = []  # empty list for term abbreviation
lst2 = []  # empty list for term def


#Gathering Data
############################################################################

######### Source #1 #########
result = requests.get("https://new.azwater.gov/dictionary?field_term_definitions_tid=All")  # get the source info
html = result.content  # store the page content
soup = BeautifulSoup(html, 'html.parser')  # create a beautifulSoup object based on the stored source variable.

if result.status_code == 200:  # Checking website info accessibility. A value of 200 indicates yes, a 403 forbidden means no.
    print("Success. Source Website #1 is accessible.")

    s1 = ''  # empty string
    s2 = ''  # empty string
    neededclass = soup.find(class_="view-content")  # AZ-DWR specific. Cuts down search with those items that have this specific class.

    for h3_tag in neededclass.find_all('h3'):  # AZ-DWR specific. Term Name and Abbreviation info has 'h3' tags.
        s1 = h3_tag.text  # removes the tag, returns the texts only.
        lst1.append(s1.strip())  # append empty list with findings. Strip excess white space.

    for p_tag in neededclass.find_all('p'):  # AZ-DWR specific. Term Definition info has 'p' tags.
        s2 = p_tag.text  # removes the tag, returns the texts only.
        lst2.append(s2.strip())  # append empty list with findings. Strip excess white space.

else:
    print("Error. Website is not accessible.")


######### Source #2 #########
result = requests.get("https://new.azwater.gov/dictionary?page=1")
html = result.content
soup = BeautifulSoup(html, 'html.parser')

if result.status_code == 200:
    print("Success. Source Website #2 is accessible.")

    s1 = ''
    s2 = ''
    neededclass = soup.find(class_="view-content")

    for h3_tag in neededclass.find_all('h3'):
        s1 = h3_tag.text
        lst1.append(s1.strip())

    for p_tag in neededclass.find_all('p'):
        s2 = p_tag.text
        lst2.append(s2.strip())

else:
    print("Error.  Website is not accessible.")


######### Source #3 #########
result = requests.get("https://new.azwater.gov/dictionary?page=2")
html = result.content
soup = BeautifulSoup(html, 'html.parser')

if result.status_code == 200:
    print("Success. Source Website #3 is accessible.")

    s1 = ''
    s2 = ''
    neededclass = soup.find(class_="view-content")

    for h3_tag in neededclass.find_all('h3'):
        s1 = h3_tag.text
        lst1.append(s1.strip())

    for p_tag in neededclass.find_all('p'):
        s2 = p_tag.text
        lst2.append(s2.strip())

else:
    print("Error. Website is not accessible.")


######### Source #4 #########
result = requests.get("https://new.azwater.gov/dictionary?page=3")
html = result.content
soup = BeautifulSoup(html, 'html.parser')

if result.status_code == 200:
    print("Success. Source Website #4 is accessible.")

    s1 = ''
    s2 = ''
    neededclass = soup.find(class_="view-content")

    for h3_tag in neededclass.find_all('h3'):
        s1 = h3_tag.text
        lst1.append(s1.strip())  #

    for p_tag in neededclass.find_all('p'):
        s2 = p_tag.text
        lst2.append(s2.strip())

else:
    print("Error. Website is not accessible.")


######### Source #5 #########
result = requests.get("https://new.azwater.gov/dictionary?page=4")
html = result.content
soup = BeautifulSoup(html, 'html.parser')

if result.status_code == 200:
    print("Success. Source Website #5 is accessible.")

    s1 = ''
    s2 = ''
    neededclass = soup.find(class_="view-content")

    for h3_tag in neededclass.find_all('h3'):
        s1 = h3_tag.text
        lst1.append(s1.strip())

    for p_tag in neededclass.find_all('p'):
        s2 = p_tag.text
        lst2.append(s2.strip())

else:
    print("Error. Website is not accessible.")


######### Source #6 #########
result = requests.get("https://new.azwater.gov/dictionary?page=5")
html = result.content
soup = BeautifulSoup(html, 'html.parser')

if result.status_code == 200:
    print("Success. Source Website #6 is accessible.")

    s1 = ''
    s2 = ''
    neededclass = soup.find(class_="view-content")

    for h3_tag in neededclass.find_all('h3'):
        s1 = h3_tag.text
        lst1.append(s1.strip())

    for p_tag in neededclass.find_all('p'):
        s2 = p_tag.text
        lst2.append(s2.strip())

else:
    print("Error. Website is not accessible.")


######### Source #7 #########
result = requests.get("https://new.azwater.gov/dictionary?page=6")
html = result.content
soup = BeautifulSoup(html, 'html.parser')

if result.status_code == 200:
    print("Success. Source Website #7 is accessible.")

    s1 = ''  # empty string
    s2 = ''  # empty string
    neededclass = soup.find(class_="view-content")

    for h3_tag in neededclass.find_all('h3'):
        s1 = h3_tag.text
        lst1.append(s1.strip())

    for p_tag in neededclass.find_all('p'):
        s2 = p_tag.text
        lst2.append(s2.strip())

else:
    print("Error. Website is not accessible.")


######### Source #8 #########
result = requests.get("https://new.azwater.gov/dictionary?page=7")
html = result.content
soup = BeautifulSoup(html, 'html.parser')

if result.status_code == 200:
    print("Success. Source Website #8 is accessible.")

    s1 = ''
    s2 = ''
    neededclass = soup.find(class_="view-content")

    for h3_tag in neededclass.find_all('h3'):  # change tag information here
        s1 = h3_tag.text
        lst1.append(s1.strip())

    for p_tag in neededclass.find_all('p'):
        s2 = p_tag.text
        lst2.append(s2.strip())

else:
    print("Error. Website is not accessible.")



#Cleaning Text
############################################################################
print("Cleaning text.")

#AZDWR Specific.

# Seperating out Term Name from Term Abbreviation into seperate lists.
# Search for items in '( )', split out.  If no, fill with blank.
for i in lst1:
    if '(' in i:
        lst1a.append(i.split('(')[0].title())  #Term Name
        lst1b.append(i[i.find("(") + 1:i.find(")")])  #Term Abbreviation
    else:
        lst1a.append(i.title())  #Term Name
        lst1b.append("")  #Term Abbreviation

# Checking and adding missing '.' at end of the definition list.
for i, s in enumerate(lst2):
    if str(s).endswith("."):
        lst2[i] = s
    else:
        lst2[i] = s + "."

# Checking and capitalizing the first character of the definition list.
for i, s in enumerate(lst2):
    if s[0].isupper():
        lst2[i] = s
    else:
        lst2[i] = s.capitalize()



#Exporting Text to xlsx file.
############################################################################
print("Exporting data to xlsx.")

# Create DataFrames from available lists.
df1 = pd.DataFrame(lst1a)  #Term Name
df2 = pd.DataFrame(lst1b)  #Term Abbreviation
df3 = pd.DataFrame(lst2)  #Term Definition

# Export DataFrames to xlsx.
with pd.ExcelWriter('Arizona Department of Water Resources Dictionary.xlsx') as writer:  # Name of xlsx file.  #AZDWR Specific.
    df1.to_excel(writer, sheet_name='termname')
    df2.to_excel(writer, sheet_name='terabbr')
    df3.to_excel(writer, sheet_name='termdef')


print("Code complete.")
