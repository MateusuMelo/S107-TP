import pytest
from src.modules.PlanejamentoViagem import PlanejamentoViagem

def test_criar_planejamento_viagem():
    data = "15/11/2023 10:30"
    viagem = PlanejamentoViagem(
        local="Rio de Janeiro",
        horario="10:30",
        data=data,
        nome_contratante="João Silva",
        valor=1200.0
    )
    assert viagem.mostrar_valor() == 1200.0
    assert str(viagem) == (
        "PlanejamentoViagem(local=Rio de Janeiro, horario=10:30, "
        "data=15/11/2023 10:30, nome_contratante=João Silva, valor=1200.0)"
    )

def test_atualizar_local():
    data = "15/11/2023 10:30"
    viagem = PlanejamentoViagem("Rio de Janeiro", "10:30", data, "João Silva", 1200.0)
    viagem.atualizar_local("São Paulo")
    assert "São Paulo" in str(viagem)

def test_atualizar_horario():
    data = "15/11/2023 10:30"
    viagem = PlanejamentoViagem("Rio de Janeiro", "10:30", data, "João Silva", 1200.0)
    viagem.atualizar_horario("15:00")
    assert "horario=15:00" in str(viagem)

def test_atualizar_data():
    data_inicial = "15/11/2023 10:30"
    nova_data = "20/12/2023 14:00"
    viagem = PlanejamentoViagem("Rio de Janeiro", "10:30", data_inicial, "João Silva", 1200.0)
    viagem.atualizar_data(nova_data)
    assert "data=20/12/2023 14:00" in str(viagem)

def test_atualizar_nome_contratante():
    data = "15/11/2023 10:30"
    viagem = PlanejamentoViagem("Rio de Janeiro", "10:30", data, "João Silva", 1200.0)
    viagem.atualizar_nome_contratante("Maria Oliveira")
    assert "Maria Oliveira" in str(viagem)

def test_atualizar_valor():
    data = "15/11/2023 10:30"
    viagem = PlanejamentoViagem("Rio de Janeiro", "10:30", data, "João Silva", 1200.0)
    viagem.atualizar_valor(1500.0)
    assert viagem.mostrar_valor() == 1500.0

