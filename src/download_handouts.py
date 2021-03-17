import re, os
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup

url = "https://www.santoantoniodaplatina.pr.gov.br/index.php?sessao=b054603368ixb0&id=1412"

response = requests.get(url)

if response.status_code != requests.codes.ok:
    response.raise_for_status()

soup = BeautifulSoup(response.content, 'html.parser')

section = soup.find('div', class_='panel-body')

links = section.find_all('a')

print(len(links))

regex = re.compile('(\d{2})\/(\d{2})\/(\d{4})')

output_folder = os.path.join('data', 'boletins')

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for link in tqdm(links):
    result = regex.findall(link['title'])
    url = link['href']
    index = url.rfind('.')
    extension = url[index:]

    if len(result) == 1 and len(result[0]) == 3:
        day, month, year = result[0]
        filename = os.path.join(output_folder, f'boletim-sap-{year}-{month}-{day}{extension}')
    else:
        # print(link['title'])
        index = link['href'].rfind('/') + 1
        filename = os.path.join(output_folder, link['href'][index:])


    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        with open(filename, 'wb') as file:
            file.write(response.content)