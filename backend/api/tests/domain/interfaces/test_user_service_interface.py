import inspect 
import importlib 
import pytest 
from abc import ABC 

class TestUserServiceInterface:
  def setUp(self) -> None:
    pass 
  
  def test_importing_the_file_from_the_folder(self) -> None:
    try:
      from api.domain.interfaces.services.user_service_interface import UserServiceInterface 
    except ImportError as e:
      raise ImportError("Was not possibile to import the user service interface")
    
  def test_if_user_service_interface_have_verify_password_method(self) -> None:
    try:
      from api.domain.interfaces.services.user_service_interface import UserServiceInterface
      assert hasattr(UserServiceInterface, "verify_password")
    except Exception as e:
      raise e
    
  def test_if_user_service_interface_have_hash_password_method(self) -> None:
    try:
      from api.domain.interfaces.services.user_service_interface import UserServiceInterface 
      assert hasattr(UserServiceInterface, "hash_password")
    except Exception as e:
      raise e
    
class TestEmailServiceInterface:
  def setUp(self) -> None:
    pass 
  
  def test_if_can_import_the_service_interface(self) -> None:
    try:
      from api.domain.interfaces.services.user_service_interface import EmailServiceInterface
    except Exception as e:
      raise e
    
  def test_if_email_service_interface_have_send_welcome_email_method(self) -> None:
    try:
      from api.domain.interfaces.services.user_service_interface import EmailServiceInterface
      assert hasattr(EmailServiceInterface, "send_welcome_email")
    except Exception as e:
      raise e
    
  def test_if_email_service_interface_have_send_password_reset_email_method(self) -> None:
    try:
      from api.domain.interfaces.services.user_service_interface import EmailServiceInterface 
      assert hasattr(EmailServiceInterface, "send_password_reset_email")
    except Exception as e:
      raise e