# capa de servicio/lógica de negocio

from ..persistence import repositories
from ..utilities import translator
from django.contrib.auth import get_user
from ..transport import transport


def getAllImages(input=None):
    # obtiene un listado de datos "crudos" desde la API, usando a transport.py.
    images = []
    json_collection = transport.getAllImages(input)

    # recorre cada dato crudo de la colección anterior, lo convierte en una Card y lo agrega a images.
    for image in json_collection:
        images.append(translator.fromRequestIntoCard(image))
        
    return images

# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    card = translator.fromTemplateIntoCard(request)
    card.user = request.user  # Usa directamente request.user en lugar de get_user
    return repositories.saveFavourite(card)  # Guarda en la base de datos

# usados desde el template 'favourites.html'
def getAllFavourites(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)
        favourite_list = repositories.getAllFavourites(user)
    
        mapped_favourites = [translator.fromRepositoryIntoCard(fav) for fav in favourite_list]
        return mapped_favourites

def deleteFavourite(fav_id):
    return repositories.deleteFavourite(fav_id)  # Pasa directamente el ID