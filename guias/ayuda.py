#ayuda
import wx
import wx.adv
from wx.lib.wordwrap import wordwrap

def Ayuda(parent_window):
    """
    Muestra la ventana nativa compacta de la guía de examen 
    usando la misma estructura limpia de la demo de wxPython.
    """
    # 1. Creamos el objeto de información nativo
    info = wx.adv.AboutDialogInfo()
    
    info.Name = "Guia de uso"
    info.Version = ""
    info.Copyright = ""
    
    # 2. Tu texto de las fórmulas
    texto_guia = (
        "GUÍA DE USO\n"
        "=========================================\n\n"
        "Esta App te permite verificar tus resultados de forma rápida\n\n"
        "PASO 1: Una vez la aplicacion esta abierta, deberás elegir una opcion entre una variable y dos variables\n\n"
        "A) Convertidor de unidades (una variable)\n\n"
        "   Deberas elegir una opcion de Magnitud para luego elegir la opcion de la unidad a la que convertira el valor que necesite Origen elegiras la unidad del valor que vas a convertir a la unidad Destino.\n\n"
        "B) Convertidor de Magnitudes Derivadas o fisicas (dos variables)\n\n"
        "   Si elegis la opcion de Dos Variables deberas seleccionar la medida que necesitas convertir elegis el Tipo de Medida entre: Distancia, Velocidad y Tiempo.\n"
        "   segun lo que requieras pondras los valores que corresponden para asi calcular lo necesario.\n\n"

    )
    
    # Ajustamos el texto al ancho de la ventanita usando el parent_window
    info.Description = wordwrap(texto_guia, 420, wx.ClientDC(parent_window))
    
    # Al pasarle el parent_window a la caja nativa, la ventana se queda fija 
    # mostrando su botón único de cerrar automático abajo.
    wx.adv.AboutBox(info, parent_window)


# Bloque de pruebas integrado por si ejecutas este archivo solo
if __name__ == '__main__':
    app = wx.App(False)
    # Creamos un frame de prueba
    frame = wx.Frame(None, title="")
    # Llamamos a la función pasando el frame
    Ayuda(frame)
    app.MainLoop()