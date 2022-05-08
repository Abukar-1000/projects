import pyautogui as pya
import cv2 as cv
import random
import keyboard
import time

# def clickButton(name,con):
#     try:
#         xpos,ypos = pya.locateCenterOnScreen(name,confidence = con)
#         pya.click(xpos,ypos)
#         time.sleep(.2)
#     except:
#         print("I cant see it ")    

# while keyboard.is_pressed('q') == False:
#     clickButton('E:\projects\startbutton.png',.8)
#     clickButton('E:\projects\powerbutton.png',.5)
#     clickButton('E:\projects\shutdown.png',.8)

def randomClicks(ofset,mode):
    xpos,ypos = pya.position()
    if mode == 'up':
        xpos += ofset
        ypos += ofset
        pya.click(xpos,ypos)
    else:
        xpos -= ofset
        ypos -= ofset
        pya.click(xpos,ypos)

while keyboard.is_pressed('q') == False:
    pya.FAILSAFE = False
    offset = random.randint(10,1000)
    mode = random.choice(['up','down'])
    randomClicks(offset,mode)