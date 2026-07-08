import wx

class AppHamburguesas(wx.Frame):
    def __init__(self, parent, title):
        super(AppHamburguesas, self).__init__(parent, title=title, size=(415, 320))

        # Se guarda todo en listas indexadas
        self.productos_menu = ["Hamburguesa con Queso", "Hamburguesa con panceta", "Hamburguesa de pollo", "Hamburguesa doble", "Hamburguesa de soja"]
        self.precios_menu = ["$ 7500", "$ 9200", "$ 8800", "$9500", "$7800"]

        # Armado de la interfaz gráfica (UI)
        pnl = wx.Panel(self)

        # Textos y fuentes personalizados
        lbl_info = wx.StaticText(pnl, label="Selecciona la hamburguesa que quieras pedir:")

        # Pasamos las claves de la lista
        self.cb_opciones = wx.ComboBox(pnl, choices=self.productos_menu, style=wx.CB_READONLY)

        # Evento inicial
        self.cb_opciones.Bind(wx.EVT_KEY_DOWN, self.onKeyDown)

        # Bloque del botón 
        b = wx.Button(pnl, 10, "Confirmar pedido")
        self.Bind(wx.EVT_BUTTON, self.OnClick, b)
        b.SetDefault()
        b.SetSize(b.GetBestSize())

        # Sizer configurados
        lay = wx.BoxSizer(wx.VERTICAL)
        lay.Add(lbl_info, 0, wx.ALL | wx.CENTER, 15)
        lay.Add(self.cb_opciones, 0, wx.ALL | wx.EXPAND, 15)
        lay.Add(b, 0, wx.ALL | wx.CENTER, 10)

        pnl.SetSizer(lay)
        self.Centre()

    def onKeyDown(self, e):
        key = e.GetKeyCode()
        if key == wx.WXK_RETURN or key == wx.WXK_NUMPAD_ENTER:
            self.onClickCombo(e)
        else:
            e.Skip()

    def OnClick(self, e):
        self.onClickCombo(e)

    def onClickCombo(self, e):
        idx_seleccion = self.cb_opciones.GetSelection()

        if idx_seleccion == wx.NOT_FOUND:
            return

        item_ok = self.productos_menu[idx_seleccion]
        val_precio = self.precios_menu[idx_seleccion]

        # Alerta con detalle de la compra
        txt_alerta = "DETALLE DE COMPRA\n\nProducto: " + item_ok + "\nPrecio total " + val_precio + " ARS"       

        # Ventana superior
        pop = wx.MessageDialog(self, txt_alerta, "Pedido Confirmado", wx.OK | wx.ICON_AUTH_NEEDED)
        pop.ShowModal()
        pop.Destroy()

        self.cb_opciones.SetSelection(-1)

if __name__ == '__main__':
    run_app = wx.App()
    frame = AppHamburguesas(None, "Hamburguesas Mc Pilar")
    frame.Show()
    run_app.MainLoop()
