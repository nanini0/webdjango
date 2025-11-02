# centro_adopcion/context_processors.py

def info_sitio(request):
    return {
        'nombre_sitio': 'Centro de Adopción ❤️ ',
        'mensaje_bienvenida': 'Dale un hogar a un nuevo amigo hoy ❤️',
    }
