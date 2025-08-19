from flask import Flask, render_template, request

app = Flask(__name__)

# Rota principal
@app.route("/")
def home():
    return render_template(
        "index.html",
        texto="Lista de Exercícios WEB",
        paragrafo="Escolha um exercício e insira os dados para resolver.",
        h2="Exercícios de lógica simples",
        H3python="Usando Flask para processar formulários"
    )

# Rota de processamento de soma_
@app.route("/soma", methods=["POST"])
def soma():
    numero1 = float(request.form["numero1"])
    numero2 = float(request.form["numero2"])
    resultado = numero1 + numero2
    return render_template("index.html", resultado_soma=f"A soma é: {resultado}")

# Rota de processamento de subtração
@app.route("/subtracao", methods=["POST"])
def subtracao():
    numero1 = float(request.form["numero1"])
    numero2 = float(request.form["numero2"])
    resultado = numero1 - numero2
    return render_template("index.html", resultado_sub=f"A subtração é: {resultado}")

# Rota de processamento de maior idade
@app.route("/maioridade", methods=["POST"])
def maioridade():
    idade = int(request.form["idade"])
    if idade >= 18:
        mensagem = "Você é maior de idade!"
    else:
        mensagem = "Você é menor de idade!"
    return render_template("index.html", resultado_idade=mensagem)

# Rota de contagem de 1 até 100 de 2 em 2
@app.route("/contar", methods=["POST"])
def contar():
    numeros = list(range(1, 101, 2))  # Começa em 1, vai até 100, de 2 em 2
    return render_template("index.html", resultado_contagem=numeros)

if __name__ == '__main__':
    app.run(debug=True)
