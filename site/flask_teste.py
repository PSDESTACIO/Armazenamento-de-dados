from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('postgreteste.html')

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome']
    email = request.form['email']
    
    # Essa parte do código que podemos enviar o dado para o PostregreSQL
    print("Nome:", nome)
    print("Email:", email)
    print("Dados recebidos com sucesso.") 

    return redirect(url_for('dados_enviados'))

# TODO: Implementar acesso a outro sites pelo Flask

# Redireciona usuario para pagina principal apos inserir dados
@app.route('/index.html')
def dados_enviados():
    return render_template('index.html')

# Abre o aplicativo na porta 5500 e o roda.
if __name__ == '__main__':
    app.run(debug=True, port = 5500)