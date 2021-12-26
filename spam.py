import pyautogui
import win32api
import os
import time
import pygame
from pygame.locals import *
pygame.init()
os.system("cls")
pygame.mixer.music.load("gg.mp3")
pygame.mixer.music.play()
scelta1="s"
while scelta1=="s":
    os.system("color 4")
    os.system("cls")
    print("MESSAGE SPAMMER\n")
    print("___$$$___$$$____\
    \n__$$$$$_$$$$$___\
    \n__$$$$$$$$$$$___\
    \n____$$$$$$$_____\
    \n______$$$_______\
    \n_______$\
    \n_____¸.•´¸.•*¸.•*´¨`*•.♥\
    \n_____*.¸¸.•*¨`")
    a=input("\nChe messaggio vuoi spammare: ")
    v=int(input("\nQuante volte vuoi spammare: "))
    if v>50: 
        pygame.mixer.music.load("gg2.mp3")
        pygame.mixer.music.play()
    t=float(input("\nOgni quanti millisecondi vuoi spammare: "))
    t=t/1000
    b=input("\nDopo che premi invio passano 4 sec e parte, premi esc per stoppare")
    pygame.mixer.music.load("1.mp3")
    pygame.mixer.music.play()
    time.sleep(1.5)
    pygame.mixer.music.load("2.mp3")
    pygame.mixer.music.play()
    time.sleep(1.5)
    pygame.mixer.music.load("3.mp3")
    pygame.mixer.music.play()
    time.sleep(1.5)
    pygame.mixer.music.load("4.mp3")
    pygame.mixer.music.play()
    time.sleep(1.5)
    for i in range(0,v):
        pyautogui.typewrite(a)
        pyautogui.press("enter")
        time.sleep(t)
    scelta1=input("\nVuoi continuare a spammare?[s/n] ")
    pygame.mixer.music.load("gg3.mp3")
    pygame.mixer.music.play()
pygame.mixer.music.load("gg4.mp3")
pygame.mixer.music.play()
time.sleep(2)



