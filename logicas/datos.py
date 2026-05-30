def convertir_datos(valor, origen, destino):

    valores = {
        "Bits": 1,
        "Bytes": 8,
        "Kilobytes": 8 * 1024,
        "Megabytes": 8 * 1024**2,
        "Gigabytes": 8 * 1024**3,
        "Terabytes": 8 * 1024**4
    }

    if origen not in valores:
        raise ValueError("Unidad de origen no válida")

    if destino not in valores:
        raise ValueError("Unidad de destino no válida")

    bits = valor * valores[origen]

    return bits / valores[destino]