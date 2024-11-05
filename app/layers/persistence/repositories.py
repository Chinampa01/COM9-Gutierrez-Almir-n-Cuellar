# capa DAO de acceso/persistencia de datos.

from app.models import Favourite

def saveFavourite(image):
    try:
        fav = Favourite.objects.create(url=image.url, name=image.name, status=image.status, last_location=image.last_location, first_seen=image.first_seen, user=image.user)
        return fav
    except Exception as e:
        print(f"Error al guardar el favorito: {e}")
        return None

def getAllFavourites(user):
    favouriteList = Favourite.objects.filter(user=user).values('id', 'url', 'name', 'status', 'last_location', 'first_seen')
    return list(favouriteList)

def deleteFavourite(id):
    try:
        favourite = Favourite.objects.get(id=id)
        favourite.delete()
        return True
    except Favourite.DoesNotExist:
        print(f"El favorito con ID {id} no existe.")
        return False
    except Exception as e:
        print(f"Error al eliminar el favorito: {e}")
        return False