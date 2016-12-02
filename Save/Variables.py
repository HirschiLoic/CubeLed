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
    nb = bin(binlayer)[2:].zfill(3) #Conversion du layer en binaire
    print(nb[0], nb[1], nb[2])
    ma_liste = [AA, BB, CC] #les trois pin qu'on allumera ou qu'on eteindra
    
    
    for i in range(0,len(ma_liste)):
        print(ma_liste[i])
        for cl in range(3):
            if nb[cl] == 0:
                GPIO.output(ma_liste[i], 0)
                
            else:
                GPIO.output(ma_liste[i], 1)
                print(nb[cl])
            
        
    
