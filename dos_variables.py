import wx

class MiPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        from wx.lib.masked import NumCtrl
        self.textbox1 = NumCtrl(
            self,
            size=(100,40)
)

        self.textbox2 = NumCtrl(
            self,
            size=(100,40)
)

        self.operacion = ""


class MiFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='convertidor de unidades', size=(600, 300))
        self.panel = MiPanel(self)
        menu_bar = wx.MenuBar()
        menu_calculos = wx.Menu()


    

        menu_dtv = wx.Menu()
        self.m_distancia = menu_dtv.Append(
             wx.ID_ANY,
            "Distancia"
)

        self.m_velocidad = menu_dtv.Append(
             wx.ID_ANY,
            "Velocidad"
)

        self.m_tiempo = menu_dtv.Append(
            wx.ID_ANY,
            "Tiempo"
)
        
        menu_calculos.AppendSubMenu(
            menu_dtv,
            "Distancia - Tiempo - Velocidad"
)
        menu_bar.Append(
            menu_calculos,
            "Calculos"
)
        self.SetMenuBar(menu_bar)

    # botones
        self.Bind(
            wx.EVT_MENU,
            self.opcion_Distancia,
            self.m_distancia
        )

        self.Bind(
            wx.EVT_MENU,
            self.opcion_Velocidad,
            self.m_velocidad
        )

        self.Bind(
            wx.EVT_MENU,
            self.opcion_Tiempo,
            self.m_tiempo
        )
        self.Show()

                # metodos 
    def opcion_Distancia(self, event):
            self.panel.operacion = "Distancia"
            print("Distancia")
        
    def opcion_Velocidad(self, event):
            self.panel.operacion = "Velocidad"
            print("Velocidad")
        
    def opcion_Tiempo(self, event):
            self.panel.operacion = "Tiempo"
            print("Tiempo")

if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = MiFrame()
    app.MainLoop()