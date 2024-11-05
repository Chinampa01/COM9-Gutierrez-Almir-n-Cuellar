from app.config import config

def version(request):
    return {'VERSION': config.VERSION} 