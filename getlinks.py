import requests as rq
from bs4 import BeautifulSoup

url = input("Link: ")
if("https" or "http") in url:
    data = rq.get(url)
else:
    data = rq.get("https://" + url)


soup=BeautifulSoup(data.text,"html.parser")
links=[]
for link in soup.find_all("a"):
    href=link.get("href")
    if href != "#" and "http" in href:
        links.append(href + "\n")

with open("myLinks.txt","w") as saved:
    saved.writelines(links)
