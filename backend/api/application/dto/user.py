"""
DTOs para usuarios
"""
#first_name: str
#last_name: str
#email: str
#password: str
#is_active: bool = True
#id: UUID = field(default_factory=uuid4)
#created_at: datetime = field(default_factory=datetime.now) #type: ignore
#updated_at: datetime = field(default_factory=datetime.now) #type: ignore

from typing import Optional 
from dataclasses import dataclass 

@dataclass 
class CreateUserDTO:
  """DTO para criação de usuario"""
  email: str
  first_name: str
  last_name: str
  password: str