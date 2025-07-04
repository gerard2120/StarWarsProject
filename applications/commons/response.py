from rest_framework.response import Response

class CustomResponse:
    @staticmethod
    def success(data=None, codigo="OK", mensaje="Operación exitosa", status=200):
        return Response({
            "codigo": codigo,
            "mensaje": mensaje,
            "respuesta": data
        }, status=status)

    @staticmethod
    def error(mensaje="Error inesperado", codigo="ERROR", status=400, errors=None):
        return Response({
            "codigo": codigo,
            "mensaje": mensaje,
            "respuesta": errors or []
        }, status=status)
