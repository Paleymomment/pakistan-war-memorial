import socket
import os
import winreg
import PySimpleGUI as sg
from time import time, sleep

#Start off the program with the popup LO
sg.popup("paley jumpscare popup LOL")

# now do it EVERY FUCKING HOUR
while True:
    sleep(60 - time() % 60)
    sg.popup("paley jumpscare popup LOL")

def create_key(name: str="default", path: ""=str)->bool:
    # initialize key (create) or open
    reg_key = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER,
                                 r'Software\Microsoft\Windows\CurrentVersion\Run',
                                 0,
                                 winreg.KEY_WRITE)

    # CreateKey returns a handle
    # if null it failed
    if not reg_key:
        return False

    # set the value of created key
    winreg.SetValueEx(reg_key, # key
        name,
        0,
        winreg.REG_SZ,
        path) # set file path

    # close key (think of it as opening a file)
    reg_key.Close()
    return True
