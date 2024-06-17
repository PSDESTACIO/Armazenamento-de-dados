# Imports que ajudam a andar pelos diretorios
import sys
import os
import uuid
from moviepy.editor import VideoFileClip # type: ignore
import psycopg2 # type: ignore

# Adicione o diretório pai ao sys.path para resolver importações de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, redirect, url_for # type: ignore
from werkzeug.utils import secure_filename # type: ignore

# Importar codigo que define funcionamento do PostgreSQL.
from model.cliente import Cliente
from repositorypostgre.cliente_repository_postgre import ClienteRepositoryPostgre

app = Flask(__name__) # Serve para inicializar
app.config['UPLOAD_FOLDER'] = 'static/uploads' # Pasta no qual vai ser direcionado
app.config['MAX_CONTENT_LENGTH'] = 50 * 1048576  # O valor é contado em MB, nesse caso vai ser 50 MB, pq o valor da esquerda é tal
app.secret_key = 'supersecretkey' # Responsável pela segurança de formulários e afins

#Responsável pela extensão do arquivo
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'mp4', 'avi', 'mov', 'mkv'}

def get_video_metadata(file_path):
    clip = VideoFileClip(file_path)
    duration = clip.duration
    width, height = clip.size
    return duration, width, height,

def save_metadata_to_db(filename, title, description, duration, width, height,):
    conn = psycopg2.connect(
        dbname="banco1",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO video_metadata (filename, title, description, duration, width, height)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (filename, title, description, duration, width, height)
    )
    conn.commit()
    cur.close()
    conn.close()

def delete_metadata_from_db(filename):
    conn = psycopg2.connect(
        dbname="banco1",
        user="postgres",
        password="root",
        host="localhost",
        port="5432" # 5432 é o certo, a 5500 é para testar
    )
    cur = conn.cursor()
    cur.execute(
            """
            DELETE FROM video_metadata WHERE filename = %s
            """,
            (filename,)
    )
    conn.commit()
    cur.close()
    conn.close()


@app.route('/')
def index():
    return render_template('postgreteste.html')

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['email']
    
    # Cria uma nova instancia de Cliente
    cliente = Cliente(nome=nome, email=email, senha=senha)
    
    # Tenta salvar cliente para PostGre
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
    video_files = os.listdir(app.config['UPLOAD_FOLDER']) # Lista todos os arquivos no diretório de uploads
    video_files = [f for f in video_files if allowed_file(f)] # Filtra apenas os arquivos de vídeo permitidos
    video_files.sort(key=lambda x: os.path.getctime(os.path.join(app.config['UPLOAD_FOLDER'], x)), reverse=True) # Ordena os arquivos por data de criação, do mais recente ao mais antigo
    
    videos = []  # Cria uma lista para armazenar os vídeos e seus títulos
    for video_file in video_files:
        
        title_file = video_file.rsplit('.', 1)[0] + '.title.txt' # Gera o nome do arquivo de título correspondente ao vídeo
        description_file = video_file.rsplit('.', 1)[0] + '.desc.txt' # Gera o nome do arquivo de descrição correspondente ao vídeo

        # Constrói o caminho completo do arquivo de título
        title_path = os.path.join(app.config['UPLOAD_FOLDER'], title_file) 
        description_path = os.path.join(app.config['UPLOAD_FOLDER'], description_file)

        title = "Sem Título" # Define o título padrão como "Sem Título"
        description = "Sem Descrição" # Define a descrição padrão como "Sem Título"

        # Se o arquivo de título existir, lê o título do arquivo
        if os.path.exists(title_path):
            with open(title_path, 'r') as f:
                title = f.read().strip()

        # Se o arquivo de descrição existir, lê a descrição do arquivo
        if os.path.exists(description_path):
            with open(description_path, 'r') as f:
                description = f.read().strip()
                
        videos.append({'filename': video_file, 'title': title, 'description': description})# Adiciona o vídeo e seu título à lista
    
    return render_template('video.html', videos=videos)

@app.route('/postgreteste.html')
def rota_postgreteste():
    return render_template('postgreteste.html')

@app.route('/upload_video', methods=['POST'])
def upload_video():
    # Verifica se o vídeo e o título foram enviados no formulário
    if 'video' not in request.files or 'video_title' not in request.form:
        return redirect('/video.html')

    file = request.files['video']
    title = request.form['video_title']
    description = request.form['video_description']

    # Se o nome do arquivo estiver vazio, redireciona de volta para a página de vídeos
    if file.filename == '':
        return redirect('/video.html')
    
    # Se o arquivo for permitido, processa o upload
    if file and allowed_file(file.filename):
        filename = secure_filename(f"{uuid.uuid4()}_{file.filename}")
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        title_filename = filename.rsplit('.', 1)[0] + '.title.txt' # Gera o nome do arquivo do título correspondente ao vídeo
        description_filename = filename.rsplit('.', 1)[0] + '.desc.txt' # Gera o nome do arquivo da descrição correspondente ao vídeo
        
        with open(os.path.join(app.config['UPLOAD_FOLDER'], title_filename), 'w') as f:
            f.write(title)

        # Salva a descrição do vídeo em um arquivo de texto
        with open(os.path.join(app.config['UPLOAD_FOLDER'], description_filename), 'w') as f:
            f.write(description)

        duration, width, height = get_video_metadata(file_path)
        save_metadata_to_db(filename, title, description, duration, width, height)

        return redirect(url_for('rota_video'))
    else:
        return redirect(request.url)
    
@app.route('/delete_video/<filename>', methods=['POST'])
def delete_video(filename):
    try:
        # Constrói o caminho completo do arquivo de vídeo a ser deletado
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # Gera os caminhos dos arquivos de título e descrição correspondentes ao vídeo
        title_file_path = file_path.rsplit('.', 1)[0] + '.title.txt'
        description_file_path = file_path.rsplit('.', 1)[0] + '.desc.txt'
        
        # Se o arquivo de vídeo existir, deleta o arquivo de vídeo, título e descrição
        if os.path.exists(file_path):
            os.remove(file_path)

            if os.path.exists(title_file_path):
                os.remove(title_file_path)

            if os.path.exists(description_file_path):
                os.remove(description_file_path)

            print(f"Arquivo '{filename}' deletado com sucesso.")

            delete_metadata_from_db(filename)
        else:
            print(f"Arquivo '{filename}' não encontrado para deletar.")
    except Exception as e:
        print(f"Erro ao deletar arquivo '{filename}': {str(e)}")
    
    return redirect(url_for('rota_video'))

# Abre o aplicativo na porta 5500 e o roda.
if __name__ == '__main__':
    app.run(debug = True, port = 5500)