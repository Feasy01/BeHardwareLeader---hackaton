from dataclasses import dataclass
from typing import TypedDict

class User(TypedDict):
    rf_id:str
    name:str
    outfit:int
    points:int
    go_somewhere_points:int = 0
    
   
            