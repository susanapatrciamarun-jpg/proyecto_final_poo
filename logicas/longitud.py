def convertir_longitud(valor, origen, destino):

    # convertir a centímetros
    if origen == "Centimetros":
        cm = valor

    elif origen == "Pulgadas":
        cm = valor * 2.54

    elif origen == "Pies":
        cm = valor * 30.48

    elif origen == "Yardas":
        cm = valor * 91.44

    else:
        raise ValueError("Unidad de origen no válida")

    # convertir desde centímetros
    if destino == "Centimetros":
        return cm

    elif destino == "Pulgadas":
        return cm / 2.54

    elif destino == "Pies":
        return cm / 30.48

    elif destino == "Yardas":
        return cm / 91.44

    else:
        raise ValueError("Unidad de destino no válida")