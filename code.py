# Write your code here :
from adafruit_circuitplayground.express import cpx
import touchio
from board import *
from time import sleep
import random
colors = [(255, 0, 255), (0, 100, 0),(0, 0, 139)]


touch = touchio.TouchIn(A1)


while True:
    if cpx.switch:
        cpx.pixels.fill((0, 0, 0))
        if cpx.button_a:
            print("La temperatura actual es %2.f" % cpx.temperature)
            sleep(0.5)
        if cpx.button_b:
            print("light value", cpx.light)
            sleep(0.5)
    else:
        print("nivel de humedad", touch.raw_value)
        sleep(0.5)
        if touch.raw_value > 1500:
            for indice in range(0,10):
                cpx.pixels[indice] = (random.choice(colors))
                sleep(0.1)
                cpx.pixels.fill((0,0,0))
                sleep(0.10)
        else:
            cpx.pixels.fill((255, 51, 0))