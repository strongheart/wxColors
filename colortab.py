#! /usr/bin/python3

import wx
from wxColors import colors as wxcolors
from colorconvert import *
# import cv2  

TITLES="Name,Color,Hex,Red,Green,Blue,Decimal,Hue,Sat,Val".split(",")
colors=wxcolors.keys()
bg_heads="sienna"
fg_heads="gold"
bg_kids="tan"
fg_kids="brown"

class Colortab(wx.ScrolledWindow):
	def __init__(self,P):
		super().__init__(P)
		self.SetScrollRate(25,25)
		self.SetBackgroundColour(wx.Colour("Midnight Blue"))
		G=wx.FlexGridSizer(10,8,4) # tf:wx.TextEntry=wx.ComboBox(self,-1,s)
		self.heads=[]
		self.kids=[] # data cells
		self.colors=sorted(colors)
		# rubber stamp headders
		def butt(s):
			b=wx.Button(self,-1,s)
			b.SetBackgroundColour(bg_heads)
			b.SetForegroundColour(fg_heads)
			b.SetFont(wx.Font(wx.FontInfo(20).Bold()))
			self.heads.append(b)
			G.Add(b,1,wx.EXPAND|wx.ALL)
			b.Bind(wx.EVT_BUTTON,self.doSort) # for sorting columns
			return  b
		
		# conveniently rubber stamp cells
		def st(s):
			tf:wx.StaticText=wx.StaticText(self,-1,s, style=wx.BORDER_RAISED)
			
			tf.SetTransparent(0)
			tf.SetBackgroundColour(wx.Colour(bg_kids))
			tf.SetForegroundColour(wx.Colour(fg_kids))

			self.kids.append(tf)
			G.Add(tf,1,wx.EXPAND|wx.ALL)
		
		for title in TITLES:
			b=butt(title)

		"""stomp out rows of cells"""
		for c in colors:
			C=wx.Colour(c)
			r,g,b=C.Get(0)
			h,s,v=c2hsv(C)
			# print((h,s,v))
			st(c)
			w=wx.Window(self)
			w.SetBackgroundColour(C)
			self.kids.append(w)
			G.Add(w,1,wx.EXPAND|wx.ALL)
			st(f"{C.GetRGB():x}")
			st(str(r))
			st(str(g))
			st(str(b))
			st(str(C.GetRGB()))
			st(str(h))
			st(str(s))
			st(str(v))
		self.SetSizer(G)
		boo=[0,0,0,0,0,0,0,0,0,0]
		self.sorts=dict(zip(TITLES,boo ))
		# self.SetSize(self.GetBestVirtualSize()) 3 no good
		self.calcWidth()
		
	
	"""calculates and sets the width of headers and sizes self to show 10/11 rows. """
	def calcWidth(self)->None:
		W,H=self.heads[0].GetSize()
		# next 2 lins fix width.
		W+=6 
		W*=3
		for h in self.heads[1:]:
			W+=h.GetSize()[0]
		self.SetClientSize((W+88,H*12))
		self.Parent.Fit() # still too narrow
		print(f"size={(W,H*12)}  z={self.Size}")

	"""After sorting colors update cell data """
	def updateData(self, cc:list)->None:
		it=iter(self.kids)	
		print(f"==cc is  a {type(cc)}")
		for c in cc:	
			# print(f"color='{c}'")
			C=wx.Colour(c)
			d=C.GetRGB()
			x=f"{d:x}"
			r,g,b=C.Get(0)
			h,s,v=c2hsv(C)
			next(it).SetLabel(c)
			next(it).SetBackgroundColour(C)
			next(it).SetLabel(x)
			next(it).SetLabel(str(r))
			next(it).SetLabel(str(g))
			next(it).SetLabel(str(b))
			next(it).SetLabel(str(d))
			next(it).SetLabel(str(h))
			next(it).SetLabel(str(s))
			next(it).SetLabel(str(v))
		# self.Refresh()
		W,H=self.GetSize()
		self.SetSize(W,H+1) # why this works???
		# self.calcWidth()

	def doSort(self,e:wx.CommandEvent):
		b=e.EventObject
		t=b.GetLabel()
		cc={}

		def redness(c):
			r,g,b=c.Get(0)
			return 3*r-(g+b) # the more other colors the less redness
		def greenness(c):
			r,g,b=c.Get(0)
			return 3*g-(r+b)
		def blueness(c):
			r,g,b=c.Get(0)
			return 3*b-(g+r)
		def hness(c):
			h,s,v=c2hsv(c)
			return h
		def sness(c):
			h,s,v=c2hsv(c)
			return s
		def vness(c):
			h,s,v=c2hsv(c)
			return v

		
		match t: 
			case "Name":
				cc=sorted(colors, reverse=self.sorts[t])
				print(f"CC is A {type(cc)}")
			case "Decimal" | "Hex"	:
				cc=sorted(colors, key=lambda c: wx.Colour(c).GetRGB(), reverse=self.sorts[t] )
			case "Red":
				# cc=sorted(colors, key=lambda c: wx.Colour(c).Get(0)[0] , reverse=self.sorts[t] )
				cc=sorted(colors, key=lambda c: redness(wx.Colour(c)), reverse=self.sorts[t])
			case "Green":
				# cc=sorted(colors, key=lambda c: wx.Colour(c).Get(0)[1], reverse=self.sorts[t] )
				cc=sorted(colors, key=lambda c: greenness(wx.Colour(c)), reverse=self.sorts[t])
			case "Blue":
				# cc=sorted(colors, key=lambda c: wx.Colour(c).Get(0)[2], reverse=self.sorts[t] )
				cc=sorted(colors, key=lambda c: blueness(wx.Colour(c)), reverse=self.sorts[t])
			case "Hue":
				cc=sorted(colors, key=lambda c: c2hsv(wx.Colour(c))[0], reverse=self.sorts[t])
			case "Sat":
				cc=sorted(colors, key=lambda c: c2hsv(wx.Colour(c))[1], reverse=self.sorts[t])
			case "Val":
				cc=sorted(colors, key=lambda c: c2hsv(wx.Colour(c))[2], reverse=self.sorts[t])

		self.updateData(cc)				
		self.sorts[t]=0 if self.sorts[t] else 1

class InfoPan(wx.Panel):
	def __init__(self,P,c="BLACK"):
		super().__init__(P)
		G=wx.FlexGridSizer(10,6,4)
		def sb(t,s):
			# b=wx.StaticBox(self,-1,t)
			z=wx.StaticBoxSizer(wx.HORIZONTAL,self,t)
			T=wx.StaticText(z.GetStaticBox(),-1,s)
			z.Add(T)
			# G.Add(z.GetStaticBox(),1,wx.EXPAND|wx.ALL,2)
			return T
		C=wx.Colour(c)
		self.bn=sb("Name",c)
		self.bc=sb("Color","")
		self.bx=sb("Hex",f'{C.GetRGB():x}')
		self.br=sb("R",str(C.Get(0)[0]))
		self.bg=sb("G",str(C.Get(0)[1]))
		self.bb=sb("B",str(C.Get(0)[2]))
		self.bd=sb("Dec",f"{C.GetRGB()}")
		self.bh=sb("H",str(c2hsv(C)[0]))
		self.bs=sb("S",str(c2hsv(C)[1]))
		self.bv=sb("V",str(c2hsv(C)[2]))
		



	
class App(wx.App):
	def __init__(self):
		super().__init__()
		F=wx.Frame(None,-1,"WX COLORS")
		z=wx.BoxSizer(wx.VERTICAL)
		cp=Colortab(F)
		z.Add(cp,12,wx.EXPAND)
		# ip=InfoPan(F)
		# z.Add(ip,1)
		
		F.SetSizer(z)
		F.Show()

if __name__=="__main__":
	App().MainLoop()




