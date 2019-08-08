# coding=utf-8
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@version :
@file : wxpython_demo.py
@time : 2019/08/09 02:10:02
@func :
"""
import wx

class Page1(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        v_box_sizer = wx.BoxSizer(wx.VERTICAL)
        v_box_sizer.Add(wx.StaticText(self, label='Page One Line1'), proportion=0, flag=wx.EXPAND)
        v_box_sizer.Add(wx.StaticText(self, label='Page One Line2'), proportion=1, flag=wx.EXPAND)

        self.SetSizer(v_box_sizer)


class Page2(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        wx.StaticText(self, label='Page Two2')


class Page3(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        wx.StaticText(self, label='Page Three3')


if __name__ == '__main__':
    app = wx.App(False)
    frame = wx.Frame(None, title="Notebook Demo")
    nb = wx.Notebook(frame,size=(200,100),style=wx.NB_LEFT)
    nb.AddPage(Page1(nb), "Page One")
    nb.AddPage(Page2(nb), "Page Two")
    nb.AddPage(Page3(nb), "Page Three")
    frame.Show()
    app.MainLoop()