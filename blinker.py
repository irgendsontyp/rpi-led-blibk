import time
import RPi.GPIO as GPIO

# Pin-Nummern wie auf dem Raspberry Board verwenden
GPIO.setmode(GPIO.BOARD)

GPIO_PIN_NR = 40

GPIO.setup(GPIO_PIN_NR, GPIO.OUT)

def exitApplication():
	GPIO.output(GPIO_PIN_NR, GPIO.LOW)
	GPIO.cleanup()

# Dauersschleife für das Blinken
try:
	while True:
	  GPIO.output(GPIO_PIN_NR, GPIO.HIGH)
	  time.sleep(0.5)
	  GPIO.output(GPIO_PIN_NR, GPIO.LOW)
	  time.sleep(0.5)
except KeyboardInterrupt:
	exitApplication()
	
