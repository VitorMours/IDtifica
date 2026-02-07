from django.test import TestCase
from djando.db import models
from backend.api.models import CustomUser 
import importlib 
import inspect 

class TestMembersModel(TestCase):
  def setUp(self) -> None:
    pass 
  
  def test_if_can_import_the_class_in_the_file(self) -> None:
    try:
      from api.models import Members
    except ImportError:
      raise ImportError("Was not possible to import the members model")
    
  def test_if_members_class_its_correct_subclass(self) -> None:
    from api.models import Members 
    self.assertTrue(issubclass(Members, CustomUser))
    
  def test_if_members_class_have_correct_fields(self) -> None:
    module = importlib.import_module("api.models")
    clazz = module.Members    
    self.assertTrue(hasattr(clazz, "id"))
    self.assertTrue(hasattr(clazz, "first_name"))
    self.assertTrue(hasattr(clazz, "last_name"))
    self.assertTrue(hasattr(clazz, "email"))
    self.assertTrue(hasattr(clazz, "birthday"))
    self.assertTrue(hasattr(clazz, "phone"))
    self.assertTrue(hasattr(clazz, "city"))
    self.assertTrue(hasattr(clazz, "state"))
    self.assertTrue(hasattr(clazz, "created_at"))
    self.assertTrue(hasattr(clazz, "updated_at"))
    self.assertTrue(hasattr(clazz, "is_superuser"))
    
  def test_if_members_class_fields_have_correct_types(self) -> None:
    module = importlib.import_module("api.models")
    clazz = module.Members
    self.assertIsInstance(clazz._meta.get_field("id"), models.UUIDField)
    self.assertIsInstance(clazz._meta.get_field("first_name"), models.CharField)
    self.assertIsInstance(clazz._meta.get_field("last_name"), models.CharField)
    self.assertIsInstance(clazz._meta.get_field("email"), models.EmailField)
    self.assertIsInstance(clazz._meta.get_field("birthday"), models.DateField)
    self.assertIsInstance(clazz._meta.get_field("phone"), models.CharField)
    self.assertIsInstance(clazz._meta.get_field("city"), models.CharField)
    self.assertIsInstance(clazz._meta.get_field("state"), models.CharField)
    self.assertIsInstance(clazz._meta.get_field("created_at"), models.DateTimeField)
    self.assertIsInstance(clazz._meta.get_field("updated_at"), models.DateTimeField)
    self.assertIsInstance(clazz._meta.get_field("is_superuser"), models.BooleanField)
    
    
    
  
    
    
  
  