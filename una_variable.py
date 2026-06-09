import wx
from logicas.longitud import convertir_longitud
from logicas.peso import convertir_peso
from logicas.temperatura import convertir_temperatura
from logicas.datos import convertir_datos


class MiPanel(wx.Panel):

    def convertidor(self, event):
        try:
            valor = float(self.textbox.GetValue())
        except:
            self.resultado.SetLabel("ingrese solo numeros")
            return
        opcion = self.destino

        if self.destino == "":
            self.resultado.SetLabel("Seleccione una unidad de destino")
            return

        if self.origen == "":
            self.resultado.SetLabel("Seleccione una unidad de origen")
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
        from wx.lib.masked import NumCtrl

        self.textbox = NumCtrl(
            self,
            size=(100,40),
            allowNegative=False,
            groupDigits=False)
        
        self.textbox.SetValue(0) 

        self.label = wx.StaticText(self, label="Ingrese solo números")
        self.boton1 = wx.Button(self, label='Convertir', size=(60,40))
        self.boton_limpiar = wx.Button(self, label='Limpiar', size=(60,40))
        self.combo_origen = wx.ComboBox(
            self,
            choices=[],
            style=wx.CB_READONLY
            )
                    
        self.resultado = wx.StaticText(self, label="")
        self.destino = ""
        self.origen = ""

        sizer_ppal = wx.BoxSizer(wx.VERTICAL)
        fila = wx.BoxSizer(wx.HORIZONTAL)

        fila.Add(self.boton1, 1, wx.ALL | wx.CENTER, 10)
        fila.Add(self.combo_origen, 1, wx.ALL | wx.CENTER, 10)
        fila.Add(self.textbox, 1, wx.ALL | wx.CENTER, 10)
        fila.Add(self.boton_limpiar, 1, wx.ALL | wx.CENTER, 10)

        sizer_ppal.Add(self.label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        sizer_ppal.Add(fila, 1, wx.EXPAND)
        sizer_ppal.Add(self.resultado, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL)

        self.SetSizer(sizer_ppal)
        
        self.boton1.Bind(wx.EVT_BUTTON, self.convertidor)
        
        self.boton_limpiar.Bind(wx.EVT_BUTTON, self.limpiar)

        self.combo_origen.Bind(
            wx.EVT_COMBOBOX,
            self.seleccionar_origen
        )

    def seleccionar_origen(self, event):
        self.origen = self.combo_origen.GetValue()


    def limpiar(self, event):
        self.textbox.SetValue(0)
        self.resultado.SetLabel("")
        self.destino = ""
        self.origen = ""
        self.combo_origen.Clear()      
    

class MiVentana(wx.Frame):

    def __init__(self):
        super().__init__(None, title='convertidor de unidades', size=(600, 300))
        self.panel = MiPanel(self)

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


        menu_bar.Append(file_menu, "archivo")
        menu_bar.Append(menu_convertir, "convertir")
        self.SetMenuBar(menu_bar)
        self.Bind(wx.EVT_MENU, self.salir, self.menu_salir)
        
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

        self.Show()

    # eventos de longitud
    def opcion_cm(self, event):
        self.panel.destino = "Centimetros"
        self.panel.combo_origen.Clear()
        self.panel.combo_origen.AppendItems([
            "Pulgadas",
            "Pies",
            "Yardas"
            ])
        self.panel.combo_origen.SetSelection(0)
        self.panel.origen = self.panel.combo_origen.GetValue()

    def opcion_pies(self, event):
        self.panel.destino = "Pies"
        self.panel.combo_origen.Clear()
        self.panel.combo_origen.AppendItems([
            "Centimetros",
            "Pulgadas",
            "Yardas"
            ])
        self.panel.combo_origen.SetSelection(0)
        self.panel.origen = self.panel.combo_origen.GetValue()
        

    def opcion_pulgadas(self, event):
        self.panel.destino = "Pulgadas"
        self.panel.combo_origen.Clear()
        self.panel.combo_origen.AppendItems([
            "Centimetros",
            "Pies",
            "Yardas"
            ])
        self.panel.combo_origen.SetSelection(0)
        self.panel.origen = self.panel.combo_origen.GetValue()

    def opcion_yardas(self, event):
        self.panel.destino = "Yardas"
        self.panel.combo_origen.Clear()
        self.panel.combo_origen.AppendItems([
            "Centimetros",
            "Pies",
            "Pulgadas"
            ])
        self.panel.combo_origen.SetSelection(0) 
        self.panel.origen = self.panel.combo_origen.GetValue()

    # eventos de peso
    def opcion_gramos(self, event):
        self.panel.destino = "Gramos"
        self.panel.combo_origen.Clear()
        self.panel.combo_origen.AppendItems([
            "Kilogramos",
            "Libras",
            "Toneladas",
            "Onzas"
        ])
        self.panel.combo_origen.SetSelection(0)
        self.panel.origen = self.panel.combo_origen.GetValue()
    
    def opcion_kilogramos(self, event):
        self.panel.destino = "Kilogramos"
        self.panel.combo_origen.Clear()
        self.panel.combo_origen.AppendItems([
            "Gramos",
            "Libras",
            "Toneladas",
            "Onzas"
        ])
        self.panel.combo_origen.SetSelection(0)
        self.panel.origen = self.panel.combo_origen.GetValue()
    
    def opcion_libras(self, event):
        self.panel.destino = "Libras"
        self.panel.combo_origen.Clear()
        self.panel.combo_origen.AppendItems([
            "Gramos",
            "Kilogramos",
            "Toneladas",
            "Onzas"
        ])
        self.panel.combo_origen.SetSelection(0)
        self.panel.origen = self.panel.combo_origen.GetValue()

    def opcion_toneladas(self, event):
        self.panel.destino = "Toneladas"
        self.panel.combo_origen.Clear()
        self.panel.combo_origen.AppendItems([
            "Gramos",
            "Kilogramos",
            "Libras",
            "Onzas"
        ])
        self.panel.combo_origen.SetSelection(0)
        self.panel.origen = self.panel.combo_origen.GetValue()
        

    def opcion_onzas(self, event):
        self.panel.destino = "Onzas"
        self.panel.combo_origen.Clear()
        self.panel.combo_origen.AppendItems([
            "Gramos",
            "Kilogramos",
            "Libras",
            "Toneladas",
        ])
        self.panel.combo_origen.SetSelection(0)
        self.panel.origen = self.panel.combo_origen.GetValue()                

    # eventos  de temperatura
    def opcion_celsius(self, event):
        self.panel.destino = "Celsius"
        self.panel.combo_origen.Clear()
        self.panel.combo_origen.AppendItems([
            "Fahrenheit",
            "Kelvin"
        ])
        self.panel.combo_origen.SetSelection(0)
        self.panel.origen = self.panel.combo_origen.GetValue()                  

    def opcion_fahrenheit(self, event):
        self.panel.destino = "Fahrenheit"
        self.panel.combo_origen.Clear()
        self.panel.combo_origen.AppendItems([
            "Celsius",
            "Kelvin"
        ])
        self.panel.combo_origen.SetSelection(0)
        self.panel.origen = self.panel.combo_origen.GetValue()                  

    def opcion_kelvin(self, event):
        self.panel.destino = "Kelvin"
        self.panel.combo_origen.Clear()
        self.panel.combo_origen.AppendItems([
            "Celsius",
            "Fahrenheit"
        ])
        self.panel.combo_origen.SetSelection(0)
        self.panel.origen = self.panel.combo_origen.GetValue()

    # eventos de datos informaticos
    def opcion_bits(self, event):
        self.panel.destino = "Bits"
        self.panel.combo_origen.Clear()
        self.panel.combo_origen.AppendItems([
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes"
        ])
        self.panel.combo_origen.SetSelection(0)
        self.panel.origen = self.panel.combo_origen.GetValue()        

    def opcion_bytes(self, event):
        self.panel.destino = "Bytes"
        self.panel.combo_origen.Clear()
        self.panel.combo_origen.AppendItems([
            "Bits",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes"
        ])
        self.panel.combo_origen.SetSelection(0)
        self.panel.origen = self.panel.combo_origen.GetValue()                

    def opcion_kilobytes(self, event):
        self.panel.destino = "Kilobytes"
        self.panel.combo_origen.Clear()
        self.panel.combo_origen.AppendItems([
            "Bits",
            "Bytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes"
        ])
        self.panel.combo_origen.SetSelection(0)
        self.panel.origen = self.panel.combo_origen.GetValue()

    def opcion_megabytes(self, event):
        self.panel.destino = "Megabytes"
        self.panel.combo_origen.Clear()
        self.panel.combo_origen.AppendItems([
            "Bits",
            "Bytes",
            "Kilobytes",
            "Gigabytes",
            "Terabytes"
        ])
        self.panel.combo_origen.SetSelection(0)
        self.panel.origen = self.panel.combo_origen.GetValue()                

    def opcion_gigabytes(self, event):
        self.panel.destino = "Gigabytes"
        self.panel.combo_origen.Clear()
        self.panel.combo_origen.AppendItems([
            "Bits",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Terabytes"
        ])        
        self.panel.combo_origen.SetSelection(0)
        self.panel.origen = self.panel.combo_origen.GetValue()

    def opcion_terabytes(self, event):
        self.panel.destino = "Terabytes"
        self.panel.combo_origen.Clear()
        self.panel.combo_origen.AppendItems([
            "Bits",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes"
        ])        
        self.panel.combo_origen.SetSelection(0)
        self.panel.origen = self.panel.combo_origen.GetValue()

    def salir(self, event):
        self.Close()


if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = MiVentana()
    app.MainLoop()