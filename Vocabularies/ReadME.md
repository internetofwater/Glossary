# IOW Glossary Text Extraction Technique Description

The Internet of Water (IOW) Glossary project aims to produce a vocabulary management system where terms are ingested into a [SKOS](https://www.w3.org/2004/02/skos/)-compliant RDF, and semantic links (skos:related and skos:exactMatch) are drawn between terms.  This is accomplished by collecting water use terms and their definition as used by US federal and state agencies.  Results can be viewed using a shiny app hosted by RStudio's free cloud hosting service here: https://internetofwater.shinyapps.io/WaterTerminologyCollection/

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

| Assinged to | State | Agency      | Completed? | In VocBench?|                          URL?                                  |
|    :---:    | :---: |  :---:      |    :---:   | :---: |                          :---                                  |
| Ryan James  | ASCE  | asce-et-g   | Yes        | Yes   |https://ascelibrary.org/doi/pdf/10.1061/9780784408056.bm |
| Ryan James  | AZ    | az-deq      | Yes        | Yes   |https://legacy.azdeq.gov/function/help/glossary.html |
| Ryan James  | AZ    | az-dwr      | Yes        | Yes   |https://new.azwater.gov/dictionary  |
| Ryan James  | AZ    | az-dwr-gpw  | Yes        | Yes   |https://new.azwater.gov/permitting-wells/terminology |
| Ryan James  | AZ    | az-dwr-amdsbt | Yes      | Yes    |http://www.azwater.gov/querycenter/query.aspx?qrysessionid=8CF17C8B1CB98E14E0534C64850A39FA | 
| Ryan James  | CA    | ca-wb-wwgd  | Yes        |Yes     | https://www.waterboards.ca.gov/publications_forms/available_documents/water_words.html |
| Ryan James  | CO    | co-cdr-g    | Yes        | Yes   |https://www.coloradoriverdistrict.org/water-glossary/ |
| Ryan James  | ID    | id-dwr-wro  | Yes        | Yes   |https://idwr.idaho.gov/water-rights/overview.html |
| Ryan James  | NM    | nm-wrap-g   | Yes        | Yes   |https://www.ose.state.nm.us/WR/glossary.php |
| Ryan James  | UT    | ut-udwq-g   | Yes        | Yes   |https://deq.utah.gov/water-quality/glossary-utah-ground-water-quality-protection-program |
| Ryan James  | UT    | ut-udwr-g   | Yes        | Yes   |https://waterrights.utah.gov/wrinfo/glossary.asp |
| Ryan James  | WY    | wy-wrri-hg  | Yes        | Yes   |http://library.wrds.uwyo.edu/glossary/wrs/wrs01/wrs01-ht.html |
| Ryan James  | WY    | wy-wrri-wqg | Yes        | Yes   |http://library.wrds.uwyo.edu/glossary/wrs/wrs01/wrs01-wqt.html |
| Joseph Brewer | OK  | ok-owrb-g	  | Yes        | Yes   |https://www.owrb.ok.gov/util/glossary.php |
| Joseph Brewer | ID  |	id-idwr-t   | Yes        | Yes   |https://idwr.idaho.gov/terminology.html |
| Joseph Brewer | OR  |	            | No	       |       |https://www.oregon.gov/owrd/WRDFormsPDF/wris_code_key.pdf |
| Joseph Brewer | OR  |	or-sos-d    | Yes        | No    |https://secure.sos.state.or.us/oard/displayDivisionRules.action?selectedDivision=3174 |
|             |    OR   |	            | No	       |       |https://www.thefreshwatertrust.org/glossary-of-terms/ |
|             |    OR   |	            | No	       |       |https://oregonexplorer.info/content/glossary-wetlands-terms?topic=4138&ptopic=98 |
|             |   WA    |	            | No	       |       |https://ecology.wa.gov/Water-Shorelines/Water-supply/Water-availability |
| Joseph Brewer |  TX   |	tx-wdb-g  | Yes	   | No    |http://www.twdb.texas.gov/waterplanning/data/glossary.asp |
| Joseph Brewer |  TX   | tx-pwd-g  | Yes	   | Yes   |https://tpwd.texas.gov/landwater/water/habitats/rivers/glossary.phtml |
| Joseph Brewer |  TX   |	tx-ceq-t&d  | Yes	   | Yes   |https://www.tceq.texas.gov/remediation/superfund/glossary.html |
| Joseph Brewer |    TX | tx-ceq-g    | Yes	   | No      | https://www.tceq.texas.gov/assets/public/comm_exec/pubs/rg/rg360/rg36013/glossary.pdf |
| Joseph Brewer |  SD   |	sd-denr-d   |	Yes        | Yes   |https://denr.sd.gov/des/wr/dictionary.aspx |
| Kyle Onda     |USBR   |  usbr-rlg   | Yes        |  Yes     |https://www.usbr.gov/library/glossary/ |
|             |USGS   |             | Yes        |       |https://www.usgs.gov/faqs/why-does-usgs-use-spelling-gage-instead-gauge?qt-news_science_products=0#qt-news_science_products |
| Joseph Brewer |  MT   |  mt-dnrc-wc_g    | Yes    |  No   | http://dnrc.mt.gov/divisions/water/management/docs/training-and-education/water-commissioner/2016_water_commissioner_glossary.pdf
| Joseph Brewer |   MT  | mt-dnrc-swp_g    |  Yes   |  Yes   | http://dnrc.mt.gov/divisions/water/management/docs/state-water-plan/2015_mt_water_plan.pdf
| Joseph Brewer |   TX  |  tx-wdb-swp_g    |  Yes   |   No  | https://www.twdb.texas.gov/waterplanning/swp/2017/chapters/10-SWP17-GLOSSARY-APPENDICES.pdf
| Joseph Brewer |  CO   | co-drn-g2wr_g    | Yes         | No    | https://www.colorado.gov/pacific/sites/default/files/wellpermitguide_1.pdf
| Joseph Brewer |  CO   | co-cfwe-cwl_g    | Yes         | No    |  https://www.courts.state.co.us/userfiles/file/Court_Probation/Water_Courts/cfwe%20Water%20Law%20Guide%20Third%20Edition%20Final%20June%2016%202009.pdf
| Joseph Brewer |  ID   | id-deq-g    | Yes        | No    | https://www.deq.idaho.gov/glossary/
| Joseph Brewer |  OR-USGS | or-or_usgs-g         | Yes         | No    | https://or.water.usgs.gov/projs_dir/willgw/glossary.html
| Joseph Brewer |  WA   |  wa-oria-g  | Yes         | No    | https://www.epermitting.wa.gov/site/alias__resourcecenter/2485/default.aspx
| Joseph Brewer | CO    | co-soc-g    | Yes        | No    | https://www.colorado.gov/pacific/sites/default/files/Glossary%20of%20Water%20Terms.doc
| Joseph Brewer | NM    | nm-wrri-g   | Yes.       | No    | https://nmwrri.nmsu.edu/nmdswb-stocks-and-flows/
| Joseph Brewer | NE    | ne-dnr-insight_t   | Yes         | No   | https://nednr.nebraska.gov/insight/terminology.html
| Joseph Brewer | ND    | nd-swc-rg_ww    | Yes   | Np   | https://www.swc.nd.gov/pdfs/water_reference_guide.pdf
| Joseph Brewer | KS  | ks-doa-dt       | Yes   | No. | https://agriculture.ks.gov/docs/default-source/dwr-ws-fact-sheets/dam-terminology.pdf?sfvrsn=47b34150_6
| Joseph Brewer | KS | ks-doa-rscmg_g | Yes | No | https://agriculture.ks.gov/docs/default-source/doc---documents/kansas-river-stream-corridor-management-guide.pdf?sfvrsn=b27a5361_2
|Joseph Brewer | AK | ak-dec-cwa_g | Yes | No | https://dec.alaska.gov/media/11575/epa-cwa-glossary-of-terms.pdf
