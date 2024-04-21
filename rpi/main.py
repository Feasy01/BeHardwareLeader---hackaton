from time import sleep
import board
import digitalio

import adafruit_ssd1306
from PIL import Image, ImageOps
import RPi.GPIO as GPIO
import threading
#TODO websocket

from main_lcd import LCD_display
from main_oled import OLED_disp

BUZZER_PIN = 19
BUTTON_PIN = 26

NUMBER_OF_FRAMES = 8
TIME_OF_FRAME_MS = 333

global_oled = None
global_lcd = None

##### FUNCTIONS #####
def init_lcd():
    global global_lcd
    global_lcd = LCD_display()

##### THREADS #####

def animation_thread_handler():
    global global_oled
    global_oled = OLED_disp()
    while True:
        global_oled.show_next_frame()
        sleep(TIME_OF_FRAME_MS/1000)


def button_thread_handler():
    GPIO.setup(BUZZER_PIN, GPIO.OUT)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    status = 0
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
            if status == 0:
                global_oled.change_image("arm.gif")
                status = 1
                GPIO.output(BUZZER_PIN, GPIO.HIGH)
                global_lcd.display("Glaskanko :3")
        else:
            if status == 1:
                global_oled.return_to_prev_animation()
                GPIO.output(BUZZER_PIN, GPIO.LOW)
                status = 0
                # global_lcd.display_prev()
                global_lcd.clear()
        sleep(0.2)
# ...


def main():
    GPIO.setmode(GPIO.BCM)
    init_lcd()

    animation_thr = threading.Thread(target=animation_thread_handler)
    button_thr = threading.Thread(target=button_thread_handler)
    animation_thr.start()
    button_thr.start()

    sleep(10)
    global_oled.change_image("sad.gif")
    global_lcd.display("Some\nmsg") #TODO delete

    sleep(10)
    global_oled.change_image("neutral.gif")
    global_lcd.clear() #TODO delete




    
if __name__ == "__main__":
    main()


