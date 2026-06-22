import wx
from logicas.longitud import convertir_longitud
from logicas.peso import convertir_peso
from logicas.temperatura import convertir_temperatura
from logicas.datos import convertir_datos
import logicas.eventos_una_variable as eventos
from logicas.historial import leer_historial_una

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
   

    def __init__(self, parent):
        super().__init__(parent)        
        
        
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
                    
        self.resultado = wx.StaticText(self, label="")
        self.destino = ""
        self.origen = ""

        sizer_ppal = wx.BoxSizer(wx.VERTICAL)

        fila_datos = wx.BoxSizer(wx.HORIZONTAL)
        fila_botones = wx.BoxSizer(wx.HORIZONTAL)


        fila_datos.Add(
            self.combo_origen, 1, 
            wx.ALL | wx.CENTER, 10)
        
        fila_datos.Add(
            self.textbox, 1, 
            wx.ALL | wx.CENTER, 
            10)
        
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

    def seleccionar_origen(self, event):
        self.origen = self.combo_origen.GetValue()


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
    

class VentanaUnaVariable(wx.Frame):

    def __init__(self, parent = None):
        super().__init__(
            parent, 
            title='convertidor de unidades',
            size=(600, 300))
        self.parent = parent
        self.panel = PanelUnaVariable(self)

        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        self.menu_salir = file_menu.Append(wx.ID_EXIT , "salir")
        
         # menu de logitud
        menu_longitud = wx.Menu()
        self.long_cm = menu_longitud.Append(wx.ID_ANY, "Centimetros")
        self.long_pies = menu_longitud.Append(wx.ID_ANY, "Pies")       
        self.long_pulgadas = menu_longitud.Append(wx.ID_ANY, "Pulgadas")
        self.long_yardas = menu_longitud.Append(wx.ID_ANY, "Yardas")

      
        # menu de peso
        menu_peso = wx.Menu()
        self.m_gr = menu_peso.Append(wx.ID_ANY, "Gramos")
        self.m_kg = menu_peso.Append(wx.ID_ANY, "Kilogramos")
        self.m_lb = menu_peso.Append(wx.ID_ANY, "Libras")
        self.m_tone = menu_peso.Append(wx.ID_ANY, "Toneladas")
        self.m_onzas = menu_peso.Append(wx.ID_ANY, "Onzas")

        # menu de temperatura
        menu_temp = wx.Menu()
        self.temp_c = menu_temp.Append(wx.ID_ANY, "Celsius")
        self.temp_f = menu_temp.Append(wx.ID_ANY, "Fahrenheit")
        self.temp_k = menu_temp.Append(wx.ID_ANY, "Kelvin")

        # menu de datos
        menu_datos = wx.Menu()
        self.datos_bit = menu_datos.Append(wx.ID_ANY, "Bits")
        self.datos_byt = menu_datos.Append(wx.ID_ANY, "Bytes")
        self.datos_kb = menu_datos.Append(wx.ID_ANY, "Kilobytes")
        self.datos_mb = menu_datos.Append(wx.ID_ANY, "Megabytes")
        self.datos_gb = menu_datos.Append(wx.ID_ANY, "Gigabytes")
        self.datos_tb = menu_datos.Append(wx.ID_ANY, "Terabytes")

        menu_convertir = wx.Menu()

        menu_convertir.AppendSubMenu(menu_longitud, "longitud")
        menu_convertir.AppendSubMenu(menu_peso, "peso")
        menu_convertir.AppendSubMenu(menu_temp, "temperatura")
        menu_convertir.AppendSubMenu(menu_datos, "datos informaticos")


        menu_historial = wx.Menu()

        self.m_ver_historial = menu_historial.Append(
            wx.ID_ANY,
            "Ver historial"
            )


        menu_bar.Append(file_menu, "archivo")
        menu_bar.Append(menu_convertir, "convertir")
        menu_bar.Append(menu_historial,"Historial")
        self.SetMenuBar(menu_bar)
        self.Bind(wx.EVT_MENU, self.salir, self.menu_salir)
        
        
        # boton de historial
        self.Bind(wx.EVT_MENU,self.ver_historial,self.m_ver_historial)

        # botones de longitud
        self.Bind(wx.EVT_MENU, self.opcion_cm, self.long_cm)
        self.Bind(wx.EVT_MENU, self.opcion_pies, self.long_pies)
        self.Bind(wx.EVT_MENU, self.opcion_pulgadas, self.long_pulgadas)
        self.Bind(wx.EVT_MENU, self.opcion_yardas, self.long_yardas)

        # botone de peso
        self.Bind(wx.EVT_MENU, self.opcion_gramos, self.m_gr)
        self.Bind(wx.EVT_MENU, self.opcion_kilogramos, self.m_kg)
        self.Bind(wx.EVT_MENU, self.opcion_libras, self.m_lb)
        self.Bind(wx.EVT_MENU, self.opcion_toneladas, self.m_tone)
        self.Bind(wx.EVT_MENU, self.opcion_onzas, self.m_onzas)

        # botones de temperatura 
        self.Bind(wx.EVT_MENU, self.opcion_celsius, self.temp_c)
        self.Bind(wx.EVT_MENU, self.opcion_fahrenheit, self.temp_f)
        self.Bind(wx.EVT_MENU, self.opcion_kelvin, self.temp_k)

        # botones de datos
        self.Bind(wx.EVT_MENU, self.opcion_bits, self.datos_bit)
        self.Bind(wx.EVT_MENU, self.opcion_bytes, self.datos_byt)
        self.Bind(wx.EVT_MENU, self.opcion_kilobytes, self.datos_kb)
        self.Bind(wx.EVT_MENU, self.opcion_megabytes, self.datos_mb)
        self.Bind(wx.EVT_MENU, self.opcion_gigabytes, self.datos_gb)
        self.Bind(wx.EVT_MENU, self.opcion_terabytes, self.datos_tb)

        self.Bind(wx.EVT_CLOSE, self.al_cerrar)

        self.Show()

    # eventos

    # eventos de longitud

# eventos de longitud
    def opcion_cm(self, event):
        eventos.opcion_cm(self.panel)

    def opcion_pies(self, event):
        eventos.opcion_pies(self.panel)

    def opcion_pulgadas(self, event):
        eventos.opcion_pulgadas(self.panel)

    def opcion_yardas(self, event):
        eventos.opcion_yardas(self.panel)

# eventos de peso
    def opcion_gramos(self, event):
        eventos.opcion_gramos(self.panel)

    def opcion_kilogramos(self, event):
        eventos.opcion_kilogramos(self.panel)

    def opcion_libras(self, event):
        eventos.opcion_libras(self.panel)

    def opcion_toneladas(self, event):
        eventos.opcion_toneladas(self.panel)

    def opcion_onzas(self, event):
        eventos.opcion_onzas(self.panel)

        # eventos de temperatura
    def opcion_celsius(self, event):
        eventos.opcion_celsius(self.panel)

    def opcion_fahrenheit(self, event):
        eventos.opcion_fahrenheit(self.panel)

    def opcion_kelvin(self, event):
        eventos.opcion_kelvin(self.panel)

        # eventos de datos
    def opcion_bits(self, event):
        eventos.opcion_bits(self.panel)

    def opcion_bytes(self, event):
        eventos.opcion_bytes(self.panel)

    def opcion_kilobytes(self, event):
        eventos.opcion_kilobytes(self.panel)

    def opcion_megabytes(self, event):
        eventos.opcion_megabytes(self.panel)

    def opcion_gigabytes(self, event):
        eventos.opcion_gigabytes(self.panel)

    def opcion_terabytes(self, event):
        eventos.opcion_terabytes(self.panel)


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