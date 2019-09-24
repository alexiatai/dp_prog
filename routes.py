from app import app
from flask import render_template, redirect
from app.forms import FormCadastro

@app.route("/", methods=['get','post'])
def carregar_pagina():
    return render_template('inicio.html', title="Aula Flask")

@app.route("/teste")
def carregar_teste():
    return render_template("teste.html")

@app.route("/cadastro")
def carregar_cadastro():
    return render_template("cadastro.html")

@app.route("/cadastrar_usuario", methods=['get','post'])
def cadastrar_usuario():
    form = FormCadastro()
    if form.validate_on_submit():
        print(form.nome.data)
        return redirect("/teste")
    return render_template('cadastro.html', form=form)