import RPi.GPIO as GPIO
#Initialisation des GPIO

CLK = 10
SDIR = 11
SDIG = 12
SDIB = 15
LA = 16
OE = 18
AA = 19
BB = 21
CC = 22
A = 0
sinAngle = 0.0
cosAngle = 0.0
cl = 0 
x = 0
y = 0
c = 0
g = 0
o = 0
p = 0
layer = 0
durer = 0


#create tab
TabRGB = []
for x in range(8):
    TabRGB.append([])
    for y in range(8):
        TabRGB[x].append([])
        for z in range(8):
            TabRGB[x][y].append([])
            for c in range(3):
                TabRGB[x][y][z].append([])

class maLed(object):

    def __init__(self, x, y, z, r, g, b):
        TabRGB[x][y][z][0] = r
        TabRGB[x][y][z][2] = g
        TabRGB[x][y][z][1] = b

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

#Creer une fonction,
#transforme en binaire le layer et attribut "high" la ou il y'a un 1 
def OUTPUT(binlayer):
    if binlayer & 1 > 0:
        print("True 1")
        GPIO.output(AA, 1)
    else:
        print("False 1")
        GPIO.output(AA, 0)
        
    if binlayer & 2 > 0:
        print("True 2")
        GPIO.output(BB, 1)
    else:
        print("False 2")
        GPIO.output(BB, 0)
    
    if binlayer & 4 > 0:
        print("True 4")
        GPIO.output(CC, 1)
    else:
        print("False 4")
        GPIO.output(CC, 0)
        
    if GPIO.input(AA):
        print('Input AA was HIGH')
    else:
        print('Input AA was LOW')

    if GPIO.input(BB):
        print('Input BB was HIGH')
    else:
        print('Input BB was LOW')

    if GPIO.input(CC):
        print('Input CC was HIGH')
    else:
        print('Input CC was LOW')
    
    
        
    #nb = bin(binlayer)[2:].zfill(3) #Conversion du layer en binaire
    #print(nb[0], nb[1], nb[2])
    #ma_liste = [CC, BB, AA] #les trois pin qu'on allumera ou qu'on eteindra

    #for i in range(0,len(ma_liste)): #on parcourt la liste
        #test2 = 0
        #print(ma_liste[i])
        #test = nb[i]
        #print(test, " -- valeur de test")
        #for cl in range(2): #On parcours le layer qu a été convertis en binaire
        #if test == 0:
            #print(nb[i], " -- Ici c'est 0")
            #GPIO.output(ma_liste[i], 0)
        #elif test == 1:
            #print(nb[i], " -- Ici c'est 1")
            #GPIO.output(ma_liste[i], 1)
        #if test2 == 0:
            #print("Le test2 fonctionne")

                
            
        
    
