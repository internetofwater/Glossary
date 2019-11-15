# IOW Glossary Text Extraction Technique Description

The Internet of Water (IOW) Glossary project aims to produce a vocabulary management system where terms are ingested into a [SKOS](https://www.w3.org/2004/02/skos/)-compliant RDF, and semantic links (skos:related and skos:exactMatch) are drawn between terms.  This is accomplished by collecting water use terms and their definition as used by US federal and state agencies.  Results can be viewed using a shiny app hosted by RStudio's free cloud hosting service here: https://internetofwater.shinyapps.io/Glossary/#section-main-term-browser

This ReadME details the process of gathering and processing glossary term and definition data.  Please note, all glossary information is needed.  The information given here is for glossary info that is publicly available online and accessible via html format.  If glossary info is not available in html format (e.g. pdf, inaccessible, etc), we still need that glossary info and users will have to use an alterative text extraction technique other than the one outlined here within this ReadME file.

This ReadME will use the Utah Division of Water Quality as a good html example.
- source info: https://deq.utah.gov/water-quality/glossary-utah-ground-water-quality-protection-program
- completed files found at: https://github.com/internetofwater/Glossary/tree/master/Vocabularies/UT
- completed py file for text extraction: ut-udwq-hg-htmltoxlsx.py
- completed IOW xlsx file: ut-udwq-g.xlsx

## Good and Bad HTML Accessible Glossary Information
Good and bad examples of available html glossary information.  

Good example: Html webpage information available online: https://deq.utah.gov/water-quality/glossary-utah-ground-water-quality-protection-program

Bad example: Html webpage information online but not accessible (text extraction is forbidden).  Will need alternative text extraction approach: https://www.coloradoriverdistrict.org/water-glossary/

Bad example: No html webpage information online.  Will need to seek alternative text extraction approach: http://water.nv.gov/programs/planning/dictionary/wwords-A.pdf



## Text Extraction Steps

### Step 1: Locate State Institution Glossary
Locate online state agency available glossary term and definition information.  If available in html format, continue to step-2.  If not, skip to step-4 and seek alternative text extraction process.

### Step 2: Update Assignment Table
Please fill in the in below State Agency Assignments table (Step 7) to help coordinate assignments and glossary progress.
- **‘Assigned to…’ column with your name.**
- **‘Agency & State’ column with name of agency.xlsx file from previous step.**
- **Completed?’ column with Yes or No.**
- **‘URL’ with link to source information.**

### Step 3: Located text Tags
Right click + inspect webpage.  Scroll through window.  Located item of interest and note the following...
- **item tag (typically in purple text) (e.g. ‘p’, ‘strong’, ‘dt, etc).**
- **item class tag if available (typically in orange text.  Will help narrow down search on text extract with items that may share the same tag).**

### Step 4: Craft Agency Specific Text Extraction Python File
Note: each source webpage is unique and will most likely require a new / different approach.  Be aware of the challenges each source webpage will require.  The text extraction technique outlined here is one such approach, but others are also acceptable.


Update and craft py file that will meet the specific challenges of the webpage in order to extract the appropriate text.

Fill out Notes at top of each .py file.

Within the ‘Retrieving html Information’ subsection, copy & Paste UWRL as ‘result’ variable.

Within the ‘Gathering Data’ subsection, fill in the following…
- **Set ‘needed class’ variable to class tag available.  If not set to ‘soup’.**
- **Within for loop, set text search for specific tag of item of interests.**

Within the ‘Cleaning Text’ subsection, create any text cleaning python scripts if needed / wanted.

Within ‘Exporting Text to xlsx file' subsection, change xlsx file name to be specific to that glossary and state agency (e.g. ‘UDWR Glossary.xlsx’, etc).

Run code.

### Step 5: Copy / Update Template.xlsx Information
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

### Step 6: Push Files to GitHub Repository
Push agency.xlsx file and text extract .py file to an appropriate organization-level folder in the 'Vocabularies' folder in this repository.

### Step 7: Update Assignment Table Again
Please update the below State Agency Assignments table that your assignment is complete.
- **‘Assigned to…’ column with your name.**
- **‘Agency & State’ column with name of agency.xlsx file from previous step.**
- **Completed?’ column with Yes or No.**
- **‘URL’ with link to source information.**

| Assinged to | State | Agency      | Completed? |                           URL?                                  |
|    :---:    | :---: |  :---:      |    :---:   |                           :---                                  |
| Ryan James  | ASCE  | asce-et-g   | Yes        | https://ascelibrary.org/doi/pdf/10.1061/9780784408056.bm |
| Ryan James  | AZ    | az-deq      | Yes        | https://legacy.azdeq.gov/function/help/glossary.html |
| Ryan James  | AZ    | az-dwr      | Yes        | https://new.azwater.gov/dictionary  |
| Ryan James  | AZ    | az-dwr-gpw  | Yes        | https://new.azwater.gov/permitting-wells/terminology |
| Ryan James  | CO    | co-cdr-g    | Yes        | https://www.coloradoriverdistrict.org/water-glossary/ |
| Ryan James  | NM    | nm-wrap-g   | Yes        | https://www.ose.state.nm.us/WR/glossary.php |
| Ryan James  | UT    | ut-udwq-g   | Yes        | https://deq.utah.gov/water-quality/glossary-utah-ground-water-quality-protection-program |
| Ryan James  | UT    | ut-udwr-g   | Yes        | https://waterrights.utah.gov/wrinfo/glossary.asp |
| Ryan James  | WY    | wy-wrri-hg  | Yes        | http://library.wrds.uwyo.edu/glossary/wrs/wrs01/wrs01-ht.html |
| Ryan James  | WY    | wy-wrri-wqg | Yes        | http://library.wrds.uwyo.edu/glossary/wrs/wrs01/wrs01-wqt.html |
| Ryan James  | ID    | id-dwr-wrg  | Yes        | https://idwr.idaho.gov/water-rights/overview.html |
|             |       |	            | No         | https://www.owrb.ok.gov/util/glossary.php |
|             |       |	            | No         | https://idwr.idaho.gov/terminology.html |
|             |       |	            | No	       | https://www.oregon.gov/owrd/WRDFormsPDF/wris_code_key.pdf |
|             |       |	            | No	       | https://secure.sos.state.or.us/oard/displayDivisionRules.action?selectedDivision=3174 |
|             |       |	            | No	       | https://www.thefreshwatertrust.org/glossary-of-terms/ |
|             |       |	            | No	       | https://oregonexplorer.info/content/glossary-wetlands-terms?topic=4138&ptopic=98 |
|             |       |	            | No	       | https://ecology.wa.gov/Water-Shorelines/Water-supply/Water-availability |
|             |       |	            | No	       | http://www.twdb.texas.gov/waterplanning/data/glossary.asp |
|             |       |	            | No	       | https://tpwd.texas.gov/landwater/water/habitats/rivers/glossary.phtml |
|             |       |	            | No	       | https://www.tceq.texas.gov/remediation/superfund/glossary.html |
|             |       |	            | No	       | https://www.tceq.texas.gov/assets/public/comm_exec/pubs/rg/rg360/rg36013/glossary.pdf |
|             |       |	            |	No         | https://denr.sd.gov/des/wr/dictionary.aspx |
