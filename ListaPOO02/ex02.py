class Viagem:
    def __init__(self):
        self._distancia = 0.0
        self._tempo = 0.0

    def set_distancia(self, d):
        if d >= 0:
            self._distancia = d
        else:
            raise ValueError("Distância não pode ser negativa.")

    def set_tempo(self, t):
        if t > 0:
            self._tempo = t
        else:
            raise ValueError("Tempo deve ser maior que zero.")

    def get_distancia(self):
        return self._distancia

    def get_tempo(self):
        return self._tempo

    def velocidade_media(self):
        return self._distancia / self._tempo


if __name__ == "__main__":
    viagem = Viagem()

    distancia = 150
    horas = 2
    minutos = 30

    tempo_total = horas + minutos / 60

    viagem.set_distancia(distancia)
    viagem.set_tempo(tempo_total)

    print("Distância:", viagem.get_distancia(), "km")
    print("Tempo:", viagem.get_tempo(), "horas")
    print("Velocidade média:", viagem.velocidade_media(), "km/h")