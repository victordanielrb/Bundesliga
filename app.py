from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():   
    ano=2023
    return render_template("index.html",ano=ano)

@app.route('/lastchamps', methods=["POST","GET"])
def lastchamps():   
    ano=2023
    if request.method == "POST":
        ano = request.form.get('ano', '')  # Obtém o valor do campo 'ano' do formulário
    else:
        ano=2023

    return render_template("lastchamps.html",ano=ano)

@app.route('/news')
def news():
    return render_template("news.html")
    

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host="0.0.0.0",port=5000)