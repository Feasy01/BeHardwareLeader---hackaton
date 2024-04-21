from dataclasses import dataclass, field
from user.tamagoczi import User
@dataclass
class Game:
    users:dict[str,User] = field(default_factory=lambda: {})
    
    def __post_init__(self):
        self.users["1234"] = User(rf_id="1234",name="Szymon Walczak",outfit=2,points=100)
    def add_user(self,rf_id:str,name:str,points:int,outfit:int):
        self.users[rf_id] = User(rf_id,name,outfit,points)
        
    def add_points(self,rf_id:str,points:int):
        pass