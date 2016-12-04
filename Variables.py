##import RPi.GPIO as GPIO
#Initialisation des GPIO, les numéros sont les pin utilisé dans se programme

CLK = 10  
SDIR = 11 
SDIG = 12 
SDIB = 15 
LA = 16   
OE = 18   
AA = 19   
BB = 21   
CC = 22
#Initialisation de certaine variables
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


#Création de la liste servant de tableau, car les tableau n'existe pas en Python.
TabRGB = []
for x in range(8):
    TabRGB.append([])
    for y in range(8):
        TabRGB[x].append([])
        for z in range(8):
            TabRGB[x][y].append([])
            for c in range(3):
                TabRGB[x][y][z].append([])

#L'objet maLed, qui représente chaque LED utiliser dans le cube
class maLed(object):

    def __init__(self, x, y, z, r, g, b):
        TabRGB[x][y][z][0] = r
        TabRGB[x][y][z][2] = g
        TabRGB[x][y][z][1] = b
        


    


    
                
            
        
    
