# IOW Glossary Text Extraction Technique Description

This ReadME details the process of gathering and processing glossary term and definition data.  Please note, all glossary information is needed. The information given here is for glossary info that is publicly available online and accessible via html format.  If glossary info is not available in html format (e.g. pdf, inaccessible, etc), we still need that glossary info and users will have to use an alterative text extraction technique other than the one outlined here within this ReadME file.



## Good and Bad HTML Accessible Glossary Information
Good and bad examples of available html glossary information.  

Good example: Html webpage information available online: https://deq.utah.gov/water-quality/glossary-utah-ground-water-quality-protection-program

Bad example: Html webpage information online but not accessible (text extraction is forbidden).  Will need alternative text extraction approach: https://www.coloradoriverdistrict.org/water-glossary/

Bad example: No html webpage information online.  Will need to seek alternative text extraction approach: http://water.nv.gov/programs/planning/dictionary/wwords-A.pdf



## Text Extraction Steps

### Step 1: Locate State Institution Glossary
Locate online state agency available glossary term and definition information.  If available in html format, continue to step-2.  If not, skip to step-4 and seek alternative text extraction process.

### Step 2: Located text Tags
Right click + inspect webpage.  Scroll through window.  Located item of interest and note the following...
- **item tag (typically in purple text) (e.g. ‘p’, ‘strong’, ‘dt, etc).**
- **item class tag if available (typically in orange text.  Will help narrow down search on text extract with items that may share the same tag).**

### 3: Craft Agency Specific Text Extraction Python File
Update and craft .py file that will meet the specific challenges of the webpage in order to extract the appropriate text.

Fill out Notes at top of each .py file.

Within the ‘Retrieving html Information’ subsection, copy & Paste UWRL as ‘result’ variable.

Within the ‘#Gathering Data’ subsection, fill in the following…
- **Set ‘needed class’ variable to class tag available.  If not set to ‘soup’.**
- **Within for loop, set text search for specific tag of item of interests.**

Within the ‘Cleaning Text’ subsection, create any text cleaning python scripts if needed / wanted.

Within ‘Exporting Text to xlsx file; subsection, change xlsx file name to be specific to that glossary and state agency (e.g. ‘UDWR Glossary.xlsx’, etc).

Run code.

### 4: Copy / Update Template.xlsx Information
Copy information over into ‘Template.xlsx’ file, located at https://github.com/internetofwater/Glossary.

Name to ‘Term Name’ column.

If available / given, term abbreviation to “Abbreviation’ column.

Definition to ‘Definition’ column.

Manually select and fill out entries for ‘Theme 1 – 5’ columns.  Choose theme that best matches the given state term definition.  Terms may have a max of 5 theme tags, and a minimum of 1.

Theme Definitions:
- **Data: Terms about specific parameters, units, and data production and dissemination**
- **Water Use: Terms about water that is withdrawn for a specific purpose, including end uses and rights/allocations**
- **Hydrology: Terms about the properties, distribution and circulation of water and snow in the natural system**
- **Legal and Regulatory: Terms about laws and regulations governing water, including quantity, quality, use, rights, and planning**
- **Water Quality: Terms about drinking or environmental water chemical, physical, and biological characteristics, their measurement and management**
- **Environment and Ecology: Terms about conditions and influences affecting the life and development of organisms and relationships between organisms**
- **Infrastructure: Terms about the built environment**
- **Utilities: Terms about entities providing drinking water, wastewater removal, and stormwater management services and the regulation thereof**

Rename Template.xlsx file to a suitable concatenation of agency and vocabulary (e.g. ut-udwq-g for 'Utah Department of Water Quality Glossary).

### 5: Push Files to GitHub Repository
Push agency.xlsx file and text extract .py file to an appropriate organization-level folder in the 'Vocabularies' folder in this repository.

### 6: Update Assignment.xlsw sheet
Fill in State Agency Assignments.xlsx file at https://github.com/internetofwater/Glossary/tree/master/Vocabularies.
- **‘Assigned to…’ column with your name.**
- **‘Agency & State’ column with name of agency.xlsx file from previous step.**
- **Completed?’ column with Yes or No.**
- **‘URL’ with link to source information.**

