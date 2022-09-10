import json
from flask import Flask, jsonify
from flask_cors import  CORS
from dotenv import dotenv_values
# se traen las rutas con los submodulos
from routes.students_route import student_module
# Se crean variables de entorno
config = dotenv_values('.env')
# Se crea la app
app = Flask(__name__)
# Se definen los CORS
cors = CORS(app)
# Se importan las rutas mediante Blueprint (submodulos) <se registran>
app.register_blueprint(student_module,url_prefix="/estudiantes")

@app.route('/')
def hello_world():
    dictRe = {'message': "Hola pelotudos"}
    return jsonify(dictRe), 201
'''
Esto es para crear las variables de entorno, ahora se debe ejecutar con py app.py y 
se importan las variables, se deben especificar, en el archivo .env se definen las variables
como si fueran un diccionario
'''
if __name__ == '__main__':
    app.run(host='localhost', port=config["PORT"],debug=True)