#Ejercicio forma 1
#ejecutar Ctr Shift R

from machine import Pin as pin
from utime import sleep, sleep_ms

#Se instancian los objetos(LEDS)
led1 = pin(5, pin.OUT)

led2 = pin(18, pin.OUT)

led3 = pin(19, pin.OUT)

led4 = pin(21, pin.OUT)

led5 = pin(22, pin.OUT)

led6 = pin(23, pin.OUT)

    #Pines de la otra parte de la ESP32
led7 = pin(26, pin.OUT)

led8 = pin(25, pin.OUT)

led9 = pin(33, pin.OUT)

led10 = pin(32, pin.OUT)

espera = 0.08

while True:
    led1.value(1)
    led10.value(1)
    sleep(espera)
    led1.value(0)
    led10.value(0)
    
    
    led2.value(1)
    led9.value(1)
    sleep(espera)
    led2.value(0)
    led9.value(0)
    
    led3.value(1)
    led8.value(1)
    sleep(espera)
    led3.value(0)
    led8.value(0)
    
    led4.value(1)
    led7.value(1)
    sleep(espera)
    led4.value(0)
    led7.value(0)
    
    led5.value(1)
    led6.value(1)
    sleep(espera)
    led5.value(0)
    led6.value(0)
    
    
    led4.value(1)
    led7.value(1)
    sleep(espera)
    led4.value(0)
    led7.value(0)
    
    led3.value(1)
    led8.value(1)
    sleep(espera)
    led3.value(0)
    led8.value(0)
    
    led2.value(1)
    led9.value(1)
    sleep(espera)
    led2.value(0)
    led9.value(0)
    