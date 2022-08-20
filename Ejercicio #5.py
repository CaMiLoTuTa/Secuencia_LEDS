#Ejercicio forma 5
#ejecutar Ctr Shift R
from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausams, sleep_us as pausaus

#Se llaman a los pines mas no a los objetos(LEDS)
pines = [5, 18, 19, 21, 22, 23, 26, 25, 33, 32]
conjunto = []

#el apend sirve para asignarle otro valor a una lista 
# en este caso se le agrega a (pin("i", pin.OUT)) y 
# lo hará con todos los valores en la lista "pines" para almacenarlo en la lista "conjunto"
for i in pines:
    conjunto.append(pin(i, pin.OUT))

print(conjunto)

def derecha():
    for i in conjunto:
        for j in range(2):
            i.value(not i.value())
        pausams(100)#0.1s
        
        
def izquierda():
    for i in reversed(conjunto):
        for j in range(2):
            i.value(not i.value())
        pausams(100)#0.1s

#Podemos escoger en que sentido se quiere la secuencia
#Si se activa derecha() va de izquierda a derecha
#Si se activa izquierda() va de derecha a iaquierda
#Cuando se dejan las dos activadas va a usar una y despues la otra
while True:
    #derecha()
    izquierda()
