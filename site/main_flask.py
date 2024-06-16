import sys
import os

# Adicione o diretório pai ao sys.path para resolver importações de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, redirect, url_for # type: ignore
from model.cliente import Cliente
from repositorypostgre.cliente_repository_postgre import ClienteRepositoryPostgre

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1048576  # O valor é contado em MB, nesse caso vai ser 50 MB, pq o valor da esquerda é tal
app.secret_key = 'supersecretkey'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'mp4'}

@app.route('/')
def index():
    return render_template('postgreteste.html')

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['email']
    
    # Create a new Cliente instance
    cliente = Cliente(nome=nome, email=email, senha=senha)
    
    # Try to save the new cliente to the PostgreSQL database
    try:
        repository = ClienteRepositoryPostgre()
        msg = repository.save(cliente)
        print(f"Dados recebidos com sucesso: {msg}")
    except Exception as error:
        print(f"Error: {error}")
        return "Um erro ocorreu enquanto os dados tentaram ser salvos"

    return redirect(url_for('dados_enviados'))

# Redireciona usuario para pagina principal apos inserir dados
@app.route('/index.html')
def dados_enviados():
    return render_template('index.html')

@app.route('/Contato.html')
def rota_Contato():
    return render_template('Contato.html')

@app.route('/QuemSomos.html')
def rota_QuemSomos():
    return render_template('QuemSomos.html')

@app.route('/video.html')
def rota_video():
    return render_template('video.html')

@app.route('/postgreteste.html')
def rota_postgreteste():
    return render_template('postgreteste.html')

# Abre o aplicativo na porta 5500 e o roda.
if __name__ == '__main__':
    app.run(debug = True, port = 5500)