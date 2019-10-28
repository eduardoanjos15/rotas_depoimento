from flask import Flask, render_template, redirect
from classe_usuario_dep import UsuarioDepoimento

app = Flask(__name__)


@app.route('/')
def but():
    return render_template('template_but.html')

@app.route('/botao')
def principal():
    return render_template('index.html')

@app.route('/depoimento/salvar', methods=["POST"])
def depoimento_salvar():
    nome = request.form['nome']
    depoimento = request.form['depoimento']
    
    usuario = UsuarioDepoimento()
    usuario.nome = nome 
    usuario.depoimento = depoimento
     
    salvar_depoimento_db(usuario)

    return redirect('/lista_depoimentos')

########## DELETAR DEPOIMENTO ##########
@app.route('/depoimento/delete')
def depoimento_deletar():
    id = request.args['id']
    deletar_depoimento(id)
    return redirect ('/lista_usuario')

########## LISTAR DEPOIMENTO ##########
@app.route('/lista_depoimentos')
def lista_depoimentos():
    lista = listar_depoimentos_usuarios_db()
    return render_template('lista_us.html', lista = lista)  

app.run()