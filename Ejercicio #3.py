#Ejercicio forma 3
#ejecutar Ctr Shift R
from machine import Pin #No se usa el "as" se usa el nombre que tiene en la libreria 
import utime #Se llama a toda la libreria

#Se instancian los objetos(LEDS)
led1 = Pin(5, Pin.OUT)
led2 = Pin(18, Pin.OUT)
led3 = Pin(19, Pin.OUT)
led4 = Pin(21, Pin.OUT)
led5 = Pin(22, Pin.OUT)
led6 = Pin(23, Pin.OUT)
    #Pines de la otra parte de la ESP32
led7 = Pin(26, Pin.OUT)
led8 = Pin(25, Pin.OUT)
led9 = Pin(33, Pin.OUT)
led10 = Pin(32, Pin.OUT)

conjunto = [led1, led2, led3, led4, led5, led6, led7, led8, led9, led10]

def derecha():
    for i in conjunto:
        i.value(1)
        utime.sleep_ms(100)#0.1s
        i.value(0)
        utime.sleep(0.01)

def izquierza():
    for i in reversed(conjunto):
        i.value(1)
        utime.sleep_ms(100)#0.1s
        i.value(0)
        utime.sleep(0.01)

#Podemos escoger en que sentido se quiere la secuencia
#Si se activa derecha() va de izquierda a derecha
#Si se activa izquierda() va de derecha a iaquierda
#Cuando se dejan las dos activadas va a usar una y despues la otra
while True:
    derecha()
    #izquierza()

