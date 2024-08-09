# Instalar la libreria request python -m pip install requests
# Import request
import requests
# Modulo para parsear en una estructura de datos mas facil de manejar pip install beautifulsoup4
from bs4 import BeautifulSoup

# get method para recibir el contenido HTML de la pagina
#url = "https://example.com/"
url = "https://httpbin.org/status/200"

# Manejar Errores
try:
    response = requests.get(url)
    response.raise_for_status()
    # Se convierte en un Soup object
    soup = BeautifulSoup(response.content, "html.parser")

    # Obtener algunos elementos de la pagina
    title = soup.title.text if soup.title else "Sin Titulo"
    content = soup.find("p").text if soup.find("p") else "Sin Contenido"
    links = [a["href"] for a in soup.find_all("a")]


    print(title)
    print(content)
    print(links)
except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")

