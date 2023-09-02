import wx


class Frame1(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title='第一题', size=(500, 300))
        self.Centre()
        panel = wx.Panel(self)

        # 复选框
        self.cb1 = wx.CheckBox(parent=panel, label='苹果', size=(120, 18), pos=(60, 30))
        self.cb2 = wx.CheckBox(parent=panel, label='桃子', size=(120, 18), pos=(60, 50))
        self.cb3 = wx.CheckBox(parent=panel, label='雪梨', size=(120, 18), pos=(60, 70))

        # 下拉菜单
        wx.StaticText(parent=panel, size=(100, 18), label=u"请选择经销商：", pos=(10, 100))
        store = ['公园1903店', '大悦城店', '西山万达广场店', '恒隆广场店']

        self.st = wx.StaticText(parent=panel, label='message', pos=(10, 150))
        self.btn = wx.Button(parent=panel, label='确定', pos=(300, 100))
        self.combo1 = wx.ComboBox(parent=panel, pos=(160, 100), value='', choices=store, name='商店')

        self.Bind(wx.EVT_BUTTON, self.onclick, self.btn)

    def onclick(self, evt):
        s = ''
        place = self.combo1.Value
        if self.cb1.IsChecked() == True:
            s = '苹果'
        elif self.cb2.IsChecked() == True:
            s = '桃子'
        elif self.cb3.IsChecked() == True:
            s = '雪梨'

        self.st.SetLabel('在%s买了%s' % (place, s))


class App(wx.App):
    def OnInit(self):
        frm = Frame1()
        frm.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()
