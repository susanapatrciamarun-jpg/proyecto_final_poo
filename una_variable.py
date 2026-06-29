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

        if opcion in {"Centimetros","Metros", "Kilometros","Pulgadas", "Pies","Yardas", "Millas"}:
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
        # Mostrar resultado y guardar en el historial
        self.resultado.SetLabel(
            f"{resultado:g} {opcion}"
        )

        guardar_historial_una(
            self.origen,
            opcion,
            valor,
            resultado
        )
   #-----------------------------------------------------------
    #-----------------------------------------
    def __init__(self, parent):
        super().__init__(parent)    
        
        #Inicia el panel, configura widgets de entrada, 
        #estilos de texto y define los estados iniciales.
            
        #Configuraci├│n de Selecci├│n de Magnitud
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
            label="Ingrese un valor y seleccione las unidades"
            )

         
        self.label_a = wx.StaticText(
            self,label="A")
        ## Aplicar estilo en negrita a la etiqueta "A"
        fuente = self.label_a.GetFont()
        fuente.SetWeight(wx.FONTWEIGHT_BOLD)
        fuente.SetPointSize(12)
        self.label_a.SetFont(fuente)


        self.label_destino = wx.StaticText(
            self,
            label="Destino: Ninguno"
            )
        #Botones de Control
        self.boton1 = wx.Button(self, label='Convertir', size=(100,40))
        self.boton_limpiar = wx.Button(self, label='Limpiar', size=(100,40))

        self.boton_volver = wx.Button(
            self,
            label="Volver",
            size=(100,40)
)
        #Combos de Unidades (Origen y Destino)
        self.combo_origen = wx.ComboBox(
            self,
            choices=[],
            style=wx.CB_READONLY,
            size = (140,-1)
            )

        self.combo_destino = wx.ComboBox(
            self,
            choices=[],
            style=wx.CB_READONLY,
            size = (140,-1)
            )
        #Variables de Estado
        self.resultado = wx.StaticText(self, label="")
        self.destino = ""
        self.origen = ""

        #-----------------------------------------------------
        # SIZER Principales
        sizer_ppal = wx.BoxSizer(wx.VERTICAL)
        fila_datos = wx.BoxSizer(wx.HORIZONTAL)
        fila_botones = wx.BoxSizer(wx.HORIZONTAL)
        fila_magnitud = wx.BoxSizer(wx.HORIZONTAL)


         # Fila de seleccion de magnitud 
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
            )
        
        

        # Fila de entrada de datos (Valor, Origen y Destino)
        fila_datos.Add(self.textbox,0,wx.ALL,10)

        fila_datos.AddSpacer(25)

        fila_datos.Add(self.combo_origen,0,wx.ALL,10)

        fila_datos.AddSpacer(15)

        fila_datos.Add(self.label_a,0,wx.ALL | wx.ALIGN_CENTER_VERTICAL,10)

        fila_datos.AddSpacer(15)

        fila_datos.Add(self.combo_destino,0,wx.ALL,10)


        #Fila de botones
        fila_botones.Add(
            self.boton1, 0, 
            wx.ALL | wx.CENTER, 10)

        fila_botones.Add(
            self.boton_limpiar,
            0,
            wx.ALL | wx.CENTER,
            10
            )

        sizer_ppal.AddStretchSpacer() ## Espaciado flexible
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
        
        # Eventos de botones 
        self.boton1.Bind(wx.EVT_BUTTON, self.convertidor)
        self.boton_limpiar.Bind(wx.EVT_BUTTON, self.limpiar)
        self.boton_volver.Bind(
            wx.EVT_BUTTON,
            self.volver)

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

     #---------------------------------------------- 
    # Metodos de Interaccion
    def seleccionar_origen(self, event):
        self.origen = self.combo_origen.GetValue()

        #Captura el valor seleccionado en el combo_origen y lo almacena 
        #en el atributo de clase self.origen.

    def seleccionar_destino(self, event):
        self.destino = self.combo_destino.GetValue()
        self.label_destino.SetLabel(
            f"Destino: {self.destino}"
            )
        
        #Captura el valor seleccionado en el combo_destino, lo almacena 
        #en self.destino y actualiza el texto del label_destino.
        
      
    def limpiar(self, event): #Reinicia los campos del formulario.
        self.textbox.SetValue(0.0)

        self.resultado.SetLabel("")
        self.destino = ""
        self.origen = ""

        self.combo_origen.Clear()
        self.combo_destino.Clear()

        self.combo_magnitud.SetSelection(0)

        self.label_destino.SetLabel("Destino: Ninguno")

        self.label.SetLabel(
            "Seleccione una unidad de origen e ingrese un valor"
        )

    def volver(self, event):
        ventana = self.GetParent()
        if ventana.parent:
            ventana.parent.Show()
            
        ventana.Close()

    def cambiar_magnitud(self, event): #Actualiza el contenido de los combos segun la categororia seleccionada.
        magnitud = self.combo_magnitud.GetStringSelection()
        self.combo_origen.Clear()
        self.combo_destino.Clear()
        
        #condicionales
    # --- Carga de unidades segun la magnitud seleccionada.  
        if magnitud == "Longitud":
            self.combo_origen.AppendItems([
                "Centimetros",
                "Metros",
                "Kilometros",
                "Pies",
                "Pulgadas",
                "Yardas",
                "Millas"
                ])
            self.combo_destino.AppendItems([
                "Centimetros",
                "Metros",
                "Kilometros",
                "Pies",
                "Pulgadas",
                "Yardas",
                "Millas"
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
    
#----------------------------------------------------------
# Ventana principal de la app.
class VentanaUnaVariable(wx.Frame):
    def __init__(self, parent = None):
        #Inicia la ventana, configura el men├║ y vincula los eventos.
        super().__init__(
            parent, 
            title='convertidor de unidades',
            size=(850, 550))
        self.parent = parent
        self.panel = PanelUnaVariable(self)

        # Configuracion de la barra de meenus.
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
        #--------------------------        
        
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