import requests
from bs4 import BeautifulSoup


url = "https://www.avito.ru/sankt-peterburg/velosipedy/dvuhpodves_gornyy_velosiped_giant_reign_2_2021_2856391798"

html = requests.get(url)

s = BeautifulSoup(html.content, 'html.parser')

results = s.find(class_='image-frame-wrapper-_NvbY')

job_title = results.find_all('img')

print(job_title[0].text)