import importlib 
import inspect 
import pytest 

class TestUserEntity:

    def test_if_can_import_user_entity(self) -> None:
        try: 
            from api.domain.entities.user import User
        except ImportError:
            raise ImportError("The user entity module cannot be imported")

    def test_user_entity_is_a_dataclass(self) -> None:
        try:
            from api.domain.entities.user import User  
            assert type(User) == type
        except ImportError: 
            raise ImportError("The user entity module cannot be imported")

    def test_if_user_entity_have_correct_fields(self) -> None: 
        try: 
            from api.domain.entities.user import User 
            user_entity_fields = ("id","first_name","last_name",
            "email","password","created_at","updated_at", "is_active")    
            
            entity_fields: dict = User.__dataclass_fields__
            for field in user_entity_fields:
                assert field in entity_fields.keys()
        except ImportError: 
            raise ImportError("The user entity module cannot be imported")

    def test_if_entity_have_validate_and_post_init_method(self) -> None:
        try:
            from api.domain.entities.user import User 
            validate_signature = inspect.signature(User.validate)
            post_init_signature = inspect.signature(User.__post_init__)
            
            assert hasattr(User, "validate")
            assert hasattr(User, "__post_init__")
            assert "self" in validate_signature.parameters.keys()
            assert "self" in post_init_signature.parameters.keys()
            
        except ImportError:
            raise ImportError("The user entity module cannot be imported")


    def test_if_can_validate_user_email(self) -> None:
        try:
            from api.domain.entities.user import User
            entity = User(
                first_name="Joao",
                last_name="Moura",
                email="jvrezendemoura@gmail.com",
                password="32323232312312asdasdasd1!@#"
            )
            
            with pytest.raises(ValueError) as error:
                wrong_entity = User(
                first_name="Lucas",
                last_name="uan",
                email="jvrezendemouragmail.com",
                password="nhanha"
                    
                )
            assert type(entity) == User
        
        except ImportError:
            raise ImportError("The user entity it's not importable")


    def test_if_can_deactivate_user(self) -> None:
        try:
            from api.domain.entities.user import User 
            entity = User(
                first_name="faker",
                last_name="song",
                email="faker.song@gmail.com",
                password="123123a!",
            )
            
            entity.deactivate_user()
            assert entity.is_active == False
            
        except ImportError:
            raise ImportError("This module cannot be imported")

    def test_if_can_activate_deactivated_user(self) -> None:
        try:
            from api.domain.entities.user import User 
            entity = User(
                first_name="Maria",
                last_name="Luiza",
                email="maria.luiza@gmail.com",
                password="123asd!",
                is_active=False
            )
            assert entity.is_active == False 
            entity.activate_user()
            assert entity.is_active == True
            
        except ImportError:
            raise ImportError("the user entity module cannot be imported")

    def test_if_can_return_user_dict_representation(self) -> None:
        try:
            from api.domain.entities.user import User 
            entity = User(
                first_name="Maria",
                last_name="Luiza",
                email="maria.luiza@gmail.com",
                password="123asd!",
                is_active=False
            )
            assert entity.to_dict() == {
                "first_name":"Maria",
                "last_name":"Luiza",
                "email":"maria.luiza@gmail.com",
                "is_active":False,
            }
            
        except ImportError:
            raise ImportError("the user entity module cannot be imported")

