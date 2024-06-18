#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Created on Mon Jun 17 17:04:36 2024
These are the wx Named Colors (Colours) and their hex values
@author: steve
"""
colors=\
{
	"AQUAMARINE":	0x93db70,
	"FIREBRICK":	0x23238e,
	"MEDIUM FOREST GREEN":	0x238e6b,
	"RED":	0x0000ff,
	"BLACK":	0x000000,
	"FOREST GREEN":	0x238e23,
	"MEDIUM GOLDENROD":	0xadeaea,
	"SALMON":	0x42426f,
	"BLUE":	0xff0000,
	"GOLD":	0x327fcc,
	"MEDIUM ORCHID":	0xdb7093,
	"SEA GREEN":	0x6b8e23,
	"BLUE VIOLET":	0x9f5f9f,
	"GOLDENROD":	0x70dbdb,
	"MEDIUM SEA GREEN":	0x426f42,
	"SIENNA":	0x236b8e,
	"BROWN":	0x2a2aa5,
	"GREY":	0x808080,
	"MEDIUM SLATE BLUE":	0xff007f,
	"SKY BLUE":	0xcc9932,
	"CADET BLUE":	0x9f9f5f,
	"GREEN":	0x00ff00,
	"MEDIUM SPRING GREEN":	0x00ff7f,
	"SLATE BLUE":	0xff7f00,
	"CORAL":	0x007fff,
	"GREEN YELLOW":	0x70db93,
	"MEDIUM TURQUOISE":	0xdbdb70,
	"SPRING GREEN":	0x7fff00,
	"CORNFLOWER BLUE":	0x6f4242,
	"INDIAN RED":	0x2f2f4f,
	"MEDIUM VIOLET RED":	0x9370db,
	"STEEL BLUE":	0x8e6b23,
	"CYAN":	0xffff00,
	"KHAKI":	0x5f9f9f,
	"MIDNIGHT BLUE":	0x4f2f2f,
	"TAN":	0x7093db,
	"DARK GREY":	0x2f2f2f,
	"LIGHT BLUE":	0xd8d8bf,
	"NAVY":	0x8e2323,
	"THISTLE":	0xd8bfd8,
	"DARK GREEN":	0x2f4f2f,
	"LIGHT GREY":	0xc0c0c0,
	"ORANGE":	0x3232cc,
	"TURQUOISE":	0xeaeaad,
	"DARK OLIVE GREEN":	0x2f4f4f,
	"LIGHT STEEL BLUE":	0xbc8f8f,
	"ORANGE RED":	0x7f00ff,
	"VIOLET":	0x4f2f4f,
	"DARK ORCHID":	0xcc3299,
	"LIME GREEN":	0x32cc32,
	"ORCHID":	0xdb70db,
	"VIOLET RED":	0x9932cc,
	"DARK SLATE BLUE":	0x8e236b,
	"MAGENTA":	0xff00ff,
	"PALE GREEN":	0x8fbc8f,
	"WHEAT":	0xbfd8d8,
	"DARK SLATE GREY":	0x4f4f2f,
	"MAROON":	0x6b238e,
	"PINK":	0xcbc0ff,
	"WHITE":	0xffffff,
	"DARK TURQUOISE":	0xdb9370,
	"MEDIUM AQUAMARINE":	0x99cc32,
	"PLUM":	0xeaadea,
	"YELLOW":	0x00ffff,
	"DIM GREY":	0x545454,
	"MEDIUM BLUE":	0xcc3232,
	"PURPLE":	0xff00b0,
	"YELLOW GREEN":	0x32cc99,
}

def torgb(x):
	r=x>> 16 & 0xFF
	g=x>> 8 & 0xff
	b=x&0xff
	return r,g,b




