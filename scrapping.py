# Instalar la libreria request python -m pip install requests
# Import request
import requests
# Modulo para parsear en una estructura de datos mas facil de manejar pip install beautifulsoup4
from bs4 import BeautifulSoup

# get method para recibir el contenido HTML de la pagina
url = "https://example.com/"
response = requests.get(url)

# Se combierte en un Soup object
soup = BeautifulSoup(response.content, "html.parser")

# Obtener algunos elementos de la pagina
title = soup.title.text
content = soup.find("p").text
links = [a["href"] for a in soup.find_all("a")]


print(title)
print(content)
print(links)
