import wx

from una_variable import VentanaUnaVariable
from dos_variables import VentanaDosVariables


class MiVentana(wx.Frame):

    def __init__(self):
        super().__init__(
            None,
            title="Convertidor de Unidades",
            size=(600, 300)
        )

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
        wx.MessageBox(
            "Convertidor de Unidades\nVersión 1.0",
            "Acerca de",
            wx.OK | wx.ICON_INFORMATION
        )

    def on_cerrar_app(self, event):
        self.Close()


if __name__ == "__main__":
    app = wx.App(False)

    frame = MiVentana()
    frame.Show()

    app.MainLoop()