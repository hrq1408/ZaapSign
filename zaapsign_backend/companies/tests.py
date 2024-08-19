# myapp/tests.py
from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import User

class UserModelTest(TestCase):
    def test_valid_email(self):
        # Testa a criação de um User com um e-mail válido
        user = User(email='valid@example.com')
        try:
            user.full_clean()  # Valida todos os campos do modelo
            user.save()  # Salva o modelo
        except ValidationError as e:
            self.fail(f"Validation error occurred: {e}")

    def test_invalid_email(self):
        # Testa a criação de um User com um e-mail inválido
        user = User(email='invalid-email')
        with self.assertRaises(ValidationError):
            user.full_clean()  # Valida todos os campos do modelo
