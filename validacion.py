class NumeroDebeSerPositivo(Exception):
    def __init__(self, mensaje="El número debe ser positivo"):
        super().__init__(mensaje)


def validar_numero(entrada):
    
    try:
        # Intentamos convertir la entrada en un número
        numero = int(entrada)
        if numero <= 0:
            raise NumeroDebeSerPositivo()
        return numero
    except ValueError:
        raise ValueError("La entrada no es un número válido")
