from ollama import chat

def perguntar_ao_tutor(pergunta):
    mensagens = [
        {
            "role": "system",
            "content": """
Você é um tutor educacional.

Sua função é ajudar o usuário a estudar e compreender novos assuntos.

Ao responder:
- Explique o conceito de forma simples e didática.
- Use exemplos quando forem úteis.
- Use analogias quando ajudarem na compreensão.
- Destaque os pontos mais importantes.
- Finalize com um pequeno resumo.
- Crie 2 perguntas para testar o conhecimento do usuário.
"""
        },
        {
            "role": "user",
            "content": pergunta
        }
    ]

    try:
        resposta = chat(
            model="gemma3:4b",
            messages=mensagens
        )

        return resposta.message.content

    except Exception as erro:
        return f"Não foi possível consultar o tutor. Erro: {erro}"


pergunta = input("O que você deseja estudar?")

if pergunta.strip():
    resposta = perguntar_ao_tutor(pergunta)
    print(resposta)
else:
    print("Você precisa digitar um assunto pra estudar.")




