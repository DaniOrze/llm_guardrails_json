# Aplicação de Geração e Validação de Dados Sintéticos com Guardrails e OpenAI
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![ChatGPT](https://img.shields.io/badge/ChatGPT-74aa9c?logo=openai&logoColor=white)](#)
[![JSON](https://img.shields.io/badge/JSON-000?logo=json&logoColor=fff)](#)

## Visão Geral

Esta aplicação utiliza as bibliotecas **GuardrailsAI** e **OpenAI** para gerar registros sintéticos formatados, seguindo um padrão pré-definido. Além disso, os dados gerados são validados usando os mecanismos de validação de JSON fornecidos pelo Guardrails.

O exemplo da aplicação é gerar dois registros sintéticos de medicamentos, com horários de administração e validar se estão no formato esperado.

Pode-se alterar o prompt para o que se encaixar melhor no seu projeto.

---

## Tecnologias Utilizadas

- **[GuardrailsAI](https://www.guardrailsai.com/)**: Validação de dados e integração com modelo de linguagem.
- **[OpenAI](https://platform.openai.com/docs/)**: Para a geração dos registros sintéticos.
- **[Python](https://www.python.org/)**: Linguagem de programação principal.
- **[Dotenv](https://pypi.org/project/python-dotenv/)**: Gerenciamento de variáveis de ambiente.

---

## Pré-requisitos

1. Python 3.12 instalado.
2. Uma chave de API válida do OpenAI.
3. As dependências dentro do arquivo pyproject.toml

## Instalação

1. Instale as dependências:

Utilize o UV para instalar as dependências:
```
uv install
```

2. Configurar a chave da API da OpenAI:

Crie um arquivo .env na raiz do projeto com a variável de ambiente OPENAI_KEY_SECRET:
```
OPENAI_KEY_SECRET=your_openai_api_key
```

3. Instale o Hub do Gaurdrails de JSON
```
guardrails hub install hub://guardrails/valid_json
```

## Execução

Basta colocar no terminal de python:
```
python data_generate.py
```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou um pull request.

## Licença

Este projeto está licenciado sob a licença [MIT](./LICENSE).