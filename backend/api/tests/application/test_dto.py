from dataclasses import dataclass, is_dataclass
import importlib
import inspect
import pytest


class TestUserDTOs:
    def test_if_can_import_user_dtos(self):
        """Testa se pode importar o módulo de DTOs de usuário"""
        try:
            import api.application.dto.user
        except Exception as e:
            pytest.fail(f"Erro ao importar módulo: {e}")

    def test_if_can_import_create_user_dto(self):
        """Testa se pode importar a classe CreateUserDTO"""
        try:
            from api.application.dto.user import CreateUserDTO

            assert is_dataclass(CreateUserDTO), "CreateUserDTO deve ser um dataclass"
        except Exception as e:
            pytest.fail(f"Erro ao importar CreateUserDTO: {e}")

    def test_if_create_user_dto_has_correct_fields(self):
        """Testa se CreateUserDTO tem os campos corretos"""
        try:
            from api.application.dto.user import CreateUserDTO

            # Verifica se é dataclass
            assert is_dataclass(CreateUserDTO), "Não é um dataclass"

            # Obtém campos do dataclass
            fields = CreateUserDTO.__dataclass_fields__

            # Campos obrigatórios
            expected_fields = ["email", "first_name", "last_name", "password"]

            for field in expected_fields:
                assert field in fields, f"Campo '{field}' faltando"

        except Exception as e:
            pytest.fail(f"Erro no teste de campos: {e}")
