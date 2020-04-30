from aplicacao import app

from flask import render_template

@app.route('/home')
def ola():
    retorno = render_template(
            'index.html',
            title='Página Flask',
            outra='Novo Texto',
            lista=['a','b','c']
            )
    return retorno

@app.route('/')
def pagina_principal():
    return '<h1>Página Principal</h1><p>Olá</p>'

@app.route('/outraPagina')
def outra_pagina():
    return '<h1>Outra página</h1>'

app.run(debug=True)