from flask import Flask # Importamos la clase Flask

app = Flask(__name__) # Instanciamos el objeto app de la clase Flask
# __name__ es para la mayoría de los casos. Esto es necesario para que Flask 
# sepa dónde buscar recursos como plantillas y archivos estáticos.

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