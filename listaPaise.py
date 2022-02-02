from bs4 import BeautifulSoup 
import requests
import re

def html(url, *arg, **kwarg):
	# pagina en la que recataremos los nombre de los paises
	url = url
	html = requests.get(url)
	soup = BeautifulSoup(html.text, "html.parser")

	return soup

def info(soup,tag=str, **kwarg):
	# recatamos todo el texto que queremos

	paise = soup.find(**kwarg)
	lista = paise.find_all(tag)

	# organizamos el texto
	rest = []
	p = re.compile(r"\S")
	for name in lista:
		pais = name.contents[0]
		#search()
		#Escanea una cadena, buscando cualquier ubicación donde coincida este RE.
		# u
		if 	p.search(pais) is not None:
			#<re.Match object; span=(0, 1), match='I'>
			rest.append(pais[:-1])

	return rest

soup  = html('https://www.dicio.com.br/paises-de-a-a-z/')
paises= info(soup, class_="box", tag="li")
print(paises)

for pais in paises:
	soup = html(f'https://paises.ibge.gov.br/#/dados/{pais}')
	info = info(soup, class_="box", tag="li")
print(info)

