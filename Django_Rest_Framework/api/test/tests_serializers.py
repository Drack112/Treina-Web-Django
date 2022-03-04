from django.test import TestCase
from api.models import Vaga

from api.serializers import vaga_serializer

# Equivalente ao Form
class VagaTestSerializer(TestCase):
    def setUp(self):
        self.Vaga = Vaga(
            titulo="Vaga de Programador React",
            descricao="Uma Vaga para quem sabe React.",
            salario="3.200",
            local="São Paulo",
            quantidade=2,
            contato="vagareact@gmail.com",
            tipo_contratacao="CLT",
            tecnologias=["Python"],
        )

        self.serializer = vaga_serializer.VagaSerializer(instance=self.Vaga)

    def teest_Verify_serializer(self):
        """Verificação Dos Campos Serializados"""
        # Armazenar todos os campos do serializer
        data = self.serializer.data
        self.assertEqual(
            set(data.keys()),
            set(
                [
                    "titulo",
                    "descricao",
                    "salario",
                    "local",
                    "quantidade",
                    "contato",
                    "tipo_contratacao",
                    "tecnologias",
                ]
            ),
        )
