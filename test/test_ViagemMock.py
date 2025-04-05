# test_agenda.py
from unittest.mock import Mock, patch
import pytest
from src.modules.Agenda import Agenda
from src.modules.Viagem import Viagem

def test_create_viagem():
    # Mock do objeto Viagem
    mock_viagem = Mock(spec=Viagem)
    agenda = Agenda()

    # Adiciona a viagem mockada
    agenda.createViagem(mock_viagem)

    # Verifica se a viagem foi adicionada corretamente
    assert len(agenda.readViagens()) == 1
    assert agenda.readViagens()[0] == mock_viagem

def test_update_viagem():
    # Mock do objeto Viagem
    mock_viagem = Mock(spec=Viagem)
    updated_mock_viagem = Mock(spec=Viagem)
    agenda = Agenda()

    # Adiciona uma viagem e depois atualiza
    agenda.createViagem(mock_viagem)
    agenda.updateViagem(0, updated_mock_viagem)

    # Verifica se a viagem foi atualizada corretamente
    assert agenda.readViagens()[0] == updated_mock_viagem

def test_delete_viagem():
    # Mock do objeto Viagem
    mock_viagem = Mock(spec=Viagem)
    agenda = Agenda()

    # Adiciona uma viagem e depois a remove
    agenda.createViagem(mock_viagem)
    agenda.deleteViagem(0)

    # Verifica se a lista de viagens está vazia
    assert len(agenda.readViagens()) == 0

def test_clear_viagens():
    # Mock de múltiplos objetos Viagem
    mock_viagem1 = Mock(spec=Viagem)
    mock_viagem2 = Mock(spec=Viagem)
    agenda = Agenda()

    # Adiciona várias viagens e depois limpa a lista
    agenda.createViagem(mock_viagem1)
    agenda.createViagem(mock_viagem2)
    agenda.clearViagens()

    # Verifica se a lista de viagens está vazia
    assert len(agenda.readViagens()) == 0

def test_mostrar_valor_viagem():
    # Mock do objeto Viagem com valor retornado pelo método mostrar_valor
    mock_viagem = Mock(spec=Viagem)
    mock_viagem.mostrar_valor.return_value = 1500.0
    agenda = Agenda()
    agenda.createViagem(mock_viagem)

    # Verifica o valor da viagem através da função mostrar_valor_viagem da classe Agenda
    valor = agenda.mostrar_valor_viagem(0)
    assert valor == 1500.0
    mock_viagem.mostrar_valor.assert_called_once()
