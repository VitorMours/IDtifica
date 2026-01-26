import inspect 
import importlib 
import pytest 
from abc import ABC


class TestUserRepositoryInterface:

    def test_if_can_import_user_repository_interface(self) -> None:
        try:
            import api.domain.interfaces.repositories.user_repository_interface
            
        except ImportError:
            raise ImportError("Cannot import the UserRepositoryInterface in the path")


    def test_if_user_repository_interface_is_a_class(self) -> None:
        try: 
            from api.domain.interfaces.repositories.user_repository_interface import UserRepositoryInterface
            assert issubclass(UserRepositoryInterface, ABC) 

        except ImportError: 
            raise ImportError("Cannot import the UserRepositoryInterface in the path")

    def test_if_user_repository_interface_file_can_import_user_entity(self) -> None:
        try:
            from api.domain.interfaces.repositories.user_repository_interface import UserRepositoryInterface
            from api.domain.interfaces.repositories.user_repository_interface import User

        except ImportError:
            raise ImportError("Cannot import the UserEntity in the user_repository_interface file")
    
        
    def test_if_user_repository_interface_class_have_get_all_users_method(self) -> None:
        module = importlib.import_module("api.domain.interfaces.repositories.user_repository_interface")
        class_ = module.UserRepositoryInterface
        assert hasattr(class_, "get_all_users")

    def test_if_user_repository_interface_class_have_get_by_id_method(self) -> None:
        module = importlib.import_module("api.domain.interfaces.repositories.user_repository_interface")
        class_ = module.UserRepositoryInterface
        assert hasattr(class_, "get_user_by_id")

    def test_if_user_repository_interface_class_have_update_method(self) -> None:
        module = importlib.import_module("api.domain.interfaces.repositories.user_repository_interface")
        class_ = module.UserRepositoryInterface
        assert hasattr(class_, "update_user")

    def test_if_user_repository_interface_class_have_delete_method(self) -> None:
        module = importlib.import_module("api.domain.interfaces.repositories.user_repository_interface")
        class_ = module.UserRepositoryInterface
        assert hasattr(class_, "delete_user")

    def test_if_user_repository_interface_class_have_soft_delete_method(self) -> None:
        module = importlib.import_module("api.domain.interfaces.repositories.user_repository_interface")
        class_ = module.UserRepositoryInterface
        assert hasattr(class_, "soft_delete")


    def test_if_user_repository_interface_have_str_represetation_method(self) -> None: 
        module = importlib.import_module("api.domain.interfaces.repositories.user_repository_interface")
        class_ = module.UserRepositoryInterface
        assert hasattr(class_, "__str__")

