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