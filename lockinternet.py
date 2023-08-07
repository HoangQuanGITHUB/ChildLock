import os

def turn_off_wifi():
    os.system("netsh interface set interface Wi-Fi admin=disable")

def turn_on_wifi():
    os.system("netsh interface set interface Wi-Fi admin=enable")
