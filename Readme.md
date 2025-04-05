# Seminário-C214

Repositório para a apresentação do seminário de C214

## Definição
- **Nome do Membro:** Luiza Ribeiro de Matha, Mateus Correa de Melo
- **Tema:** Aplicativo de Planejamento de Viagens

## Concepção e Escopo do Projeto

### Objetivo
O objetivo deste projeto é criar um aplicativo que facilite o planejamento de viagens para os usuários. O aplicativo permitirá que os usuários gerenciem todos os aspectos de suas viagens, desde a seleção de destinos e datas até a organização de atividades e controle de custos. A ideia é proporcionar uma experiência de planejamento mais organizada e eficiente.

### Funcionalidades Principais:
- **Gerenciamento de Viagens:**
  - Adicionar novas viagens.
  - Atualizar informações de viagens existentes.
  - Remover viagens que não são mais necessárias.
  - Listar todas as viagens planejadas de forma clara e acessível.
  
- **Cálculo de Custos:**
  - Exibir o custo estimado total de cada viagem.
  - Permitir que os usuários insiram e atualizem os custos de diversos itens, como transporte, hospedagem e atividades.

- **Planejamento Detalhado:**
  - Inserir e acompanhar detalhes sobre destinos, datas e atividades planejadas.

---

## Instruções para Execução

### 1. Configuração do Ambiente Virtual

Para configurar o ambiente de desenvolvimento, siga os seguintes passos:

1. Crie um ambiente virtual utilizando o comando:
   ```bash
   python3 -m venv venv

2. Ative o ambiente virtual:
   ```bash
   .venv/Scripts/activate
   
3. Instale as dependencias:
   ```bash
   pip install -r requirements.txt

### 2. Executar o programa

Para configurar o ambiente de desenvolvimento, siga os seguintes passos:

1. Rode o seguinte comando:
   ```bash
   python src/index.py

### 3. Executar os testes

Para configurar o ambiente de desenvolvimento, siga os seguintes passos:

1. Rode os testes unitario executando seguinte comando:
   ```bash
   pytest ./test/
   
2. Rode os testes de cobertura com o seguinte comando:
    ```bash
   coverage run -m pytest .\test\    

3. Para gerar o relatorio de testes rode 
    ```bash
   coverage html    
    ```
   obs: O relatorio se encontra em htmlcov/index.html