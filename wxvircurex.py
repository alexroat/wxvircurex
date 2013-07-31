import wx
import time
import datetime
import matplotlib
import matplotlib.dates
from gui import *
from vircurex import Vircurex
from configobj import *

lgpl='''                   GNU LESSER GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.


  This version of the GNU Lesser General Public License incorporates
the terms and conditions of version 3 of the GNU General Public
License, supplemented by the additional permissions listed below.

  0. Additional Definitions.

  As used herein, "this License" refers to version 3 of the GNU Lesser
General Public License, and the "GNU GPL" refers to version 3 of the GNU
General Public License.

  "The Library" refers to a covered work governed by this License,
other than an Application or a Combined Work as defined below.

  An "Application" is any work that makes use of an interface provided
by the Library, but which is not otherwise based on the Library.
Defining a subclass of a class defined by the Library is deemed a mode
of using an interface provided by the Library.

  A "Combined Work" is a work produced by combining or linking an
Application with the Library.  The particular version of the Library
with which the Combined Work was made is also called the "Linked
Version".

  The "Minimal Corresponding Source" for a Combined Work means the
Corresponding Source for the Combined Work, excluding any source code
for portions of the Combined Work that, considered in isolation, are
based on the Application, and not on the Linked Version.

  The "Corresponding Application Code" for a Combined Work means the
object code and/or source code for the Application, including any data
and utility programs needed for reproducing the Combined Work from the
Application, but excluding the System Libraries of the Combined Work.

  1. Exception to Section 3 of the GNU GPL.

  You may convey a covered work under sections 3 and 4 of this License
without being bound by section 3 of the GNU GPL.

  2. Conveying Modified Versions.

  If you modify a copy of the Library, and, in your modifications, a
facility refers to a function or data to be supplied by an Application
that uses the facility (other than as an argument passed when the
facility is invoked), then you may convey a copy of the modified
version:

   a) under this License, provided that you make a good faith effort to
   ensure that, in the event an Application does not supply the
   function or data, the facility still operates, and performs
   whatever part of its purpose remains meaningful, or

   b) under the GNU GPL, with none of the additional permissions of
   this License applicable to that copy.

  3. Object Code Incorporating Material from Library Header Files.

  The object code form of an Application may incorporate material from
a header file that is part of the Library.  You may convey such object
code under terms of your choice, provided that, if the incorporated
material is not limited to numerical parameters, data structure
layouts and accessors, or small macros, inline functions and templates
(ten or fewer lines in length), you do both of the following:

   a) Give prominent notice with each copy of the object code that the
   Library is used in it and that the Library and its use are
   covered by this License.

   b) Accompany the object code with a copy of the GNU GPL and this license
   document.

  4. Combined Works.

  You may convey a Combined Work under terms of your choice that,
taken together, effectively do not restrict modification of the
portions of the Library contained in the Combined Work and reverse
engineering for debugging such modifications, if you also do each of
the following:

   a) Give prominent notice with each copy of the Combined Work that
   the Library is used in it and that the Library and its use are
   covered by this License.

   b) Accompany the Combined Work with a copy of the GNU GPL and this license
   document.

   c) For a Combined Work that displays copyright notices during
   execution, include the copyright notice for the Library among
   these notices, as well as a reference directing the user to the
   copies of the GNU GPL and this license document.

   d) Do one of the following:

       0) Convey the Minimal Corresponding Source under the terms of this
       License, and the Corresponding Application Code in a form
       suitable for, and under terms that permit, the user to
       recombine or relink the Application with a modified version of
       the Linked Version to produce a modified Combined Work, in the
       manner specified by section 6 of the GNU GPL for conveying
       Corresponding Source.

       1) Use a suitable shared library mechanism for linking with the
       Library.  A suitable mechanism is one that (a) uses at run time
       a copy of the Library already present on the user's computer
       system, and (b) will operate properly with a modified version
       of the Library that is interface-compatible with the Linked
       Version.

   e) Provide Installation Information, but only if you would otherwise
   be required to provide such information under section 6 of the
   GNU GPL, and only to the extent that such information is
   necessary to install and execute a modified version of the
   Combined Work produced by recombining or relinking the
   Application with a modified version of the Linked Version. (If
   you use option 4d0, the Installation Information must accompany
   the Minimal Corresponding Source and Corresponding Application
   Code. If you use option 4d1, you must provide the Installation
   Information in the manner specified by section 6 of the GNU GPL
   for conveying Corresponding Source.)

  5. Combined Libraries.

  You may place library facilities that are a work based on the
Library side by side in a single library together with other library
facilities that are not Applications and are not covered by this
License, and convey such a combined library under terms of your
choice, if you do both of the following:

   a) Accompany the combined library with a copy of the same work based
   on the Library, uncombined with any other library facilities,
   conveyed under the terms of this License.

   b) Give prominent notice with the combined library that part of it
   is a work based on the Library, and explaining where to find the
   accompanying uncombined form of the same work.

  6. Revised Versions of the GNU Lesser General Public License.

  The Free Software Foundation may publish revised and/or new versions
of the GNU Lesser General Public License from time to time. Such new
versions will be similar in spirit to the present version, but may
differ in detail to address new problems or concerns.

  Each version is given a distinguishing version number. If the
Library as you received it specifies that a certain numbered version
of the GNU Lesser General Public License "or any later version"
applies to it, you have the option of following the terms and
conditions either of that published version or of any later version
published by the Free Software Foundation. If the Library as you
received it does not specify a version number of the GNU Lesser
General Public License, you may choose any version of the GNU Lesser
General Public License ever published by the Free Software Foundation.

  If the Library as you received it specifies that a proxy can decide
whether future versions of the GNU Lesser General Public License shall
apply, that proxy's public statement of acceptance of any version is
permanent authorization for you to choose that version for the
Library.'''

def getListCtrlItemsText(listctrl,item):
	return [listctrl.GetItem(item,c).GetText() for c in xrange(listctrl.GetColumnCount())]
def getListCtrlFirstSelectedItemsText(listctrl):
	return getListCtrlItemsText(listctrl,listctrl.GetFirstSelected())
def getListCtrlSelectedItemsText(listctrl):
	return [getListCtrlItemsText(listctrl,i) for i in xrange(listctrl.GetItemCount()) if listctrl.IsSelected(i)]
def getListCtrlAllItemsText(listctrl):
	return [getListCtrlItemsText(listctrl,i) for i in xrange(listctrl.GetItemCount())]
	
class VircurexFrame(MainFrame):
	def __init__(self):
		MainFrame.__init__(self,None)
		self.SetIcon(wx.Icon("64.ico", wx.BITMAP_TYPE_ICO))
		self.client=Vircurex()
		self.config=ConfigObj("wxvircurex.cfg")
		self.applyConfig()
		self.updateAll()
	def updateAll(self):
		try:
			self.updateBalance()
			self.updateOrders()
			self.updateCurrencyInfo()
			self.updateNewOrder()
		except:
			pass
	def updateBalance(self):
		self.lstBalance.ClearAll()
		self.lstBalance.InsertColumn(0, 'Currency')
		self.lstBalance.InsertColumn(1, 'balance')
		self.lstBalance.InsertColumn(2, 'available balance')
		balances=self.client.get_balances()["balances"]
		for k,v in balances.items():
			self.lstBalance.Append([k,v["balance"],v["availablebalance"]])
	def updateOrders(self):
		self.lstUnreleasedOrders.ClearAll()
		self.lstUnreleasedOrders.InsertColumn(0, 'id')
		self.lstUnreleasedOrders.InsertColumn(1, 'type')
		self.lstUnreleasedOrders.InsertColumn(2, 'from')
		self.lstUnreleasedOrders.InsertColumn(3, 'to')
		self.lstUnreleasedOrders.InsertColumn(4, 'amount')
		self.lstUnreleasedOrders.InsertColumn(5, 'price')
		self.lstUnreleasedOrders.InsertColumn(6, 'createtime')
		for k,v in self.client.read_orders(0).items():
			if k.startswith("order-"):
				self.lstUnreleasedOrders.Append(map(lambda x:v[x],["orderid","ordertype","currency1","currency2","quantity","unitprice","createdat"]))
		self.lstReleasedOrders.ClearAll()
		self.lstReleasedOrders.InsertColumn(0, 'id')
		self.lstReleasedOrders.InsertColumn(1, 'type')
		self.lstReleasedOrders.InsertColumn(2, 'from')
		self.lstReleasedOrders.InsertColumn(3, 'to')
		self.lstReleasedOrders.InsertColumn(4, 'amount')
		self.lstReleasedOrders.InsertColumn(5, 'price')
		self.lstReleasedOrders.InsertColumn(6, 'createtime')
		for k,v in self.client.read_orders(1).items():
			if k.startswith("order-"):
				self.lstUnreleasedOrders.Append(map(lambda x:v[x],["orderid","ordertype","currency1","currency2","quantity","unitprice","createdat"]))		
	def getCurrencies(self):
		return self.client.get_currency_info().keys()
	def updateNewOrder(self):
		currencies=self.getCurrencies()
		self.choiceCurrency1.Clear()
		self.choiceCurrency1.AppendItems(currencies)
		self.choiceCurrency2.Clear()
		self.choiceCurrency2.AppendItems(currencies)
	def updateFigure(self):
		c1=self.choiceCurrency1.GetStringSelection()
		c2=self.choiceCurrency2.GetStringSelection()
		#ottiene gli utlimi ordini
		trades=self.client.trades(c1,c2)
		dates=map(lambda x: long(x["date"]),trades)
		prices=map(lambda x: float(x["price"]),trades)
		amounts=map(lambda x: float(x["amount"]),trades)
		#crea gli assi
		self.figure.clear()
		ax = self.figure.add_subplot(111)
		#riordina per data
		dates,prices,amounts=zip(*sorted(zip(dates,prices,amounts)))
		ts=[datetime.datetime.fromtimestamp(t) for t in dates]
		if self.figChangeChoice.GetStringSelection()=="path":
			ax.plot(ts, prices, '-o')
		else:
			k=100/max(amounts)
			amounts=map(lambda x:x*k,amounts)
			ax.scatter(ts, prices, s=amounts, alpha=0.50)
		self.figure.autofmt_xdate()
		self.figChange.draw()
	def updateNewOrderOrderbook(self):
		c1=self.choiceCurrency1.GetStringSelection()
		c2=self.choiceCurrency2.GetStringSelection()
		self.lblAmount.SetLabel('amount [%s]'%c1)
		self.lblPrice.SetLabel('price [%s/%s]'%(c2,c1))
		ob=self.client.orderbook(c1,c2)
		self.listBuyOrders.ClearAll()
		self.listBuyOrders.InsertColumn(0, 'price [%s/%s]'%(c2,c1))
		self.listBuyOrders.InsertColumn(1, 'quantity [%s]'%c1) 
		self.listBuyOrders.InsertColumn(2, 'volume [%s]'%c2)
		for price,quantity in ob["bids"]:	
			self.listBuyOrders.Append([price,quantity, float(price)*float(quantity)])
		self.listSellOrders.ClearAll()
		self.listSellOrders.InsertColumn(0, 'price [%s/%s]'%(c2,c1))
		self.listSellOrders.InsertColumn(1, 'quantity [%s]'%c1)
		self.listSellOrders.InsertColumn(2, 'volume [%s]'%c2)
		for price,quantity in ob["asks"]:	
			self.listSellOrders.Append([price,quantity, float(price)*float(quantity)])
	def updateCurrencyInfo(self):
		self.lstCurrencyInfo.ClearAll()
		self.lstCurrencyInfo.InsertColumn(0, 'currency')
		self.lstCurrencyInfo.InsertColumn(1, 'name')
		self.lstCurrencyInfo.InsertColumn(2, 'max_daily_withdrawal')
		self.lstCurrencyInfo.InsertColumn(3, 'withdrawal_fee')
		self.lstCurrencyInfo.InsertColumn(4, 'confirmations')
		for k,v in self.client.get_currency_info().items():
			self.lstCurrencyInfo.Append([k,v["name"],v["max_daily_withdrawal"],v["withdrawal_fee"],v["confirmations"]])
			#override eventi
	def getNewOrderDef(self):
		action=self.radioBuy.GetValue() and "buy" or "sell"
		c1=self.choiceCurrency1.GetStringSelection()
		c2=self.choiceCurrency2.GetStringSelection()
		amount=float(self.spinAmount.GetValue())
		price=float(self.spinPrice.GetValue())
		return action,c1,c2,amount,price
	def onBtnCreateOrder( self, event ):
		print self.getNewOrderDef()
		action,c1,c2,amount,price=self.getNewOrderDef()
		self.client.create_order(action,amount,c1,price,c2)#create order
		self.updateOrders()
	def onBtnCreateReleaseOrder( self, event ):
		print self.getNewOrderDef()
	def onChoiceCurrency1( self, event ):
		self.updateNewOrderOrderbook()
		self.updateFigure()
	def onChoiceCurrency2( self, event ):
		self.updateNewOrderOrderbook()
		self.updateFigure()
	def onFigChangeChoice( self, event ):
		self.updateFigure()
	def onListBuyOrderItemSelected( self, event ):
		price,quantity,volume=map(float,getListCtrlFirstSelectedItemsText(self.listBuyOrders))
		self.spinPrice.SetValue(str(price))
		self.spinAmount.SetValue(str(quantity))
		self.radioSell.SetValue(True)
	def onListSellOrderItemSelected( self, event ):
		price,quantity,volume=map(float,getListCtrlFirstSelectedItemsText(self.listSellOrders))
		self.spinPrice.SetValue(str(price))
		self.spinAmount.SetValue(str(quantity))
		self.radioBuy.SetValue(True)
	def onBtnDeleteUnreleased( self, event ):
		for r in getListCtrlSelectedItemsText(self.lstUnreleasedOrders):
			self.client.delete_order(r[0],0)
		self.updateOrders()
	def onBtnDeleteAllUnreleased( self, event ):
		for r in getListCtrlAllItemsText(self.lstUnreleasedOrders):
			self.client.delete_order(r[0],0)
		self.updateOrders()
	def onBtnDeleteReleased( self, event ):
		for r in getListCtrlSelectedItemsText(self.lstUnreleasedOrders):
			self.client.delete_order(r[0],1)
		self.updateOrders()
	def onBtnDeleteAllReleased( self, event ):
		for r in getListCtrlAllItemsText(self.lstUnreleasedOrders):
			self.client.delete_order(r[0],1)
		self.updateOrders()
	def onMenuAccountSetup( self, event ):
		VircurexDialogAccount(self).ShowModal()
	def onMenuQuit( self, event ):
		event.Skip()
	def onMenuAbout( self, event ):
		global lgpl
		description="A standalone client for Cryptocurrency Exchange Market vircurex.com"
		info = wx.AboutDialogInfo()
		info.SetIcon(wx.Icon('logo.png', wx.BITMAP_TYPE_PNG))
		info.SetName('WxVircurex')
		info.SetVersion('1.0')
		info.SetDescription(description)
		info.SetCopyright('(C) 2013 Alessandro Roat')
		info.SetLicence(lgpl)
		info.AddDeveloper('Alessandro Roat')
		wx.AboutBox(info).ShowModal()
	def applyConfig(self):
		self.config.reload()
		self.client.user=self.config.get('username')
		self.client.secrets['get_balance']=self.config.get('get_balance')
		self.client.secrets['create_order']=self.config.get('create_order')
		self.client.secrets['release_order']=self.config.get('release_order')
		self.client.secrets['delete_order']=self.config.get('delete_order')
		self.client.secrets['read_order']=self.config.get('read_order')
		self.client.secrets['read_orders']=self.config.get('read_orders')
		self.client.secrets['read_orderexecutions']=self.config.get('read_orderexecutions')
		self.client.secrets['create_coupon']=self.config.get('create_coupon')
		self.client.secrets['redeem_coupon']=self.config.get('redeem_coupon')
		print "config applied"
class VircurexDialogAccount(DialogAccount):
	def __init__(self,parent):
		DialogAccount.__init__(self,parent)
		cfg=self.GetParent().config
		cfg.reload()
		self.GetParent().applyConfig()
		self.textUsername.SetValue(cfg.get("username",""))
		self.textGetBalance.SetValue(cfg.get("get_balance",""))
		self.textCreateOrder.SetValue(cfg.get("create_order",""))
		self.textReleaseOrder.SetValue(cfg.get("release_order",""))
		self.textDeleteOrder.SetValue(cfg.get("delete_order",""))
		self.textReadOrder.SetValue(cfg.get("read_order",""))
		self.textReadOrders.SetValue(cfg.get("read_orders",""))
		self.textReadOrderExecutions.SetValue(cfg.get("read_orderexecutions",""))
		self.textCreateCoupon.SetValue(cfg.get("create_coupon",""))
		self.textRedeemCoupon.SetValue(cfg.get("redeem_coupon",""))
	def onBtnSave( self, event ):
		cfg=self.GetParent().config
		cfg["username"]=self.textUsername.GetValue()
		cfg["get_balance"]=self.textGetBalance.GetValue()
		cfg["create_order"]=self.textCreateOrder.GetValue()
		cfg["release_order"]=self.textReleaseOrder.GetValue()
		cfg["delete_order"]=self.textDeleteOrder.GetValue()
		cfg["read_order"]=self.textReadOrder.GetValue()
		cfg["read_orders"]=self.textReadOrders.GetValue()
		cfg["read_orderexecutions"]=self.textReadOrderExecutions.GetValue()
		cfg["create_coupon"]=self.textCreateCoupon.GetValue()
		cfg["redeem_coupon"]=self.textRedeemCoupon.GetValue()
		cfg.write()
		self.GetParent().applyConfig()
		self.GetParent().updateAll()
		self.Destroy()
	def onBtnCancel( self, event ):
		self.GetParent().applyConfig()
		self.GetParent().updateAll()
		self.Destroy()
		
class MyApp(wx.App):
	def __init__(self, redirect=False, filename=None):
		wx.App.__init__(self, redirect, filename)
		self.frame = VircurexFrame()
		self.frame.Show()
		

if __name__ == '__main__':
	app = MyApp()
	app.MainLoop()

