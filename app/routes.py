from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    usuario = {"nome": "Liedeson", "sobrenome": "Moraes"}
    
    return render_template('index.html', usuario=usuario, titulo='Pagina inicial')
    
@app.route('/contato')
def contato():
    return render_template('contato.html', titulo="Contato")



