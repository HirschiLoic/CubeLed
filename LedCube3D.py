import RPi.GPIO as GPIO   #Necessaire pour l'utilisation des GPIO
import threading #Necessaire pour l'utilisation des thread
from Variables import *
GPIO.setmode(GPIO.BOARD) #Enclenche le mode GPIO pour la Raspberry
from FonctionCube import Affiche32
GPIO.setwarnings(False) #Enleve les erreurs inutile dû a GPIO
SETUP()

def thread1(): #Fonction du thread
    test = 0
    while test <= 0:
        for layer in range(0, 8, 1):
            Affiche32(layer) #envoie chaque layer à la fonction Affiche32
            test = test + 1
#def thread2():
 #   start()

if __name__ == '__main__':
    #Thread.__init__(self)
    thread1()
    #thread_1 = thread1()
    #thread_1.start()
    #thread_1.join()

    


    
