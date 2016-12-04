import RPi.GPIO as GPIO
from traceback import *
from Variables import *
import time

def Affiche32(choixlayer):
    GPIO.setmode(GPIO.BOARD)
    try:
        i = 0
        j = 1
        k = 0
        n = 8
        if choixlayer == 0:
            OUTPUT(choixlayer)
            
        elif choixlayer == 1:
            OUTPUT(choixlayer)
            
        elif choixlayer == 2:
            OUTPUT(choixlayer)
            
        elif choixlayer == 3:
            OUTPUT(choixlayer)
            
        elif choixlayer == 4:
            OUTPUT(choixlayer)
            
        elif choixlayer == 5:
            OUTPUT(choixlayer)
            
        elif choixlayer == 6:
            OUTPUT(choixlayer)
            
        elif choixlayer == 7:
            OUTPUT(choixlayer)
            
        
        for i in range(32):
            for j in range(1, -1, -1):
                for k in range(8):
                    if TabRGB[choixlayer][j][k][0] < n:
                        GPIO.output(SDIR, 0)
                    else:
                        GPIO.output(SDIR, 1)
                        
                    if TabRGB[choixlayer][j][k][1] < n: 
                        GPIO.output(SDIG, 0)
                    else:
                        GPIO.output(SDIG, 1)
                        
                    if TabRGB[choixlayer][j][k][2] < n:
                        GPIO.output(SDIB, 0)
                    else:
                        GPIO.output(SDIB, 1)
                        
                    GPIO.output(CLK, 1)
                    GPIO.output(CLK, 0)

            for j in range(3, 1, -1):
                for k in range(0, 8, 1):
                    if TabRGB[choixlayer][j][k][0] < n:
                       GPIO.output(SDIR, 0)
                    else:
                        GPIO.output(SDIR, 1)
                    if TabRGB[choixlayer][j][k][2] < n:
                        GPIO.output(SDIB, 0)
                    else:
                        GPIO.output(SDIB, 1)
                    GPIO.output(CLK, 1)
                    GPIO.output(CLK, 0)

            for j in range(5, 3, -1):
                for k in range(0, 8, 1):
                    if TabRGB[choixlayer][j][k][0] < n:
                        GPIO.output(SDIR, 0)
                    else:
                        GPIO.output(SDIR, 1)
                    if TabRGB[choixlayer][j][k][1] < n:
                        GPIO.output(SDIG, 0)
                    else:
                        GPIO.output(SDIG, 1)
                    if TabRGB[choixlayer][j][k][2] < n:
                        GPIO.output(SDIB, 0)
                    else:
                        GPIO.output(SDIB, 1)
                    GPIO.output(CLK, 1)
                    GPIO.output(CLK, 0)

            for j in range(7, 5, -1):
                for k in range(0, 8, 1):
                    if TabRGB[choixlayer][j][k][0] < n:
                        GPIO.output(SDIR, 0)
                    else:
                        GPIO.output(SDIR, 1)
                    if TabRGB[choixlayer][j][k][1] < n:
                        GPIO.output(SDIG, 0)
                    else:
                        GPIO.output(SDIG, 1)
                    if TabRGB[choixlayer][j][k][2] < n:
                        GPIO.output(SDIB, 0)
                    else:
                        GPIO.output(SDIB, 1)
                    GPIO.output(CLK, 1)
                    GPIO.output(CLK, 0)
            n = n + 8
            GPIO.output(LA, 1)
            GPIO.output(LA, 0)
    except Exception:
        print("Exception. Problème lors de l'allumage des GPIO")
        print_exc()
    #finally:
        #GPIO.cleanup()
    #GPIO.cleanup()
#Fonction qui définis les couleurs de départ du cube
def CouleurDepart():
    print("CouleurDepart")
    maLed(7, 0, 0, 146, 0, 223)
    maLed(7, 1, 0, 0, 0, 255)
    maLed(7, 2, 0, 0, 230, 255)
    maLed(7, 3, 0, 0, 255, 0)
    maLed(7, 4, 0, 255, 255, 0)
    maLed(7, 5, 0, 255, 140, 0)
    maLed(7, 6, 0, 255, 0, 0)
    maLed(7, 7, 0, 240, 130, 240)
    

#Fonction qui éteind entiéremment le cube
def EteindreCube():
    print("EteindreCube")
     #Numero du layer (0 a 7)
    L = 0
     #Numero de la LED sur axe Y (0 a 7)
    Y = 0
     #Numero de la LED sur axe X (0 a 7)
    X = 0

    #Cr = 0  # Rouge
    #Cb = 1  # Bleu
    #Cv = 2  # Vert

    #Parcours les LEDs et les eteinds
    for L in range(0, 8, 1):
        for Y in range(0, 8, 1):
            for X in range(0, 8, 1):
                maLed(L, Y, X, 0, 0, 0)
                #TabRGB[L, Y, X, Cr] = 0
                #TabRGB[L, Y, X, Cb] = 0
                #TabRGB[L, Y, X, Cv] = 0

#Fonction qui sert à set les GPIO
def SETUP():
    try:
        GPIO.setup(CLK, GPIO.OUT)  # Clock
        GPIO.setup(SDIR, GPIO.OUT)  # data 1
        GPIO.setup(SDIG, GPIO.OUT)  # data 2
        GPIO.setup(SDIB, GPIO.OUT)  # data 3
        GPIO.setup(LA, GPIO.OUT)  # latch
        GPIO.setup(OE, GPIO.OUT)  # output enable
        GPIO.setup(AA, GPIO.OUT)  # layer bit0
        GPIO.setup(BB, GPIO.OUT)  # layer bit1
        GPIO.setup(CC, GPIO.OUT)  # layer bit2
        
    except:
        print("Erreur lors de l'initialisation des GPIO")

##Fonction qui transforme le layer actuel en binaire (Format 000).
##Met les 3 pin AA BB et CC à HIGH ou à LOW grâce au &.
##Si le layer actuel est supérieur à 0, on met à HIGH (1)
##Les prints servent de test
def OUTPUT(binlayer):
    if binlayer & 1 > 0:
##        print("True 1")
        GPIO.output(AA, 1)
    else:
##        print("False 1")
        GPIO.output(AA, 0)
        
    if binlayer & 2 > 0:
##        print("True 2")
        GPIO.output(BB, 1)
    else:
##        print("False 2")
        GPIO.output(BB, 0)
    
    if binlayer & 4 > 0:
##        print("True 4")
        GPIO.output(CC, 1)
    else:
##        print("False 4")
        GPIO.output(CC, 0)
        
#Exécute les       
def start():
    var = 0
    while var < 2:
        
        CouleurDepart()
        time.sleep(2)
        EteindreCube()
        time.sleep(2)
        var = var + 1




