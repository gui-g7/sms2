<h1>Flask</h1>
<p>
  Se ler a documentação do Flask irá encontrar:

```
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

```
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
