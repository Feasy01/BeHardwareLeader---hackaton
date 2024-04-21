# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This demo will fill the screen with white, draw a black box on top
and then print Hello World! in the center of the display

This example is for use on (Linux) computers that are using CPython with
Adafruit Blinka to support CircuitPython libraries. CircuitPython does
not support PIL/pillow (python imaging library)!
"""

import time
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont, ImageOps
import adafruit_ssd1306
import adafruit_imageload
import displayio

# Define the Reset Pin
oled_reset = None

# Change these
# to the right size for your display!
WIDTH = 128
HEIGHT = 64
BORDER = 5

# Use for I2C.
i2c = board.I2C()  # uses board.SCL and board.SDA
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

# Clear display.
oled.fill(0)
oled.show()

image = Image.open("black_gif1.gif", "r")
# image = image.convert(mode = "1")
# image = ImageOps.invert(image)
# if image.width not in [128, 64] or image.height not in [128, 64]:
#     print("WRONG SIZE!")
#     exit()

# if image.width == 64:
#     image = image.rotate(90, Image.NEAREST, expand = 1)

print("img size:", image.width, "x", image.height)

print("dur", image.info["duration"], "n_fr", image.n_frames)

images = []

for n in range(image.n_frames):
    image.seek(n)
    im = image.copy()
    im = im.convert(mode = "1")
    im = ImageOps.invert(im)
    if im.width == 64:
        im = im.rotate(90, Image.NEAREST, expand = 1)
    images.append(im)

print("images", len(images))

while 1:
    for im in images:
        oled.image(im)
        oled.show()
        time.sleep(image.info["duration"]/1000)
    


# oled.image(image)
# oled.show()


