# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas, NavigationToolbar2WxAgg as NavigationToolbar

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Vircurex.com", pos = wx.DefaultPosition, size = wx.Size( 880,646 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel31 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_splitter1 = wx.SplitterWindow( self.m_panel31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter1.Bind( wx.EVT_IDLE, self.m_splitter1OnIdle )
		
		self.m_panel9 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		figChangeChoiceChoices = [ u"path", u"scatter" ]
		self.figChangeChoice = wx.Choice( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, figChangeChoiceChoices, 0 )
		self.figChangeChoice.SetSelection( 0 )
		bSizer17.Add( self.figChangeChoice, 0, wx.ALL, 5 )
		
		self.figure=Figure()
		self.figChange=FigCanvas(self.m_panel9, -1, self.figure)
		bSizer17.Add( self.figChange, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel9.SetSizer( bSizer17 )
		self.m_panel9.Layout()
		bSizer17.Fit( self.m_panel9 )
		self.m_panel10 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel4 = wx.Panel( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText4 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"base", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer12.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		choiceCurrency1Choices = []
		self.choiceCurrency1 = wx.Choice( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceCurrency1Choices, 0 )
		self.choiceCurrency1.SetSelection( 0 )
		bSizer12.Add( self.choiceCurrency1, 0, wx.ALL, 5 )
		
		
		bSizer11.Add( bSizer12, 0, wx.EXPAND, 5 )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"alt", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer13.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		choiceCurrency2Choices = []
		self.choiceCurrency2 = wx.Choice( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceCurrency2Choices, 0 )
		self.choiceCurrency2.SetSelection( 0 )
		bSizer13.Add( self.choiceCurrency2, 0, wx.ALL, 5 )
		
		
		bSizer11.Add( bSizer13, 0, wx.EXPAND, 5 )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblAmount = wx.StaticText( self.m_panel4, wx.ID_ANY, u"amount", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblAmount.Wrap( -1 )
		bSizer14.Add( self.lblAmount, 0, wx.ALL, 5 )
		
		self.spinAmount = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.spinAmount, 0, wx.ALL, 5 )
		
		
		bSizer11.Add( bSizer14, 0, wx.EXPAND, 5 )
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblPrice = wx.StaticText( self.m_panel4, wx.ID_ANY, u"price", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblPrice.Wrap( -1 )
		bSizer15.Add( self.lblPrice, 0, wx.ALL, 5 )
		
		self.spinPrice = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.spinPrice, 0, wx.ALL, 5 )
		
		
		bSizer11.Add( bSizer15, 0, wx.EXPAND, 5 )
		
		
		bSizer5.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radioBuy = wx.RadioButton( self.m_panel4, wx.ID_ANY, u"buy", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.radioBuy.SetValue( True ) 
		bSizer8.Add( self.radioBuy, 0, wx.ALL, 5 )
		
		self.radioSell = wx.RadioButton( self.m_panel4, wx.ID_ANY, u"sell", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.radioSell, 0, wx.ALL, 5 )
		
		self.btnCreateOrder = wx.Button( self.m_panel4, wx.ID_ANY, u"Create Order", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.btnCreateOrder, 0, wx.ALL, 5 )
		
		self.btnCreateReleaseOrder = wx.Button( self.m_panel4, wx.ID_ANY, u"Create and Release Order", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.btnCreateReleaseOrder, 0, wx.ALL, 5 )
		
		
		bSizer5.Add( bSizer8, 0, wx.EXPAND, 5 )
		
		
		self.m_panel4.SetSizer( bSizer5 )
		self.m_panel4.Layout()
		bSizer5.Fit( self.m_panel4 )
		bSizer18.Add( self.m_panel4, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel5 = wx.Panel( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer1.AddGrowableCol( 0 )
		fgSizer1.AddGrowableCol( 1 )
		fgSizer1.AddGrowableRow( 1 )
		fgSizer1.SetFlexibleDirection( wx.VERTICAL )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel7 = wx.Panel( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText8 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Buy Orders", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer20.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		
		self.m_panel7.SetSizer( bSizer20 )
		self.m_panel7.Layout()
		bSizer20.Fit( self.m_panel7 )
		fgSizer1.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel8 = wx.Panel( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText9 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Sell Orders", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer21.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		
		self.m_panel8.SetSizer( bSizer21 )
		self.m_panel8.Layout()
		bSizer21.Fit( self.m_panel8 )
		fgSizer1.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.listBuyOrders = wx.ListCtrl( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		fgSizer1.Add( self.listBuyOrders, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.listSellOrders = wx.ListCtrl( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		fgSizer1.Add( self.listSellOrders, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel5.SetSizer( fgSizer1 )
		self.m_panel5.Layout()
		fgSizer1.Fit( self.m_panel5 )
		bSizer18.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel10.SetSizer( bSizer18 )
		self.m_panel10.Layout()
		bSizer18.Fit( self.m_panel10 )
		self.m_splitter1.SplitHorizontally( self.m_panel9, self.m_panel10, 0 )
		bSizer4.Add( self.m_splitter1, 1, wx.EXPAND, 5 )
		
		
		self.m_panel31.SetSizer( bSizer4 )
		self.m_panel31.Layout()
		bSizer4.Fit( self.m_panel31 )
		self.m_notebook1.AddPage( self.m_panel31, u"new order", True )
		self.m_panel6 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Unreleased", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer7.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.lstUnreleasedOrders = wx.ListCtrl( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		bSizer7.Add( self.lstUnreleasedOrders, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnDeleteUnreleased = wx.Button( self.m_panel6, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.btnDeleteUnreleased, 0, wx.ALL, 5 )
		
		self.btnDeleteAllUnreleased = wx.Button( self.m_panel6, wx.ID_ANY, u"Delete All", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.btnDeleteAllUnreleased, 0, wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer16, 0, wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Released", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer7.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.lstReleasedOrders = wx.ListCtrl( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		bSizer7.Add( self.lstReleasedOrders, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer161 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnDeleteReleased = wx.Button( self.m_panel6, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer161.Add( self.btnDeleteReleased, 0, wx.ALL, 5 )
		
		self.btnDeleteAllReleased = wx.Button( self.m_panel6, wx.ID_ANY, u"Delete All", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer161.Add( self.btnDeleteAllReleased, 0, wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer161, 0, wx.EXPAND, 5 )
		
		
		self.m_panel6.SetSizer( bSizer7 )
		self.m_panel6.Layout()
		bSizer7.Fit( self.m_panel6 )
		self.m_notebook1.AddPage( self.m_panel6, u"orders", False )
		self.m_panel3 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.lstBalance = wx.ListCtrl( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		bSizer2.Add( self.lstBalance, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel3.SetSizer( bSizer2 )
		self.m_panel3.Layout()
		bSizer2.Fit( self.m_panel3 )
		self.m_notebook1.AddPage( self.m_panel3, u"balance", False )
		self.m_panel61 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer71 = wx.BoxSizer( wx.VERTICAL )
		
		self.lstCurrencyInfo = wx.ListCtrl( self.m_panel61, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		bSizer71.Add( self.lstCurrencyInfo, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel61.SetSizer( bSizer71 )
		self.m_panel61.Layout()
		bSizer71.Fit( self.m_panel61 )
		self.m_notebook1.AddPage( self.m_panel61, u"currency info", False )
		
		bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar2 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Account Setup", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem3 )
		
		self.m_menu1.AppendSeparator()
		
		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Quit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem2 )
		
		self.m_menubar2.Append( self.m_menu1, u"File" ) 
		
		self.m_menu2 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_menuItem1 )
		
		self.m_menubar2.Append( self.m_menu2, u"?" ) 
		
		self.SetMenuBar( self.m_menubar2 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.figChangeChoice.Bind( wx.EVT_CHOICE, self.onFigChangeChoice )
		self.choiceCurrency1.Bind( wx.EVT_CHOICE, self.onChoiceCurrency1 )
		self.choiceCurrency2.Bind( wx.EVT_CHOICE, self.onChoiceCurrency2 )
		self.btnCreateOrder.Bind( wx.EVT_BUTTON, self.onBtnCreateOrder )
		self.btnCreateReleaseOrder.Bind( wx.EVT_BUTTON, self.onBtnCreateReleaseOrder )
		self.listBuyOrders.Bind( wx.EVT_LIST_ITEM_SELECTED, self.onListBuyOrderItemSelected )
		self.listSellOrders.Bind( wx.EVT_LIST_ITEM_SELECTED, self.onListSellOrderItemSelected )
		self.btnDeleteUnreleased.Bind( wx.EVT_BUTTON, self.onBtnDeleteUnreleased )
		self.btnDeleteAllUnreleased.Bind( wx.EVT_BUTTON, self.onBtnDeleteAllUnreleased )
		self.btnDeleteReleased.Bind( wx.EVT_BUTTON, self.onBtnDeleteReleased )
		self.btnDeleteAllReleased.Bind( wx.EVT_BUTTON, self.onBtnDeleteAllReleased )
		self.Bind( wx.EVT_MENU, self.onMenuAccountSetup, id = self.m_menuItem3.GetId() )
		self.Bind( wx.EVT_MENU, self.onMenuQuit, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.onMenuAbout, id = self.m_menuItem1.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onFigChangeChoice( self, event ):
		event.Skip()
	
	def onChoiceCurrency1( self, event ):
		event.Skip()
	
	def onChoiceCurrency2( self, event ):
		event.Skip()
	
	def onBtnCreateOrder( self, event ):
		event.Skip()
	
	def onBtnCreateReleaseOrder( self, event ):
		event.Skip()
	
	def onListBuyOrderItemSelected( self, event ):
		event.Skip()
	
	def onListSellOrderItemSelected( self, event ):
		event.Skip()
	
	def onBtnDeleteUnreleased( self, event ):
		event.Skip()
	
	def onBtnDeleteAllUnreleased( self, event ):
		event.Skip()
	
	def onBtnDeleteReleased( self, event ):
		event.Skip()
	
	def onBtnDeleteAllReleased( self, event ):
		event.Skip()
	
	def onMenuAccountSetup( self, event ):
		event.Skip()
	
	def onMenuQuit( self, event ):
		event.Skip()
	
	def onMenuAbout( self, event ):
		event.Skip()
	
	def m_splitter1OnIdle( self, event ):
		self.m_splitter1.SetSashPosition( 0 )
		self.m_splitter1.Unbind( wx.EVT_IDLE )
	

###########################################################################
## Class DialogAccount
###########################################################################

class DialogAccount ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Account", pos = wx.DefaultPosition, size = wx.Size( 468,392 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer19 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		bSizer21.Add( self.m_staticText35, 0, wx.ALL, 5 )
		
		self.textUsername = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.textUsername, 1, wx.ALL, 5 )
		
		
		bSizer19.Add( bSizer21, 0, wx.EXPAND, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Get balance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		fgSizer3.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.textGetBalance = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer3.Add( self.textGetBalance, 0, wx.ALL, 5 )
		
		self.m_staticText151 = wx.StaticText( self, wx.ID_ANY, u"Create order", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText151.Wrap( -1 )
		fgSizer3.Add( self.m_staticText151, 0, wx.ALL, 5 )
		
		self.textCreateOrder = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer3.Add( self.textCreateOrder, 0, wx.ALL, 5 )
		
		self.m_staticText152 = wx.StaticText( self, wx.ID_ANY, u"Release order", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText152.Wrap( -1 )
		fgSizer3.Add( self.m_staticText152, 0, wx.ALL, 5 )
		
		self.textReleaseOrder = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer3.Add( self.textReleaseOrder, 0, wx.ALL, 5 )
		
		self.m_staticText153 = wx.StaticText( self, wx.ID_ANY, u"Delete order", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText153.Wrap( -1 )
		fgSizer3.Add( self.m_staticText153, 0, wx.ALL, 5 )
		
		self.textDeleteOrder = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer3.Add( self.textDeleteOrder, 0, wx.ALL, 5 )
		
		self.m_staticText154 = wx.StaticText( self, wx.ID_ANY, u"Read order", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText154.Wrap( -1 )
		fgSizer3.Add( self.m_staticText154, 0, wx.ALL, 5 )
		
		self.textReadOrder = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer3.Add( self.textReadOrder, 0, wx.ALL, 5 )
		
		self.m_staticText155 = wx.StaticText( self, wx.ID_ANY, u"Read orders", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText155.Wrap( -1 )
		fgSizer3.Add( self.m_staticText155, 0, wx.ALL, 5 )
		
		self.textReadOrders = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer3.Add( self.textReadOrders, 0, wx.ALL, 5 )
		
		self.m_staticText156 = wx.StaticText( self, wx.ID_ANY, u"Read orderexecutions", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText156.Wrap( -1 )
		fgSizer3.Add( self.m_staticText156, 0, wx.ALL, 5 )
		
		self.textReadOrderExecutions = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer3.Add( self.textReadOrderExecutions, 0, wx.ALL, 5 )
		
		self.m_staticText157 = wx.StaticText( self, wx.ID_ANY, u"Create coupon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText157.Wrap( -1 )
		fgSizer3.Add( self.m_staticText157, 0, wx.ALL, 5 )
		
		self.textCreateCoupon = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer3.Add( self.textCreateCoupon, 0, wx.ALL, 5 )
		
		self.m_staticText158 = wx.StaticText( self, wx.ID_ANY, u"Redeem coupon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText158.Wrap( -1 )
		fgSizer3.Add( self.m_staticText158, 0, wx.ALL, 5 )
		
		self.textRedeemCoupon = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer3.Add( self.textRedeemCoupon, 0, wx.ALL, 5 )
		
		
		bSizer19.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnSave = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.btnSave, 0, wx.ALL, 5 )
		
		self.btnCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.btnCancel, 0, wx.ALL, 5 )
		
		
		bSizer19.Add( bSizer20, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer19 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnSave.Bind( wx.EVT_BUTTON, self.onBtnSave )
		self.btnCancel.Bind( wx.EVT_BUTTON, self.onBtnCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onBtnSave( self, event ):
		event.Skip()
	
	def onBtnCancel( self, event ):
		event.Skip()
	

