from pyvirtualdisplay import Display

from selenium import webdriver

from bs4 import BeautifulSoup

import time

import csv

import argparse

from utils import limpa_unicode

def export_to_csv(rows):

	print (rows)

	file = './data/all_data_springer.csv'

	print(u'Exportando para csv...')

	header = ["Item Title","Publication Title","Book Series Title","Journal Volume",\
				"Journal Issue","Item DOI","Authors","Publication Year","URL","Content Type" \
				"Abstract","Title-fixec","Authors-fixed"
			]

	with open(file, 'w', encoding='utf-8') as csvfile:
		outcsv = csv.writer(csvfile, delimiter=',',quotechar='"', quoting = csv.QUOTE_MINIMAL)

		outcsv.writerow(header)    

		for row in rows:
			outcsv.writerow(row)    

def crawler(file):

	articles = []

	with open(file, newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in spamreader:
			articles.append(row)

	display = Display(visible=0, size=(800, 600))
	display.start()
	driver = webdriver.Chrome()

	rows = []

	for row in articles[1:]:
		
		driver.get(row[8])

		time.sleep(1) 
		
		soup = BeautifulSoup(driver.page_source, 'html.parser')
		
		abstract = soup.find("p",{"class": "Para"})
		try:
			abstract = abstract.text
			abstract = abstract.strip()
		except AttributeError:
			pass

		authors = []
		for aut in soup.find_all('span', {'class': 'authors__name'}):
			authors.append(aut.text)

		title = soup.find("h1",{"class": "ArticleTitle"})
		try:
			title = title.text
		except AttributeError:
			title = soup.find("h1",{"class": "ChapterTitle"})
			title = title.textpad

		rows.append(row + [limpa_unicode(abstract), ", ".join(authors), title ]) 

	driver.close()

	export_to_csv(rows)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("file", help=u"Informe o arquivo csv exportado da ACM (tem que ser padrão da ACM).\
		Os resumos serão buscados automaticamente e será criado um novo csv com a coluna de abstract.")
	
	args = parser.parse_args()

	crawler(args.file)
