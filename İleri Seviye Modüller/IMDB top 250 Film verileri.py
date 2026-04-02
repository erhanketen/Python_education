import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

response = requests.get(url)

print(response)

hmtl = response.content.decode("utf-8",errors='ignore')

soup = BeautifulSoup(hmtl, "html.parser")

for i in soup.find_all("h3",{"class":"ipc-title__text"}):
    print(i)














