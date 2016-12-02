import RPi.GPIO as GPIO
from traceback import *
from Variables import *

def Affiche32(choixlayer):
    GPIO.setmode(GPIO.BOARD)
    
    try:
        i = 0
        j = 1
        k = 0
        n = 8
        if choixlayer == 0:
            OUTPUT(choixlayer)
            print('Affiche Layer ', choixlayer)

        elif choixlayer == 1:
            OUTPUT(choixlayer)
            print('Affiche Layer ', choixlayer)

        elif choixlayer == 2:
            OUTPUT(choixlayer)
            print('Affiche Layer ', choixlayer)

        elif choixlayer == 3:
            OUTPUT(choixlayer)
            print('Affiche Layer ', choixlayer)

        elif choixlayer == 4:
            OUTPUT(choixlayer)
            print('Affiche Layer ', choixlayer)

        elif choixlayer == 5:
            OUTPUT(choixlayer)
            print('Affiche Layer ', choixlayer)

        elif choixlayer == 6:
            OUTPUT(choixlayer)
            print('Affiche Layer ', choixlayer)
            
        elif choixlayer == 7:
            OUTPUT(choixlayer)
            print('Affiche Layer ', choixlayer)
            

        for i in range(32):
            for j in range(1, -1, -1):
                for k in range(8):
                    if TabRGB[choixlayer][j][k][0] < n:
                        GPIO.output(SDIR, GPIO.LOW)
                    else:
                        GPIO.output(SDIR, GPIO.HIGH)
                        
                    if TabRGB[choixlayer][j][k][1] < n:
                        GPIO.output(SDIG, GPIO.LOW)
                    else:
                        GPIO.output(SDIG, GPIO.HIGH)
                        
                    if TabRGB[choixlayer][j][k][2] < n:
                        GPIO.output(SDIB, GPIO.LOW)
                    else:
                        GPIO.output(SDIB, GPIO.HIGH)
                        
                    GPIO.output(CLK, GPIO.HIGH)
                    GPIO.output(CLK, GPIO.LOW)

            for j in range(3, 1, -1):
                for k in range(0, 8, 1):
                    if TabRGB[choixlayer][j][k][0] < n:
                       GPIO.output(SDIR, GPIO.LOW)
                    else:
                        GPIO.output(SDIR, GPIO.HIGH)
                    if TabRGB[choixlayer][j][k][2] < n:
                        GPIO.output(SDIB, GPIO.LOW)
                    else:
                        GPIO.output(SDIB, GPIO.HIGH)
                    GPIO.output(CLK, GPIO.HIGH)
                    GPIO.output(CLK, GPIO.LOW)

            for j in range(5, 3, -1):
                for k in range(0, 8, 1):
                    if TabRGB[choixlayer][j][k][0] < n:
                        GPIO.output(SDIR.LOW)
                    else:
                        GPIO.output(SDIR.HIGH)
                    if TabRGB[choixlayer][j][k][1] < n:
                        GPIO.output(SDIG.LOW)
                    else:
                        GPIO.output(SDIG.HIGH)
                    if TabRGB[choixlayer][j][k][2] < n:
                        GPIO.output(SDIB.LOW)
                    else:
                        GPIO.output(SDIB.HIGH)
                    GPIO.output(CLK, GPIO.HIGH)
                    GPIO.output(CLK, GPIO.LOW)

            for j in range(7, 5, -1):
                for k in range(0, 8, 1):
                    if TabRGB[choixlayer][j][k][0] < n:
                        GPIO.output(SDIR.LOW)
                    else:
                        GPIO.output(SDIR.HIGH)
                    if TabRGB[choixlayer][j][k][1] < n:
                        GPIO.output(SDIG.LOW)
                    else:
                        GPIO.output(SDIG.HIGH)
                    if TabRGB[choixlayer][j][k][2] < n:
                        GPIO.output(SDIB.LOW)
                    else:
                        GPIO.output(SDIB.HIGH)
                    GPIO.output(CLK, GPIO.HIGH)
                    GPIO.output(CLK, GPIO.LOW)
            n = n + 8
            GPIO.output(CLK.HIGH)
            GPIO.output(CLK.LOW)
    except Exception:
        print("Exception. Problème lors de l'allumage des GPIO")
        print_exc()
    #finally:
        #GPIO.cleanup()
    #GPIO.cleanup()

def CouleurDepart():
    maLed(7, 0, 0, 146, 0, 223)
    maLed(7, 1, 0, 0, 0, 255)
    maLed(7, 2, 0, 0, 230, 255)
    maLed(7, 3, 0, 0, 255, 0)
    maLed(7, 4, 0, 255, 255, 0)
    maLed(7, 5, 0, 255, 140, 0)
    maLed(7, 6, 0, 255, 0, 0)
    maLed(7, 7, 0, 240, 130, 240)


def EteindreCube():
     #Numero du layer (0 a 7)
    L = 0
     #Numero de la LED sur axe Y (0 a 7)
    Y = 0
     #Numero de la LED sur axe Y (0 a 7)
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


var = 0
while var < 2:
    EteindreCube()
    #print(TabRGB)
    CouleurDepart()
    #print(TabRGB)
    #print("Le cube va s'eteindre...'")

    var = var + 1
#CouleurDepart()
#print(TabRGB)
#print("At this point, all LED are off (0)")
#EteindreCube()
#print(TabRGB)

