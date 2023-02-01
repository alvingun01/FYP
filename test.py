from escpos import *
import os
import sys 
from win32 import win32print
p = win32print.OpenPrinter ("EPSON L3110 Series")
job = win32print.StartDocPrinter(p, 1, ("test of raw data", None, "RAW")) 
win32print.StartPagePrinter(p) 
win32print.WritePrinter(p, b"\n\n\ndata to print \n blablabla \n line 3") 
win32print.EndPagePrinter(p)
# Printer = printer.Usb(0x04B8, 0x1142)
# Printer.text("requirements")