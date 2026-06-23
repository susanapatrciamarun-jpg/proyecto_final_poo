import wx
from logicas.distancia_velocida_tiempo import (
    calcular_distancia,
    calcular_velocidad,
    calcular_tiempo
)
from logicas.historial import (
    leer_historial_dos,
    guardar_historial_dos
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

            guardar_historial_dos(
                self.operacion,
                f"{valor1} {unidad1}",
                f"{valor2} {unidad2}",
                f"{resultado:.2f} {resultado_unidad}"
                )

        except ValueError as e:
             self.resultado.SetLabel(
                str(e)
                )

    def __init__(self, parent):
        super().__init__(parent)
        
        # === NUEVO DESPLEGABLE PARA SELECCIONAR TIPO DE MEDIDA ===
        self.label_tipo = wx.StaticText(self, label="Tipo de Medida:")
        self.combo_tipo = wx.Choice(
            self,
            choices=["Seleccionar...", "Distancia", "Velocidad", "Tiempo"]
        )
        self.combo_tipo.SetSelection(0) # Inicia en "Seleccionar..."
        
        self.textbox1 = wx.SpinCtrlDouble(self, value="0.00", size=(120,40), min=0, max=1000000, inc=0.01)
        self.textbox1.SetDigits(2)

        self.textbox2 = wx.SpinCtrlDouble(self, value="0.00", size=(120,40), min=0, max=1000000, inc=0.01)
        self.textbox2.SetDigits(2)

        self.operacion = ""

        self.datos1 = wx.Choice(self, choices=[])
        self.datos2 = wx.Choice(self, choices=[])

        self.boton_calcular = wx.Button(self, label="calcular", size=(100, 40))
        self.boton_limpiar = wx.Button(self, label="limpiar", size=(100, 40))
        self.boton_volver = wx.Button(self, label="Volver", size=(100,40))
        
        self.label1 = wx.StaticText(self, label="Dato 1")
        self.label2 = wx.StaticText(self, label="Dato 2")
        self.resultado = wx.StaticText(self, label="Resultado:")

        # Sizers (Organizadores visuales)
        sizer_principal = wx.BoxSizer(wx.VERTICAL)
        fila_tipo = wx.BoxSizer(wx.HORIZONTAL) # Fila para el nuevo selector
        fila_datos = wx.BoxSizer(wx.HORIZONTAL)
        fila_botones = wx.BoxSizer(wx.HORIZONTAL)

        # Añadimos elementos a la fila del tipo de medida
        fila_tipo.Add(self.label_tipo, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 10)
        fila_tipo.Add(self.combo_tipo, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 10)

        fila_datos.Add(self.label1, 0, wx.ALL, 10)
        fila_datos.Add(self.textbox1, 0, wx.ALL, 10)
        fila_datos.Add(self.datos1, 0, wx.ALL, 10)

        fila_datos.Add(self.label2, 0, wx.ALL, 10)
        fila_datos.Add(self.textbox2, 0, wx.ALL, 10)
        fila_datos.Add(self.datos2, 0, wx.ALL, 10)

        fila_botones.Add(self.boton_calcular, 0, wx.ALL, 10)
        fila_botones.Add(self.boton_limpiar, 0, wx.ALL, 10)

        sizer_principal.AddStretchSpacer()
        sizer_principal.Add(fila_tipo, 0, wx.ALIGN_CENTER) # Colocamos el selector arriba
        sizer_principal.Add(fila_datos, 0, wx.ALIGN_CENTER)
        sizer_principal.Add(fila_botones, 0, wx.ALIGN_CENTER)
        sizer_principal.Add(self.resultado, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        sizer_principal.AddStretchSpacer()
        sizer_principal.Add(self.boton_volver, 0, wx.ALL | wx.ALIGN_RIGHT, 10)
        
        self.SetSizer(sizer_principal)

        # Enlaces de eventos
        self.boton_calcular.Bind(wx.EVT_BUTTON, self.calcular)
        self.boton_limpiar.Bind(wx.EVT_BUTTON, self.limpiar)
        self.boton_volver.Bind(wx.EVT_BUTTON, self.volver)
        
        # EVENTO DEL NUEVO DESPLEGABLE
        self.combo_tipo.Bind(wx.EVT_CHOICE, self.on_cambiar_tipo_medida)

    def on_cambiar_tipo_medida(self, event):
        """Cambia dinámicamente las etiquetas y unidades según la selección"""
        seleccion = self.combo_tipo.GetStringSelection()
        
        if seleccion == "Distancia":
            self.operacion = "Distancia"
            self.label1.SetLabel("velocidad")
            self.label2.SetLabel("tiempo")
            self.datos1.SetItems(["Km/h"])
            self.datos2.SetItems(["Minutos", "Horas", "Dias"])
            self.datos1.SetSelection(0)
            self.datos2.SetSelection(0)

        elif seleccion == "Velocidad":
            self.operacion = "Velocidad"
            self.label1.SetLabel("distancia")
            self.label2.SetLabel("tiempo")
            self.datos1.SetItems(["Metros", "Kilometros", "Yardas", "Millas"])
            self.datos2.SetItems(["Minutos", "Horas", "Dias"])
            self.datos1.SetSelection(0)
            self.datos2.SetSelection(0)

        elif seleccion == "Tiempo":
            self.operacion = "Tiempo"
            self.label1.SetLabel("distancia")
            self.label2.SetLabel("velocidad")
            self.datos1.SetItems(["Metros", "Kilometros", "Yardas", "Millas"])
            self.datos2.SetItems(["Km/h"])
            self.datos1.SetSelection(0)
            self.datos2.SetSelection(0)
        else:
            self.limpiar(None)

    def limpiar(self, event):
        self.textbox1.SetValue(0.0)
        self.textbox2.SetValue(0.0)
        self.resultado.SetLabel("Resultado:")
        self.operacion = ""
        self.datos1.Clear()
        self.datos2.Clear()
        self.label1.SetLabel("Dato 1")
        self.label2.SetLabel("Dato 2")
        if event: # Solo resetea el combo si se pulsó el botón limpiar explícitamente
            self.combo_tipo.SetSelection(0)

    def volver(self, event):
        ventana = self.GetParent()
        if ventana.parent:
            ventana.parent.Show()
        ventana.Close()


class VentanaDosVariables(wx.Frame):
    def __init__(self, parent = None):
        super().__init__(parent, title='convertidor de unidades', size=(700, 450)) # Ajustamos alto
        self.parent = parent
        self.panel = PanelDosVariables(self)
        
        # Mantenemos tu menú original por si quieres seguir usándolo
        menu_bar = wx.MenuBar()
        menu_calculos = wx.Menu()
        menu_dtv = wx.Menu()
        
        self.m_distancia = menu_dtv.Append(wx.ID_ANY, "Distancia")
        self.m_velocidad = menu_dtv.Append(wx.ID_ANY, "Velocidad")
        self.m_tiempo = menu_dtv.Append(wx.ID_ANY, "Tiempo")
        
        menu_calculos.AppendSubMenu(menu_dtv, "Distancia - Tiempo - Velocidad")
        self.m_salir = menu_calculos.Append(wx.ID_EXIT, "SALIR")
        menu_bar.Append(menu_calculos, "Calculos")

        menu_historial = wx.Menu()
        self.m_ver_historial = menu_historial.Append(
            wx.ID_ANY,
            "Ver historial"
            )

        menu_bar.Append(
            menu_historial,
            "Historial")

        self.SetMenuBar(menu_bar)
   
        self.Bind(wx.EVT_MENU, self.opcion_Distancia, self.m_distancia)
        self.Bind(wx.EVT_MENU, self.opcion_Velocidad, self.m_velocidad)
        self.Bind(wx.EVT_MENU, self.opcion_Tiempo, self.m_tiempo)
        self.Bind(wx.EVT_MENU, self.salir, self.m_salir)
        self.Bind(wx.EVT_CLOSE, self.al_cerrar)
        self.Bind(wx.EVT_MENU,self.ver_historial,self.m_ver_historial)
        self.Show()

    # Estos métodos ahora actualizan tanto la lógica como el nuevo menú visual
    def opcion_Distancia(self, event):
        self.panel.combo_tipo.SetStringSelection("Distancia")
        self.panel.on_cambiar_tipo_medida(None)

    def opcion_Velocidad(self, event):
        self.panel.combo_tipo.SetStringSelection("Velocidad")
        self.panel.on_cambiar_tipo_medida(None)
            
    def opcion_Tiempo(self, event):
        self.panel.combo_tipo.SetStringSelection("Tiempo")
        self.panel.on_cambiar_tipo_medida(None)

    def salir(self, event):
        if self.parent:
            self.parent.Show()
        self.Close()

    def al_cerrar(self, event):
        if self.parent:
            self.parent.Show()
        event.Skip()
    
    def ver_historial(self, event):
        historial = leer_historial_dos()
        
        if historial.strip() == "":
            historial = "No hay cálculos registrados"

        wx.MessageBox(
            historial,
            "Historial de cálculos",
            wx.OK | wx.ICON_INFORMATION
            )

    
if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = VentanaDosVariables()
    app.MainLoop()