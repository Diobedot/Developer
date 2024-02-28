import gpiozero

print("LEDs Test\n")
led = gpiozero.LED(17)
button = gpiozero.Button(4)

while True:
    button.when_pressed = led.on
    button.when_released = led.off
