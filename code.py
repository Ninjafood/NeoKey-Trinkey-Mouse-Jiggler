import time
import board
from board import TOUCH
import random
import touchio
import usb_hid
import neopixel
from adafruit_hid.mouse import Mouse

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
touch = touchio.TouchIn(TOUCH)
mouse = Mouse(usb_hid.devices)
pixels[0] = (10, 25, 0)

def waitsleep():
    x = random.randrange(1, 60)
    y = 60 - x
    time.sleep(x)
    for i in range(0, 5):
        pixels[0] = (0, 0, 0)
        time.sleep(0.1)
        pixels[0] = (10, 25, 0)
        time.sleep(0.05)
    time.sleep(int(y))
    for i in range(0, 10):
        pixels[0] = (25, 0, 0)
        time.sleep(0.25)
        pixels[0] = (10, 25, 0)
        time.sleep(0.25)

def moveit(x,y):
    pixels[0] = (25, 0, 0)
    time.sleep(1)
    for i in range(0 , 5):
        pixels[0] = (10, 25, 0)
        time.sleep(.2)
        pixels[0] = (25, 0, 0)
        time.sleep(.2)
        pixels[0] = (10, 25, 0)
        time.sleep(.2)
        pixels[0] = (25, 0, 0)
    pixels[0] = (25, 0, 0)
    time.sleep(1.5)
    pixels[0] = (0, 5, 20)
    mouse.move(x, y)
    time.sleep(.2)
    pixels[0] = (25, 0, 0)
    time.sleep(1)
    pixels[0] = (10, 25, 0)
    time.sleep(.1)
    pixels[0] = (25, 0, 0)
    time.sleep(.1)
    pixels[0] = (10, 25, 0)

z=0
q=0
while True:
    if q == 1:
        pixels[0] = (25, 25, 25)
        while q == 1:
            time.sleep(1)
            if touch.value:
                q=0
                pixels[0] = (10, 25, 0)
    if z == 1:
        waitsleep()
        moveit(-100,100)
        z=z-1
        if touch.value:
            q=1
    waitsleep()
    moveit(100,-100)
    z=z+1
    if touch.value:
        q=1
