from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

with open('avito_citroen_adt.csv', "w", encoding="utf-8") as file:
	writer = csv.writer(file)
	writer.writerow(('Name', 'Price', 'Link'))

i = 1

while i != 101:
	URL = f'https://www.avito.ru/rossiya/avtomobili/citroen-ASgBAgICAUTgtg36lyg?cd=1&p={i}'
	driver = webdriver.Chrome(
		executable_path="C:\\Users\\Пользователь\\Desktop\\project\\parsing\\parser\\ChromeWebDriver\\chromedriver.exe"
	)

	try:
		driver.get(url=URL)
		main_page = driver.page_source
		time.sleep(1)
		main_source = BeautifulSoup(main_page, 'lxml')
		adt = main_source.find_all('div', class_='iva-item-content-rejJg')
		for item in adt:
			title = item.find('h3', class_='title-root-zZCwT')
			price = item.find('span', class_='price-text-_YGDY')
			link = item.find('a', class_='link-link-MbQDP')

			link = link.get('href')
			link = 'https://www.avito.ru' + link

			with open('avito_citroen_adt.csv', "a", encoding='utf-8') as file:
				writer = csv.writer(file)
				writer.writerow((title.text.strip(), price.text.strip(), link.strip()))

	except Exception as ex:
		print(ex)
	finally:
		driver.close()
		driver.quit()
	i += 1