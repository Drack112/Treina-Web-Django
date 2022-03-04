from django.test import TestCase
from api.models import Vaga


class VagaTestModel(TestCase):
    def setUp(self):
        self.Vaga = Vaga(
            titulo="Vaga de Programador React",
            descricao="Uma Vaga para quem sabe React.",
            salario="3.200",
            local="São Paulo",
            quantidade="2",
            contato="vagareact@gmail.com",
            tipo_contratacao="CLT",
        )

    def test_verify(self):
        """Retornar o nome da Tecnologia que foi passada acima."""
        self.assertQuerysetEqual(self.Vaga.titulo, "Vaga de Programador React")
        self.assertQuerysetEqual(self.Vaga.descricao, "Uma Vaga para quem sabe React.")
        self.assertQuerysetEqual(self.Vaga.salario, "3.200")
        self.assertQuerysetEqual(self.Vaga.local, "São Paulo")
        self.assertQuerysetEqual(self.Vaga.quantidade, "2")
        self.assertQuerysetEqual(self.Vaga.contato, "vagareact@gmail.com")
        self.assertQuerysetEqual(self.Vaga.tipo_contratacao, "CLT")
