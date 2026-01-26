from abc import abstractmethod, ABC 


class UserServiceInterface(ABC):
  """ Servico Relacionado ao Usuario"""
  @abstractmethod
  def verify_password(self, password: str) -> None:
    """Verifica a senha do usuario"""
    pass
  
  @abstractmethod
  def hash_password(self, password: str) -> None:
    """ Cria hash da senha do usuario"""
    pass
  
  
class EmailServiceInterface(ABC):
  
  @abstractmethod
  def send_welcome_email(self, to: str, username: str) -> None:
    """Send the welcome email"""
    pass 
  
  @abstractmethod
  def send_password_reset_email(self) -> None:
    """Send password reset email"""
    pass