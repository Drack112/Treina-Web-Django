from mixer.backend.django import mixer

from api.models import Vaga, Tecnologia

mixer.cycle(100).blend(Tecnologia)
mixer.cycle(100).blend(Vaga)
