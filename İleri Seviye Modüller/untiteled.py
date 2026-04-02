import requests
from bs4 import BeautifulSoup

url = "https://genius.com/"
response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi, 'html.parser')

print(soup.find_all('div', {"class":"ChartSong-desktop__Cover-sc-143619f6-1 jyqqTo"}))








