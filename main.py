import requests
from bs4 import BeautifulSoup
linksToVisit = []
url3="https://en.wikipedia.org/wiki/Main_Page"
def getLink(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  body = soup.find("body")
  links = body.find_all("a",href=True)
  for i in links:
    if i['href'][0] != "h":
      linksToVisit.append(url+i['href'])
    else:
      linksToVisit.append(i['href'])
def write_to_file(arr):
  newArr = ",".join(arr)
  f = open("linkss.lin","w")
  f.write(newArr)
getLink(url3)
for i in range(1,100):
  print(linksToVisit[i])
  getLink(linksToVisit[i])
write_to_file(linksToVisit)