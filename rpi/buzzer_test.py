import RPi.GPIO as GPIO
import time

BUZZER_PIN = 21
BUTTON_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
 
while 1:
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        print("BUZZER ON")
    else:
        GPIO.output(BUZZER_PIN, GPIO.LOW)
    print(".")
    time.sleep(0.1)