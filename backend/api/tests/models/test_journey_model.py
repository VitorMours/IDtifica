from django.test import TestCase 
from django.db import models
import importlib 
import inspect 


class TestJourneyModel(TestCase):
  def setUp(self) -> None:
    pass 
  
  def test_if_can_import_model_class_in_module(self) -> None:
    try:
      from api.models import Journey
    except ImportError: 
      raise ImportError("Was not possible to import the journey model")
    
  def test_if_journey_class_superclass_its_correct(self) -> None:
    from api.models import Journey 
    self.assertTrue(issubclass(Journey, models.Model))
    
    
  def test_if_journey_model_have_correct_fields(self) -> None:
    module = importlib.import_module("api.models")
    class_ = module.Journey
    self.assertTrue(hasattr(class_, "id"))
    self.assertTrue(hasattr(class_, "name"))
    self.assertTrue(hasattr(class_, "description"))
    self.assertTrue(hasattr(class_, "is_active"))
    self.assertTrue(hasattr(class_, "sector"))
    self.assertTrue(hasattr(class_, "created_at"))
    self.assertTrue(hasattr(class_, "updated_at"))
    
  def test_if_journey_model_fields_have_correct_types(self) -> None:
    module = importlib.import_module("api.models")
    class_ = module.Journey 
    self.assertIsInstance(class_._meta.get_field("id"), models.UUIDField)
    self.assertIsInstance(class_._meta.get_field("name"), models.CharField)
    self.assertIsInstance(class_._meta.get_field("description"), models.CharField)
    self.assertIsInstance(class_._meta.get_field("is_active"), models.BooleanField)
    self.assertIsInstance(class_._meta.get_field("sector"), models.ForeignKey)
    self.assertIsInstance(class_._meta.get_field("created_at"), models.DateTimeField)
    self.assertIsInstance(class_._meta.get_field("updated_at"), models.DateTimeField)
    
    
  def test_if_journey_model_fields_have_correct_attributes(self) -> None:
    module = importlib.import_module("api.models")
    class_ = module.Journey 
    id_field = class_._meta.get_field("id")
    self.assertTrue(id_field.primary_key)
    self.assertFalse(id_field.editable)
    self.assertTrue(id_field.default is not None)
    self.assertFalse(id_field.blank)
    self.assertFalse(id_field.null)
    
    is_active_field = class_._meta.get_field("is_active")