from flask import flask

app = flask(__name__)

@app.route('/home')
def ola():
    return '<h1>Olá mundo de novo!</h1>'

@app.route('/')
def pagina_principal():
    return '<h1>Página Principal</h1>'

@app.route('/')
def outra_pagina():
    return '<h1>Outra página</h1>'

app.run()