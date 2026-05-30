def convertir_peso(valor, origen, destino):

    # convertir todo a gramos
    if origen == "Gramos":
        gramos = valor

    elif origen == "Kilogramos":
        gramos = valor * 1000

    elif origen == "Libras":
        gramos = valor * 453.592

    elif origen == "Toneladas":
        gramos = valor * 1000000

    elif origen == "Onzas":
        gramos = valor * 28.3495

    else:
        raise ValueError("Unidad de origen no válida")


    # convertir desde gramos
    if destino == "Gramos":
        return gramos

    elif destino == "Kilogramos":
        return gramos / 1000

    elif destino == "Libras":
        return gramos / 453.592

    elif destino == "Toneladas":
        return gramos / 1000000

    elif destino == "Onzas":
        return gramos / 28.3495

    else:
        raise ValueError("Unidad de destino no válida")