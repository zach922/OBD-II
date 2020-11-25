import os 
import time
import Diagnostics as da
import PySimpleGUI as sg

SCREENX = 1920
SCREENY = 1080

print("### PROGRAM STARTING ###")

diag = da.Diagnostics()
layout = [[sg.Text(str(diag.speed)+" MPH")],[sg.Text(str(diag.RPM)+" RPM")],[sg.Button("Close")]]

sg.theme('Dark Brown 4')
win = sg.Window("HUD", layout, no_titlebar=True, location=(0,0), size=(SCREENX,SCREENY), keep_on_top=True).Finalize()
win.Maximize()

print("    ### INIALIZED AND EXECUTING ###")

while True:
    event, values = win.read()

    if event == "Close" or event == sg.WIN_CLOSED:
        break

win.close()
print ("### PROGRAM TERMINATING ###")
