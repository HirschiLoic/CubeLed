import RPi.GPIO as GPIO   #Necessaire pour l'utilisation des GPIO
from threading import Thread #Necessaire pour l'utilisation des thread
import time 
GPIO.setmode(GPIO.BOARD) #Enclenche le mode GPIO pour la Raspberry
from FonctionCube import *
GPIO.setwarnings(False) #Enleve les erreurs inutile dû a GPIO



def thread1(): #Fonction du thread1, affiche le tableau en continu
    test = 0
    while test < 2:
        for layer in range(0, 8, 1):
            print(" Thread 1")
            Affiche32(layer) #envoie chaque layer à la fonction Affiche32
            test = test + 1
            
def thread2():#Fonction du thread2, modifie le tableau en continu
    varTest = 0
    while varTest < 2:
            print(" Thread 2")
            start()
            varTest = varTest + 1
            
#Début du programme principal   
if __name__ == '__main__':
    SETUP()
    thread_1 = Thread(target=thread1)#Callback, active le thread
    thread_2 = Thread(target=thread2)

    #Lancement des threads
    thread_2.start()
    time.sleep(2.5)#Obligatoire, le thread2 doit être lancé en premier,
                   #et il faut quelque seconde pour que le tableau TabRGB sois configuré.
    thread_1.start()
    
    #Attend que les threads se terminent
    thread_1.join()
    thread_2.join()
    
    
    print("Fin du programme")


    
        
    

    


    
