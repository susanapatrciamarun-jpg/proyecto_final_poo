import wx

class MiPanel(wx.Panel):

    def distancia_a_km(self, valor, unidad):
        if unidad == "Metros":
            return valor / 1000

        elif unidad == "Kilometros":
            return valor

        elif unidad == "Yardas":
            return valor * 0.0009144

        elif unidad == "Millas":
            return valor * 1.60934

        return 0

    def tiempo_a_horas(self, valor, unidad):
        if unidad == "Minutos":
            return valor / 60
        
        elif unidad == "Horas":
            return valor 
        
        elif unidad == "Dias":
            return valor * 24
        
        return 0 
         

    def calcular(self, event):
        valor1 = self.textbox1.GetValue()
        valor2 = self.textbox2.GetValue()

        unidad1 = self.datos1.GetStringSelection()
        unidad2 = self.datos2.GetStringSelection()

        #print("unidad1:", unidad1)
        #print("unidad2:", unidad2)

        if self.operacion == "Distancia":
            velocidad_kmh = valor1
            tiempo_horas = self.tiempo_a_horas(valor2, unidad2)

            resultado = velocidad_kmh * tiempo_horas

            resultado_unidad = "km"
                

        elif self.operacion == "Velocidad":
             
            distancia_km = self.distancia_a_km(valor1, unidad1)
            tiempo_horas = self.tiempo_a_horas(valor2, unidad2)
            
            if tiempo_horas == 0:
                self.resultado.SetLabel("el tiempo no puede ser 0")
                return
            
            resultado = distancia_km / tiempo_horas

            resultado_unidad = "km/h"

        elif self.operacion == "Tiempo":
             
            distancia_km = self.distancia_a_km(valor1, unidad1)

            if valor2 == 0:
                self.resultado.SetLabel("la velocidad no puede ser nunca 0")
                return
            
            resultado = distancia_km / valor2

            resultado_unidad = "horas"
            

        else:
            self.resultado.SetLabel("Seleccione una operación")
            return

        self.resultado.SetLabel(
            f"Resultado {resultado:.2f} {resultado_unidad}" 
        )


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
        self.SetSizer(sizer_principal)

        self.boton_calcular.Bind(
              wx.EVT_BUTTON,
              self.calcular
        )

        self.boton_limpiar.Bind(
              wx.EVT_BUTTON,
              self.limpiar
        )

        # EVENTOS     
    def limpiar(self, event):
        self.textbox1.SetValue(0)
        self.textbox2.SetValue(0)
        self.resultado.SetLabel("Resultado:")
        self.operacion = ""

        self.datos1.Clear()
        self.datos2.Clear()
              
        self.label1.SetLabel("dato 1")
        self.label2.SetLabel("dato 2")



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

if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = MiFrame()
    app.MainLoop()