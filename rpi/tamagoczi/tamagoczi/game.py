from dataclasses import dataclass
from enum import Enum, auto
import asyncio
from main_oled import OLED_disp
from main_lcd import LCD_display

class Moods(Enum):
    HAPPY = auto()
    DEFAULT = auto()
    SAD = auto()
    NOTIFICATION = auto()
    FOOTBALL = auto()


OUTFITS = [
    {
        Moods.HAPPY: "rpi/smile.gif",
        Moods.DEFAULT: "rpi/neutral.gif",
        Moods.SAD: "rpi/sad.gif",
        Moods.NOTIFICATION: "rpi/arm.gif",
        Moods.FOOTBALL: "rpi/ball.gif",
        
    },
    {
        Moods.HAPPY: "rpi/hat.gif",
        Moods.DEFAULT: "rpi/hat.gif",
        Moods.SAD: "rpi/hat.gif",
        Moods.NOTIFICATION: "rpi/hat.gif",
        Moods.FOOTBALL: "rpi/ball_hat.gif",
    }
]


@dataclass
class Game:
    rf_id: str
    name: str
    outfit: 0
    mood: Moods.HAPPY
    action: str
    points: int
    oled_hook: OLED_disp
    lcd_hook: LCD_display

    async def change_mood(self,mood):
        self.mood = mood
        self.oled_hook.change_image(OUTFITS[self.outfit][self.mood])
        # callback to OLED screen here src = OUTFITS[self.outfit][self.mood]
    async def change_outfit(self, outfit_number):
        self.outfit = outfit_number
        self.oled_hook.change_image(OUTFITS[self.outfit][self.mood])
        # callback to OLED screen here src = OUTFITS[self.outfit][self.mood]
        
    async def change_action(self,action_message):
        self.action = action_message
        self.lcd_hook.display(action_message)
        # callback to LCD here → display action message
        await asyncio.sleep(15)
        # clear LCD
        self.lcd_hook.clear()
    
    async def action_confirmed(self,action_message,action_points):
        self.action = ""
        # callback to LCD here → display action message and points available
        self.change_mood(Moods.HAPPY)
        self.lcd_hook.display("Dostales punkty!")
        await asyncio.sleep(5)
        # clear LCD
        self.lcd_hook.clear()
        
