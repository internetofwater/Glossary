import requests
import PyPDF2
import io
import pandas as pd


url = "https://www.tceq.texas.gov/assets/public/comm_exec/pubs/rg/rg360/rg36013/glossary.pdf"
file = '/Users/joseph/Desktop/2016_water_commissioner_glossary.pdf'

result = requests.get(url)
pdf = io.BytesIO(result.content)




reader = PyPDF2.PdfFileReader(pdf)
print(reader.numPages)

num_pages = reader.numPages
count = 0
text =""
contents = ""

while count < num_pages:
    pageObj = reader.getPage(count)
    count += 1
    text += pageObj.extractText()
    print('pause')



print(text)


df = pd.DataFrame(contents)

print('done')

#Œ