import requests
import PyPDF2
import io
import pandas as pd


url = "http://dnrc.mt.gov/divisions/water/management/docs/training-and-education/water-commissioner/2016_water_commissioner_glossary.pdf"
file = '/Users/joseph/Desktop/2016_water_commissioner_glossary.pdf'

result = requests.get(url)
html = io.BytesIO(result.content)

reader = PyPDF2.PdfFileReader(html)
contents = reader.getPage(1).extractText()



df = pd.DataFrame(contents)

print('done')

Œ