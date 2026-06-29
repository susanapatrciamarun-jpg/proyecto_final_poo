import wx
import wx.lib.dialogs 
from wx.lib.wordwrap import wordwrap
import os

def abrir_manual(parent_window):
    """
    Muestra el texto largo de la guía en una ventana compacta
    con barra de desplazamiento vertical.
    """
    bitmapDir = os.path.dirname(os.path.abspath(__file__))
    # Cambia "mi_logo.ico" o "mi_logo.png" por el nombre real de tu archivo
    ruta_icono = os.path.join(
            bitmapDir,
            "imagenes",
            "manual.png")
        
    if os.path.exists(ruta_icono):
            # Creamos el objeto Icon. Si usa un PNG, cambia wx.BITMAP_TYPE_ICO por wx.BITMAP_TYPE_PNG
            icono = wx.Icon(ruta_icono, wx.BITMAP_TYPE_PNG)
            parent_window.SetIcon(icono)
    else:
            print(f"No se encontró el archivo de icono en {ruta_icono}")

    texto_guia = (
        " GUÍA DE CÁLCULO MANUAL - PREPARACIÓN DE EXAMEN\n"
        " ===================================================\n"
        "REGLA DE ORO: En el examen solo usarás la calculadora científica. \n"
        "Asegurate de plantear siempre la fórmula en papel antes de operar.\n\n"
        "1. CONVERSIONES DE UNA VARIABLE (Magnitudes)\n"
        "-------------------------------------------------------------------\n"
        "A) LONGITUD (De unidad menor a mayor: Metros a Kilómetros)\n"
        "  • Método: Dividir el valor inicial por 1000, ya que 1 kilómetro tiene 1000 metros.\n"
        "  • Fórmula: km = m / 1000\n"
        "  ✏️ Ejemplo de Examen: Convertir 2500 metros a kilómetros.\n"
        "     Desarrollo: 2500 / 1000 = 2.5 km\n\n"
        " B) TEMPERATURA (Escala Celsius a Fahrenheit)\n"
        "  • Método: Multiplicar los grados Celsius por 1.8 (o 9/5) para escalar la proporción y luego sumar 32 que es el punto de congelación en Fahrenheit.\n"
        "  • Fórmula: °F = (°C × 1.8) + 32\n"
        "  ✏️ Ejemplo de Examen: Convertir 25 °C a °F.\n"
        "     Desarrollo: (25 × 1.8) + 32 = 45 + 32 = 77 °F\n\n"
        " C) INFORMÁTICA / DATOS (De unidad menor a mayor: Bytes a Kilobytes)\n"
        "  • Método: Dividir el valor por 1024. ¡ATENCIÓN!: En informática no se usa el sistema métrico decimal (1000), sino el sistema binario basado en potencias de 2 (2^10 = 1024).\n"
        "  • Fórmula: KB = Bytes / 1024\n"
        "  ✏️ Ejemplo de Examen: Convertir 4096 Bytes a Kilobytes.\n"
        "     Desarrollo: 4096 / 1024 = 4 KB\n\n"
        " 2. CÁLCULOS FÍSICOS DE DOS VARIABLES (Cinemática - MRU)\n"
        "-------------------------------------------------------------------\n"
        "Para recordar cómo despejar las variables en papel, utiliza el triángulo clásico de Cinemática. Tapando la letra que buscas, la posición de las otras dos te dice qué operación matemática hacer:\n"
        "\n"
        "         /\\ \n"
        "        /  \\ \n"
        "       /  D \\      <-- Distancia (Arriba)\n"
        "      /------\\ \n"
        "     / V |  T \\    <-- Velocidad y Tiempo (Abajo, se multiplican)\n"
        "  /____|____\\ \n\n"
        "• Para hallar VELOCIDAD (V): Al tapar la V, queda la Distancia sobre el Tiempo.\n"
        "  • Fórmula: V = Distancia / Tiempo\n"
        "  ✏️ Ejemplo: Un auto recorre 180 km en 3 horas. ¿A qué velocidad iba?\n"
        "     Desarrollo: V = 180 / 3 = 60 km/h\n\n"
        " • Para hallar DISTANCIA (D): Al tapar la D, quedan la Velocidad y el Tiempo juntos abajo.\n"
        "  • Fórmula: D = Velocidad × Tiempo\n"
        "  ✏️ Ejemplo: Un ciclista viaja a 25 km/h durante 2 horas. ¿Qué distancia recorrió?\n"
        "     Desarrollo: D = 25 × 2 = 50 km\n\n"
        " • Para hallar TIEMPO (T): Al tapar la T, queda la Distancia sobre la Velocidad.\n"
        "  • Fórmula: T = Distancia / Velocidad\n"
        "  ✏️ Ejemplo: ¿Cuánto tardará un tren en recorrer 400 km si viaja a una velocidad constante de 80 km/h?\n"
        "     Desarrollo: T = 400 / 80 = 5 horas\n\n"
        " ⚠️ ¡ALERTAS CRÍTICAS PARA EL EXAMEN!\n"
        "-------------------------------------------------------------------\n"
        "1. Compatibilidad de Unidades: NUNCA operes directamente si las unidades no coinciden. Si la distancia está en kilómetros (km) y el tiempo en minutos (min), primero debes pasar los minutos a horas dividiendo por 60 antes de usar el triángulo de física.\n"
        "2. Paréntesis en la Calculadora: Al calcular la temperatura, asegurate de escribir los paréntesis en tu calculadora científica: '(Valor × 1.8) + 32' para evitar que separe mal los términos.\n"
    )
    
    # Ajustamos el texto al ancho de la ventana usando parent_window
    texto_ajustado = wordwrap(texto_guia, 460, wx.ClientDC(parent_window))
    
    # Llamamos a la ruta completa del componente
    dlg = wx.Dialog(parent_window, title="Manual de Usuario", size=(540, 500))
    panel=wx.Panel(dlg)
    txt_ctrl = wx.TextCtrl(panel, value=texto_ajustado, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH)

    boton_ok = wx.Button(panel, label="OK")
    boton_ok.Bind(wx.EVT_BUTTON, lambda event: dlg.EndModal(wx.ID_OK))

    sizer_interno = wx.BoxSizer(wx.VERTICAL)
    sizer_interno.Add(txt_ctrl,1, wx.EXPAND | wx.ALL, 10)
    sizer_interno.Add(boton_ok, 0,wx.ALL | wx.ALIGN_RIGHT,10)
    panel.SetSizer(sizer_interno)


    dlg.ShowModal()
    dlg.Destroy()

# Bloque de pruebas integrado
if __name__ == '__main__':
    app = wx.App(False)
    frame = wx.Frame(None)
    abrir_manual(frame)
    app.MainLoop()