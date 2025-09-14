# Quiz com ChatGPT

### Como instalar e executar.
1. Criar o ambiente e ativar.
```sh
# Criar ambiente
python -m venv .venv

# Ativar
# Se for Posix
source .venv/bin/activate
# Se for Windows
.venv\Scripts\activate.bat
```

2. Instalar os pacotes.
```sh
pip install -r requirements.txt
```

3. Criar arquivo de configurações.
```sh
cp env_example .env
# colocar o valor no parâmetro OPENAI_KEY
```

4. Executar o projeto.
```sh
python main.py
```

### Imagens do projeto.
#### Início do Quiz.
![Viewport do Projeto][imagem1]

#### Questão que o chatGPT buscou.
![Viewport do Projeto][imagem2]

#### Resposta certa.
![Viewport do Projeto][imagem3]

#### Resposrta Errada.
![Viewport do Projeto][imagem4]


### Pacotes instalados.
```sh
pip install rich openai python-dotenv
```

[imagem1]: https://github.com/Jhonatan-Pereira/quiz-chatgpt/blob/main/images/imagem_1.png "Imagem 1"
[imagem2]: https://github.com/Jhonatan-Pereira/quiz-chatgpt/blob/main/images/imagem_2.png "Imagem 2"
[imagem3]: https://github.com/Jhonatan-Pereira/quiz-chatgpt/blob/main/images/imagem_3.png "Imagem 3"
[imagem4]: https://github.com/Jhonatan-Pereira/quiz-chatgpt/blob/main/images/imagem_4.png "Imagem 4"