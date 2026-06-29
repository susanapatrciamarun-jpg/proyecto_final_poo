import os
import wx
import wx.adv
import wx.lib.agw.advancedsplash as AS

from una_variable import VentanaUnaVariable
from dos_variables import VentanaDosVariables

from guias.manualusuario import abrir_manual
from guias.ayuda import Ayuda
 
class MiVentana(wx.Frame):

    def __init__(self):
        super().__init__(
            None,
            title="Convertidor de Unidades y Calculadora Fisica",
            size=(600, 400)
        )
        # Ocultamos la ventana explícitamente mientras carga el splash
        self.Hide()

        # Obtener el directorio donde está guardado este script (main.py)
        bitmapDir = os.path.dirname(os.path.abspath(__file__))

        # --------------------
        # AGREGADO: Icono de la barra de título (SetIcon)
        # --------------------
        # Cambia "mi_logo.ico" o "mi_logo.png" por el nombre real de tu archivo
        ruta_icono = os.path.join(
            bitmapDir,
            "imagenes",
            "mi_logo.png")
        
        if os.path.exists(ruta_icono):
            # Creamos el objeto Icon. Si usa un PNG, cambia wx.BITMAP_TYPE_ICO por wx.BITMAP_TYPE_PNG
            icono = wx.Icon(ruta_icono, wx.BITMAP_TYPE_PNG)
            self.SetIcon(icono)
        else:
            print(f"No se encontró el archivo de icono en {ruta_icono}")

        # --------------------
        # Pantalla de Bienvenida (AdvancedSplash)
        # --------------------
        bitmapDir = os.path.dirname(os.path.abspath(__file__))
        pn = os.path.normpath(os.path.join(
            bitmapDir,
            "imagenes",
            "advancedsplash.png"))
        
        if os.path.exists(pn):
            bitmap = wx.Bitmap(pn, wx.BITMAP_TYPE_PNG)
            shadow = wx.WHITE

        # Creamos el Splash Screen. Se cerrará en 3000ms (3 segundos)
        # Usamos None en lugar de self porque la ventana principal aún se está construyendo
            self.splash = AS.AdvancedSplash(None, bitmap=bitmap, timeout=3000,
                                            agwStyle=AS.AS_TIMEOUT |
                                                     AS.AS_CENTER_ON_SCREEN |
                                                     AS.AS_SHADOW_BITMAP,
                                            shadowcolour=shadow)
        else:
            print(f"Advertencia: No se encontró la imagen en {pn}")

        # --------------------
        # Barra de menú
        # --------------------
        barrabotones = wx.MenuBar()

        menu_opciones = wx.Menu()

        item_una_var = menu_opciones.Append(
            wx.ID_ANY,
            "&Una Variable\tCtrl+1"
        )

        item_dos_var = menu_opciones.Append(
            wx.ID_ANY,
            "&Dos Variables\tCtrl+2"
        )

        menu_opciones.AppendSeparator()

        item_salir = menu_opciones.Append(
            wx.ID_EXIT,
            "&Salir\tCtrl+Q"
        )

        menu_ayuda = wx.Menu()

        item_acerca = menu_ayuda.Append(
            wx.ID_ABOUT,
            "&Acerca de"
        )

        item_manual = menu_ayuda.Append(
            wx.ID_ANY,
            "&Manual De Usuario\tCtrl+3"
        )

        item_ayuda = menu_ayuda.Append(
            wx.ID_ANY,
            "&Guía de Ayuda\tCtrl+3"
        )

        barrabotones.Append(menu_opciones, "&Opciones")
        barrabotones.Append(menu_ayuda, "&Ayuda")

        self.SetMenuBar(barrabotones)

        # --------------------
        # Panel principal
        # --------------------
        panel = wx.Panel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)

        self.btn_una_var = wx.Button(
            panel,
            label="Una Variable (Conversión)"
        )

        self.btn_dos_var = wx.Button(
            panel,
            label="Dos Variables (Cálculo Físico)"
        )

        self.btn_manual = wx.Button(
            panel,
            label="Manual de Usuario"
        )

        self.btn_ayuda = wx.Button(
            panel,
            label="Guía de Ayuda"
        )

        self.btn_cerrar = wx.Button(
            panel,
            label="Cerrar App"
        )

        sizer.Add(
            self.btn_una_var,
            0,
            wx.ALL | wx.CENTER,
            10
        )

        sizer.Add(
            self.btn_dos_var,
            0,
            wx.ALL | wx.CENTER,
            10
        )

        sizer.Add(
            self.btn_manual,
            0,
            wx.ALL | wx.CENTER,
            10
        )

        sizer.Add(
            self.btn_ayuda,
            0,
            wx.ALL | wx.CENTER,
            10
        )

        sizer.Add(
            self.btn_cerrar,
            0,
            wx.ALL | wx.CENTER,
            10
        )

        panel.SetSizer(sizer)

        # --------------------
        # Eventos botones
        # --------------------
        self.btn_una_var.Bind(
            wx.EVT_BUTTON,
            self.on_abrir_una_variable
        )

        self.btn_dos_var.Bind(
            wx.EVT_BUTTON,
            self.on_abrir_dos_variables
        )

        self.btn_manual.Bind(
            wx.EVT_BUTTON,
            self.on_manual
        )

        self.btn_ayuda.Bind(
            wx.EVT_BUTTON,
            self.on_ayuda
        )

        self.btn_cerrar.Bind(
            wx.EVT_BUTTON,
            self.on_cerrar_app
        )

        # --------------------
        # Eventos menú
        # --------------------
        self.Bind(
            wx.EVT_MENU,
            self.on_abrir_una_variable,
            item_una_var
        )

        self.Bind(
            wx.EVT_MENU,
            self.on_abrir_dos_variables,
            item_dos_var
        )

        self.Bind(
            wx.EVT_MENU,
            self.on_manual,
            item_manual
        )

        self.Bind(
            wx.EVT_MENU,
            self.on_ayuda,
            item_ayuda
        )

        self.Bind(
            wx.EVT_MENU,
            self.on_cerrar_app,
            item_salir
        )

        self.Bind(
            wx.EVT_MENU,
            self.on_mostrar_acerca_de,
            item_acerca
        )

        self.Centre()

    def on_abrir_una_variable(self, event):
        self.Hide()
        ventana = VentanaUnaVariable(parent=self)
        ventana.Show()

    def on_abrir_dos_variables(self, event):
        self.Hide()

        ventana = VentanaDosVariables(parent=self)
        ventana.Show()

    def on_mostrar_acerca_de(self, event):
        info = wx.adv.AboutDialogInfo()
        info.SetName("Convertidor de Unidades y Calculadora Física")
        info.SetVersion("1.0")

        info.SetDescription(
            "Aplicación desarrollada en Python utilizando wxPython.\n\n"
            "Permite realizar conversiones de unidades y resolver "
            "cálculos físicos de distancia, velocidad y tiempo."
    )

        info.SetCopyright(
            "© 2026")

        info.SetDevelopers([
            "Mikel Sebastián Chacón Vásquez",
            "Susana Patriciamaru"
            ])
        
        info.SetLicense(
            "Este software fue desarrollado con fines académicos."
            )
        info.SetWebSite(
            "https://github.com/sebastianchacon140700/proyecto_final_poo.git",
            "Repositorio del proyecto"
            )

        wx.adv.AboutBox(info)

    def on_manual(self, event):
        abrir_manual(self)

    def on_ayuda(self, event):
        Ayuda(self)

    def on_cerrar_app(self, event):
        self.Close()


if __name__ == "__main__":
    app = wx.App(False)

    frame = MiVentana()
    frame.Show()

    app.MainLoop()