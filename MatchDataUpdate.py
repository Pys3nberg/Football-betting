from bs4 import BeautifulSoup as bs4
from databaseOps import DBComms
import requests as req

url = 'http://www.football-data.co.uk/englandm.php'
data = req.get(url).content

soup = bs4(data, "html.parser")
soupLinks = soup.find_all('a')
links = []

for l in soupLinks:
    if l.get('href').endswith('.csv'):
        links.append(l.get('href'))
        print(l.text)

dbcomms = DBComms()
dbcomms.update_from_links(links, ['1516'])