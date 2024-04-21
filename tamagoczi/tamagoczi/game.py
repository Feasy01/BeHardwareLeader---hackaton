from dataclasses import dataclass
from enum import Enum, auto
import asyncio

class Moods(Enum):
    HAPPY = auto()
    DEFAULT = auto()
    SAD = auto()
    NOTIFICATION = auto()
    FOOTBALL = auto()


OUTFITS = [
    {
        Moods.HAPPY: "src",
        Moods.DEFAULT: "src",
        Moods.SAD: "src",
        Moods.NOTIFICATION: "src",
        Moods.FOOTBALL: "src",
        
    },
    {
        Moods.HAPPY: "src",
        Moods.DEFAULT: "src",
        Moods.SAD: "src",
        Moods.NOTIFICATION: "src",
        Moods.FOOTBALL: "src"
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

    async def change_mood(self,mood):
        self.mood = mood
        # callback to OLED screen here src = OUTFITS[self.outfit][self.mood]
    async def change_outfit(self, outfit_number):
        self.outfit = outfit_number
        # callback to OLED screen here src = OUTFITS[self.outfit][self.mood]
        
    async def change_action(self,action_message):
        self.action = action_message
        # callback to LCD here → display action message
        await asyncio.sleep(15)
        # clear LCD
    
    async def action_confirmed(self,action_message,action_points):
        self.action = ""
        # callback to LCD here → display action message and points available
        self.change_mood(Moods.HAPPY)
        
