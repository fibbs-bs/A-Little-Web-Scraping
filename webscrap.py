from bs4 import BeautifulSoup
import requests

url = 'https://aprenderingles.org/palabras-en-ingles/'
arch = open("out.txt","w")

respuesta = requests.get(url, timeout=5)
contenido = BeautifulSoup(respuesta.content, "html.parser")

palabrasFilas = contenido.find_all("tr")
for fila in palabrasFilas:
    tdPalabraEN = fila.find_all("td",attrs={"class":"column-2"})
    for span in tdPalabraEN:
        palabra = span.find("span").text
        arch.write('"'+palabra+'",')