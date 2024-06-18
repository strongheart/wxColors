"""
algorithm modified from wiki page
the values are good enough to make sorting patterns.
"""
import wx


def rgb(C:wx.Colour):
	return C.Get(0)

def c2hsv(C):
	return rgb2hsv(*rgb(C))

def rgb2hsv(R,G,B):
	r,g,b= R,G,B 
	m=min(r,g,b)
	M=max(r,g,b)
	d=M-m
	# print(f"M,m,d={(M,m,d)} for {{r,g,b}}")
	H=0
	if d!=0:
		if M==r:
			H=60*((g-b)/d)%6
		elif M==g:
			H=60*((b-r)/d+2)
		elif M==b:
			H=60*((r-g)/d+4)
	S=0 if M==0 else d/M
	V=M
	h=int(H)
	s=int(S*255)
	# print(h,s,V)
	return h,s,V


