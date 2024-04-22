from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():   
    ano=0
    return render_template("index.html",ano=ano)

@app.route('/lastchamps', methods=["POST","GET"])
def lastchamps():   
    if request.method == "POST":
        ano = request.form.get('ano', '')  # Obtém o valor do campo 'ano' do formulário
    else:
        ano = request.args.get('ano', '')  # Se a solicitação for GET, obtém o valor de 'ano' dos parâmetros da URL

    return render_template("lastchamps.html", ano=ano)

    

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host="0.0.0.0",port=5000)