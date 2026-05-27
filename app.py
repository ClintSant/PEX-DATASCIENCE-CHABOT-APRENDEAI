from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from fluxo import processar_mensagem

app = Flask(__name__)
CORS(app, resources={r"/chat": {"origins": "*"}})

@app.after_request
def add_headers(response):
    response.headers["ngrok-skip-browser-warning"] = "true"
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    dados = request.get_json()
    sessao = dados.get("sessao", {})
    entrada = dados.get("mensagem", "")
    resposta, sessao_atualizada = processar_mensagem(entrada, sessao)
    return jsonify({"resposta": resposta, "sessao": sessao_atualizada})

if __name__ == "__main__":
    app.run(debug=True)