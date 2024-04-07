'''
The website where the original daily COVID-19 reports were published is no longer available.

Even so, this code was kept for legacy reasons.
'''
import re, os
import logging
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
from pathlib import Path

logging.basicConfig(filename='covid-sap-logger.log',
                    format='%(asctime)d-%(levelname)s-%(message)s')

# This site is no longer available
url = "https://www.santoantoniodaplatina.pr.gov.br/index.php?sessao=b054603368ixb0&id=1412"

response = requests.get(url)

if response.status_code != requests.codes.ok:
    response.raise_for_status()

soup = BeautifulSoup(response.content, 'html.parser')

section = soup.find('div', class_='panel-body')

links = section.find_all('a')

print(len(links))

regex = re.compile('(\d{2})\/(\d{2})\/(\d{4})')

output_folder = Path('..', 'data', 'boletins')

if not output_folder.exists():
    output_folder.mkdir()

for link in tqdm(links):
    result = regex.findall(link['title'])
    url = link['href']
    index = url.rfind('.')
    extension = url[index:]

    if len(result) == 1 and len(result[0]) == 3:
        day, month, year = result[0]
        filename = Path(output_folder, f'boletim-sap-{year}-{month}-{day}{extension}')
    else:
        # print(link['title'])
        index = link['href'].rfind('/') + 1
        filename = Path(output_folder, link['href'][index:])


    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        logging.info(f'{url} : {response.status_code}')
        with open(filename, 'wb') as file:
            file.write(response.content)
    else:
        logging.error(f'{url} : {response.status_code}')