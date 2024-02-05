
# Projeto de Teste Automatizado - Calculadora

Este projeto demonstra a automação de testes para uma aplicação de calculadora em dispositivos Android usando Behave e Appium. Utiliza o padrão Page Object Model (POM) para melhor organização e manutenibilidade do código de teste.

## Requisitos

- Python 3.8 ou superior
- Appium 1.20.2 ou superior
- Node.js 12.16.1 ou superior (para Appium)
- Emulador Android ou dispositivo real

## Configuração do Ambiente

### Instalação do Appium

```bash
npm install -g appium
```

### Configuração do Python e Dependências

```bash
python3 -m venv venv
source venv/bin/activate  # No Linux/macOS
venv\Scripts\activate.bat  # No Windows

pip install -r requirements.txt
```

### Iniciar o Servidor Appium

```bash
appium
```

## Estrutura do Projeto

```
TesteAppiumTopaz/
│
├── features/          # Arquivos de feature do Behave
│   ├── calculadora.feature
│   ├── environment.py  # Configurações de ambiente e hooks do Behave
│   └── steps/         # Implementação dos steps do Behave
│       └── soma_steps.py
│
├── pages/             # Diretório para as classes Page Object
│   ├── __init__.py
│   └── calculator_page.py
│
└── requirements.txt   # Dependências do projeto
```

## Execução dos Testes

Para executar os testes, certifique-se de que o servidor Appium esteja rodando e o dispositivo/emulador Android esteja conectado e configurado corretamente.

```bash
behave
```
