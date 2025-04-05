
from src.modules.Agenda import Agenda
from src.modules.PlanejamentoViagem import PlanejamentoViagem

def main():
    agenda = Agenda()
    
    # Criação de planejamentos de viagem
    viagem1 = PlanejamentoViagem("Praia de Copacabana", "09:00", "20/12/2024", "João", 1000.00)
    viagem2 = PlanejamentoViagem("Serra Gaúcha", "08:00", "22/12/2024", "Maria", 1500.00)
    viagem3 = PlanejamentoViagem("Foz do Iguaçu", "10:00", "25/12/2024", "Joaquim", 2000.00)
    
    # Adicionando os planejamentos à agenda
    agenda.createViagem(viagem1)
    agenda.createViagem(viagem2)
    agenda.createViagem(viagem3)

    # Lendo e exibindo os planejamentos
    viagens = agenda.readViagens()
    print("Planejamentos de viagem:")
    for viagem in viagens:
        print(viagem)

    # Atualizando um planejamento
    viagem4 = PlanejamentoViagem("Viagem de Aniversário", "15:00", "30/12/2024", "Eduardo", 1200.00)
    agenda.updateViagem(1, viagem4)

    # Lendo e exibindo os planejamentos após a atualização
    planejamentos = agenda.readViagens()
    print("\nPlanejamentos de viagem após atualização:")
    for viagem in planejamentos:
        print(viagem)

    # Removendo um planejamento
    agenda.deleteViagem(1)

    # Lendo e exibindo os planejamentos após a exclusão
    planejamentos = agenda.readViagens()
    print("\nPlanejamentos de viagem após exclusão:")
    for viagem in planejamentos:
        print(viagem)

if __name__ == "__main__":
    main()
