from dotenv import load_dotenv
from rich.console import Console
from rich.prompt import Prompt
from openai import OpenAI
import os
import json

load_dotenv()
console = Console()
chatgpt = OpenAI(
    api_key=os.getenv("OPENAI_KEY")
).chat


def esperar_enter():
    console.input(
        prompt="\nPressione [bold green]Enter[/bold green] para continuar...",
        password=True
    )


def gerar_pergunta(topico):
    resposta = chatgpt.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": """
                    Você é um especialista muito experiente com conhecimento em diferentes
                    assuntos e conceitos teóricos e práticos sobre {topico}.
                    Você está trabalhando em um processo de contratação e seu trabalho agora é escrever perguntas
                    para uma entrevista. Cada pergunta deve ter quatro respostas possíveis e uma delas
                    deve ser correta. Escreva essas perguntas no seguinte formato:
                    {{"enunciado": "pergunta", "opcoes": [
                        "Opção 1", "Opção 2", "Opção 3", "Opção 4"], "resposta_correta": "Opção 1"}}
                """
            },
            {
                "role": "user",
                "content": f"Gere uma questão sobre {topico}"
            }
        ],
    )

    conteudo = resposta.choices[0].message.content
    return json.loads(conteudo)


def gerar_quiz():
    pontos = 0
    continuar = ""

    topico = Prompt.ask("Sobre qual tópico você quer o quiz?")

    while continuar.lower() != "n":

        with console.status("[bold green]Processando...[/bold green]", spinner="dots"):
            pergunta = gerar_pergunta(topico)

        opcoes = pergunta["opcoes"]

        console.clear()
        console.print(f"\n[bold yellow]{pergunta['enunciado']}[/bold yellow]")
        for i, opcao in enumerate(opcoes, start=1):
            console.print(f"{i}) {opcao}")

        resposta_indice = int(Prompt.ask(
            prompt="Opção:",
            choices=["1", "2", "3", "4"]
        )
        ) - 1

        resposta_correta = pergunta["resposta_correta"]
        resposta = opcoes[resposta_indice]

        console.clear()
        if resposta == resposta_correta:
            pontos += 1
            console.print(
                f"[bold green]Resposta correta![/bold green]. Agora você tem {pontos} pontos.")
        else:
            console.print(
                f"[bold red]Resposta incorreta![/bold red]. Você continua com {pontos} pontos.")
            console.print(
                f"A resposta correta é: [yellow]{resposta_correta}.")

        continuar = Prompt.ask(
            prompt="Deseja continuar?",
            choices=["S", "n"],
            default="S"
        )


def main():
    titulo = "[bold purple]Quiz GPT[/bold purple]"
    console.clear()
    console.print(f"Bem vindo ao {titulo}")

    gerar_quiz()


main()
