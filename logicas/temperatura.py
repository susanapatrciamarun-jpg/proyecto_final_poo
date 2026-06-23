def convertir_temperatura(valor, origen, destino):
    # Aseguramos que el valor sea un número decimal para poder hacer las operaciones matemáticas
    valor = float(valor)

    # 1. SI EL ORIGEN ES CELSIUS
    if origen == "Celsius":
        if destino == "Celsius":
            return valor
        elif destino == "Fahrenheit":
            return (valor * 9/5) + 32
        elif destino == "Kelvin":
            return valor + 273.15

    # 2. SI EL ORIGEN ES FAHRENHEIT 
    elif origen == "Fahrenheit":
        if destino == "Celsius":
            return (valor - 32) * 5/9
        elif destino == "Kelvin":
            return (valor - 32) * 5/9 + 273.15
        elif destino == "Fahrenheit":
            return valor

    # 3. SI EL ORIGEN ES KELVIN 
    elif origen == "Kelvin":
        if destino == "Celsius":
            return valor - 273.15
        elif destino == "Fahrenheit":
            return (valor - 273.15) * 9/5 + 32
        elif destino == "Kelvin":
            return valor