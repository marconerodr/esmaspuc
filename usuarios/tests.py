from django.test import TestCase, LiveServerTestCase
from .models import PopulacaoUsuaria

# Create your tests here.

class PopulacaoUsuariaTestCase(TestCase):
    def test_create_user(self):
        # Cria um usuário
        usuario = PopulacaoUsuaria.objects.create(nome='John', sobrenome='Doe', email='john.doe@example.com', cpf='12345678900')
        
        # Verifica se os atributos foram definidos corretamente
        self.assertEqual(usuario.nome, 'John')
        self.assertEqual(usuario.sobrenome, 'Doe')
        self.assertEqual(usuario.email, 'john.doe@example.com')
        self.assertEqual(usuario.cpf, '12345678900')