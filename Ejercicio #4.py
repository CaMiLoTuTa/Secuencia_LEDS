#Ejercicio forma 4
#ejecutar Ctr Shift R
from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausams, sleep_us as pausaus

#Se instancian los objetos(LEDS)
leda = pin(5, pin.OUT) 
ledb = pin(18, pin.OUT)
ledc = pin(19, pin.OUT)
ledd = pin(21, pin.OUT)
lede = pin(22, pin.OUT)
ledf = pin(23, pin.OUT)
    #Pines de la otra parte de la ESP32
ledg = pin(26, pin.OUT)
ledh = pin(25, pin.OUT)
ledi = pin(33, pin.OUT)
ledj = pin(32, pin.OUT)

leds = [leda,ledb,ledc,ledd,lede, ledf, ledg,ledh,ledi,ledj]

def derecha():
    for i in leds:
        for j in range(2):#El numero en "range()" significa cuantoas veces se va a encender y apagar
            i.value(not i.value())
            pausams(100)#0.1s

def izquierda():
    for i in reversed(leds):
        for j in range(2):
            i.value(not i.value())
            pausams(100)#0.1s

#Podemos escoger en que sentido se quiere la secuencia
#Si se activa derecha() va de izquierda a derecha
#Si se activa izquierda() va de derecha a iaquierda
#Cuando se dejan las dos activadas va a usar una y despues la otra
while True:
    izquierda()
    #derecha()
