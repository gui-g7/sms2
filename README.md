<h1>Flask</h1>
<p>
  Se ler a documentação do Flask irá encontrar:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

```

  Sendo uma aplicação minima.
</p>
<p>
  Sem dúvidas é um back-end muito "enchuto", simples, direto e junto com a principal vantagem da linguagem Python é extremamente legível, fácil de explicar até para um leigo, o único defeito desse código é que ele não faz nada, por isso criei uma real aplicação quase minima, apenas duas páginas e que pode ser realmente usada.
</p>
<p>
  Para isso usei a estrutura padrão do Flask
</p>

```
SMS 2/
├── main.py
│
└── templates
    ├── index.html
    └── homepage.html
```

<p>
  templates é o nome padrão para a pasta do font-end no Flask e o main.py que é o que nos interessa é:
</p>

```python
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config["SECRET"] = "ajuiahfa78fh9f78shfs768fgs7f6"
#app.config["DEBUG"] = True
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("message")
def gerenciar_mensagens(mensagem):
    print(f"Mensagem: {mensagem}")
    send(mensagem, broadcast=True)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, host='localhost')
```

<p>E agora vamos destrinchar o código linha a linha. Começando por:</p>

```python
from flask import Flask, render_template
from flask_socketio import SocketIO, send
```

<p>
  Começamos como de costume importando as dependências necessárias. "Flask" e "render_templete" são módulos da biblioteca "flask". Como é de se imaginar, "Flask" é o módulo principal dessa biblioteca e está em todo uso dela e "render_template" é usada para renderizar o nosso front-end que está se chamando "templates".
</p>
<p>
  Além disso importamos "SocketIO" e "send" da biblioteca "flask_socketio". Em qualquer linguagem, "Socket" é usada para criar pontes conectando diversos aparelhos, normalmente para chats, mas também é possível usar web sockets para jogos online multiplayer por exemplo, em outras palavras, ela permite troca de informações em tempo real. E nesse caso estamos usando a SocketIO de dentro do próprio Flask, junto com um módulo dela para realizar o envio de mensagens, o "send" que traduzindo, "enviar".
</p>

```python
app = Flask(__name__)
if __name__ == "__main__":
```

<p>
  Agora peguei duas linhas de pontos diferentes para explicar algo em comum, o parâmetro/valor "__name__" que aparece nas duas.
</p>
<p>
  __name__ se refere a sua máquina, ao local onde você está executando esse código, na primeira linha passamos a sua máquina como parâmtro para a função "Flask()", isso está básicamente dizendo "Quero que a minha máquina seja o servidor." E está armazenando isso numa variável "app", armazenar o resultado de uma função é sempre importante para que ela não caia no "garbage colector" ( "Coletor de lixo" ), se algo não está armazenado em nenhuma variável o Python entende que aquilo não é importante, você não usará mais e descarta. Além disso vamos usar esse "app" posteriormente.
</p>
<p>
  A segunda linha é extremamente comum em códigos Python. """if __name__ == "__main__":""". if: significa "se:", se uma condição for atendida e nesse caso a condição é __name__ == "__main__". == é um comparador de igualdade, se o número antes dele é igual ao número após ele. Name como eu disse é a máquina e "main" é traduzido como "principal", se a sua máquina for a principal, se o código realmente estiver sendo executado no seu aparelho o código pode seguir, caso não esteja não pode. Por exemplo, não tem como usar nada com essa linha no google colab, pois nele você está usando o servidor do google.
</p>
<p>
  O próximo trecho a se comentar é:
</p>

```python
app.config["SECRET"] = "ajuiahfa78fh9f78shfs768fgs7f6"
#app.config["DEBUG"] = True
```

