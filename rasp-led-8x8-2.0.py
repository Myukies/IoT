import max7219.led as led
from time import sleep

device = led.Matrix8x8(1, 0, 10, 11, 8)

device.brightness(5)

def display_message(message):
    device.show_message(message)

while True:
    message = input("Enter message to display (or 'quit' to exit): ")
  
    if message.lower() == "quit":
        break
      
    display_message(message)
  
device.clear()
