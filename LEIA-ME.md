# Projeto de Automação de Testes com Playwright (Python)

Este projeto demonstra automação de testes de API e interface utilizando Python, Playwright e Pytest.

---

## Funcionalidades

- Testes de API com Playwright
- Automação de interface (login e fluxo de checkout)
- Uso de fixtures reutilizáveis com Pytest
- Validação de status code e corpo da resposta
- Estrutura organizada de testes

---

## Tecnologias

- Python
- Playwright
- Pytest

---

## Estrutura do Projeto

automation/
│
├── tests/
│   ├── api/
│   ├── login/
│   ├── checkout/
│
├── conftest.py
├── requirements.txt
├── README.md

---

## Setup

1. Clone o repositório:
    git clone https://github.com/romulo-pires/Automation.git
    cd Automation

2. Instale as dependências:
    pip install -r requirements.txt

3. Instale o Playwright:
    playwright install

4. Executar os testes:
    pytest -s -v

---

## Observações

- Este projeto utiliza a API ReqRes para fins de aprendizado.
