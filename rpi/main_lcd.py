from time import sleep
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

# Modify this if you have a different sized character LCD
lcd_columns = 16
lcd_rows = 2

# compatible with all versions of RPI as of Jan. 2019
# v1 - v3B+
lcd_rs = digitalio.DigitalInOut(board.D22)
lcd_en = digitalio.DigitalInOut(board.D17)
lcd_d4 = digitalio.DigitalInOut(board.D13)
lcd_d5 = digitalio.DigitalInOut(board.D6)
lcd_d6 = digitalio.DigitalInOut(board.D5)
lcd_d7 = digitalio.DigitalInOut(board.D27)

class LCD_display():
    def __init__(self) -> None:
        self.lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                      lcd_d7, lcd_columns, lcd_rows)
        self.lcd.clear()
        self.lcd.message = "Hello\nLeader"
        sleep(2)
        self.clear()

    def display(self, message):
        if self.prev_message == message:
            return
        self.lcd.clear()
        self.prev_message = message
        self.lcd.message = message

    def display_prev(self):
        if self.prev_message == "":
            self.lcd.clear()
            return
        self.lcd.clear()
        self.lcd.message = self.prev_message

    def clear(self):
        self.prev_message = ""
        self.lcd.clear()
        self.lcd.message = "Pamietaj,\ndbaj o siebie"
