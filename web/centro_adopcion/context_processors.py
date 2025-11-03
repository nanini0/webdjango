from .models import ConfiguracionSitio

def info_sitio(request):
    try:
        # Obtener la configuración activa
        config = ConfiguracionSitio.objects.get(activo=True)
        return {
            'nombre_sitio': config.nombre_sitio,
            'mensaje_bienvenida': config.mensaje_bienvenida,
        }
    except ConfiguracionSitio.DoesNotExist:
        # Valores por defecto si no hay configuración
        return {
            'nombre_sitio': 'Centro de Adopción ❤️',
            'mensaje_bienvenida': 'Dale un hogar a un nuevo amigo hoy ❤️',
        }