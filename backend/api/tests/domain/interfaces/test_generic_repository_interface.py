import importlib 
import inspect 
import pytest 
from abc import ABC, abstractmethod 



class TestRepositoryInterface:
  def setUp(self) -> None:
    pass 
  def test_if_can_import_the_generic_repository_interface(self) -> None: 
    try: 
      from api.domain.interfaces.repositories.repository_interface import RepositoryInterface 
    except ImportError:
      raise ImportError("Was not possible to import the generice repository interface")