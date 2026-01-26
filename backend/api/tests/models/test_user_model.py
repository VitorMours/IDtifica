from django.contrib.auth.models import AbstractUser
from django.test import TestCase 
import importlib 
import inspect 

class TestUserModel(TestCase):
  def setUp(self) -> None:
    self.state_choices = [
    ("AC", "Acre"),
    ("AL", "Alagoas"),
    ("AP", "Amapá"),
    ("AM", "Amazonas"),
    ("BA", "Bahia"),
    ("CE", "Ceará"),
    ("DF", "Distrito Federal"),
    ("ES", "Espírito Santo"),
    ("GO", "Goiás"),
    ("MA", "Maranhão"),
    ("MT", "Mato Grosso"),
    ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"),
    ("PA", "Pará"),
    ("PB", "Paraíba"),
    ("PR", "Paraná"),
    ("PE", "Pernambuco"),
    ("PI", "Piauí"),
    ("RJ", "Rio de Janeiro"),
    ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"),
    ("RO", "Rondônia"),
    ("RR", "Roraima"),
    ("SC", "Santa Catarina"),
    ("SP", "São Paulo"),
    ("SE", "Sergipe"),
    ("TO", "Tocantins"),
  ]
  
  def test_if_can_import_the_class_in_the_file(self) -> None:
    try:
      from api.models import CustomUser
    except ImportError:
      raise ImportError("Was not possible to import the user custom model")
    
  def test_if_class_its_correct_subclass(self) -> None:
    from api.models import CustomUser
    
  def test_if_custom_user_class_have_correct_fields(self) -> None:
    module = importlib.import_module("api.models")
    class_ = module.CustomUser
    self.assertTrue(hasattr(class_, "id"))
    self.assertTrue(hasattr(class_, "first_name"))
    self.assertTrue(hasattr(class_, "last_name"))
    self.assertTrue(hasattr(class_, "email"))
    self.assertTrue(hasattr(class_, "birthday"))
    self.assertTrue(hasattr(class_, "phone"))
    self.assertTrue(hasattr(class_, "city"))
    self.assertTrue(hasattr(class_, "state"))
    self.assertTrue(hasattr(class_, "created_at"))
    self.assertTrue(hasattr(class_, "updated_at"))
    self.assertTrue(hasattr(class_, "is_superuser"))
    
  def test_if_custom_user_have_states_choices_variable(self) -> None:
    module = importlib.import_module("api.models")
    class_ = module.CustomUser
    state_field = class_._meta.get_field("state")
    self.assertTrue(hasattr(state_field, "choices"))
    self.assertIsNotNone(state_field.choices)
    self.assertEqual(state_field.choices, self.state_choices)
  
  def test_if_custom_user_class_have_full_name_method(self) -> None:
    module = importlib.import_module("api.models")
    class_ = module.CustomUser
    self.assertTrue(hasattr(class_, "get_full_name"))
  
  def test_email_field_in_the_model(self) -> None:
    pass