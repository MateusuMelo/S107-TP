# Viagem.py

class Viagem:
    def __init__(self, destino, data, custo):
        self.destino = destino
        self.data = data
        self.custo = custo

    def mostrar_valor(self):
        return self.custo

    def __repr__(self):
        return f"Viagem(destino='{self.destino}', data='{self.data}', custo={self.custo})"
