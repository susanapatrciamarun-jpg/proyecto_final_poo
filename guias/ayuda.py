#ayuda
import wx
import wx.adv
from wx.lib.wordwrap import wordwrap

def Ayuda(parent_window):
    """
    Muestra la ventana compacta de la guía de uso,
    usando la misma estructurade la demo de wxPython.
    """
    # 1. Creamos el objeto de información nativo
    info = wx.adv.AboutDialogInfo()
    info.Name = "Guía de uso"
    info.Version = ""
    info.Copyright = ""
    
    texto_guia = (
        "GUÍA DE USO\n"
        "=========================================\n\n"
        "Esta App te permite verificar tus resultados de forma rápida\n\n"
        "PASO 1: Una vez la aplicación este abierta, deberás elegír una opción entre una variable y dos variables\n\n"
        "A) Convertidor de unidades (una variable)\n\n"
        "   Deberás elegír una opción de Magnitudes para luego elegír la opción de la unidad a la que convertirá el valor que necesite ¬Origen- elegiras la unidad del valor que vas a convertir a la unidad ¬Destino-.\n\n"
        "B) Convertidor de Magnitudes Derivadas o físicas (dos variables)\n\n"
        "   Si elegis la opción de ¬Dos Variables- deberás seleccionar la medida que necesitas convertir, elegis el Tipo de Medida entre: Distancia, Velocidad y Tiempo.\n"
        "   según lo que necesitas, pondras los valores que corresponden para asi realizar el cálculo.\n\n"

    )
    
    # Ajustamos el texto al ancho de la ventana usando parent_window
    info.Description = wordwrap(texto_guia, 420, wx.ClientDC(parent_window))
    
    # Al pasar el parent_window a la caja nativa, la ventana se queda fija 
    # mostrando su botón único de cerrar automático abajo.
    dlg = wx.Dialog(parent_window, title="Instructivo Cientifico", size=(540, 500))
    panel=wx.Panel(dlg)
    txt_ctrl = wx.TextCtrl(panel, value=info.Description, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH)

    boton_ok = wx.Button(panel, label="OK")
    boton_ok.Bind(wx.EVT_BUTTON, lambda event: dlg.EndModal(wx.ID_OK))

    sizer_interno = wx.BoxSizer(wx.VERTICAL)
    sizer_interno.Add(txt_ctrl,1, wx.EXPAND | wx.ALL, 10)
    sizer_interno.Add(boton_ok, 0,wx.ALL | wx.ALIGN_RIGHT,10)
    panel.SetSizer(sizer_interno)

    dlg.ShowModal()
    dlg.Destroy()

# Bloque de pruebas integrado por si ejecutas este archivo solo
if __name__ == '__main__':
    app = wx.App(False)
    frame = wx.Frame(None, title="")
    Ayuda(frame)
    app.MainLoop()