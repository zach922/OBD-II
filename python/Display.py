import os 
import time
import Diagnostics as da
import PySimpleGUI as sg

SCREENX = 1920
SCREENY = 1080

diag = da.Diagnostics()
layout = [[sg.Text(diag.speed)],[sg.Button("OK")]]

win = sg.Window("HUD", layout, no_titlebar=True, location=(0,0), size=(SCREENX,SCREENY), keep_on_top=True).Finalize()
win.Maximize()



while True:
    event, values = win.read()

    if event == "OK" or event == sg.WIN_CLOSED:
        break

win.close()
print ("Program Terminated")
