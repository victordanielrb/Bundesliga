from flask import Flask, render_template, request, url_for,redirect
import time
from flask_mysqldb import MySQL
from MySQLdb import _mysql

app = Flask(__name__)

# Configurações do MySQL
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'corinthians'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'  # Isso é opcional, mas torna o retorno do MySQL em um dicionário, o que é mais conveniente para trabalhar com dados

mysql = MySQL(app)



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
    

@app.route('/processar', methods=['POST'])
def processar():
    if request.method == 'POST':

        nome = request.form['nome']
        email = request.form['email']
        
              # Conectar ao banco de dados e inserir os dados
                ##ERRO AQUI## -- > **cur = mysql.connection.cursor()**
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO newsletter (name, email) VALUES (%s, %s)", (nome, email))
        mysql.connection.commit()
        cur.close()
        
       
        
        return redirect(url_for('news'))
      

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host="0.0.0.0",port=5000)