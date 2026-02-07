from django.test import TestCase 
from django.db import models 
import importlib 
import inspect 

class TestSectorModel(TestCase):
  def setUp(self) -> None:
    pass
  
  def test_if_can_import_model_class_in_module(self) -> None:
    try: 
      from api.models import Sector
    except ImportError:
      raise ImportError("Was not possible to import the esctor model")
    
  def test_if_esctor_model_have_correct_superclass(self) -> None:
    from api.models import Sector 
    self.assertTrue(issubclass(Sector, models.Model))
    
  def test_if_sector_model_have_correct_fields(self) -> None:
    module = importlib.import_module("api.models")
    class_ = module.Sector
    self.assertTrue(hasattr(class_, "id"))
    self.assertTrue(hasattr(class_, "search_code"))
    self.assertTrue(hasattr(class_, "name"))
    self.assertTrue(hasattr(class_, "description"))
    self.assertTrue(hasattr(class_, "is_active"))
    self.assertTrue(hasattr(class_, "created_at"))
    self.assertTrue(hasattr(class_, "updated_at"))
    self.assertTrue(hasattr(class_, "responsable"))
    
    
  def test_if_sector_model_fields_have_correct_type(self) -> None:
    module = importlib.import_module("api.models")
    class_ = module.Sector 
    self.assertIsInstance(class_._meta.get_field("id"), models.UUIDField)
    self.assertIsInstance(class_._meta.get_field("search_code"), models.CharField)
    self.assertIsInstance(class_._meta.get_field("name"), models.CharField)
    self.assertIsInstance(class_._meta.get_field("description"), models.TextField)
    self.assertIsInstance(class_._meta.get_field("created_at"), models.DateTimeField)
    self.assertIsInstance(class_._meta.get_field("updated_at"), models.DateTimeField)
    self.assertIsInstance(class_._meta.get_field("is_active"), models.BooleanField)
    self.assertIsInstance(class_._meta.get_field("responsable"), models.ForeignKey)
    
    
  def test_if_sector_model_fields_have_correct_attributes(self) -> None:
    pass
  
  
