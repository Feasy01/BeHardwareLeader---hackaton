from PIL import Image, ImageDraw, ImageFont, ImageOps
import adafruit_ssd1306
import time
import board


# Define the Reset Pin
oled_reset = None

# Change these
# to the right size for your display!
WIDTH = 128
HEIGHT = 64
BORDER = 5

class OLED_disp():
    def __init__(self):
        # Use for I2C.
        i2c = board.I2C()
        self.oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)
        self.oled.fill(0)
        self.oled.show()
        self.current_frame = 0
        self.frames = []
        self.current_img_name = None
        self.prev_img_name = None
        self.change_image("rpi/smile.gif")

    def change_image(self, image_file_name):
        image = Image.open(image_file_name, "r")
        self.current_frame = 0
        self.frames = []
        for n in range(image.n_frames):
            image.seek(n)
            im = image.copy()
            im = im.convert(mode = "1")
            im = ImageOps.invert(im)
            if im.width == 64:
                im = im.rotate(90, Image.NEAREST, expand = 1)
            self.frames.append(im)
        self.current_frame = 0
        self.prev_img_name = self.current_img_name
        self.current_img_name = image_file_name
        self.show_next_frame()

    def return_to_prev_animation(self):
        if self.prev_img_name is not None:
            self.change_image(self.prev_img_name)

    def show_next_frame(self):
        self.current_frame += 1
        if self.current_frame >= len(self.frames):
            self.current_frame = 0
        self.oled.image(self.frames[self.current_frame])
        self.oled.show()


