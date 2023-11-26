import time
import random
import pyautogui as pg

animals = ("smart","beuty","I don't know",)

time.sleep(15)




for i in range(50):
    anml = random.choice(animals)
    pg.write("He is"+ anml)
    pg.press("enter")
    

