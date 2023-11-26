import time
import random
import pyautogui as pg

animals = ("smart","beuty","nasser")

time.sleep(15)




for i in range(100):
    anml = random.choice(animals)
    pg.write("He is -"+ anml)
    pg.press("enter")
    

