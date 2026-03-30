from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Sistema de Gestão de Biblioteca", 200

@app.route("/sobre")
def sobre():
    return "Sistema desenvolvido em Flask para estudo de CI/CD", 200

@app.route("/livros")
def livros():
    return "Lista de livros cadastrados", 200

@app.route("/autores")
def autores():
    return "Lista de autores cadastrados", 200

@app.route("/contato")
def contato():
    return "Página de contato do sistema", 200

@app.route("/cadastro-livro")
def cadastro_livro():
    return "Formulário de cadastro de livros", 200

@app.route("/status")
def status():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(debug=True)