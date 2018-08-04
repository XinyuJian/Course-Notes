# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.1 on Fri May  4 03:32:50 2018
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
import matplotlib_canvas
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((874, 625))
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.text_ctrl_inputdata = wx.TextCtrl(self.panel_1, wx.ID_ANY, "Example:\n1,1\n2,2\n3,3\n4,4\n5,5", style=wx.TE_MULTILINE)
        self.matplotlib_canvas = matplotlib_canvas.MatplotlibCanvas(self.panel_1, wx.ID_ANY)
        self.button_1 = wx.Button(self.panel_1, wx.ID_ANY, "Import Data")
        self.text_ctrl_fairing = wx.TextCtrl(self.panel_1, wx.ID_ANY, "0")
        self.button_plot = wx.Button(self.panel_1, wx.ID_ANY, "Plot")
        self.button_clear = wx.Button(self.panel_1, wx.ID_ANY, "Clear")
        self.text_ctrl_output = wx.TextCtrl(self.panel_1, wx.ID_ANY, "Function: Fairing curves.\nUsage:   1. Input data manully as examples or press button \"Import Data\" to importa a .txt or .csv file.\n             2. You can set the \"Fairing Coefficient\" to decide the degree of fairing.\n             3. Click \"Plot\" button to generate the plot.\n             4. Click \"Reset\" button to delete the plot.\n------------------------------------------\nXinyuJian@2018 All rights reserved. \n------------------------------------------\n", style=wx.TE_MULTILINE)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.on_import_button_clicked, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.on_button_plot, self.button_plot)
        self.Bind(wx.EVT_BUTTON, self.on_button_clear, self.button_clear)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Fairing Curve")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("A:\\Course\\现代造船技术\\Project\\logo.jpg", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.text_ctrl_inputdata.SetMinSize((100, 400))
        self.matplotlib_canvas.SetMinSize((600, 400))
        self.button_plot.SetDefault()
        self.text_ctrl_output.SetMinSize((853, 100))
        self.text_ctrl_output.SetBackgroundColour(wx.Colour(196, 196, 196))
        self.panel_1.SetMinSize((858, 500))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        label_3 = wx.StaticText(self.panel_1, wx.ID_ANY, "Please Input Data Here: ")
        sizer_7.Add(label_3, 0, 0, 0)
        sizer_7.Add(self.text_ctrl_inputdata, 0, wx.EXPAND, 0)
        sizer_3.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_3.Add(self.matplotlib_canvas, 1, wx.ALL | wx.EXPAND, 3)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        static_line_1 = wx.StaticLine(self.panel_1, wx.ID_ANY)
        static_line_1.SetMinSize((0, 2))
        sizer_4.Add(static_line_1, 0, 0, 0)
        sizer_4.Add(self.button_1, 0, 0, 0)
        sizer_4.Add((20, 20), 1, 0, 0)
        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "Fairing Coefficient: ")
        sizer_4.Add(label_1, 0, wx.ALL | wx.EXPAND, 4)
        sizer_4.Add(self.text_ctrl_fairing, 0, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 2)
        sizer_4.Add((200, 26), 0, wx.ALIGN_CENTER, 5)
        sizer_4.Add(self.button_plot, 0, 0, 0)
        sizer_4.Add(self.button_clear, 0, wx.LEFT, 8)
        sizer_2.Add(sizer_4, 0, wx.ALL | wx.EXPAND, 5)
        static_line_2 = wx.StaticLine(self.panel_1, wx.ID_ANY)
        sizer_6.Add(static_line_2, 0, wx.ALL | wx.EXPAND, 0)
        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, "Output Window")
        sizer_6.Add(label_2, 0, 0, 0)
        sizer_6.Add(self.text_ctrl_output, 0, wx.EXPAND, 0)
        sizer_5.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_5, 1, wx.EXPAND, 0)
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def on_button_plot(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'on_button_plot' not implemented!")
        event.Skip()

    def on_button_clear(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'on_button_clear' not implemented!")
        event.Skip()

    def on_import_button_clicked(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'on_import_button_clicked' not implemented!")
        event.Skip()
# end of class MyFrame
