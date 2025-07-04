from rest_framework.views import exception_handler
from .response import CustomResponse

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        codigo = "ERROR"
        mensaje = str(exc)

        if response.status_code == 404:
            codigo = "NOT_FOUND"
            mensaje = "Recurso no encontrado"
        elif response.status_code == 403:
            codigo = "FORBIDDEN"
            mensaje = "Permisos insuficientes"
        elif response.status_code == 401:
            codigo = "UNAUTHORIZED"
            mensaje = "No autenticado"
        elif response.status_code == 400:
            codigo = "BAD_REQUEST"
            mensaje = "Datos inválidos"

        response.data = {
            "codigo": codigo,
            "mensaje": mensaje,
            "respuesta": response.data
        }

    return response
