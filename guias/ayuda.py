#ayuda
import wx
import wx.adv
from wx.lib.wordwrap import wordwrap
import os

def Ayuda(parent_window):
    """
    Muestra la ventana compacta de la guía de uso,
    usando la misma estructurade la demo de wxPython.
    """
    # Creamos el objeto de información nativo
    licenseText = "Este software está bajo la licencia MIT. Copyright (c) 2026."
    
    texto_guia = (
        "GUÍA DE USO\n"
    
        "Esta App te permite verificar tus resultados de forma rápida\n\n"
        "PASO 1: Una vez la aplicación este abierta, deberás elegír una opción entre una variable y dos variables\n\n"
        "A) Convertidor de unidades (una variable)\n\n"
        "   Deberás elegír una opción de Magnitudes para luego elegír la opción de la unidad a la que convertirá el valor que necesite ¬Origen- elegiras la unidad del valor que vas a convertir a la unidad ¬Destino-.\n\n"
        "B) Convertidor de Magnitudes Derivadas o físicas (dos variables)\n\n"
        "   Si elegis la opción de ¬Dos Variables- deberás seleccionar la medida que necesitas convertir, elegis el Tipo de Medida entre: Distancia, Velocidad y Tiempo.\n"
        "   según lo que necesitas, pondras los valores que corresponden para asi realizar el cálculo.\n\n")
    
    # Configuramos el objeto info
    info = wx.adv.AboutDialogInfo()
    # Cargar la imagen y convertirla en ícono
    icono = wx.Icon("imagenes/ayuda.png", wx.BITMAP_TYPE_PNG)
    info.Icon = icono
    try:
            info.Icon = wx.Icon("imagenes/ayuda.png", wx.BITMAP_TYPE_PNG)
    except:
            print("No se pudo cargar el logo")
    

    info.Name = "Guía de uso"
    info.Version = "1.0.2"
    info.Copyright = "(C) 2026 Universidad Nacional de Pilar"
    
    # Aquí agregamos los desarrolladores
    info.Developers = ["Profesor: Javier Castrillo",
                       "Alumnos: Sebastian Chacon y Susana Marun",
                       "Estudiantes de la Universidad Nacional de Pilar",
                       "Facultad de Producción y Tecnología",
                       "Carrera: Tecnicatura en Desarrollo Web"]
    
    # Aquí agregamos el sitio web si quieres
    info.WebSite = ("")
    
    # 3. Aplicamos el formato con wordwrap
    # Usamos el DC de la ventana para que el texto se ajuste al ancho
    dc = wx.ClientDC(parent_window)
    info.License = wordwrap(licenseText, 450, dc)
    info.Description = wordwrap(texto_guia, 450, dc)
    
    # 4. Abrimos la ventana nativa única
    wx.adv.AboutBox(info)
# Bloque de pruebas integrado por si ejecutas este archivo solo
if __name__ == '__main__':
    app = wx.App(False)
    frame = wx.Frame(None, title="")
    Ayuda(frame)
    app.MainLoop()