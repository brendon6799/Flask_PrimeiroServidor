from flask import render_template
from aplicacao import app

@app.route('/home')
def ola():
    render_template('index.html')

@app.route('/')
def pagina_principal():
    return '<h1>Página Principal</h1>'

@app.route('/')
def outra_pagina():
    return '<h1>Outra página</h1>'

app.run()