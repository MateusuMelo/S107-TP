from src.modules.Viagem import Viagem
class Agenda:
    def __init__(self):
        self.__viagens = []

    def createViagem(self, viagem:Viagem):
        self.__viagens.append(viagem)

    def readViagens(self):
        return self.__viagens

    def updateViagem(self, index, updated_viagem):
        self.__viagens[index] = updated_viagem

    def deleteViagem(self, index):
        self.__viagens.pop(index)

    def clearViagens(self):
        self.__viagens = []

    def mostrar_valor_viagem(self, index):
        if 0 <= index < len(self.__viagens):
            return self.__viagens[index].mostrar_valor()
        else:
            return "Índice inválido."
