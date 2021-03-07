import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
linksToVisit = []
pageStuff = []
url3="https://en.wikipedia.org/wiki/Main_Page"
def getLink(url):
  try:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    body = soup.find("body")
    links = body.find_all("a",href=True)
    for i in links:
      if i['href'][0] != "h":
        linksToVisit.append(urljoin(url,i['href']))
      else:
        linksToVisit.append(i['href'])
    paras = body.find_all("p")
    texts = ""
    for i in paras:
      texts+=i.text
    pageStuff.append({
      "link":url,
      "text":texts
    })
  except:
    print("DIE ONION")
def write_to_file(arr,urlInfo):
  newArr = ",".join(arr)
  f = open("linkss.lin","w")
  f.write(newArr)
  newArr2 = []
  for i in urlInfo:
    newArr2.append(i['link']+";"+i['text'])
  newArr2 = ",".join(newArr2)
  m = open("pages.lin","w")
  m.write(newArr2)

getLink(url3)
i=0
while True:
  i+=1
  print(linksToVisit[i])
  getLink(linksToVisit[i])
  write_to_file(linksToVisit,pageStuff)