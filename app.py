from flask import Flask, redirect, url_for, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__) # Instanciamos el objeto app de la clase Flask
# __name__ es para la mayoría de los casos. Esto es necesario para que Flask 
# sepa dónde buscar recursos como plantillas y archivos estáticos.

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

@app.route("/")
def app_init():
    return """
    <h1>Form para agregar reasons</h1>
    <form>
      <label for="usuario" >Usuario: </label>
      <input type="text" id="usuario" name="usuario"><br><br>
      <label for="tipo" >Tipo: </label>
      <input type="text" id="tipo" name="tipo"><br><br>
      <label for="reason" >Reason: </label>
      <textarea id="reason" name="reason" rows="5" cols="40"></textarea><br><br>
      <input type="submit" value="Enviar" >
    </form>
    """

@app.route("/form")
def form():
    return """
    <form method="POST" action="/">
    {{ form.csrf_token }}
    {{ form.name.label }} {{ form.name(size=20) }}
    <input type="submit" value="Go">
    </form>
    """

@app.route("/front", methods=['POST'])
def front():
    data = request.form
    

    return f"Formulario {data} recibido con éxtito"
    