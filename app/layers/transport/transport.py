# capa de transporte/comunicación con otras interfaces o sistemas externos.

import requests
from ...config import config

# comunicación con la REST API.
# este método se encarga de "pegarle" a la API y traer una lista de objetos JSON crudos (raw).
def getAllImages(input=None):
    if input is None:
        json_response = requests.get(config.DEFAULT_REST_API_URL).json()
    else:
        json_response = requests.get(config.DEFAULT_REST_API_SEARCH + input).json()

    json_collection = []

    # si la búsqueda no arroja resultados, entonces retornamos una lista vacía de elementos.
    if 'error' in json_response:
        print("[transport.py]: la búsqueda no arrojó resultados.")
        return json_collection

    for object in json_response['results']:
        try:
            if 'image' in object:  # verificar si la clave 'image' está presente en el objeto (sin 'image' NO nos sirve, ya que no mostrará las imágenes).
                json_collection.append(object)
            else:
                print("[transport.py]: se encontró un objeto sin clave 'image', omitiendo...")

        except KeyError: 
            # puede ocurrir que no todos los objetos tenga la info. completa, en ese caso descartamos dicho objeto y seguimos con el siguiente en la próxima iteración.
            pass

    return json_collection