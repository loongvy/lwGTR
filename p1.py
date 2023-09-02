import wx


class Frame1(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title='第一题', size=(500, 300))
        self.Centre()
        panel = wx.Panel(self)

        # 单选框
        smpls1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        wx.RadioBox(parent=panel, label='选择商品个数', choices=smpls1, pos=(10, 10))
        smpls2 = [u'苹果', u'桃', u'梨']
        wx.RadioBox(parent=panel, label='选择商品种类', choices=smpls2, pos=(280, 10))

        # 复选框
        self.cb1 = wx.CheckBox(parent=panel, label='苹果', size=(120, 18), pos=(60, 80))
        self.ch2 = wx.CheckBox(parent=panel, label='桃子', size=(120, 18), pos=(60, 100))
        self.ch3 = wx.CheckBox(parent=panel, label='雪梨', size=(120, 18), pos=(60, 120))

        # 下拉菜单
        st1 = wx.StaticText(parent=panel, size=(100, 18), label=u"请选择经销商：", pos=(10, 150))
        store = ['公园1903店', '大悦城店', '西山万达广场店', '恒隆广场店']
        self.combo1 = wx.ComboBox(parent=panel, pos=(160, 150), value='', choices=store, name='商店')


class App(wx.App):
    def OnInit(self):
        frm = Frame1()
        frm.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()
