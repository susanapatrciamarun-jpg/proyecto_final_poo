def convertir_temperatura(valor, origen, destino):

    if origen == "Celsius":

        if destino == "Celsius":
            return valor

        elif destino == "Fahrenheit":
            return (valor * 9/5) + 32

        elif destino == "Kelvin":
            return valor + 273.15