from flask import Flask, render_template, request, redirect, url_for
from services.setor_service import listar_setores, criar_setor

app = Flask(__name__)

@app.route("/")
def index():
    setores = listar_setores()
    return render_template("index.html", setores=setores)

@app.route("/setor/criar", methods=["POST"])
def criar_setor_route():
    nome = request.form.get("nome")
    descricao = request.form.get("descricao")
    criar_setor(nome, descricao)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
