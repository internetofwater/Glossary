import requests
import PyPDF2
import io
import pandas as pd


url = "http://dnrc.mt.gov/divisions/water/management/docs/state-water-plan/2015_mt_water_plan.pdf"
file = '/Users/joseph/Desktop/2016_water_commissioner_glossary.pdf'

result = requests.get(url)
html = io.BytesIO(result.content)

contents = ""


reader = PyPDF2.PdfFileReader(html)

count = 81
pageObj = reader.getPage(count)
contents += pageObj.extractText()
num_pages = reader.numPages
contents = ""

while count < num_pages + 1:
    pageObj = reader.getPage(count)
    count += 1
    contents += pageObj.extractText()
    print('success')



df = pd.DataFrame(contents)

print('done')

#Œ