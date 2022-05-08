import random
import pyautogui as pg
import time
import keyboard

def defaultClick(images):
    # while (keyboard.is_pressed("a") == False):
    for image in images:
        try:
            x,y = pg.locateCenterOnScreen(image, grayscale = True, confidence = .6)
            pg.click(x,y)
        except:
            pass

def multiplier(values,times):
    result = []
    for items in values:
        for x in range(times):
            result.append(items)
    return result

def recursiveClick(images,index):
    if (index > (len(images) - 1)):
        return
    else:
        try:
            if (index <= (len(images) - 1)):
                # if (images[index] != "close.png"):
                x,y = pg.locateCenterOnScreen(images[index], grayscale = True, confidence = .6)
                pg.click(x,y)
                return recursiveClick(images,index + 1)
                # else:
                #     x,y = pg.locateCenterOnScreen(images[index], grayscale = True, confidence = .8)
                #     pg.click(x,y)
                #     return recursiveClick(images,index + 1)
        except:
            pass

cache = {}
def memedRecursiveClick(images,index):
    if (index > (len(images) - 1)):
        return
    elif (images[index] in cache.keys()):
        x,y = cache[(images[index])]
        pg.click(x,y)
        return memedRecursiveClick(images,index + 1)
    else:
        try:
            if (index <= (len(images) - 1)):
                x,y = pg.locateCenterOnScreen(images[index], grayscale = True, confidence = .6)
                pg.click(x,y)
                cache[(images[index])] = (x,y)
                return memedRecursiveClick(images,index + 1)
        except:
            pass

def main():
    start = time.time()
    images = ["reloadButton.png","reloadButton.png","minimize.png","maximize.png","minimize.png","maximize.png"]
    images2 = multiplier(images,100)
    print(len(images2))
    random.shuffle(images2)
    # process 600 images
    # took 192.99 seconds
    # defaultClick(images2)
    # took 179.12 seconds
    # recursiveClick(images2,0)
    # took 66.57 seconds
    memedRecursiveClick(images2,0)
    stop = time.time()
    print(f"took {round((stop - start),2)} seconds")

    print ("second run")
    start = time.time()
    memedRecursiveClick(images2,0)
    stop = time.time()
    print(f"took {round((stop - start),2)} seconds")

if __name__ == "__main__":
    main()