from mixer.backend.django import mixer
from clientes.models import Pedido

# Gerar dados falsos para teste em banco de dados
mixer.cycle(150).blend(Pedido)
