import bs4 as BeautifulSoup
import requests
import time
def webScraper:
with open("C:/user/desk/FE595/companies.text","t") as f:
for i in range(0,50):
res=requests.get("http://3.85.131.173:8000/random_company")
html=res.text
suppy=BeautifulSoup(html,"html.parser")
IDs=soup.find_all("a")
for IDs in a:
text.g = text.getText()
purpose=IDs[purpose]
if purpose in test.g:
print(text.g,file=f)
time.sleep=(0.2)
except:
return"error"
if_IDs_=="_main_":
assignment2
