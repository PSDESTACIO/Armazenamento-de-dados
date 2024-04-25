from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('postgreteste.html')

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome']
    email = request.form['email']
    
    # Here, you can process the name and email as needed
    # For now, let's just print them
    print("Nome:", nome)
    print("Email:", email)
    
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)