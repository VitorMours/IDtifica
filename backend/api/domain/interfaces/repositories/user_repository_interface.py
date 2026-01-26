from abc import ABC, abstractmethod 
from api.domain.entities.user import User 
from typing import List

class UserRepositoryInterface(ABC):
    """Interface para deteriminar comportamento de repositorios de usuario"""

    @abstractmethod 
    def get_all_users(self) -> List[User]:
        """Pega todas as entidades do banco de dados"""
        pass


    @abstractmethod
    def get_user_by_id(self, _id: int) -> User:
        """Pega um unico usuario por meio do seu id"""
        pass 

    @abstractmethod 
    def update_user(self, user: User, user_data: User) -> User:
        """Atualiza um determinado usuario"""
        pass    

    @abstractmethod 
    def delete_user(self, user: User) -> bool:
        """Deleta um determinado usuario"""
        pass 
    
    @abstractmethod
    def soft_delete(self, user: User) -> bool:
        """Faz soft delete em um determinado usuario"""
        pass
    
    
    def __str__(self) -> None:
        return "<UserRepositoryInterface>"