import wx 






















class MiVentana(wx.Frame):

    def __init__(self):
        super().__init__(None, title='convertidor de unidades', size=(600, 300))
        #panel = MiPanel(self)
        self.Show()


if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = MiVentana()
    app.MainLoop()