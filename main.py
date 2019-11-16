#!/usr/bin/env python3
import subprocess
import pyautogui
import urllib.request
import time

bg_url = None
bg_path = "/home/alan/Pictures/unsplash/"

def getResolution():
    global bg_url
    try:
        width, height = pyautogui.size()
        bg_url = "https://source.unsplash.com/random/"+str(width)+"x"+str(height)
        print("log: image url = ", bg_url)
    except:
        bg_url = "https://source.unsplash.com/random"
        print("ERROR getting resolution")


def downloadImage():
    try:
        global bg_url, bg_path
        timestr = time.strftime("%Y%m%d-%H%M%S")
        bg_path += str(timestr) +".jpg"
        data = urllib.request.urlretrieve(str(bg_url), str(bg_path)) 
        print("log: image data = ", data)
    except:
        bg_path = None
        print("ERROR downloading image")


def setImage():
    try:
        global bg_path
        if bg_path: 
            bg_uri = "file://" + bg_path
            subprocess.call(["gsettings","set","org.gnome.desktop.background","picture-uri",bg_uri])
            print("log: sucessully set image at uri = ", bg_uri)
    except:
        print("ERROR setting image")


def main():
    try:
        getResolution()
        downloadImage()
        setImage()
    except:
        print("ERROR in main")

main()
