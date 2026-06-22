import wx
from logicas.distancia_velocida_tiempo import (
    calcular_distancia,
    calcular_velocidad,
    calcular_tiempo
)

class PanelDosVariables(wx.Panel):
    
    
    def calcular(self, event):
        valor1 = self.textbox1.GetValue()
        valor2 = self.textbox2.GetValue()

        unidad1 = self.datos1.GetStringSelection()
        unidad2 = self.datos2.GetStringSelection()

        try:
            
            if self.operacion == "Distancia":
                
                resultado = calcular_distancia(
                    valor1,
                    valor2,
                    unidad2
                    )

                resultado_unidad = "km"

            elif self.operacion == "Velocidad":
                
                resultado = calcular_velocidad(
                     valor1,
                    unidad1,
                    valor2,
                    unidad2
                    )

                resultado_unidad = "km/h"

            elif self.operacion == "Tiempo":
                
                resultado = calcular_tiempo(
                    valor1,
                    unidad1,
                    valor2
                    )

                resultado_unidad = "horas"

            else:
                self.resultado.SetLabel(
                     "Seleccione una operación"
                     )
                return

            self.resultado.SetLabel(
                    f"Resultado {resultado:.2f} {resultado_unidad}"
                )

        except ValueError as e:
             self.resultado.SetLabel(
                str(e)
                )


    def __init__(self, parent):
        super().__init__(parent)
        
        self.textbox1 = wx.SpinCtrlDouble(
            self,
            value="0.00",
            size=(120,40),
            min=0,
            max=1000000,
            inc=0.01
)
        self.textbox1.SetDigits(2)


        self.textbox2 = wx.SpinCtrlDouble(
            self,
            value="0.00",
            size=(120,40),
            min=0,
            max=1000000,
            inc=0.01
)
        self.textbox2.SetDigits(2)

            


        self.operacion = ""

        self.datos1 = wx.Choice(
            self,
            choices =[] 
        )

        self.datos2 = wx.Choice(
             self,
             choices= []
        )


        self.boton_calcular = wx.Button(
            self, label = "calcular", size=(100, 40)
        )
        self.boton_limpiar = wx.Button(
              self, label= "limpiar", size= (100, 40)
        )

        self.boton_volver = wx.Button(
            self,
            label="Volver",
            size=(100,40)
            )
        
        self.label1 = wx.StaticText(self, label="Dato 1")
        self.label2 = wx.StaticText(self, label="Dato 2")

        self.resultado = wx.StaticText(
              self,label="Resultado:")


        # sizer 
        sizer_principal = wx.BoxSizer(wx.VERTICAL)
        fila_datos = wx.BoxSizer(wx.HORIZONTAL)
        fila_botones = wx.BoxSizer(wx.HORIZONTAL)


        fila_datos.Add(self.label1, 0, wx.ALL, 10)
        fila_datos.Add(self.textbox1, 0, wx.ALL, 10)
        fila_datos.Add(self.datos1, 0, wx.ALL, 10)

        fila_datos.Add(self.label2, 0, wx.ALL, 10)
        fila_datos.Add(self.textbox2, 0, wx.ALL, 10)
        fila_datos.Add(self.datos2, 0, wx.ALL, 10)

        fila_botones.Add(self.boton_calcular, 0, wx.ALL, 10)
        fila_botones.Add(self.boton_limpiar, 0, wx.ALL, 10)

        sizer_principal.AddStretchSpacer()

        sizer_principal.Add(
          fila_datos,
            0,
            wx.ALIGN_CENTER
)
        sizer_principal.Add(
              fila_botones, 0, 
              wx.ALIGN_CENTER
        )

        sizer_principal.Add(
              self.resultado, 0,
              wx.ALIGN_CENTER | wx.ALL,
              10
        )

        sizer_principal.AddStretchSpacer()

        sizer_principal.Add(
            self.boton_volver,
            0,
            wx.ALL | wx.ALIGN_RIGHT,
            10
            )
        
        self.SetSizer(sizer_principal)

        self.boton_calcular.Bind(
              wx.EVT_BUTTON,
              self.calcular
        )

        self.boton_limpiar.Bind(
              wx.EVT_BUTTON,
              self.limpiar
        )

        self.boton_volver.Bind(
            wx.EVT_BUTTON,
            self.volver
)

        # EVENTOS     
    def limpiar(self, event):
        self.textbox1.SetValue(0.0)
        self.textbox2.SetValue(0.0)
        self.resultado.SetLabel("Resultado:")
        self.operacion = ""

        self.datos1.Clear()
        self.datos2.Clear()
              
        self.label1.SetLabel("Dato 1")
        self.label2.SetLabel("Dato 2")

    def volver(self, event):
        ventana = self.GetParent()
        if ventana.parent:
            ventana.parent.Show()

        ventana.Close()


class VentanaDosVariables(wx.Frame):
    def __init__(self , parent = None):
        super().__init__(
            parent,
            title='convertidor de unidades',
            size=(700, 300))
        self.parent = parent
        self.panel = PanelDosVariables(self)
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
        self.m_salir = menu_calculos.Append(
            wx.ID_EXIT,
            "SALIR"
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

        self.Bind(
            wx.EVT_MENU,
            self.salir,
            self.m_salir
        )

        self.Bind(wx.EVT_CLOSE, self.al_cerrar)

        self.Show()

        # metodos 
    def opcion_Distancia(self, event):
            self.panel.operacion = "Distancia"
            self.panel.label1.SetLabel("velocidad")
            self.panel.label2.SetLabel("tiempo")
            self.panel.datos1.SetItems(
                ["Km/h"]
            )
            self.panel.datos2.SetItems(
                 ["Minutos", "Horas", "Dias"]
            )
            self.panel.datos1.SetSelection(0)
            self.panel.datos2.SetSelection(0)

    def opcion_Velocidad(self, event):
            self.panel.operacion = "Velocidad"
            self.panel.label1.SetLabel("distancia")
            self.panel.label2.SetLabel("tiempo")
            self.panel.datos1.SetItems(
                 ["Metros", "Kilometros", "Yardas", "Millas"]
            )
            self.panel.datos2.SetItems(
                 ["Minutos", "Horas", "Dias"]
            )
            self.panel.datos1.SetSelection(0)
            self.panel.datos2.SetSelection(0)         
            
    def opcion_Tiempo(self, event):
            self.panel.operacion = "Tiempo"
            self.panel.label1.SetLabel("distancia")
            self.panel.label2.SetLabel("velocidad")
            self.panel.datos1.SetItems(
                ["Metros", "Kilometros", "Yardas", "Millas"]
            )
            self.panel.datos2.SetItems(
                 ["Km/h"]
            )
            self.panel.datos1.SetSelection(0)
            self.panel.datos2.SetSelection(0)
   

    def salir(self, event):
        if self.parent:
            self.parent.Show()

        self.Close()


    def al_cerrar(self, event):
        if self.parent:
            self.parent.Show()

        event.Skip()

    
if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = VentanaDosVariables()
    app.MainLoop()