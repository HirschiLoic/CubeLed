import RPi.GPIO as GPIO
from Variables import *
GPIO.setmode(GPIO.BOARD)
from FonctionCube import Affiche32
SETUP()

def thread1():
    test = 0
    while test <= 0:
        for layer in range(0, 8, 1):
            #print("Test boucle Thread Ok")
            Affiche32(layer)
            test = test + 1

if __name__ == '__main__':
    
    thread1()
    #thread_1 = thread1()
    #thread_1.start()
    #thread_1.join()

    


    
