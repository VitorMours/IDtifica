from dataclasses import dataclass, field 
from uuid import UUID, uuid4
from datetime import datetime
import re 

@dataclass
class User: 
    first_name: str
    last_name: str
    email: str
    password: str
    is_active: bool = True
    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=datetime.now) #type: ignore
    updated_at: datetime = field(default_factory=datetime.now) #type: ignore
    
    def __post_init__(self) -> None:
        self.validate()
    
    def validate(self) -> None:
        try:
            EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            
            if not re.fullmatch(EMAIL_PATTERN, self.email):
                raise ValueError("The passed value is not an email")
        
        except Exception as e:
            raise e        
        
    def activate_user(self) -> None:
        self.is_active = True 
        
    def deactivate_user(self) -> None:
        self.is_active = False
        
    def to_dict(self) -> dict[str, str]:
        return {
            "first_name":self.first_name,
            "last_name":self.last_name,
            "email":self.email,
            "is_active":self.is_active,
        }