import wx
from logicas.longitud import convertir_longitud
from logicas.peso import convertir_peso
from logicas.temperatura import convertir_temperatura
from logicas.datos import convertir_datos
from logicas.historial import (
    leer_historial_una,
    guardar_historial_una
)

class PanelUnaVariable(wx.Panel):

    def convertidor(self, event):
        valor = self.textbox.GetValue()
        opcion = self.destino
        
        if self.destino == "":
            self.resultado.SetLabel(
            "Seleccione una unidad de destino"
        )
            return

        if self.origen == "":
            self.resultado.SetLabel(
            "Seleccione una unidad de origen"
        )
            return

        if opcion in {"Centimetros" ,"Pulgadas", "Pies", "Yardas"}:
            resultado = convertir_longitud(
                valor,
                self.origen,
                opcion
            )

        elif opcion in {
            "Gramos",
            "Kilogramos",
            "Libras",
            "Toneladas",
            "Onzas"
        }:
            resultado = convertir_peso(
                valor,
                self.origen,
                opcion
            )
        
        elif opcion in{
            "Celsius",
            "Fahrenheit",
            "Kelvin"
        }:
            resultado = convertir_temperatura(
                valor,
                self.origen,
                opcion
            )

        elif opcion in{
            "Bits",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes"
        }:
            resultado = convertir_datos(
                valor,
                self.origen,
                opcion
            ) 

        else:
            self.resultado.SetLabel("seleccione una opcion")
            return
        self.resultado.SetLabel(
            f"{resultado:g} {opcion}"
        )

        guardar_historial_una(
            self.origen,
            opcion,
            valor,
            resultado
        )
   

    def __init__(self, parent):
        super().__init__(parent)        
        
        self.label_magnitud = wx.StaticText(
            self,
            label="Magnitud:"
            )

        self.combo_magnitud = wx.Choice(
            self,
            choices=[
                "Seleccionar...",
                "Longitud",
                "Peso",
                "Temperatura",
                "Datos"
                ])

        self.combo_magnitud.SetSelection(0)
        
        
        self.textbox = wx.SpinCtrlDouble(
           self,
            value="0.00",
            size=(120,40),
            min=-1000000,
            max=1000000,
            inc=0.01
            )

        self.textbox.SetDigits(2)

        self.label = wx.StaticText(
            self, 
            label="Seleccione una unidad de origen e ingrese un valor"
            )
        self.label_destino = wx.StaticText(
            self,
            label="Destino: Ninguno"
            )

        self.boton1 = wx.Button(self, label='Convertir', size=(100,40))
        self.boton_limpiar = wx.Button(self, label='Limpiar', size=(60,40))

        self.boton_volver = wx.Button(
            self,
            label="Volver",
            size=(100,40)
)
        self.combo_origen = wx.ComboBox(
            self,
            choices=[],
            style=wx.CB_READONLY
            )

        self.combo_destino = wx.ComboBox(
            self,
            choices=[],
            style=wx.CB_READONLY
            )
                    
        self.resultado = wx.StaticText(self, label="")
        self.destino = ""
        self.origen = ""


        # SIZER 

        sizer_ppal = wx.BoxSizer(wx.VERTICAL)
        fila_datos = wx.BoxSizer(wx.HORIZONTAL)
        fila_botones = wx.BoxSizer(wx.HORIZONTAL)
        fila_magnitud = wx.BoxSizer(wx.HORIZONTAL)


        # FILA MAGNITUD 
        fila_magnitud.Add(
            self.label_magnitud,
            0,
            wx.ALL | wx.ALIGN_CENTER_VERTICAL,
            10
            )

        fila_magnitud.Add(
            self.combo_magnitud,
            0,
            wx.ALL | wx.ALIGN_CENTER_VERTICAL,
            10)
        
        

        # FILA BOTONES
        fila_datos.Add(
            self.combo_origen, 1, 
            wx.ALL | wx.CENTER, 10)
        
        fila_datos.Add(
            self.textbox, 1, 
            wx.ALL | wx.CENTER, 
            10)
        
        fila_datos.Add(
            self.combo_destino,
            1,
            wx.ALL | wx.CENTER,
            10
            )


        # FILA BOTONES  
        fila_botones.Add(
            self.boton1, 1, 
            wx.ALL | wx.CENTER, 10)

        fila_botones.Add(
            self.boton_limpiar,
            1,
            wx.ALL | wx.CENTER,
            10
            )

        sizer_ppal.Add(
            self.label, 0,
              wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5
              )

        sizer_ppal.Add(
            self.label_destino,
            0,
            wx.ALL | wx.ALIGN_CENTER_HORIZONTAL,
            5
            )
    
        sizer_ppal.Add(
            fila_magnitud,
            0,
            wx.ALIGN_CENTER)



        sizer_ppal.Add(
         fila_datos, 0,
           wx.ALIGN_CENTER)
        
        sizer_ppal.Add(
            fila_botones,
            0,
            wx.ALIGN_CENTER
        )
        
        sizer_ppal.Add(self.resultado,
            0,
            wx.ALL | wx.ALIGN_CENTER_HORIZONTAL)

        sizer_ppal.AddStretchSpacer()

        sizer_ppal.Add(
            self.boton_volver,
            0,
            wx.ALL | wx.ALIGN_RIGHT,
            10
)

        self.SetSizer(sizer_ppal)
        
        # BING DE LOS BOTONE 
        self.boton1.Bind(wx.EVT_BUTTON, self.convertidor)
        
        self.boton_limpiar.Bind(wx.EVT_BUTTON, self.limpiar)
        
        self.boton_volver.Bind(
            wx.EVT_BUTTON,
            self.volver
)

        self.combo_origen.Bind(
            wx.EVT_COMBOBOX,
            self.seleccionar_origen
        )

        self.combo_destino.Bind(
            wx.EVT_COMBOBOX,
            self.seleccionar_destino
            )

        self.combo_magnitud.Bind(
            wx.EVT_CHOICE,
            self.cambiar_magnitud
            )

    ##########
    # EVENTOS#
    ##########
    def seleccionar_origen(self, event):
        self.origen = self.combo_origen.GetValue()

    def seleccionar_destino(self, event):
        self.destino = self.combo_destino.GetValue()
        self.label_destino.SetLabel(
            f"Destino: {self.destino}"
            )
        


    def limpiar(self, event):
        self.textbox.SetValue(0.0)
        self.resultado.SetLabel("")
        self.destino = ""
        self.origen = ""
        self.combo_origen.Clear()
        self.label_destino.SetLabel("Destino: Ninguno") 

    def volver(self, event):
        ventana = self.GetParent()
        if ventana.parent:
            ventana.parent.Show()
            
        ventana.Close()

    def cambiar_magnitud(self, event):
        
        magnitud = self.combo_magnitud.GetStringSelection()
        
        self.combo_origen.Clear()
        self.combo_destino.Clear()
        
        if magnitud == "Longitud":
            self.combo_origen.AppendItems([
                "Centimetros",
                "Pies",
                "Pulgadas",
                "Yardas"
                ])
            self.combo_destino.AppendItems([
                "Centimetros",
                "Pies",
                "Pulgadas",
                "Yardas"
                ])
            
        elif magnitud == "Peso":
            self.combo_origen.AppendItems([
                "Gramos",
                "Kilogramos",
                "Libras",
                "Toneladas",
                "Onzas"
                ])
            self.combo_destino.AppendItems([
                "Gramos",
                "Kilogramos",
                "Libras",
                "Toneladas",
                "Onzas"
                ])

        elif magnitud == "Temperatura":
            self.combo_origen.AppendItems([
                "Celsius",
                "Fahrenheit",
                "Kelvin"
                ])
            self.combo_destino.AppendItems([
                "Celsius",
                "Fahrenheit",
                "Kelvin",
                ])

        elif magnitud == "Datos":
            self.combo_origen.AppendItems([
                "Bits",
                "Bytes",
                "Kilobytes",
                "Megabytes",
                "Gigabytes",
                "Terabytes"
                ])
            self.combo_destino.AppendItems([
                "Bits",
                "Bytes",
                "Kilobytes",
                "Megabytes",
                "Gigabytes",
                "Terabytes"
            ])

        if self.combo_origen.GetCount() > 0:
            self.combo_origen.SetSelection(0)
            self.origen = self.combo_origen.GetValue()
        if self.combo_destino.GetCount() > 0:
            self.combo_destino.SetSelection(0)
            self.destino = self.combo_destino.GetValue()

            self.label_destino.SetLabel(
                f"Destino: {self.destino}"
                )
    

class VentanaUnaVariable(wx.Frame):

    def __init__(self, parent = None):
        super().__init__(
            parent, 
            title='convertidor de unidades',
            size=(750, 500))
        self.parent = parent
        self.panel = PanelUnaVariable(self)

        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        self.menu_salir = file_menu.Append(wx.ID_EXIT , "salir")
        



        menu_historial = wx.Menu()

        self.m_ver_historial = menu_historial.Append(
            wx.ID_ANY,
            "Ver historial"
            )


        menu_bar.Append(file_menu, "archivo")
        menu_bar.Append(menu_historial,"Historial")
        
        self.SetMenuBar(menu_bar)
        self.Bind(wx.EVT_MENU, self.salir, self.menu_salir)
        
        
        # boton de historial
        self.Bind(wx.EVT_MENU,self.ver_historial,self.m_ver_historial)



        self.Bind(wx.EVT_CLOSE, self.al_cerrar)

        self.Show()



    def salir(self, event):
        if self.parent:
            self.parent.Show()

        self.Close()

    def al_cerrar(self, event):
        if self.parent:
            self.parent.Show()

        event.Skip()
    
    def ver_historial(self, event):
        historial = leer_historial_una()

        if historial.strip() == "":
            historial = "No hay conversiones registradas"

        wx.MessageBox(
            historial,
            "Historial de conversiones",
            wx.OK | wx.ICON_INFORMATION
            )


if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = VentanaUnaVariable()
    app.MainLoop()