# 🤖 Assistente de Estudos com IA

Meu primeiro projeto desenvolvido com foco em Python e Inteligência Artificial.

O Assistente de Estudos permite que o usuário informe um assunto ou uma dúvida pelo terminal e receba uma explicação didática gerada por um modelo de linguagem executado localmente.

O projeto foi desenvolvido principalmente com o objetivo de aprender, na prática, como uma aplicação Python pode se comunicar com um LLM.

## 🎯 Objetivo

Criar uma aplicação simples de IA capaz de atuar como um tutor educacional.

O assistente é instruído a:

- Explicar conceitos de forma simples e didática
- Utilizar exemplos quando forem úteis
- Criar analogias para facilitar a compreensão
- Destacar os pontos mais importantes
- Gerar um pequeno resumo
- Criar perguntas para testar o conhecimento

## 🧠 Como funciona

O fluxo da aplicação é:

text
Usuário
   ↓
Aplicação Python
   ↓
Prompt de sistema + pergunta
   ↓
Ollama
   ↓
Gemma 3 4B
   ↓
Resposta
   ↓
Terminal


O Python recebe a pergunta do usuário e cria as mensagens que serão enviadas ao modelo.

O Ollama é utilizado para executar o modelo de linguagem localmente.

O Gemma 3 4B recebe as instruções e a pergunta e gera a resposta utilizada pela aplicação.

## 🛠️ Tecnologias utilizadas

- Python
- Ollama
- Gemma 3 4B
- Git
- GitHub

## 📂 Estrutura do projeto

text
Projeto-ia-documentos/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md


A pasta .venv é utilizada localmente para o ambiente virtual Python e não é versionada pelo Git.

## 🚀 Como executar

### 1. Clone o repositório

bash
git clone URL_DO_REPOSITORIO


### 2. Entre na pasta do projeto

bash
cd Projeto-ia-documentos


### 3. Crie um ambiente virtual

bash
python -m venv .venv


### 4. Ative o ambiente virtual

No Windows PowerShell:

powershell
.\.venv\Scripts\Activate.ps1


### 5. Instale as dependências Python

bash
python -m pip install -r requirements.txt


### 6. Instale o Ollama e baixe o modelo

Com o Ollama instalado:

bash
ollama pull gemma3:4b


### 7. Execute a aplicação

bash
python app.py


Depois, basta informar o assunto que deseja estudar.

## 💡 Exemplo

text
O que você deseja estudar? Explique o que é uma API REST


O assistente utilizará o modelo de IA para criar uma explicação voltada para estudos.

## 📚 Conceitos praticados

Durante o desenvolvimento deste projeto foram praticados conceitos como:

- Variáveis e strings em Python
- input() e print()
- Listas e dicionários
- Funções
- Parâmetros e argumentos
- return
- Condicionais
- Tratamento de exceções
- Ambientes virtuais
- Gerenciamento de dependências com pip
- Integração de Python com um LLM
- Prompt engineering
- System prompts e user prompts
- Git e controle de versão

## 🔮 Próximas evoluções

Este projeto representa a primeira versão do Assistente de Estudos.

Possíveis evoluções futuras incluem:

- Interface web
- Histórico de perguntas
- RAG para estudar utilizando PDFs e documentos
- Agentes de IA
- Integração com serviços de IA na nuvem
- Exploração de Azure AI e Microsoft Foundry

## 📌 Status

✅ V1 funcional

A primeira versão permite realizar perguntas pelo terminal e receber respostas educacionais utilizando um modelo de linguagem executado localmente.