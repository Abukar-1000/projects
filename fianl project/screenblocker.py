import pygetwindow as gw
import random

# allWindows = gw.getAllWindows()

# for window in allWindows:
#     print(window.title)

allowed = ['Windows Input Experience','Program Manager','Chat | Microsoft Teams [QSP]','New Tab - Google Chrome']

while True:
    x = random.randint(0,1080)
    y = random.randint(0,1920)
    allWindows = gw.getAllWindows()

    for window in allWindows:
        if window.title not in allowed:
            window.resizeTo(x,y)


