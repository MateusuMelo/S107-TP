class PlanejamentoViagem:
    def __init__(self, local: str, horario: str, data: str, nome_contratante: str, valor: float):
        self.__local = local
        self.__horario = horario
        self.__data = data
        self.__nome_contratante = nome_contratante
        self.__valor = valor

    def __repr__(self):
        return (f"PlanejamentoViagem(local={self.__local}, horario={self.__horario}, "
                f"data={self.__data}, nome_contratante={self.__nome_contratante}, "
                f"valor={self.__valor})")

    def mostrar_valor(self):
        return self.__valor

    # Métodos de atualização para cada variável
    def atualizar_local(self, novo_local: str):
        self.__local = novo_local

    def atualizar_horario(self, novo_horario: str):
        self.__horario = novo_horario

    def atualizar_data(self, nova_data: str):
        self.__data = nova_data

    def atualizar_nome_contratante(self, novo_nome_contratante: str):
        self.__nome_contratante = novo_nome_contratante

    def atualizar_valor(self, novo_valor: float):
        self.__valor = novo_valor
