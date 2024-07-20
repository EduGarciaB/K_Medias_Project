import pandas as pd
import requests

# URL del CSV
url = "https://raw.githubusercontent.com/4GeeksAcademy/k-means-project-tutorial/main/housing.csv"

# Hacer la solicitud usando requests con verificación SSL desactivada
response = requests.get(url, verify=False)

# Leer el contenido del CSV desde la respuesta
csv_content = response.content

# Guardar el contenido en un archivo CSV en la computadora
with open("housing.csv", "wb") as file:
    file.write(csv_content)

print("Archivo CSV guardado como 'housing.csv'")

















